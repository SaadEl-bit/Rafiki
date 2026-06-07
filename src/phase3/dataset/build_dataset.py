#!/usr/bin/env python3
"""
build_dataset.py — Phase 3 Q&A Triplet Builder

Generates {input, thinking, output} triplets from all 8 Phase 1 chunk folders.
Pushes the resulting dataset to HuggingFace.

Strategies per folder:
  - pair_exercise_solution:  Maths corriges (14 exercises + 14 solutions)
  - convert_concept_qna:      Maths cours, Physics cours (definitions, theorems)
  - convert_cadre_objectives: 3 cadre de reference folders
  - convert_english_cours:    English cours
  - convert_english_examen:   English examen

Usage:
    python -m src.phase3.dataset.build_dataset --push-to-hub
    python -m src.phase3.dataset.build_dataset               # dry-run, print stats
"""

import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

try:
    from datasets import Dataset
    _HF_AVAILABLE = True
except ImportError:
    _HF_AVAILABLE = False

# --- Constants -------------------------------------------------------------

EXTRACTED_DIR = Path("output") / "phase1-extracted"
HUB_DATASET = "Saad-Elouakate/rafiki-qna-triplets"

TARGET_RANGE = (150, 500)
MAX_INPUT_CHARS = 3000
MAX_OUTPUT_CHARS = 7000
BAD_EXERCISE_PAIR_CHUNK_IDS = {
    # Source extraction mixed unrelated statements/solutions in these chunks.
    "maths_fonctions_corrige_serie_d_exercices_p01_c05",
    "maths_fonctions_corrige_serie_d_exercices_p04_c07",
}

# --- Subjects & Languages --------------------------------------------------

SUBJECT_TAGS = {
    # folder: (document_type, subject, language)
    "cadre-de-reference-english": ("cadre_reference", "english", "en"),
    "cadre-de-reference-maths": ("cadre_reference", "mathematics", "fr"),
    "cadre-de-reference-physique": ("cadre_reference", "physics", "fr"),
    "English-cours": ("course", "english", "en"),
    "English-examen": ("exam", "english", "en"),
    "Maths-fonctions-corrige-serie-d-exercices": ("corrected_exercises", "mathematics", "fr"),
    "Maths-fonctions-cours": ("course", "mathematics", "fr"),
    "Physique-lois-de-newton-cours-Exercices": ("course_exercises", "physics", "fr"),
}

SYSTEM_MESSAGE = (
    "You are Rafiki, a Moroccan 2Bac professor. Explain concepts clearly and step by step, "
    "using appropriate terminology for the Moroccan baccalaureate curriculum."
)

# --- Helpers ---------------------------------------------------------------


def load_chunks(folder: Path) -> List[Dict]:
    with open(folder / "chunks.json", "r", encoding="utf-8") as f:
        return json.load(f)


def clean_text(text: str) -> str:
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def eprint(msg: str):
    """Print without Unicode to avoid Windows cp1252 errors."""
    safe = msg.encode("ascii", errors="replace").decode("ascii")
    print(safe)


def get_tags(folder_name: str) -> Tuple[str, str, str]:
    document_type, subject, lang = SUBJECT_TAGS.get(
        folder_name, ("unknown", "unknown", "fr")
    )
    return document_type, subject, lang


def make_triplet(
    input: str,
    thinking: str,
    output: str,
    subject: str,
    lang: str,
    source: str,
    chunk_id: str,
    content_type: str = "",
    document_type: str = "",
) -> Dict:
    return {
        "input": clean_text(input),
        "thinking": clean_text(thinking),
        "output": clean_text(output),
        "subject": subject,
        "language": lang,
        "document_type": document_type,
        "source": source,
        "chunk_id": chunk_id,
        "content_type": content_type,
    }


def build_template_messages(sample: Dict) -> List[Dict]:
    return [
        {"role": "system", "content": SYSTEM_MESSAGE},
        {"role": "user", "content": sample["input"]},
        {
            "role": "assistant",
            "content": f"<think>\n{sample['thinking']}\n</think>\n{sample['output']}"
            if sample["thinking"]
            else sample["output"],
        },
    ]


