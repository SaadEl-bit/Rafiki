import os
import re
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
CADRE_DIR = BASE_DIR / "Document-Data-Set" / "cadre"

CADRE_FILES = {
    "maths": "maths-cadre-reference.md",
    "physics": "physics-cadre-reference.md",
    "english": "english-cadre-reference.md",
}

SUBJECT_NAMES = {
    "maths": "Mathématiques",
    "physics": "Physique-Chimie",
    "english": "Anglais",
}

_cache = {}

def _clean_line(line: str) -> str:
    line = re.sub(r'<!--.*?-->', '', line).strip()
    return line

def _is_objective_line(text: str) -> bool:
    return bool(re.match(r'^\d+\.\d+\.\d+', text.strip()))

def _parse_objective_code(text: str) -> tuple:
    m = re.match(r'^(\d+\.\d+\.\d+)\.?\s*(.*)', text.strip())
    if m:
        return m.group(1), m.group(2).strip()
    return None, text.strip()

def parse_file(subject: str) -> dict:
    filename = CADRE_FILES.get(subject)
    if not filename:
        return {"subject": subject, "error": "Unknown subject"}
    filepath = CADRE_DIR / filename
    if not filepath.exists():
        logger.warning(f"Cadre file not found: {filepath}")
        return {"subject": subject, "error": "File not found"}

    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    struct = {
        "subject": SUBJECT_NAMES.get(subject, subject),
        "subject_key": subject,
        "type": "objectives" if subject == "maths" else "document",
        "domains": [],
        "sections": [],
    }

    current_domain = None
    current_subdomain = None

    for raw_line in lines:
        line = _clean_line(raw_line)
        if not line or line.startswith("---"):
            continue

        if line.startswith("### "):
            text = line[4:].strip()
            if current_subdomain is not None:
                code, obj_text = _parse_objective_code(text)
                current_subdomain["objectives"].append({
                    "code": code or f"{len(current_subdomain['objectives'])+1}",
                    "text": obj_text or text,
                })

        elif line.startswith("## "):
            text = line[3:].strip()
            current_subdomain = {
                "name": text,
                "objectives": [],
            }
            if current_domain is not None:
                current_domain["sub_domains"].append(current_subdomain)

        elif line.startswith("# "):
            text = line[2:].strip()

            if _is_objective_line(text):
                if current_subdomain is not None:
                    code, obj_text = _parse_objective_code(text)
                    current_subdomain["objectives"].append({
                        "code": code or f"{len(current_subdomain['objectives'])+1}",
                        "text": obj_text or text,
                    })
            else:
                current_domain = {
                    "name": text,
                    "sub_domains": [],
                }
                struct["domains"].append(current_domain)
                current_subdomain = None

        else:
            if subject != "maths":
                struct["sections"].append({
                    "type": "text",
                    "content": line,
                })

    for domain in struct["domains"]:
        for sub in domain["sub_domains"]:
            for i, obj in enumerate(sub["objectives"]):
                if obj["code"] and not obj["code"].startswith("1."):
                    _, rest = _parse_objective_code(obj["text"])
                    if rest:
                        obj["text"] = rest

    return struct

def get_cadre(subject: str = None) -> list:
    if subject:
        key = f"cadre_{subject}"
        if key not in _cache:
            _cache[key] = parse_file(subject)
        return [_cache[key]]

    result = []
    for subj in CADRE_FILES:
        key = f"cadre_{subj}"
        if key not in _cache:
            _cache[key] = parse_file(subj)
        result.append(_cache[key])
    return result
