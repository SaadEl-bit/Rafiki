"""
PDF Processor — Phase 1
=======================
Handles opening, page iteration, image rendering, and raw text extraction.
Wraps PyMuPDF (fitz) and returns PIL Images for the VLM.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Dict, Generator, Optional, Tuple

from PIL import Image
import fitz  # PyMuPDF

logger = logging.getLogger(__name__)


class PDFProcessor:
    """
    Thin wrapper around a PyMuPDF document.

    Usage
    -----
    with PDFProcessor("path/to/file.pdf", dpi=150) as pdf:
        for page_num, image, raw_text in pdf.iter_pages():
            ...
    """

    def __init__(self, pdf_path: str | Path, dpi: int = 150):
        self.pdf_path = Path(pdf_path)
        self.dpi = dpi
        self._doc: Optional[fitz.Document] = None

    # ── Context manager ────────────────────────────────────────────────────

    def __enter__(self) -> "PDFProcessor":
        return self.open()

    def __exit__(self, *_) -> None:
        self.close()

    # ── Lifecycle ──────────────────────────────────────────────────────────

    def open(self) -> "PDFProcessor":
        if not self.pdf_path.exists():
            raise FileNotFoundError(f"PDF not found: {self.pdf_path}")
        self._doc = fitz.open(str(self.pdf_path))
        logger.info("Opened PDF: %s  (%d pages)", self.pdf_path.name, self.page_count)
        return self

    def close(self) -> None:
        if self._doc:
            self._doc.close()
            self._doc = None

    # ── Properties ────────────────────────────────────────────────────────

    @property
    def page_count(self) -> int:
        return len(self._doc) if self._doc else 0

    # ── Page access ───────────────────────────────────────────────────────

    def page_to_image(self, page_num: int) -> Image.Image:
        """Render a single page to a PIL Image at the configured DPI."""
        page = self._doc[page_num]
        mat = fitz.Matrix(self.dpi / 72, self.dpi / 72)
        pix = page.get_pixmap(matrix=mat, alpha=False)
        return Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    def page_to_text(self, page_num: int) -> str:
        """Extract raw text from a page (fallback / hint for the VLM)."""
        return self._doc[page_num].get_text()

    def get_page_range(
        self,
        start: int = 0,
        end: Optional[int] = None,
    ) -> range:
        end = end if end is not None else self.page_count
        return range(start, min(end, self.page_count))

    # ── Iteration helper ──────────────────────────────────────────────────

    def iter_pages(
        self,
        start: int = 0,
        end: Optional[int] = None,
    ) -> Generator[Tuple[int, Image.Image, str], None, None]:
        """
        Yield ``(page_num, image, raw_text)`` for each page in range.
        This is the primary interface used by the pipeline.
        """
        for page_num in self.get_page_range(start, end):
            image    = self.page_to_image(page_num)
            raw_text = self.page_to_text(page_num)
            yield page_num, image, raw_text

    # ── Bulk helpers ──────────────────────────────────────────────────────

    def extract_all_text(
        self,
        start: int = 0,
        end: Optional[int] = None,
    ) -> Dict[int, str]:
        """Return {page_num: raw_text} for the given range."""
        return {
            page_num: self.page_to_text(page_num)
            for page_num in self.get_page_range(start, end)
        }