def format_chat_text(sample: Dict) -> str:
    system = SYSTEM_MESSAGE
    user = sample["input"]
    thinking = sample.get("thinking", "") or ""
    output = sample["output"]

    if thinking.strip():
        assistant = f"<think>\n{thinking}\n</think>\n{output}"
    else:
        assistant = output

    return (
        f"<|im_start|>system\n{system}<|im_end|>\n"
        f"<|im_start|>user\n{user}<|im_end|>\n"
        f"<|im_start|>assistant\n{assistant}<|im_end|>"
    )


def add_training_fields(sample: Dict) -> Dict:
    enriched = dict(sample)
    enriched["messages"] = build_template_messages(enriched)
    enriched["text"] = format_chat_text(enriched)
    return enriched


# --- Triplet Generation Strategies -----------------------------------------


def _extract_title(text: str) -> str:
    first_line = text.split("\n")[0].strip()
    return re.sub(r"^#+\s*", "", first_line).strip()


def _is_heading_only(text: str) -> bool:
    plain = re.sub(r"^#+\s*", "", text.strip())
    if len(plain) <= 25 and re.search(r"\b(exercice|solutions?|correction|m3allem)\b", plain, re.I):
        return True
    return bool(len(plain) <= 18 and "\n" not in text)


def _starts_exercise(text: str) -> bool:
    return bool(re.search(r"\bexercice\s*\d+\b", text, re.I))


def _is_low_quality_pair(input_text: str, output_text: str) -> bool:
    if len(input_text) < 80 or len(output_text) < 120:
        return True
    if len(input_text) > MAX_INPUT_CHARS or len(output_text) > MAX_OUTPUT_CHARS:
        return True
    if input_text.strip() == output_text.strip():
        return True
    exercise_count = len(re.findall(r"\bexercice\s*\d+\b", input_text, re.I))
    if exercise_count > 1:
        return True
    return False


def _chunk_min_len(t: str) -> int:
    return {"course_content": 200, "exercise": 50, "solution": 50}.get(t, 50)


def strategy_pair_exercise_solution(
    chunks: List[Dict], folder_name: str
) -> List[Dict]:
    """
    Walk chunks in order.
    - Accumulate exercise-like chunks (exercise, definition, course_content,
      example) that are substantial.
    - When a run of 'solution' chunks is found, merge all consecutive
      solutions (skipping any that look like headings) and pair with the
      accumulated exercise buffer.
    - Also generate concept triplets from non-exercise-solution content
      (theorems, properties, definitions that aren't part of an exercise).
    """
    document_type, subject, lang = get_tags(folder_name)
    triplets: List[Dict] = []
    pending: List[Dict] = []

    MIN_EX = 40
    MIN_SOL = 100

    i = 0
    while i < len(chunks):
        chunk = chunks[i]
        ct = chunk["content_type"]
        text = clean_text(chunk["content"])
        tlen = len(text)

        if ct == "solution":
            # merge consecutive solutions
            sol_parts: List[str] = []
            while i < len(chunks) and chunks[i]["content_type"] == "solution":
                t = clean_text(chunks[i]["content"])
                if len(t) >= MIN_SOL and not _is_heading_only(t):
                    sol_parts.append(t)
                i += 1

            if pending and sol_parts:
                sol_text = "\n\n".join(sol_parts)
                ex_parts = [
                    clean_text(c["content"])
                    for c in pending
                    if len(clean_text(c["content"])) >= MIN_EX
                    and not _is_heading_only(clean_text(c["content"]))
                ]
                ex_text = "\n\n".join(ex_parts) if ex_parts else ""
                if ex_text and not _is_low_quality_pair(ex_text, sol_text):
                    triplets.append(
                        make_triplet(
                            input=ex_text,
                            thinking=sol_text,
                            output=sol_text,
                            subject=subject,
                            lang=lang,
                            source=folder_name,
                            chunk_id=chunk["chunk_id"],
                            content_type="exercise_solution",
                            document_type=document_type,
                        )
                    )
                pending = []
            # if no pending, solutions are orphans -- skip
            continue  # i already advanced

        # ---- non-solution chunks ----
        # accumulate exercise-like content
        if ct == "exercise" and _starts_exercise(text):
            pending = []

        if ct in ("exercise", "definition", "course_content"):
            if tlen >= MIN_EX and not _is_heading_only(text):
                pending.append(chunk)

        # also generate concept triplets for theorems / properties / etc.
        if ct in ("theorem", "property", "proof", "example", "definition", "remark"):
            if tlen >= _chunk_min_len(ct):
                title = _extract_title(text)
                if ct == "theorem":
                    q = f"Enonce le theoreme suivant : {title}" if title else "Enonce le theoreme."
                elif ct == "property":
                    q = f"Quelle est la propriete concernant {title} ?" if title else "Quelle est la propriete ?"
                elif ct == "proof":
                    q = f"Demontre : {title}" if title else "Fais la demonstration."
                elif ct == "definition":
                    q = f"Definis : {title}" if title else "Donne la definition."
                elif ct == "example":
                    q = f"Donne un exemple : {title}" if title else "Donne un exemple."
                else:  # remark
                    q = f"Explique : {title}" if title else "Explique le contenu suivant."

                triplets.append(
                    make_triplet(
                        input=q,
                        thinking=text,
                        output=text,
                        subject=subject,
                        lang=lang,
                        source=folder_name,
                        chunk_id=chunk["chunk_id"],
                        content_type=ct,
                        document_type=document_type,
                    )
                )

        i += 1

    return triplets


