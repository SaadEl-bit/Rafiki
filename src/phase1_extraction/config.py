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
    """
    MVP subjects: 2ème Bac (Maths, Physics, English).
    Post-MVP: extend with SVT, Philosophie, Arabic, etc.
    """
    MATHEMATIQUES   = "Mathématiques"
    PHYSIQUE_CHIMIE = "Physique-Chimie"
    ENGLISH         = "English"


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
    # We use the HuggingFace ID by default. Kaggle will download it automatically
    # using its fast internet connection.
    model_name: str = "Qwen/Qwen2.5-VL-2B-Instruct"
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

    # ── Curriculum metadata ───────────────────────────────────────────
    # MVP is 2ème Bac only. Level is ALWAYS 2Bac — never changes.
    # Subject is auto-detected from the filename in FileMetadata.from_path().
    default_subject: str = Subject.MATHEMATIQUES.value   # fallback if filename unrecognised
    default_level: str   = BacLevel.DEUXIEME_BAC.value   # FIXED: 2Bac only
    default_language: str = "fr"                          # French for Maths & PC; English overrides below
    default_specialization: str = Specialization.SCIENCES_MATHS_A.value
    curriculum: str = "Moroccan National Bac Curriculum 2ème Bac"


# ---------------------------------------------------------------------------
# Per-file metadata (used when processing a whole folder)
# ---------------------------------------------------------------------------

@dataclass
class FileMetadata:
    """
    Metadata for a single PDF file.

    MVP naming convention (any separator works: dash, underscore, space):
        Maths-cours.pdf        → subject=Mathématiques, level=2Bac, lang=fr
        Physique-exercices.pdf → subject=Physique-Chimie, level=2Bac, lang=fr
        English-cours.pdf      → subject=English,         level=2Bac, lang=en

    Files that do NOT match any of the 3 MVP subjects are SKIPPED with a warning.
    """
    pdf_path: Path
    subject: str
    level: str
    language: str        = "fr"
    specialization: str  = ""
    chapter: str         = ""   # optional — filled from PDF content later

    # Sentinel used to mark an unrecognised file so the pipeline can skip it.
    UNKNOWN_SUBJECT = "__UNKNOWN__"

    # Keywords that map to each MVP subject
    _SUBJECT_KEYWORDS: dict = None   # initialised as a class var below

    @classmethod
    def from_path(cls, path: Path, config: PipelineConfig) -> "FileMetadata":
        """
        Detect subject from filename.
        Level is ALWAYS 2Bac (MVP constraint — no need to detect from filename).
        Language defaults to French; English PDFs get lang=en automatically.
        """
        import logging
        logger = logging.getLogger(__name__)

        stem_lower = path.stem.lower()   # e.g. "english-cours", "maths-fonctions"

        # ── Subject detection ─────────────────────────────────────────────
        if any(k in stem_lower for k in ("math", "maths")):
            subject  = Subject.MATHEMATIQUES.value
            language = "fr"
        elif any(k in stem_lower for k in ("pc", "physique", "chimie")):
            subject  = Subject.PHYSIQUE_CHIMIE.value
            language = "fr"
        elif any(k in stem_lower for k in ("english", "anglais")):
            subject  = Subject.ENGLISH.value
            language = "en"   # English PDFs are in English, not French
        else:
            # File is not part of the MVP — skip it.
            logger.warning(
                "Skipping '%s': subject not recognised. "
                "MVP only supports: Maths, Physique-Chimie, English.",
                path.name,
            )
            return cls(
                pdf_path=path,
                subject=cls.UNKNOWN_SUBJECT,
                level=BacLevel.DEUXIEME_BAC.value,
                language=config.default_language,
                specialization="",
            )

        # ── Level is ALWAYS 2Bac ───────────────────────────────────────────
        level = BacLevel.DEUXIEME_BAC.value

        logger.info(
            "Detected: %s → subject='%s'  level='%s'  lang='%s'",
            path.name, subject, level, language,
        )
        return cls(
            pdf_path=path,
            subject=subject,
            level=level,
            language=language,
            specialization=config.default_specialization,
        )
