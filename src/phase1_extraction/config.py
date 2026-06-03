"""
Configuration — Phase 1 PDF Extraction
=======================================
Centralises all settings for the extraction pipeline.
Supports environment variables so secrets (HF token) never touch the code.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Optional


# ---------------------------------------------------------------------------
# Moroccan Bac curriculum taxonomy
# ---------------------------------------------------------------------------

class BacLevel(str, Enum):
    """Moroccan high-school levels."""
    TRONC_COMMUN   = "TC"         # Tronc Commun  (Year 10)
    PREMIERE_BAC   = "1Bac"       # 1ère Bac      (Year 11)
    DEUXIEME_BAC   = "2Bac"       # 2ème Bac      (Year 12)


class Subject(str, Enum):
    """Core Bac subjects (extend as you add more PDFs)."""
    MATHEMATIQUES          = "Mathématiques"
    PHYSIQUE_CHIMIE        = "Physique-Chimie"
    ENGLISH                = "English"
    SVT                    = "SVT"
    FRANCAIS               = "Français"
    PHILOSOPHIE            = "Philosophie"
    HISTOIRE_GEOGRAPHIE    = "Histoire-Géographie"
    INFORMATIQUE           = "Informatique"
    ARABIC                 = "العربية"
    ISLAMIC                = "التربية الإسلامية"


class Specialization(str, Enum):
    """2Bac streams."""
    SCIENCES_MATHS_A    = "Sciences Maths A"
    SCIENCES_MATHS_B    = "Sciences Maths B"
    SVT_STREAM          = "Sciences de la Vie et de la Terre"
    PC_STREAM           = "Sciences Physiques-Chimiques"
    LETTRES             = "Lettres et Sciences Humaines"
    ORIGINAL_TEACHING   = "Enseignement Original"


# ---------------------------------------------------------------------------
# Main pipeline configuration
# ---------------------------------------------------------------------------

@dataclass
class PipelineConfig:
    """
    All settings for the Phase 1 extraction pipeline.

    Key design decisions
    --------------------
    * `input_dir`  — drop any number of PDFs here; the pipeline processes all.
    * `output_dir` — flat structure: one subfolder per PDF (named after the file).
    * `model_name` — default points to the Kaggle-cached Qwen model path;
                     override with an HF model ID for internet-enabled runs.
    * `use_vlm`    — set False for a fast CPU text-only fallback (no GPU needed),
                     useful for testing the rest of the pipeline locally.
    """

    # ── Input / Output ────────────────────────────────────────────────────
    input_dir: str = "data/raw_pdfs"
    output_dir: str = "data/extracted"

    # ── Vision-Language Model ─────────────────────────────────────────────
    # On Kaggle with the model added as a Dataset input, use the local path.
    # If internet is ON in the notebook, use the HuggingFace model ID instead.
    model_name: str = (
        "/kaggle/input/qwen2-5-vl/transformers/2b-instruct/1"
        # Fallback (internet ON): "Qwen/Qwen2.5-VL-2B-Instruct"
    )
    use_vlm: bool = True          # False → fast text-only fallback (CPU)
    max_new_tokens: int = 2048
    temperature: float = 0.1
    top_p: float = 0.9

    # ── PDF rendering ─────────────────────────────────────────────────────
    dpi: int = 150                # 150 saves VRAM vs 200; enough for A4 text
    start_page: int = 0           # 0-indexed; skip cover/TOC if needed
    end_page: Optional[int] = None  # None = all pages

    # ── HuggingFace Hub ───────────────────────────────────────────────────
    push_to_hub: bool = False
    hub_dataset_name: str = "Saad-Elouakate/AI-Adaptive-Learning"
    hub_token: Optional[str] = field(
        default_factory=lambda: os.getenv("HF_TOKEN")
    )

    # ── Curriculum metadata (applied to ALL PDFs in one run) ──────────────
    # Override these per-file via the FileMetadata helper below.
    # Defaults for the MVP: 2Bac Maths (auto-overridden from filename)
    default_subject: str = Subject.MATHEMATIQUES.value
    default_level: str   = BacLevel.DEUXIEME_BAC.value
    default_language: str = "fr"
    default_specialization: str = Specialization.SCIENCES_MATHS_A.value
    curriculum: str = "Moroccan National Bac Curriculum"


# ---------------------------------------------------------------------------
# Per-file metadata (used when processing a whole folder)
# ---------------------------------------------------------------------------

@dataclass
class FileMetadata:
    """
    Metadata for a single PDF file.

    The pipeline auto-detects subject/level from the filename if you follow
    the naming convention:  <Subject>_<Level>_<title>.pdf
    e.g.   Maths_2Bac_Probabilites.pdf
           PC_1Bac_Ondes.pdf
    """
    pdf_path: Path
    subject: str
    level: str
    language: str        = "fr"
    specialization: str  = ""
    chapter: str         = ""    # optional — filled from PDF content

    @classmethod
    def from_path(cls, path: Path, config: PipelineConfig) -> "FileMetadata":
        """
        Auto-populate metadata from filename where possible,
        falling back to config defaults.
        """
        stem = path.stem  # e.g. "Maths_2Bac_Probabilites"
        parts = stem.split("_")

        subject = config.default_subject
        level   = config.default_level

        # Simple heuristics — extend to your naming convention
        for part in parts:
            part_lower = part.lower()
            if part_lower in ("1bac", "tc", "tronc"):
                level = BacLevel.PREMIERE_BAC.value if "1" in part_lower else BacLevel.TRONC_COMMUN.value
            elif part_lower in ("2bac",):
                level = BacLevel.DEUXIEME_BAC.value
            elif part_lower in ("math", "maths"):
                subject = Subject.MATHEMATIQUES.value
            elif part_lower in ("pc", "physique"):
                subject = Subject.PHYSIQUE_CHIMIE.value
            elif part_lower in ("english", "anglais"):
                subject = Subject.ENGLISH.value
            elif part_lower in ("svt",):
                subject = Subject.SVT.value
            elif part_lower in ("philo",):
                subject = Subject.PHILOSOPHIE.value

        return cls(
            pdf_path=path,
            subject=subject,
            level=level,
            language=config.default_language,
            specialization=config.default_specialization,
        )