def strategy_convert_concept_qna(
    chunks: List[Dict], folder_name: str
) -> List[Dict]:
    document_type, subject, lang = get_tags(folder_name)
    triplets: List[Dict] = []
    seen: set = set()

    for chunk in chunks:
        ct = chunk["content_type"]
        text = clean_text(chunk["content"])
        if len(text) < 50:
            continue
        if text[:100] in seen:
            continue
        seen.add(text[:100])

        title = _extract_title(text)

        if ct == "definition":
            q = f"Definis : {title}" if title else "Donne la definition."
        elif ct == "theorem":
            q = f"Enonce le theoreme suivant : {title}" if title else "Enonce le theoreme."
        elif ct == "property":
            q = f"Quelle est la propriete concernant {title} ?" if title else "Quelle est la propriete ?"
        elif ct == "example":
            q = f"Donne un exemple : {title}" if title else "Donne un exemple."
        elif ct == "course_content" and len(text) > 300:
            first_sent = text.split(".")[0].strip()
            q = f"Explique : {first_sent}." if len(first_sent) > 15 else "Explique le contenu suivant."
        else:
            continue

        triplets.append(
            make_triplet(
                input=q,
                thinking=text,
                output=text,
                subject=subject,
                lang=lang,
                source=folder_name,
                chunk_id=chunk["chunk_id"],
                content_type=ct,
                document_type=document_type,
            )
        )

    return triplets


def strategy_convert_cadre_objectives(
    chunks: List[Dict], folder_name: str
) -> List[Dict]:
    document_type, subject, lang = get_tags(folder_name)
    triplets: List[Dict] = []
    seen: set = set()

    for chunk in chunks:
        ct = chunk["content_type"]
        text = clean_text(chunk["content"])
        if len(text) < 80:
            continue
        if text[:120] in seen:
            continue
        seen.add(text[:120])

        title = _extract_title(text)

        if ct == "course_content":
            q = f"Quels sont les objectifs d'apprentissage pour {title} ?" if title and len(title) > 10 else "Quels sont les objectifs d'apprentissage dans ce cadre referenciel ?"
        elif ct == "definition":
            q = f"Definis : {title}" if title else "Donne la definition."
        elif ct == "example":
            q = f"Donne un exemple : {title}" if title else "Donne un exemple."
        elif ct == "property":
            q = f"Quelle est la propriete {title} ?" if title else "Quelle est la propriete ?"
        elif ct in ("theorem", "proof"):
            q = f"Enonce et demontre : {title}" if title else "Enonce le theoreme."
        else:
            continue

        triplets.append(
            make_triplet(
                input=q,
                thinking=text,
                output=text,
                subject=subject,
                lang=lang,
                source=folder_name,
                chunk_id=chunk["chunk_id"],
                content_type=ct,
                document_type=document_type,
            )
        )

    return triplets


