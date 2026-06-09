import os
import logging
from pathlib import Path
from typing import Optional
from huggingface_hub import snapshot_download
from src.phase2_rag.retriever import RAGRetriever
import chromadb
import uuid

logger = logging.getLogger(__name__)

INDEX_REPO = "Saad-Elouakate/AI-Adaptive-Learning-Index"
CHROMA_DB_DIR = os.getenv("CHROMA_DB_DIR", "./chroma_db_cache")

_retriever = None
_ephemeral_client = chromadb.Client()  # In-memory client for temporary RAG

# In-memory conversation memory per session
# { session_id: [{"role": "user"/"assistant", "content": "..."}] }
_conversation_memory: dict[str, list[dict]] = {}
MAX_HISTORY_PER_SESSION = 20
MAX_SESSIONS = 500

def get_retriever() -> RAGRetriever:
    global _retriever
    if _retriever is not None:
        return _retriever

    chroma_path = Path(CHROMA_DB_DIR)
    
    # Check if the path exists and is not empty
    if not chroma_path.exists() or not any(chroma_path.iterdir()):
        logger.info(f"Downloading ChromaDB index from {INDEX_REPO}...")
        snapshot_download(
            repo_id=INDEX_REPO,
            repo_type="dataset",
            local_dir=str(chroma_path),
            token=os.getenv("HF_TOKEN")
        )
        logger.info("Download complete.")
    else:
        logger.info(f"Using existing ChromaDB index at {chroma_path}")
    
    _retriever = RAGRetriever.from_disk(str(chroma_path))
    return _retriever

def chunk_text(text: str, chunk_size: int = 250, overlap: int = 50) -> list[str]:
    """A simple word-based text chunker."""
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)
        i += chunk_size - overlap
        if i >= len(words):
            break
    return chunks

def add_to_session_rag(session_id: str, text: str, subject: str) -> None:
    """Chunks the extracted text and stores it in an ephemeral ChromaDB collection for this session."""
    retriever = get_retriever()
    
    # Create or get collection
    collection = _ephemeral_client.get_or_create_collection(name=f"session_{session_id}")
    
    chunks = chunk_text(text)
    if not chunks:
        return

    # Embed chunks
    embeddings = retriever._model.encode(chunks, normalize_embeddings=True).tolist()
    
    # Generate IDs and metadata
    ids = [f"chunk_{i}" for i in range(len(chunks))]
    metadatas = [{"source_file": "Uploaded Document", "page_number": "N/A", "subject": subject} for _ in chunks]
    
    # Add to in-memory DB
    collection.add(
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas,
        ids=ids
    )
    logger.info(f"Added {len(chunks)} chunks to session {session_id}")

def add_to_conversation(session_id: str, role: str, content: str) -> None:
    if len(_conversation_memory) >= MAX_SESSIONS:
        oldest = next(iter(_conversation_memory))
        del _conversation_memory[oldest]
        logger.warning(f"Conversation memory full, evicted session {oldest}")
    if session_id not in _conversation_memory:
        _conversation_memory[session_id] = []
    _conversation_memory[session_id].append({"role": role, "content": content})
    if len(_conversation_memory[session_id]) > MAX_HISTORY_PER_SESSION:
        _conversation_memory[session_id] = _conversation_memory[session_id][-MAX_HISTORY_PER_SESSION:]

def get_conversation_history(session_id: str, last_n: int = 6) -> list[dict]:
    return _conversation_memory.get(session_id, [])[-last_n:]

def session_exists(session_id: str) -> bool:
    """Check if a session has uploaded document data in the ephemeral ChromaDB."""
    try:
        collection = _ephemeral_client.get_collection(name=f"session_{session_id}")
        return collection.count() > 0
    except Exception:
        return False

def retrieve_context(question: str, subject: str, session_id: Optional[str] = None) -> str:
    retriever = get_retriever()
    
    # 1. Retrieve from permanent KB
    global_chunks = retriever.retrieve(question, subject=subject, top_k=3)
    
    # 2. Retrieve from temporary session DB (if exists)
    session_chunks = []
    if session_id:
        try:
            collection = _ephemeral_client.get_collection(name=f"session_{session_id}")
            query_embedding = retriever._model.encode(question, normalize_embeddings=True).tolist()
            
            results = collection.query(
                query_embeddings=[query_embedding],
                n_results=min(3, collection.count()),
                include=["documents", "metadatas", "distances"]
            )
            
            if results["documents"] and results["documents"][0]:
                docs = results["documents"][0]
                metas = results["metadatas"][0]
                dists = results["distances"][0]
                for doc, meta, dist in zip(docs, metas, dists):
                    session_chunks.append({
                        "text": doc,
                        "metadata": meta,
                        "distance": round(dist, 4)
                    })
        except Exception as e:
            logger.warning(f"Could not retrieve from session RAG for {session_id}: {e}")

    # Merge chunks
    all_chunks = session_chunks + global_chunks
    # Sort by distance
    all_chunks = sorted(all_chunks, key=lambda x: x["distance"])
    
    # Limit to top 5 overall to save context window
    all_chunks = all_chunks[:5]
    
    return retriever.format_context(all_chunks)
