"""
Retriever — Phase 2 RAG Knowledge Base
========================================
Loads the ChromaDB built by embedder.py and exposes a simple
`retrieve(question, subject)` function for the Gradio app.

Usage in Phase 4 (Gradio app):
    from src.phase2_rag import RAGRetriever

    retriever = RAGRetriever.from_disk("/path/to/chromadb")
    chunks = retriever.retrieve("What is the passive voice?", subject="English")
    for chunk in chunks:
        print(chunk["text"])
        print(chunk["metadata"])
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


class RAGRetriever:
    """
    Wrapper around ChromaDB that handles embedding a query and
    returning the most relevant chunks for a given subject.

    Parameters
    ----------
    chromadb_dir : str | Path
        Path to the folder created by `build_index()` in embedder.py.
    embedding_model : str
        The SAME sentence-transformers model used during indexing.
        Default matches the one in config.py.
    top_k : int
        Number of chunks to return per query.
    """

    def __init__(
        self,
        chromadb_dir: str | Path,
        embedding_model: str = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
        top_k: int = 5,
    ):
        import chromadb
        from sentence_transformers import SentenceTransformer

        from .config import SUBJECT_TO_COLLECTION

        self._subject_map = SUBJECT_TO_COLLECTION
        self._top_k = top_k

        logger.info("Loading retriever from: %s", chromadb_dir)
        self._client = chromadb.PersistentClient(path=str(chromadb_dir))

        logger.info("Loading embedding model: %s", embedding_model)
        self._model = SentenceTransformer(embedding_model)
        logger.info("RAGRetriever ready.")

    # ── Factory ───────────────────────────────────────────────────────────

    @classmethod
    def from_disk(
        cls,
        chromadb_dir: str | Path,
        embedding_model: str = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
        top_k: int = 5,
    ) -> "RAGRetriever":
        """Load a previously built index from disk."""
        return cls(chromadb_dir, embedding_model, top_k)

    @classmethod
    def from_config(cls, config) -> "RAGRetriever":
        """Load using a RAGConfig object."""
        return cls(config.chromadb_dir, config.embedding_model, config.top_k)

    # ── Core retrieval ────────────────────────────────────────────────────

    def retrieve(
        self,
        question: str,
        subject: str,
        top_k: int | None = None,
    ) -> list[dict[str, Any]]:
        """
        Retrieve the most relevant chunks for a student question.

        Parameters
        ----------
        question : str
            The student's raw question (in French or English).
        subject : str
            One of: "Mathématiques", "Physique-Chimie", "English".
            Used to scope the search to the correct collection.
        top_k : int, optional
            Override the default top_k for this query.

        Returns
        -------
        List of dicts, each with keys:
            "text"     — the original extracted chunk text
            "metadata" — dict with source_file, page_number, subject, etc.
            "distance" — cosine distance (lower = more similar)
        """
        k = top_k or self._top_k

        # Map human-readable subject to collection name
        collection_name = self._subject_map.get(subject)
        if collection_name is None:
            raise ValueError(
                f"Unknown subject '{subject}'. "
                f"Valid subjects: {list(self._subject_map.keys())}"
            )

        try:
            collection = self._client.get_collection(collection_name)
        except Exception:
            logger.error(
                "Collection '%s' not found in ChromaDB at '%s'. "
                "Did you run the indexer (main.py) first?",
                collection_name, self._client,
            )
            return []

        # Embed the question
        query_embedding = self._model.encode(
            question,
            normalize_embeddings=True,
        ).tolist()

        # Query ChromaDB
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=min(k, collection.count()),
            include=["documents", "metadatas", "distances"],
        )

        # Unpack and return
        chunks = []
        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        for doc, meta, dist in zip(documents, metadatas, distances):
            chunks.append({
                "text": doc,
                "metadata": meta,
                "distance": round(dist, 4),
            })

        logger.debug(
            "retrieve('%s', subject='%s') → %d chunks (best dist=%.4f)",
            question[:60], subject, len(chunks),
            distances[0] if distances else 0,
        )
        return chunks

    # ── Utilities ─────────────────────────────────────────────────────────

    def list_collections(self) -> list[str]:
        """Return the names of all collections currently in ChromaDB."""
        return [c.name for c in self._client.list_collections()]

    def collection_count(self, subject: str) -> int:
        """Return how many chunks are indexed for a given subject."""
        collection_name = self._subject_map.get(subject, "")
        try:
            return self._client.get_collection(collection_name).count()
        except Exception:
            return 0

    def format_context(self, chunks: list[dict[str, Any]]) -> str:
        """
        Format retrieved chunks into a single string ready to inject
        into an LLM prompt.

        Example output:
            [Source: English-cours.pdf, Page 3]
            The passive voice is used when...

            [Source: English-cours.pdf, Page 4]
            Examples of passive constructions...
        """
        parts = []
        for i, chunk in enumerate(chunks, 1):
            meta = chunk["metadata"]
            source = meta.get("source_file", "unknown")
            page = meta.get("page_number", "?")
            parts.append(f"[Source: {source}, Page {page}]\n{chunk['text']}")
        return "\n\n".join(parts)