def strategy_convert_english_cours(
    chunks: List[Dict], folder_name: str
) -> List[Dict]:
    document_type, subject, lang = get_tags(folder_name)
    triplets: List[Dict] = []
    seen: set = set()

    for chunk in chunks:
        ct = chunk["content_type"]
        text = clean_text(chunk["content"])
        if len(text) < 60:
            continue
        if text[:120] in seen:
            continue
        seen.add(text[:120])

        title = _extract_title(text)

        if ct == "course_content":
            q = f"Explain: {title}." if title and len(title) > 10 else "Explain the following in English."
        elif ct == "example":
            q = f"Give an example: {title}" if title else "Give an example."
        elif ct == "definition":
            q = f"Define: {title}" if title else "Define the term."
        else:
            continue

        triplets.append(
            make_triplet(
                input=q,
                thinking=text,
                output=text,
                subject=subject,
                lang=lang,
                source=folder_name,
                chunk_id=chunk["chunk_id"],
                content_type=ct,
                document_type=document_type,
            )
        )

    return triplets


def strategy_convert_english_examen(
    chunks: List[Dict], folder_name: str
) -> List[Dict]:
    document_type, subject, lang = get_tags(folder_name)
    triplets: List[Dict] = []
    seen: set = set()

    for chunk in chunks:
        ct = chunk["content_type"]
        text = clean_text(chunk["content"])
        if len(text) < 80:
            continue
        if text[:120] in seen:
            continue
        seen.add(text[:120])

        title = _extract_title(text)

        if ct == "course_content":
            q = f"Exam question: {title}" if title else "Answer the following exam question."
        else:
            continue

        triplets.append(
            make_triplet(
                input=q,
                thinking=text,
                output=text,
                subject=subject,
                lang=lang,
                source=folder_name,
                chunk_id=chunk["chunk_id"],
                content_type=ct,
                document_type=document_type,
            )
        )

    return triplets


def strategy_convert_physics(
    chunks: List[Dict], folder_name: str
) -> List[Dict]:
    document_type, subject, lang = get_tags(folder_name)
    triplets: List[Dict] = []
    seen: set = set()

    for chunk in chunks:
        ct = chunk["content_type"]
        text = clean_text(chunk["content"])
        if len(text) < 50:
            continue
        if text[:120] in seen:
            continue
        seen.add(text[:120])

        title = _extract_title(text)

        if ct == "course_content" and len(text) > 200:
            q = f"Explique : {title}." if title else "Explique le contenu."
        elif ct == "theorem":
            q = f"Enonce le theoreme : {title}" if title else "Enonce le theoreme."
        elif ct == "definition":
            q = f"Definis : {title}" if title else "Donne la definition."
        else:
            continue

        triplets.append(
            make_triplet(
                input=q,
                thinking=text,
                output=text,
                subject=subject,
                lang=lang,
                source=folder_name,
                chunk_id=chunk["chunk_id"],
                content_type=ct,
                document_type=document_type,
            )
        )

    return triplets


# --- Strategy Routing ------------------------------------------------------

STRATEGY_MAP = {
    "cadre-de-reference-english": strategy_convert_cadre_objectives,
    "cadre-de-reference-maths": strategy_convert_cadre_objectives,
    "cadre-de-reference-physique": strategy_convert_cadre_objectives,
    "English-cours": strategy_convert_english_cours,
    "English-examen": strategy_convert_english_examen,
    "Maths-fonctions-corrige-serie-d-exercices": strategy_pair_exercise_solution,
    "Maths-fonctions-cours": strategy_convert_concept_qna,
    "Physique-lois-de-newton-cours-Exercices": strategy_convert_physics,
}


# --- Orchestration ---------------------------------------------------------


def collect_folders() -> List[Tuple[str, Path]]:
    folders = []
    for p in sorted(EXTRACTED_DIR.iterdir()):
        if p.is_dir() and (p / "chunks.json").exists():
            folders.append((p.name, p))
    return folders


