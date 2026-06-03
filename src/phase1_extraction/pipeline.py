"""
Pipeline — Phase 1
===================
Orchestrates PDF → Markdown extraction for one or many PDFs.

Outputs (per PDF, inside output_dir/<pdf_stem>/):
  pages/page_XX.md     — per-page Markdown
  full_course.md       — all pages concatenated
  structured_data.json — per-page entries with metadata
  chunks.json          — flat list of all chunks (Phase 2 input)
  summary.json         — run statistics

Optionally pushes chunks.json as a HuggingFace Dataset.
"""

from __future__ import annotations

import json
import logging
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

from .config import PipelineConfig, FileMetadata
from .pdf_processor import PDFProcessor
from .extractor import VLMExtractor, TextExtractor, BaseExtractor
from .structurer import build_page_entry

logger = logging.getLogger(__name__)


class M3allemPDFPipeline:
    """
    End-to-end Phase 1 pipeline.

    Single PDF
    ----------
    pipeline = M3allemPDFPipeline(config)
    pipeline.run_file("data/raw_pdfs/Maths_2Bac_Probabilites.pdf")

    All PDFs in a folder
    --------------------
    pipeline = M3allemPDFPipeline(config)
    pipeline.run_folder("data/raw_pdfs/")
    """

    def __init__(self, config: PipelineConfig):
        self.config    = config
        self._extractor: Optional[BaseExtractor] = None

    # ── Extractor lifecycle ───────────────────────────────────────────────

    def _get_extractor(self) -> BaseExtractor:
        """Lazy-load the extractor (VLM or text fallback)."""
        if self._extractor is None:
            if self.config.use_vlm:
                vlm = VLMExtractor(
                    model_name      = self.config.model_name,
                    max_new_tokens  = self.config.max_new_tokens,
                    temperature     = self.config.temperature,
                    top_p           = self.config.top_p,
                )
                vlm.load()
                self._extractor = vlm
            else:
                logger.info("VLM disabled — using TextExtractor (CPU fallback)")
                self._extractor = TextExtractor()
        return self._extractor

    def close(self) -> None:
        """Release GPU memory after all PDFs are processed."""
        if self._extractor is not None:
            self._extractor.close()
            self._extractor = None

    # ── Public entry points ───────────────────────────────────────────────

    def run_folder(self, folder: str | Path) -> List[Dict[str, Any]]:
        """Process every PDF in *folder* and return a combined chunk list."""
        folder = Path(folder)
        pdfs   = sorted(folder.glob("*.pdf"))
        if not pdfs:
            logger.warning("No PDFs found in: %s", folder)
            return []

        logger.info("Found %d PDF(s) in %s", len(pdfs), folder)
        all_chunks: List[Dict[str, Any]] = []
        try:
            for pdf_path in pdfs:
                chunks = self.run_file(pdf_path)
                all_chunks.extend(chunks)
        finally:
            self.close()

        logger.info("Total chunks produced: %d", len(all_chunks))
        return all_chunks

    def run_file(self, pdf_path: str | Path) -> List[Dict[str, Any]]:
        """
        Process a single PDF and return its flat chunk list.
        Metadata is auto-detected from the filename (see FileMetadata).
        Files whose subject is not recognised are skipped (returns []).
        """
        pdf_path  = Path(pdf_path)
        file_meta = FileMetadata.from_path(pdf_path, self.config)

        # Skip files not belonging to the 3 MVP subjects
        if file_meta.subject == FileMetadata.UNKNOWN_SUBJECT:
            logger.warning("Skipping (unrecognised subject): %s", pdf_path.name)
            return []

        return self._run(file_meta)

    # ── Core processing ───────────────────────────────────────────────────

    def _run(self, file_meta: FileMetadata) -> List[Dict[str, Any]]:
        start = time.time()
        logger.info("=" * 60)
        logger.info("Processing: %s", file_meta.pdf_path.name)
        logger.info("  subject=%s  level=%s", file_meta.subject, file_meta.level)
        logger.info("=" * 60)

        extractor = self._get_extractor()
        page_entries: List[Dict[str, Any]] = []

        with PDFProcessor(file_meta.pdf_path, dpi=self.config.dpi) as pdf:
            total = pdf.page_count
            page_range = list(pdf.get_page_range(
                self.config.start_page,
                self.config.end_page,
            ))

            for page_num, image, raw_text in pdf.iter_pages(
                self.config.start_page,
                self.config.end_page,
            ):
                logger.info(
                    "[Page %d/%d]  extracting…", page_num + 1, total
                )
                try:
                    markdown = extractor.extract(
                        image        = image,
                        page_num     = page_num,
                        total_pages  = total,
                        raw_text_hint= raw_text,
                    )
                except Exception as exc:
                    logger.error("Page %d failed: %s", page_num + 1, exc)
                    markdown = f"<!-- ERROR page {page_num + 1}: {exc} -->\n\n{raw_text}"
                    time.sleep(10)   # GPU cooldown

                entry = build_page_entry(page_num, markdown, file_meta)
                page_entries.append(entry)
                logger.info(
                    "  → %d chars, %d chunks", entry["char_count"], entry["total_chunks"]
                )
                time.sleep(0.5)   # let GPU breathe between pages

        elapsed = time.time() - start
        logger.info("Finished %s in %.1fs", file_meta.pdf_path.name, elapsed)

        # Save outputs for this PDF
        all_chunks = self._save_outputs(file_meta, page_entries)

        # Optionally push to HuggingFace
        if self.config.push_to_hub:
            self._push_to_hub(all_chunks, file_meta)

        return all_chunks

    # ── Saving ────────────────────────────────────────────────────────────

    def _save_outputs(
        self,
        file_meta: FileMetadata,
        page_entries: List[Dict[str, Any]],
    ) -> List[Dict[str, Any]]:
        """Write all output files for one PDF. Returns the flat chunk list."""
        stem       = Path(file_meta.pdf_path).stem
        output_dir = Path(self.config.output_dir) / stem
        output_dir.mkdir(parents=True, exist_ok=True)

        # 1. Per-page Markdown files
        pages_dir = output_dir / "pages"
        pages_dir.mkdir(exist_ok=True)
        for entry in page_entries:
            (pages_dir / f"page_{entry['page_number']:02d}.md").write_text(
                entry["raw_markdown"], encoding="utf-8"
            )
        logger.info("Saved %d page files → %s", len(page_entries), pages_dir)

        # 2. Combined Markdown
        combined = []
        for entry in page_entries:
            combined.append(f"<!-- Page {entry['page_number']} -->\n")
            combined.append(entry["raw_markdown"])
            combined.append("\n\n---\n\n")
        (output_dir / "full_course.md").write_text(
            "\n".join(combined), encoding="utf-8"
        )

        # 3. Per-page structured JSON
        (output_dir / "structured_data.json").write_text(
            json.dumps(page_entries, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

        # 4. Flat chunks (this is what Phase 2 reads)
        all_chunks: List[Dict[str, Any]] = []
        for entry in page_entries:
            all_chunks.extend(entry["chunks"])

        (output_dir / "chunks.json").write_text(
            json.dumps(all_chunks, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        logger.info("Saved %d chunks → %s/chunks.json", len(all_chunks), output_dir)

        # 5. Summary statistics
        content_type_counts: Dict[str, int] = {}
        for chunk in all_chunks:
            ct = chunk["content_type"]
            content_type_counts[ct] = content_type_counts.get(ct, 0) + 1

        summary = {
            "source_file":     Path(file_meta.pdf_path).name,
            "subject":         file_meta.subject,
            "level":           file_meta.level,
            "language":        file_meta.language,
            "pages_processed": len(page_entries),
            "total_chunks":    len(all_chunks),
            "total_chars":     sum(e["char_count"] for e in page_entries),
            "total_math":      sum(len(e["math_formulas"]) for e in page_entries),
            "content_types":   content_type_counts,
        }
        (output_dir / "summary.json").write_text(
            json.dumps(summary, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        logger.info("Summary: %s", summary)

        return all_chunks

    # ── HuggingFace Hub push ──────────────────────────────────────────

    def _push_to_hub(
        self,
        chunks: List[Dict[str, Any]],
        file_meta: FileMetadata,
    ) -> None:
        """Push chunks to a HuggingFace Dataset repository.

        Token resolution order:
          1. Kaggle Secrets  (HF_TOKEN) — used when running on Kaggle.
          2. Environment variable HF_TOKEN — used when running locally.
          3. config.hub_token  — set programmatically (e.g. tests).
        """
        try:
            from datasets import Dataset
            from huggingface_hub import login

            # ── Resolve token (Kaggle → env var → config) ───────────────────
            token = self.config.hub_token  # may already be set from env var

            try:
                from kaggle_secrets import UserSecretsClient
                kaggle_token = UserSecretsClient().get_secret("HF_TOKEN")
                if kaggle_token:
                    token = kaggle_token
                    logger.info("HF token loaded from Kaggle Secrets.")
            except Exception:
                # Not running on Kaggle, or secret not attached — that's fine
                pass

            if not token:
                logger.warning(
                    "HF_TOKEN not found (Kaggle secret not attached, env var not set, "
                    "config.hub_token not provided). Skipping hub push."
                )
                return

            # ── Login + push ───────────────────────────────────────────
            login(token=token)
            dataset = Dataset.from_list(chunks)

            split_name = (
                f"{file_meta.subject}_{file_meta.level}"
                .replace(" ", "_")
                .replace("-", "_")
            )
            dataset.push_to_hub(
                self.config.hub_dataset_name,
                split=split_name,
            )
            logger.info(
                "✅ Pushed %d chunks to Hub: %s  (split=%s)",
                len(chunks), self.config.hub_dataset_name, split_name,
            )

        except Exception as exc:
            logger.error("Hub push failed: %s", exc)
