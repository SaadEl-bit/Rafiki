"""
Main — Phase 2 RAG Knowledge Base
====================================
Entry point for the Kaggle notebook.

Run with:
    python -m src.phase2_rag.main \\
        --chromadb-dir /kaggle/working/chromadb \\
        --push-to-hub

What this script does:
    1. Logs in to HuggingFace (via Kaggle Secret HF_TOKEN).
    2. Calls embedder.build_index() to download Phase 1 chunks and
       build the ChromaDB vector database on disk.
    3. Zips the ChromaDB folder.
    4. Pushes the zip to HuggingFace (new repo: AI-Adaptive-Learning-Index).
    5. Runs 3 sample retrieval queries to verify the index works.
"""

from __future__ import annotations

import argparse
import logging
import os
import shutil
import sys
import zipfile
from pathlib import Path

# ── Logging setup ─────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


# ── Verification queries ───────────────────────────────────────────────────────
# These are run after indexing to confirm retrieval works correctly.
VERIFICATION_QUERIES = [
    {
        "question": "What is the passive voice and how is it used?",
        "subject": "English",
    },
    {
        "question": "Qu'est-ce que la dérivée d'une fonction?",
        "subject": "Mathématiques",
    },
    {
        "question": "Lois de Newton en mécanique",
        "subject": "Physique-Chimie",
    },
]


def _login_huggingface(token: str | None) -> str | None:
    """Log in to HuggingFace. Tries Kaggle Secrets first, then env var."""
    # Try Kaggle Secrets
    if token is None:
        try:
            from kaggle_secrets import UserSecretsClient
            token = UserSecretsClient().get_secret("HF_TOKEN")
            logger.info("HF token loaded from Kaggle Secrets.")
        except Exception:
            pass

    # Try environment variable
    if token is None:
        token = os.getenv("HF_TOKEN")
        if token:
            logger.info("HF token loaded from environment variable.")

    if token:
        from huggingface_hub import login
        login(token=token, add_to_git_credential=False)
        logger.info("Logged in to HuggingFace successfully.")
    else:
        logger.warning(
            "No HF_TOKEN found. Push to HuggingFace will be skipped. "
            "Add HF_TOKEN to Kaggle Secrets or set the environment variable."
        )

    return token


def _zip_chromadb(chromadb_dir: Path) -> Path:
    """Zip the ChromaDB folder into a single archive for upload."""
    zip_path = chromadb_dir.parent / "chromadb.zip"
    logger.info("Zipping ChromaDB folder → %s", zip_path)

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for file in chromadb_dir.rglob("*"):
            zf.write(file, file.relative_to(chromadb_dir.parent))

    size_mb = zip_path.stat().st_size / (1024 * 1024)
    logger.info("✅ Created %s (%.1f MB)", zip_path.name, size_mb)
    return zip_path


def _push_to_hub(zip_path: Path, config) -> None:
    """Upload the ChromaDB zip to a HuggingFace dataset repository."""
    from huggingface_hub import HfApi

    api = HfApi(token=config.hub_token)

    # Create the repo if it doesn't exist yet
    try:
        api.create_repo(
            repo_id=config.hf_index_repo,
            repo_type="dataset",
            exist_ok=True,
            private=False,
        )
        logger.info("HuggingFace repo ready: %s", config.hf_index_repo)
    except Exception as e:
        logger.error("Failed to create/access HF repo: %s", e)
        raise

    # Upload the zip
    logger.info("Uploading %s → %s …", zip_path.name, config.hf_index_repo)
    api.upload_file(
        path_or_fileobj=str(zip_path),
        path_in_repo="chromadb.zip",
        repo_id=config.hf_index_repo,
        repo_type="dataset",
        commit_message="Phase 2: update ChromaDB vector index",
    )
    logger.info(
        "✅ Pushed ChromaDB to: https://huggingface.co/datasets/%s",
        config.hf_index_repo,
    )


