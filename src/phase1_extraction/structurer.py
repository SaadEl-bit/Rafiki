"""
Content Structurer — Phase 1
=============================
Post-processes raw Markdown extracted by the VLM or TextExtractor into
clean, chunked, typed curriculum entries ready for Phase 2 embedding.

Output schema (per chunk) — matches what Phase 2 ChromaDB expects:
{
    "chunk_id":       "Maths_2Bac_p03_chunk_02",
    "source_file":    "Maths_2Bac_Probabilites.pdf",
    "page_number":    3,
    "subject":        "Mathématiques",
    "level":          "2Bac",
    "language":       "fr",
    "specialization": "Sciences Maths A",
    "chapter":        "Probabilités et Statistiques",
    "section_title":  "Probabilité conditionnelle",
    "content_type":   "theorem",          # definition/theorem/example/exercise/…
    "content":        "## Probabilité ...",
    "math_formulas":  ["P(B|A) = ...", ...],
    "char_count":     342,
}
"""

from __future__ import annotations

import re
import unicodedata
from pathlib import Path
from typing import Any, Dict, List


# ─────────────────────────────────────────────────────────────────────────────
# Content type detection
# ─────────────────────────────────────────────────────────────────────────────

_CONTENT_TYPES: List[tuple[str, List[str]]] = [
    ("exercise",    ["exercice", "exercise", "travaux dirigés", "td"]),
    ("solution",    ["solution", "correction", "corrigé"]),
    ("definition",  ["définition", "definition", "def."]),
    ("theorem",     ["théorème", "theoreme", "theorem", "corollaire", "lemme"]),
    ("proof",       ["démonstration", "demonstration", "preuve", "proof"]),
    ("property",    ["propriété", "propriete", "property"]),
    ("example",     ["exemple", "example"]),
    ("remark",      ["remarque", "note", "observation"]),
    ("method",      ["méthode", "methode", "algorithme", "étapes", "démarche"]),
    ("formula",     ["formule", "formula"]),
    ("summary",     ["résumé", "bilan", "synthèse"]),
]


def detect_content_type(text: str) -> str:
    text_lower = text.lower()
    for content_type, keywords in _CONTENT_TYPES:
        if any(kw in text_lower for kw in keywords):
            return content_type
    return "course_content"


# ─────────────────────────────────────────────────────────────────────────────
# Markdown cleaning
# ─────────────────────────────────────────────────────────────────────────────

def clean_markdown(text: str) -> str:
    """Normalise common VLM output quirks."""
    # Strip markdown code fences the VLM sometimes wraps output in
    text = re.sub(r"^```(?:markdown)?\s*\n", "", text, flags=re.MULTILINE)
    text = re.sub(r"\n```\s*$", "", text, flags=re.MULTILINE)

    # Collapse 3+ blank lines → 2
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Normalise LaTeX delimiters (the VLM sometimes uses \[ \] or \( \))
    text = text.replace("\\[", "$$").replace("\\]", "$$")
    text = text.replace("\\(", "$").replace("\\)", "$")

    # Fix broken Unicode that sometimes appears in OCR output
    text = unicodedata.normalize("NFC", text)

    # Remove trailing whitespace on each line
    text = "\n".join(line.rstrip() for line in text.splitlines())

    return text.strip()


# ─────────────────────────────────────────────────────────────────────────────
# Math formula extraction
# ─────────────────────────────────────────────────────────────────────────────

def extract_math_formulas(text: str) -> List[str]:
    display = re.findall(r"\$\$(.*?)\$\$", text, re.DOTALL)
    inline  = re.findall(r"(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)", text)
    return [f.strip() for f in display + inline if f.strip()]


# ─────────────────────────────────────────────────────────────────────────────
# Heading-based chunker
# ─────────────────────────────────────────────────────────────────────────────

def chunk_by_headings(markdown_text: str) -> List[Dict[str, Any]]:
    """
    Split a Markdown document into chunks on ## and ### headings.
    Each chunk is a self-contained curriculum unit (section / subsection).
    """
    lines = markdown_text.split("\n")
    chunks: List[Dict[str, Any]] = []
    current_lines: List[str] = []
    current_heading = "preamble"

    def _flush(heading: str, lines: List[str]) -> None:
        chunk_text = "\n".join(lines).strip()
        if chunk_text:
            chunks.append({
                "section_title": heading,
                "content_type":  detect_content_type(chunk_text),
                "content":       chunk_text,
                "math_formulas": extract_math_formulas(chunk_text),
                "char_count":    len(chunk_text),
            })

    for line in lines:
        m = re.match(r"^(#{2,3})\s+(.+)$", line)
        if m:
            _flush(current_heading, current_lines)
            current_heading = m.group(2).strip()
            current_lines = [line]
        else:
            current_lines.append(line)

    _flush(current_heading, current_lines)
    return chunks


# ─────────────────────────────────────────────────────────────────────────────
# Chunk ID generation
# ─────────────────────────────────────────────────────────────────────────────

def _slugify(text: str) -> str:
    """Create a filename-safe slug from an arbitrary string."""
    text = unicodedata.normalize("NFD", text)
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    text = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[\s_-]+", "_", text).strip("_")


def make_chunk_id(source_stem: str, page_num: int, chunk_idx: int) -> str:
    return f"{_slugify(source_stem)}_p{page_num:02d}_c{chunk_idx:02d}"


# ─────────────────────────────────────────────────────────────────────────────
# Main builder — called by the pipeline for each page
# ─────────────────────────────────────────────────────────────────────────────

def build_page_entry(
    page_num: int,
    raw_markdown: str,
    file_meta: Any,      # FileMetadata from config.py
) -> Dict[str, Any]:
    """
    Build a structured entry for one PDF page.
    Returns the full record that the pipeline stores in structured_data.json.
    """
    cleaned = clean_markdown(raw_markdown)
    chunks  = chunk_by_headings(cleaned)
    source_stem = Path(file_meta.pdf_path).stem

    # Enrich each chunk with full metadata + a unique ID
    enriched_chunks = []
    for idx, chunk in enumerate(chunks):
        enriched_chunks.append({
            "chunk_id":       make_chunk_id(source_stem, page_num + 1, idx),
            "source_file":    Path(file_meta.pdf_path).name,
            "page_number":    page_num + 1,
            "subject":        file_meta.subject,
            "level":          file_meta.level,
            "language":       file_meta.language,
            "specialization": file_meta.specialization,
            "chapter":        file_meta.chapter,
            **chunk,  # section_title, content_type, content, math_formulas, char_count
        })

    return {
        "page_number":    page_num + 1,
        "source_file":    Path(file_meta.pdf_path).name,
        "subject":        file_meta.subject,
        "level":          file_meta.level,
        "language":       file_meta.language,
        "specialization": file_meta.specialization,
        "raw_markdown":   cleaned,
        "chunks":         enriched_chunks,
        "total_chunks":   len(enriched_chunks),
        "math_formulas":  extract_math_formulas(cleaned),
        "char_count":     len(cleaned),
    }