def build_triplets() -> List[Dict]:
    all_triplets: List[Dict] = []
    stats: Dict[str, int] = {}

    for folder_name, folder_path in collect_folders():
        strategy = STRATEGY_MAP.get(folder_name)
        if strategy is None:
            eprint(f"  [SKIP]  {folder_name}: no strategy assigned")
            continue

        chunks = load_chunks(folder_path)
        triplets = strategy(chunks, folder_name)
        all_triplets.extend(triplets)
        stats[folder_name] = len(triplets)
        eprint(f"  [BUILD] {folder_name} -> {len(triplets)} triplets")

    eprint("")
    eprint(f"  Total triplets generated: {len(all_triplets)}")
    eprint(f"  Target range: {TARGET_RANGE[0]}-{TARGET_RANGE[1]}")
    eprint("")
    for name, count in sorted(stats.items(), key=lambda x: -x[1]):
        eprint(f"    {name:55s} {count:4d}")
    eprint("")

    all_triplets = validate_and_prepare(all_triplets)

    eprint(f"  Training-ready triplets: {len(all_triplets)}")
    eprint("")

    if len(all_triplets) < TARGET_RANGE[0]:
        eprint(
            f"  [WARN] Only {len(all_triplets)} triplets -- below target of "
            f"{TARGET_RANGE[0]}."
        )

    return all_triplets


def validate_and_prepare(triplets: List[Dict]) -> List[Dict]:
    prepared: List[Dict] = []
    seen = set()

    for triplet in triplets:
        triplet = {
            k: clean_text(v) if isinstance(v, str) else v
            for k, v in triplet.items()
        }

        if not triplet.get("input") or not triplet.get("output"):
            continue
        if triplet.get("language") not in {"fr", "en"}:
            continue
        if triplet.get("subject") not in {"mathematics", "physics", "english"}:
            continue
        if len(triplet["input"]) > MAX_INPUT_CHARS and triplet.get("content_type") != "course_content":
            continue
        if len(triplet["output"]) > MAX_OUTPUT_CHARS:
            continue
        if (
            triplet.get("content_type") == "exercise_solution"
            and triplet["input"] == triplet["output"]
        ):
            continue
        if (
            triplet.get("content_type") == "exercise_solution"
            and triplet.get("chunk_id") in BAD_EXERCISE_PAIR_CHUNK_IDS
        ):
            continue

        dedup_key = (
            triplet.get("input", "")[:300],
            triplet.get("output", "")[:300],
            triplet.get("source", ""),
        )
        if dedup_key in seen:
            continue
        seen.add(dedup_key)

        prepared.append(add_training_fields(triplet))

    return prepared


def push_to_hub(triplets: List[Dict]):
    if not _HF_AVAILABLE:
        eprint("  [ERR] datasets not installed. Install with: pip install datasets")
        return

    ds = Dataset.from_list(triplets)

    eprint(f"  Pushing {len(ds)} examples to {HUB_DATASET} ...")
    ds.push_to_hub(HUB_DATASET, private=True)
    eprint(f"  [OK] Dataset pushed to https://huggingface.co/datasets/{HUB_DATASET}")


def save_local(triplets: List[Dict], path: str = "output/phase3/triplets.json"):
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(triplets, f, ensure_ascii=False, indent=2)
    eprint(f"  [OK] Saved {len(triplets)} triplets to {out}")

    jsonl_path = path.replace(".json", ".jsonl")
    with open(jsonl_path, "w", encoding="utf-8") as f:
        for t in triplets:
            f.write(json.dumps(t, ensure_ascii=False) + "\n")
    eprint(f"  [OK] Saved {len(triplets)} triplets as JSONL to {jsonl_path}")


# --- CLI -------------------------------------------------------------------


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Build Q&A triplet dataset from Phase 1 chunks")
    parser.add_argument("--push-to-hub", action="store_true", help="Push to HuggingFace Hub")
    parser.add_argument("--save-local", action="store_true", default=True, help="Save locally (default: True)")
    parser.add_argument("--output", type=str, default="output/phase3/triplets.json", help="Output path")
    args = parser.parse_args()

    eprint("=" * 60)
    eprint("  Rafiki Phase 3 - Q&A Triplet Builder")
    eprint("=" * 60)
    eprint("")

    triplets = build_triplets()

    if not triplets:
        eprint("  [ERR] No triplets generated. Check your chunk files.")
        sys.exit(1)

    if args.save_local:
        save_local(triplets, args.output)

    if args.push_to_hub:
        push_to_hub(triplets)

    eprint("")
    eprint("  Done.")


if __name__ == "__main__":
    main()