def _run_verification(config) -> None:
    """Run sample retrieval queries and print results."""
    from .retriever import RAGRetriever

    logger.info("=" * 60)
    logger.info("Running verification queries …")
    retriever = RAGRetriever.from_config(config)

    available = retriever.list_collections()
    logger.info("Available collections: %s", available)

    for query in VERIFICATION_QUERIES:
        subject = query["subject"]
        question = query["question"]

        # Skip subjects that weren't indexed in this run
        from .config import SUBJECT_TO_COLLECTION
        collection_name = SUBJECT_TO_COLLECTION.get(subject)
        if collection_name not in available:
            logger.info("Skipping query for '%s' (not indexed).", subject)
            continue

        logger.info("-" * 60)
        logger.info("Question [%s]: %s", subject, question)
        chunks = retriever.retrieve(question, subject=subject, top_k=3)

        if not chunks:
            logger.warning("  No results returned!")
        else:
            for i, chunk in enumerate(chunks, 1):
                preview = chunk["text"][:120].replace("\n", " ")
                logger.info(
                    "  [%d] dist=%.4f | page=%s | %s…",
                    i,
                    chunk["distance"],
                    chunk["metadata"].get("page_number", "?"),
                    preview,
                )

    logger.info("=" * 60)
    logger.info("✅ Verification complete.")


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Phase 2 — Build ChromaDB RAG index from HuggingFace dataset."
    )
    parser.add_argument(
        "--chromadb-dir",
        default="/kaggle/working/chromadb",
        help="Where to save the ChromaDB folder (default: /kaggle/working/chromadb).",
    )
    parser.add_argument(
        "--source-dataset",
        default=None,
        help="Override HuggingFace source dataset (default from config.py).",
    )
    parser.add_argument(
        "--index-repo",
        default=None,
        help="Override HuggingFace index repository name (default from config.py).",
    )
    parser.add_argument(
        "--push-to-hub",
        action="store_true",
        help="If set, push the ChromaDB zip to HuggingFace after indexing.",
    )
    parser.add_argument(
        "--skip-verify",
        action="store_true",
        help="Skip the verification queries at the end.",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()

    from .config import RAGConfig
    from .embedder import build_index

    # ── Build config ──────────────────────────────────────────────────────
    config = RAGConfig(chromadb_dir=args.chromadb_dir)
    if args.source_dataset:
        config.hf_source_dataset = args.source_dataset
    if args.index_repo:
        config.hf_index_repo = args.index_repo

    logger.info("=" * 60)
    logger.info("Rafiki — Phase 2: RAG Knowledge Base Builder")
    logger.info("=" * 60)
    logger.info("Source dataset : %s", config.hf_source_dataset)
    logger.info("ChromaDB dir   : %s", config.chromadb_dir)
    logger.info("Embedding model: %s", config.embedding_model)
    logger.info("Push to Hub    : %s", args.push_to_hub)
    logger.info("=" * 60)

    # ── Step 1: Authenticate ──────────────────────────────────────────────
    token = _login_huggingface(config.hub_token)
    config.hub_token = token

    # ── Step 2: Build the index ───────────────────────────────────────────
    stats = build_index(config)

    if not stats:
        logger.error("No chunks were indexed! Check your HuggingFace dataset.")
        sys.exit(1)

    total_chunks = sum(stats.values())
    logger.info("Total chunks indexed across all subjects: %d", total_chunks)

    # ── Step 3: Push to HuggingFace ──────────────────────────────────────
    if args.push_to_hub:
        if not token:
            logger.error("Cannot push to Hub: no HF_TOKEN found.")
            sys.exit(1)
        zip_path = _zip_chromadb(Path(config.chromadb_dir))
        _push_to_hub(zip_path, config)
    else:
        logger.info(
            "Skipping Hub push (run with --push-to-hub to upload)."
        )

    # ── Step 4: Verify ────────────────────────────────────────────────────
    if not args.skip_verify:
        _run_verification(config)

    logger.info("Phase 2 complete! ✅")


if __name__ == "__main__":
    main()
