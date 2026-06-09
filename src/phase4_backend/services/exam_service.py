import json
import os
import logging
import re
from pathlib import Path
from src.phase4_backend.services.llm_service import generate_content
from src.phase4_backend.services.rag_service import retrieve_context

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
EXAM_DIR = BASE_DIR / "Document-Data-Set" / "Fine-Tunning"

EXAM_FILES = {
    "maths": ["Maths/Maths-examen-1.json", "Maths/Maths-examen-2.json", "Maths/Maths-examen-3.json"],
    "physics": ["Physics/physics-exam-1.json", "Physics/physics-exam-2.json"],
    "english": ["English/english_exam_1.json", "English/english_exam_2.json"],
}

SUBJECT_NAMES = {
    "maths": "Mathématiques",
    "physics": "Physique-Chimie",
    "english": "Anglais",
}

_exam_cache = {}

def _load_exam(filepath: str) -> dict:
    full_path = EXAM_DIR / filepath
    if not full_path.exists():
        logger.warning(f"Exam file not found: {full_path}")
        return None
    with open(full_path, "r", encoding="utf-8") as f:
        return json.load(f)

def _get_exam_pairs(exam: dict) -> list[dict]:
    pairs = []
    q_keys = sorted([k for k in exam if not k.startswith("Corr ") and k != "subject"])
    for qk in q_keys:
        corr_key = f"Corr {qk}"
        pairs.append({
            "question": qk,
            "question_text": exam[qk],
            "correction": exam.get(corr_key, ""),
        })
    return pairs

def get_format_exam(subject_key: str, exam_index: int = 0) -> dict:
    cache_key = f"exam_format_{subject_key}_{exam_index}"
    if cache_key in _exam_cache:
        return _exam_cache[cache_key]

    files = EXAM_FILES.get(subject_key, [])
    if not files or exam_index >= len(files):
        files = EXAM_FILES.get(subject_key, [])
        exam_index = 0

    exam = _load_exam(files[exam_index])
    if not exam:
        return None

    pairs = _get_exam_pairs(exam)

    result = {
        "subject": exam.get("subject", ""),
        "subject_key": subject_key,
        "pairs": pairs,
    }
    _exam_cache[cache_key] = result
    return result

def generate_exam(subject_key: str, topic: str = "") -> dict:
    subject_display = SUBJECT_NAMES.get(subject_key, subject_key)

    query = f"Générer un examen de {subject_display}"
    if topic:
        query += f" sur le thème: {topic}"
    context = retrieve_context(query, subject=subject_display)

    format_exam = get_format_exam(subject_key, 0)
    if not format_exam:
        return {"error": "Aucun examen de référence trouvé"}

    format_json = json.dumps(format_exam["pairs"], ensure_ascii=False, indent=2)

    system_prompt = (
        f"Vous êtes Rafiki, un professeur de {subject_display} pour le Bac marocain (2ème Bac).\n"
        "Générez un NOUVEL examen complet en suivant EXACTEMENT le format JSON fourni.\n"
        "Utilisez le contexte du cours fourni ci-dessous.\n"
        "Chaque question doit avoir sa correction détaillée.\n"
        "Répondez en français.\n"
        "Utilisez LaTeX pour toutes les formules mathématiques.\n\n"
        "Votre réponse doit être UNIQUEMENT un objet JSON valide, sans texte avant ni après.\n"
        "Le JSON doit avoir exactement la même structure que l'exemple.\n"
        "Propriétés: 'subject' (string) et les paires question/correction comme dans l'exemple."
    )

    instruction = (
        f"Génère un NOUVEL examen de {subject_display}"
        + (f" sur le thème '{topic}'" if topic else "")
        + ".\n\n"
        "Voici un exemple du format à suivre (questions et corrections d'un examen réel):\n"
        f"{format_json}\n\n"
        "Génère un examen COMPLET avec le même nombre de questions, "
        "en respectant la même structure JSON.\n"
        "Réponds UNIQUEMENT avec le JSON."
    )

    raw = generate_content(
        context=context,
        instruction=instruction,
        system_prompt=system_prompt,
        max_tokens=4000,
        temperature=0.4,
    )

    parsed = _parse_json_response(raw)
    if "error" in parsed:
        return parsed

    pairs = _get_exam_pairs(parsed)
    return {
        "subject": subject_display,
        "subject_key": subject_key,
        "topic": topic or "Général",
        "pairs": pairs,
        "exam_title": parsed.get("subject", f"Examen de {subject_display} (Généré)"),
    }

def _parse_json_response(raw: str) -> dict:
    json_match = re.search(r'\{.*\}', raw, re.DOTALL)
    if not json_match:
        return {"error": "Le modèle n'a pas généré un JSON valide"}

    try:
        return json.loads(json_match.group())
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse exam JSON: {e}")
        return {"error": f"Erreur de parsing du JSON: {str(e)}"}
