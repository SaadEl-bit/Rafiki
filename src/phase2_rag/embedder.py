"""
Embedder — Phase 2 RAG Knowledge Base
======================================
Downloads all Phase 1 chunks from HuggingFace, embeds them with the
multilingual MiniLM model, and inserts them into ChromaDB.

Usage (called from main.py):
    from src.phase2_rag.embedder import build_index
    build_index(config)
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


def build_index(config) -> dict[str, int]:
    """
    Build the ChromaDB vector index from the Phase 1 HuggingFace dataset.

    Steps
    -----
    1. Load all splits (English_2Bac, Maths_2Bac, Physics_2Bac, …) from HF.
    2. Filter out chunks that are too short (noise / markdown headers).
    3. Embed each chunk's `content_string` in batches using the multilingual model.
    4. Upsert into the subject-specific ChromaDB collection.

    Returns
    -------
    dict mapping collection_name → number of chunks inserted.
    """
    import chromadb
    from datasets import load_dataset
    from sentence_transformers import SentenceTransformer

    from .config import SUBJECT_TO_COLLECTION

    # ── 1. Load embedding model ───────────────────────────────────────────
    logger.info("Loading embedding model: %s", config.embedding_model)
    model = SentenceTransformer(config.embedding_model)
    logger.info("Embedding model loaded (dim=%d)", model.get_sentence_embedding_dimension())

    # ── 2. Connect to / create ChromaDB ──────────────────────────────────
    chroma_path = Path(config.chromadb_dir)
    chroma_path.mkdir(parents=True, exist_ok=True)
    client = chromadb.PersistentClient(path=str(chroma_path))
    logger.info("ChromaDB initialised at: %s", chroma_path)

    # ── 3. Load dataset from HuggingFace ─────────────────────────────────
    logger.info("Loading dataset: %s", config.hf_source_dataset)
    dataset_dict = load_dataset(
        config.hf_source_dataset,
        token=config.hub_token,
    )
    logger.info("Available splits: %s", list(dataset_dict.keys()))

    stats: dict[str, int] = {}

    # ── 4. Process each split ─────────────────────────────────────────────
    for split_name, split_data in dataset_dict.items():
        logger.info("=" * 60)
        logger.info("Processing split: %s  (%d rows)", split_name, len(split_data))

        # Determine subject from the first non-null row
        subjects_in_split = list(set(split_data["subject"]))
        if not subjects_in_split:
            logger.warning("Split '%s' has no subject column — skipping.", split_name)
            continue

        subject = subjects_in_split[0]
        collection_name = SUBJECT_TO_COLLECTION.get(subject)
        if collection_name is None:
            logger.warning(
                "Subject '%s' not in SUBJECT_TO_COLLECTION map — skipping split '%s'.",
                subject, split_name,
            )
            continue

        logger.info("Subject: '%s'  →  collection: '%s'", subject, collection_name)

        # Get or create collection (cosine similarity is best for semantic search)
        collection = client.get_or_create_collection(
            name=collection_name,
            metadata={"hnsw:space": "cosine"},
        )

        # ── 5. Filter and embed ───────────────────────────────────────────
        rows = split_data.to_list()
        valid_rows = [
            r for r in rows
            if r.get("content") and len(str(r["content"]).strip()) >= config.min_chunk_chars
        ]
        skipped = len(rows) - len(valid_rows)
        if skipped:
            logger.info("Skipped %d short/empty chunks (min %d chars).", skipped, config.min_chunk_chars)

        if not valid_rows:
            logger.warning("No valid chunks in split '%s' — skipping.", split_name)
            continue

        texts = [str(r["content"]) for r in valid_rows]
        ids   = [str(r["chunk_id"]) for r in valid_rows]
        metadatas = [
            {
                "source_file":   str(r.get("source_file", "")),
                "page_number":   int(r.get("page_number", 0)),
                "subject":       str(r.get("subject", "")),
                "level":         str(r.get("level", "")),
                "language":      str(r.get("language", "")),
                "content_type":  str(r.get("content_type", "")),
                "section_title": str(r.get("section_title", "")),
                "char_count":    int(r.get("char_count", 0)),
            }
            for r in valid_rows
        ]

        logger.info("Embedding %d chunks in batches of %d …", len(texts), config.embed_batch_size)
        embeddings = _embed_in_batches(model, texts, config.embed_batch_size)

        # ── 6. Upsert into ChromaDB ───────────────────────────────────────
        # Upsert (not add) so re-running is safe — existing IDs are updated.
        batch_size = 500
        for start in range(0, len(texts), batch_size):
            end = start + batch_size
            collection.upsert(
                ids=ids[start:end],
                embeddings=[e.tolist() for e in embeddings[start:end]],
                documents=texts[start:end],
                metadatas=metadatas[start:end],
            )
            logger.info("  Upserted rows %d–%d", start, min(end, len(texts)))

        count = collection.count()
        stats[collection_name] = count
        logger.info("✅ Collection '%s' now has %d vectors.", collection_name, count)

    logger.info("=" * 60)
    logger.info("Index build complete. Stats: %s", stats)
    return stats


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _embed_in_batches(model, texts: list[str], batch_size: int):
    """Embed texts in batches with progress logging."""
    import numpy as np

    all_embeddings = []
    total = len(texts)

    for start in range(0, total, batch_size):
        end = min(start + batch_size, total)
        batch = texts[start:end]
        embeddings = model.encode(batch, show_progress_bar=False, normalize_embeddings=True)
        all_embeddings.extend(embeddings)
        logger.info("  Embedded %d / %d chunks", end, total)

    return all_embeddings
