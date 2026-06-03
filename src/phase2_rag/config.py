"""
Configuration — Phase 2 RAG Knowledge Base
==========================================
All settings for the embedding and retrieval pipeline.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


# ---------------------------------------------------------------------------
# Subject → ChromaDB collection name mapping
# ---------------------------------------------------------------------------
# One collection per subject so retrieval is always scoped correctly.
# The key is the exact string stored in the HuggingFace dataset `subject` column.

SUBJECT_TO_COLLECTION: dict[str, str] = {
    "Mathématiques": "maths_2bac",
    "Physique-Chimie": "physics_2bac",
    "English": "english_2bac",
}

# Reverse mapping — useful in the Gradio app
COLLECTION_TO_SUBJECT: dict[str, str] = {v: k for k, v in SUBJECT_TO_COLLECTION.items()}

# All valid collection names
ALL_COLLECTIONS: list[str] = list(SUBJECT_TO_COLLECTION.values())


# ---------------------------------------------------------------------------
# Main RAG configuration
# ---------------------------------------------------------------------------

@dataclass
class RAGConfig:
    """
    All settings for the Phase 2 RAG pipeline.

    Key design decisions
    --------------------
    * `embedding_model` — multilingual MiniLM supports both French (Maths/PC)
      and English. Runs on CPU in ~50ms per query. No GPU needed.
    * `chromadb_dir`    — a plain folder on disk. Zip it → upload to HF → done.
    * `top_k`           — 5 chunks gives enough context without overloading
      the LLM prompt window.
    * `hf_source_dataset` — the Phase 1 output we are building the index from.
    * `hf_index_repo`     — a NEW HuggingFace dataset repo for the ChromaDB zip.
    """

    # ── Embedding Model ───────────────────────────────────────────────────
    # Multilingual: handles French (Maths, PC) AND English in the same model.
    embedding_model: str = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

    # ── ChromaDB ──────────────────────────────────────────────────────────
    # Default path used on Kaggle; override locally via CLI --chromadb-dir
    chromadb_dir: str = "/kaggle/working/chromadb"

    # Number of chunks returned per retrieval query
    top_k: int = 5

    # ── HuggingFace — Source (Phase 1 output) ────────────────────────────
    hf_source_dataset: str = "Saad-Elouakate/AI-Adaptive-Learning"

    # ── HuggingFace — Destination (ChromaDB zip) ─────────────────────────
    # This is a NEW repo we create specifically for the vector index.
    hf_index_repo: str = "Saad-Elouakate/AI-Adaptive-Learning-Index"

    # ── Authentication ────────────────────────────────────────────────────
    hub_token: Optional[str] = field(
        default_factory=lambda: os.getenv("HF_TOKEN")
    )

    # ── Processing ────────────────────────────────────────────────────────
    # Batch size for embedding — larger = faster but more RAM
    embed_batch_size: int = 64

    # Minimum characters a chunk must have to be embedded (skip empty/noise)
    min_chunk_chars: int = 10
