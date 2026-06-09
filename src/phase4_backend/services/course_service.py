import os
import re
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
COURSE_DIR = BASE_DIR / "Document-Data-Set" / "courses"

COURSE_FILES = {
    "maths": "maths-course.md",
    "physics": "physics-course.md",
    "english": "english-course.md",
}

SUBJECT_NAMES = {
    "maths": "Mathématiques",
    "physics": "Physique-Chimie",
    "english": "Anglais",
}

_cache = {}

def extract_chapters(markdown: str) -> list[dict]:
    chapters = []
    for line in markdown.split("\n"):
        m = re.match(r'^##\s+(.+)$', line.strip())
        if m:
            chapters.append({"title": m.group(1).strip(), "anchor": m.group(1).strip().lower().replace(" ", "-").replace("–", "-").replace("'", "").replace("/", "-").replace("(", "").replace(")", "").replace(",", "").replace(".", "")})
    return chapters

def get_course(subject: str) -> dict:
    cache_key = f"course_{subject}"
    if cache_key in _cache:
        return _cache[cache_key]

    filename = COURSE_FILES.get(subject)
    if not filename:
        return {"error": "Unknown subject", "subject": subject}

    filepath = COURSE_DIR / filename
    if not filepath.exists():
        logger.warning(f"Course file not found: {filepath}")
        return {"error": "File not found", "subject": subject}

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    chapters = extract_chapters(content)

    result = {
        "subject": SUBJECT_NAMES.get(subject, subject),
        "subject_key": subject,
        "content": content,
        "chapters": chapters,
    }
    _cache[cache_key] = result
    return result

def list_courses() -> list[dict]:
    result = []
    for subj in COURSE_FILES:
        course = get_course(subj)
        if "error" not in course:
            result.append({
                "subject": course["subject"],
                "subject_key": course["subject_key"],
                "chapters": course["chapters"],
            })
    return result
