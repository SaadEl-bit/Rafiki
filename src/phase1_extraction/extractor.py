"""
Extractor — Phase 1
====================
Two extraction strategies:

1. VLMExtractor  — uses Qwen2.5-VL-2B (requires GPU / Kaggle).
                   Understands diagrams, tables, and hand-written math.

2. TextExtractor — pure PyMuPDF text dump (CPU, instant).
                   Good for:  testing the pipeline structure locally,
                              clean digital PDFs with no images/diagrams.

The pipeline (pipeline.py) picks the right one based on config.use_vlm.
"""

from __future__ import annotations

import logging
import time
from abc import ABC, abstractmethod
from typing import Optional

from PIL import Image

logger = logging.getLogger(__name__)


# ─────────────────────────────────────────────────────────────────────────────
# Base interface
# ─────────────────────────────────────────────────────────────────────────────

class BaseExtractor(ABC):
    """Common interface for both extraction strategies."""

    @abstractmethod
    def extract(
        self,
        image: Image.Image,
        page_num: int,
        total_pages: int,
        raw_text_hint: str = "",
    ) -> str:
        """Return structured Markdown for one page."""
        ...

    def close(self) -> None:
        """Release GPU memory / model resources if applicable."""


# ─────────────────────────────────────────────────────────────────────────────
# Strategy 1 — Vision-Language Model (Qwen2.5-VL-2B)
# ─────────────────────────────────────────────────────────────────────────────

class VLMExtractor(BaseExtractor):
    """
    Uses Qwen2.5-VL-2B-Instruct to parse PDF page images into Markdown.

    Requires:
        transformers>=4.49.0, qwen-vl-utils, accelerate, torch (CUDA)

    Memory footprint: ~4 GB VRAM in bfloat16 on a T4 GPU.
    """

    EXTRACTION_PROMPT = """\
You are an AI assistant for the Rafiki project, extracting Moroccan Bac curriculum content from PDF pages.

Page {page} of {total}

Your task is to extract ALL content from this page image and convert it to clean Markdown.

RULES:
- Preserve the exact academic content (definitions, theorems, formulas, proofs, examples, exercises)
- Write ALL mathematical formulas in LaTeX:
    • Inline math:   $...$
    • Display math:  $$...$$
- Use proper Markdown headings:
    • # for chapter title
    • ## for main section
    • ### for subsection
- Format special blocks:
    • **Définition :**  ...
    • **Théorème :**    ...
    • **Démonstration :**  ...
    • **Exemple X :**   ...
    • **Exercice X :**  ...
    • **Propriété :**   ...
    • **Remarque :**    ...
- Keep original French or Arabic text exactly as written
- Format tables as Markdown tables
- If a figure/diagram is present, note it as: [Diagram: brief description]
- Extract EVERYTHING — do not skip any content

Output ONLY the Markdown content, no preamble or commentary.
"""

    def __init__(self, model_name: str, max_new_tokens: int = 2048,
                 temperature: float = 0.1, top_p: float = 0.9):
        self.model_name = model_name
        self.max_new_tokens = max_new_tokens
        self.temperature = temperature
        self.top_p = top_p
        self._model = None
        self._processor = None
        self._device = None

    # ── Loading ───────────────────────────────────────────────────────────

    def load(self) -> "VLMExtractor":
        """Load model + processor. Call once before processing pages."""
        import torch
        from transformers import AutoModelForImageTextToText, AutoProcessor

        self._device = "cuda" if torch.cuda.is_available() else "cpu"
        logger.info("Loading VLM: %s  (device=%s)", self.model_name, self._device)

        # Attempt flash attention 2; fall back to SDPA silently
        attn = "sdpa"
        try:
            import flash_attn  # noqa: F401
            attn = "flash_attention_2"
            logger.info("Using Flash Attention 2")
        except ImportError:
            logger.info("flash_attn not found — using SDPA")

        self._model = AutoModelForImageTextToText.from_pretrained(
            self.model_name,
            torch_dtype=torch.bfloat16,
            device_map="auto",
            attn_implementation=attn,
        )
        self._processor = AutoProcessor.from_pretrained(
            self.model_name,
            min_pixels=256 * 256,
            max_pixels=768 * 768,
        )
        logger.info("VLM loaded successfully")
        return self

    # ── Extraction ────────────────────────────────────────────────────────

    def extract(
        self,
        image: Image.Image,
        page_num: int,
        total_pages: int,
        raw_text_hint: str = "",
    ) -> str:
        import torch

        prompt_text = self.EXTRACTION_PROMPT.format(
            page=page_num + 1, total=total_pages
        )
        if raw_text_hint.strip():
            prompt_text += (
                f"\n\nRaw text from this page (use as reference only):\n"
                f"{raw_text_hint[:500]}"
            )

        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "image", "image": image},
                    {"type": "text",  "text": prompt_text},
                ],
            }
        ]

        text = self._processor.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        inputs = self._processor(
            text=[text],
            images=[image],
            padding=True,
            return_tensors="pt",
        )
        if self._device == "cuda":
            inputs = inputs.to("cuda")

        with torch.no_grad():
            generated_ids = self._model.generate(
                **inputs,
                max_new_tokens=self.max_new_tokens,
                temperature=self.temperature,
                top_p=self.top_p,
                do_sample=True,
            )

        trimmed = [
            out[len(inp):]
            for inp, out in zip(inputs.input_ids, generated_ids)
        ]
        output = self._processor.batch_decode(
            trimmed,
            skip_special_tokens=True,
            clean_up_tokenization_spaces=False,
        )[0]

        return output.strip()

    def close(self) -> None:
        """Free GPU memory."""
        if self._model is not None:
            import torch
            del self._model
            del self._processor
            self._model = None
            self._processor = None
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
            logger.info("VLM unloaded and GPU memory freed")


# ─────────────────────────────────────────────────────────────────────────────
# Strategy 2 — Text-only fallback (CPU, no model needed)
# ─────────────────────────────────────────────────────────────────────────────

class TextExtractor(BaseExtractor):
    """
    Fast, CPU-only fallback: returns PyMuPDF raw text wrapped in basic Markdown.

    Useful for:
    • Testing the full pipeline structure without a GPU.
    • Digital-native PDFs that have clean embedded text (no scanned images).

    Limitations:
    • Will NOT reconstruct math formulas from scanned/image PDFs.
    • Layout reconstruction is basic.
    """

    def extract(
        self,
        image: Image.Image,          # unused — kept for interface compatibility
        page_num: int,
        total_pages: int,
        raw_text_hint: str = "",
    ) -> str:
        if not raw_text_hint.strip():
            return f"<!-- Page {page_num + 1}: no text extracted -->"

        # Very light formatting — enough to feed the chunker
        lines = []
        for line in raw_text_hint.splitlines():
            stripped = line.strip()
            if not stripped:
                lines.append("")
                continue
            # Heuristic: short ALL-CAPS lines are likely headings
            if stripped.isupper() and len(stripped) < 60:
                lines.append(f"## {stripped}")
            else:
                lines.append(stripped)

        return "\n".join(lines).strip()
