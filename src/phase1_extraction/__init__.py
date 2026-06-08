"""
Phase 1 — PDF to Structured Markdown Extraction
================================================
Converts raw Moroccan Bac curriculum PDFs into clean, chunked Markdown
with LaTeX math notation, ready for Phase 2 RAG indexing.
"""

from .config import PipelineConfig, BacLevel, Subject
from .pipeline import RafikiPDFPipeline

__all__ = ["PipelineConfig", "BacLevel", "Subject", "RafikiPDFPipeline"]
