import logging
from src.phase4_backend.services.llm_service import generate_content
from src.phase4_backend.services.rag_service import retrieve_context
from src.phase4_backend.services.course_service import list_courses
import json
import re

logger = logging.getLogger(__name__)

TOPICS_CACHE = None

def get_topics() -> dict:
    global TOPICS_CACHE
    if TOPICS_CACHE:
        return TOPICS_CACHE
    topics = {}
    courses = list_courses()
    for c in courses:
        chapter_titles = [ch["title"] for ch in c["chapters"]]
        topics[c["subject_key"]] = {
            "display_name": c["subject"],
            "topics": chapter_titles,
        }
    TOPICS_CACHE = topics
    return topics

SUBJECT_DISPLAY = {"maths": "Mathématiques", "physics": "Physique-Chimie", "english": "Anglais"}

def generate_exercise(subject_key: str, topic: str) -> dict:
    subject_display = SUBJECT_DISPLAY.get(subject_key, subject_key)

    query = f"Générer un exercice de {subject_display} sur le thème: {topic}"
    context = retrieve_context(query, subject=subject_display)

    system_prompt = (
        f"Vous êtes Rafiki, un professeur de {subject_display} pour le Bac marocain (2ème Bac).\n"
        "Générez UN SEUL exercice avec sa solution complète et détaillée.\n"
        "L'exercice doit correspondre au programme 2ème Bac marocain.\n"
        "Utilisez le contexte du cours fourni ci-dessous.\n"
        "Répondez en français.\n"
        "Utilisez LaTeX ($...$ ou $$...$$) pour toutes les formules mathématiques.\n\n"
        "Votre réponse doit avoir EXACTEMENT ce format, en deux sections séparées par le marqueur '---SOLUTION---':\n\n"
        "## Exercice\n"
        "[énoncé de l'exercice]\n\n"
        "---SOLUTION---\n\n"
        "## Solution\n"
        "[solution détaillée étape par étape]"
    )

    instruction = (
        f"Génère UN exercice de {subject_display} sur le thème '{topic}'.\n"
        "L'exercice doit être de niveau 2ème Bac marocain.\n"
        "Écris d'abord l'énoncé, puis la solution détaillée."
    )

    raw = generate_content(
        context=context,
        instruction=instruction,
        system_prompt=system_prompt,
        max_tokens=2500,
        temperature=0.4,
    )

    exercise, solution = _split_response(raw)

    return {
        "subject": subject_display,
        "topic": topic,
        "exercise": exercise,
        "solution": solution,
    }

def _split_response(raw: str) -> tuple[str, str]:
    parts = re.split(r'---SOLUTION---|---\s*Solution\s*---', raw, maxsplit=1, flags=re.IGNORECASE)
    if len(parts) == 2:
        exercise = parts[0].strip()
        solution = parts[1].strip()
        exercise = re.sub(r'^##\s*Exercice\s*', '', exercise).strip()
        solution = re.sub(r'^##\s*Solution\s*', '', solution).strip()
        return exercise, solution
    return raw.strip(), ""
