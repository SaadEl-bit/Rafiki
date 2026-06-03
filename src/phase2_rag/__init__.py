"""
Phase 2 — RAG Knowledge Base
=============================
Builds a ChromaDB vector database from the Phase 1 HuggingFace dataset
and exposes a simple retriever for use in the Gradio app (Phase 4).

Public API:
    from src.phase2_rag import RAGRetriever
    retriever = RAGRetriever.from_disk("path/to/chromadb")
    chunks = retriever.retrieve("What is the passive voice?", subject="English")
"""

from .retriever import RAGRetriever

__all__ = ["RAGRetriever"]
