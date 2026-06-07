#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, io
# Force UTF-8 stdout on Windows so print() never raises UnicodeEncodeError
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
"""
generate_triplets.py
====================
Converts any M3allem exam JSON file into fine-tuning triplets for
Qwen2.5-1.5B-Instruct LoRA training and appends them to a master JSONL dataset.

Usage
-----
    python generate_triplets.py <input_exam.json> [options]

Examples
--------
    # Process a Maths exam, append to default dataset
    python generate_triplets.py Maths/Maths-examen-2.json

    # Process a Physics exam, specify output file
    python generate_triplets.py Physics/physics-exam-1.json -o my_dataset.jsonl

    # Process all exams in a folder at once
    python generate_triplets.py --all

    # Dry-run: show what would be generated without writing
    python generate_triplets.py Maths/Maths-examen-1.json --dry-run
"""

import json
import argparse
import sys
import hashlib
from pathlib import Path
from datetime import datetime

# ──────────────────────────────────────────────────────────────────────────────
# CONFIGURATION
# ──────────────────────────────────────────────────────────────────────────────

SCRIPT_DIR   = Path(__file__).parent          # Fine-Tunning/
DEFAULT_OUT  = SCRIPT_DIR / "dataset.jsonl"   # master JSONL output file
SUBJECT_DIRS = {
    "Maths":   SCRIPT_DIR / "Maths",
    "Physics": SCRIPT_DIR / "Physics",
    "English": SCRIPT_DIR / "English",
}

# ──────────────────────────────────────────────────────────────────────────────
# SYSTEM PROMPTS  (one per language)
# ──────────────────────────────────────────────────────────────────────────────

SYSTEM_FR = (
    "You are Rafiki, a Moroccan 2Bac professor specialising in {module}. "
    "Explain concepts clearly and step by step, using appropriate terminology "
    "for the Moroccan baccalaureate curriculum. Always show your reasoning "
    "before giving the final answer."
)

SYSTEM_EN = (
    "You are Rafiki, a Moroccan 2Bac professor specialising in English. "
    "Explain grammar rules, vocabulary, and writing strategies clearly and "
    "step by step, using appropriate terminology for the Moroccan "
    "baccalaureate curriculum. Always show your reasoning before giving "
    "the final answer."
)

# ──────────────────────────────────────────────────────────────────────────────
# USER MESSAGE TEMPLATES  (one per language × subject)
# ──────────────────────────────────────────────────────────────────────────────

USER_TEMPLATE_MATHS = (
    "Je prépare mon baccalauréat et j'étudie « {subject} ». "
    "La question {key} me pose des difficultés :\n\n"
    "{question}\n\n"
    "Pouvez-vous m'expliquer comment résoudre cette question étape par étape ?"
)

USER_TEMPLATE_PHYSICS = (
    "Je prépare mon baccalauréat et j'étudie « {subject} ». "
    "Je bloque sur la question {key} :\n\n"
    "{question}\n\n"
    "Pouvez-vous m'expliquer la démarche complète à suivre ?"
)

USER_TEMPLATE_ENGLISH = (
    "I'm preparing for my Bac exam « {subject} ». "
    "I'm struggling with question {key}:\n\n"
    "{question}\n\n"
    "Can you explain the correct answer and the rule behind it step by step?"
)

# ──────────────────────────────────────────────────────────────────────────────
# THINK-BLOCK TEMPLATES  (pedagogical reasoning hint)
# ──────────────────────────────────────────────────────────────────────────────

THINK_MATHS = (
    "This is question {key} from {subject}. "
    "I need to present a rigorous, step-by-step mathematical solution. "
    "I will identify the core concept being tested, plan each logical step, "
    "use proper LaTeX notation for all formulas, and conclude clearly. "
    "The tone should be encouraging and pedagogically structured."
)

THINK_PHYSICS = (
    "This is question {key} from {subject}. "
    "I need to apply the appropriate physics law or chemistry principle. "
    "I will state the system and forces/quantities involved, apply the relevant "
    "formula with correct SI units, show numerical computation, and state the "
    "final result clearly. The tone should be methodical and precise."
)

THINK_ENGLISH = (
    "This is question {key} from {subject}. "
    "I need to identify the grammar rule, vocabulary item, or writing strategy "
    "being tested. I will explain the rule, show why the correct answer fits, "
    "explain why the alternatives are wrong when relevant, and give a memory "
    "tip for the Bac exam."
)

# ──────────────────────────────────────────────────────────────────────────────
# ASSISTANT RESPONSE TEMPLATES
# ──────────────────────────────────────────────────────────────────────────────

ASSISTANT_TEMPLATE = "<think>\n{think}\n</think>\n\n{correction}"


# ──────────────────────────────────────────────────────────────────────────────
# SUBJECT DETECTION
# ──────────────────────────────────────────────────────────────────────────────

def detect_module(json_path: Path, subject_field: str) -> str:
    """
    Detect the academic module (Maths / Physics / English) from the file path
    or the 'subject' field inside the JSON.

    Returns one of: 'Maths', 'Physics', 'English'
    """
    path_str = str(json_path).lower()
    subject_lower = subject_field.lower()

    if "maths" in path_str or "math" in path_str or "mathématiques" in subject_lower:
        return "Maths"
    if "physic" in path_str or "physique" in subject_lower or "chimie" in subject_lower:
        return "Physics"
    if "english" in path_str or "anglais" in subject_lower:
        return "English"

    # fallback: ask user
    print(f"\n⚠️  Cannot auto-detect module for: {json_path.name}")
    print("    Subject field found: «", subject_field, "»")
    choice = input("    Enter module [Maths / Physics / English]: ").strip()
    if choice in ("Maths", "Physics", "English"):
        return choice
    print("    Defaulting to 'Maths'.")
    return "Maths"


def is_english_module(module: str) -> bool:
    return module == "English"


# ──────────────────────────────────────────────────────────────────────────────
# TRIPLET BUILDER
# ──────────────────────────────────────────────────────────────────────────────

def build_triplet(
    question_key: str,
    question_text: str,
    correction_text: str,
    subject: str,
    module: str,
) -> dict:
    """
    Build a single training triplet dict in the ChatML messages format.

    Parameters
    ----------
    question_key   : e.g. "Ex1.Q1.a"
    question_text  : the raw question string from the JSON
    correction_text: the raw correction string from the JSON
    subject        : full subject string, e.g. "Examen National Mathématiques 2024"
    module         : "Maths" | "Physics" | "English"
    """
    english = is_english_module(module)

    # --- System ---
    if english:
        system_content = SYSTEM_EN
    else:
        system_content = SYSTEM_FR.format(module=module)

    # --- User ---
    if module == "Maths":
        user_content = USER_TEMPLATE_MATHS.format(
            subject=subject, key=question_key, question=question_text
        )
    elif module == "Physics":
        user_content = USER_TEMPLATE_PHYSICS.format(
            subject=subject, key=question_key, question=question_text
        )
    else:
        user_content = USER_TEMPLATE_ENGLISH.format(
            subject=subject, key=question_key, question=question_text
        )

    # --- Think block ---
    if module == "Maths":
        think = THINK_MATHS.format(key=question_key, subject=subject)
    elif module == "Physics":
        think = THINK_PHYSICS.format(key=question_key, subject=subject)
    else:
        think = THINK_ENGLISH.format(key=question_key, subject=subject)

    # --- Assistant ---
    assistant_content = ASSISTANT_TEMPLATE.format(
        think=think,
        correction=correction_text,
    )

    return {
        "messages": [
            {"role": "system",    "content": system_content},
            {"role": "user",      "content": user_content},
            {"role": "assistant", "content": assistant_content},
        ],
        # metadata (stripped before training if needed)
        "_meta": {
            "source_key": question_key,
            "subject":    subject,
            "module":     module,
        },
    }


# ──────────────────────────────────────────────────────────────────────────────
# FINGERPRINTING  (avoid duplicates)
# ──────────────────────────────────────────────────────────────────────────────

def fingerprint(subject: str, key: str) -> str:
    """Return a short hash identifying a (subject, key) pair."""
    raw = f"{subject}::{key}"
    return hashlib.md5(raw.encode()).hexdigest()[:12]


def load_existing_fingerprints(output_path: Path) -> set:
    """Read the output JSONL and collect all existing fingerprints."""
    fps = set()
    if not output_path.exists():
        return fps
    with output_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
                meta = obj.get("_meta", {})
                if meta.get("subject") and meta.get("source_key"):
                    fps.add(fingerprint(meta["subject"], meta["source_key"]))
            except json.JSONDecodeError:
                pass
    return fps


# ──────────────────────────────────────────────────────────────────────────────
# CORE PROCESSING FUNCTION
# ──────────────────────────────────────────────────────────────────────────────

def process_exam_file(
    json_path: Path,
    output_path: Path,
    dry_run: bool = False,
    verbose: bool = True,
) -> dict:
    """
    Parse one exam JSON file, generate triplets for every Q&A pair,
    and append new ones to the output JSONL.

    Returns a stats dict with keys: total_pairs, added, skipped_duplicate,
                                    skipped_no_correction, errors
    """
    stats = {
        "total_pairs":          0,
        "added":                0,
        "skipped_duplicate":    0,
        "skipped_no_correction":0,
        "errors":               0,
    }

    # ── load JSON ──────────────────────────────────────────────────────────────
    try:
        with json_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"  ❌ JSON parse error in {json_path.name}: {e}")
        stats["errors"] += 1
        return stats

    subject = data.get("subject", json_path.stem)
    module  = detect_module(json_path, subject)

    if verbose:
        print(f"\n{'--'*30}")
        print(f"  File   : {json_path.name}")
        print(f"  Subject: {subject}")
        print(f"  Module : {module}")
        print(f"{'--'*30}")

    # ── load existing fingerprints ────────────────────────────────────────────
    existing_fps = load_existing_fingerprints(output_path)

    # ── collect question keys (skip 'subject' and 'Corr ...' keys) ───────────
    question_keys = [
        k for k in data.keys()
        if k != "subject" and not k.startswith("Corr ")
    ]

    # ── process each pair ─────────────────────────────────────────────────────
    new_triplets = []

    for qk in question_keys:
        corr_key = f"Corr {qk}"
        stats["total_pairs"] += 1

        # check correction exists
        if corr_key not in data:
            if verbose:
                print(f"  [WARN] No correction found for key: {qk}")
            stats["skipped_no_correction"] += 1
            continue

        question_text   = str(data[qk]).strip()
        correction_text = str(data[corr_key]).strip()

        # skip empty
        if not question_text or not correction_text:
            stats["skipped_no_correction"] += 1
            continue

        # deduplicate
        fp = fingerprint(subject, qk)
        if fp in existing_fps:
            if verbose:
                print(f"  [SKIP] Duplicate: {qk}")
            stats["skipped_duplicate"] += 1
            continue

        # build triplet
        try:
            triplet = build_triplet(qk, question_text, correction_text, subject, module)
            new_triplets.append((fp, triplet))
            if verbose:
                print(f"  [OK]   Prepared : {qk}")
        except Exception as e:
            print(f"  [ERR] Error building triplet for {qk}: {e}")
            stats["errors"] += 1

    # ── write to JSONL (append mode) ──────────────────────────────────────────
    if not dry_run and new_triplets:
        with output_path.open("a", encoding="utf-8") as out:
            for fp, triplet in new_triplets:
                out.write(json.dumps(triplet, ensure_ascii=False) + "\n")
                existing_fps.add(fp)
                stats["added"] += 1
    else:
        stats["added"] = len(new_triplets)  # show count even in dry-run

    return stats


# ──────────────────────────────────────────────────────────────────────────────
# BATCH PROCESSING
# ──────────────────────────────────────────────────────────────────────────────

def process_all(output_path: Path, dry_run: bool = False) -> None:
    """Process every .json exam file found in all subject directories."""
    total_stats = {
        "total_pairs": 0, "added": 0,
        "skipped_duplicate": 0, "skipped_no_correction": 0, "errors": 0,
    }

    found_files = []
    for module, dir_path in SUBJECT_DIRS.items():
        if dir_path.exists():
            found_files.extend(sorted(dir_path.glob("*.json")))

    if not found_files:
        print("❌ No JSON files found in subject directories.")
        return

    print(f"\n[SCAN] Found {len(found_files)} exam file(s) to process:")
    for f in found_files:
        print(f"   - {f.relative_to(SCRIPT_DIR)}")

    for json_path in found_files:
        stats = process_exam_file(json_path, output_path, dry_run=dry_run)
        for k in total_stats:
            total_stats[k] += stats[k]

    print_summary(total_stats, output_path, dry_run)


# ──────────────────────────────────────────────────────────────────────────────
# SUMMARY PRINTER
# ──────────────────────────────────────────────────────────────────────────────

def print_summary(stats: dict, output_path: Path, dry_run: bool) -> None:
    dry_tag = " [DRY RUN - nothing written]" if dry_run else ""
    print(f"\n{'='*60}")
    print(f"  SUMMARY{dry_tag}")
    print(f"{'='*60}")
    print(f"  Q&A pairs found          : {stats['total_pairs']}")
    print(f"  [OK]  Triplets added     : {stats['added']}")
    print(f"  [SKIP] Duplicates        : {stats['skipped_duplicate']}")
    print(f"  [WARN] Missing corr.     : {stats['skipped_no_correction']}")
    print(f"  [ERR]  Errors            : {stats['errors']}")
    if not dry_run:
        try:
            with output_path.open("r", encoding="utf-8") as f:
                total_lines = sum(1 for l in f if l.strip())
            print(f"  Total triplets in dataset: {total_lines}")
        except FileNotFoundError:
            pass
        print(f"  Output file: {output_path}")
    print(f"{'='*60}\n")


# ──────────────────────────────────────────────────────────────────────────────
# UTILITIES
# ──────────────────────────────────────────────────────────────────────────────

def jsonl_to_json_array(jsonl_path: Path) -> None:
    """Convert the JSONL dataset to a pretty-printed JSON array (for inspection)."""
    triplets = []
    with jsonl_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                triplets.append(json.loads(line))

    out_path = jsonl_path.with_suffix(".json")
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(triplets, f, ensure_ascii=False, indent=2)
    print(f"[OK] Exported {len(triplets)} triplets to {out_path}")


def strip_meta(jsonl_path: Path) -> None:
    """Remove _meta fields from all triplets (for clean HuggingFace upload)."""
    lines = []
    with jsonl_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            obj.pop("_meta", None)
            lines.append(json.dumps(obj, ensure_ascii=False))

    out_path = jsonl_path.with_stem(jsonl_path.stem + "_clean")
    with out_path.open("w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"[OK] Clean dataset (no _meta) saved to {out_path}")


# ──────────────────────────────────────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────────────────────────────────────

def parse_args():
    parser = argparse.ArgumentParser(
        description="Convert M3allem exam JSON files to fine-tuning triplets (JSONL).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )

    parser.add_argument(
        "input",
        nargs="?",
        type=Path,
        help="Path to a single exam JSON file. If omitted, use --all.",
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default=DEFAULT_OUT,
        help=f"Output JSONL file (default: {DEFAULT_OUT.name})",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Process ALL exam JSON files in all subject directories.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be added without writing to disk.",
    )
    parser.add_argument(
        "--export-json",
        action="store_true",
        help="After processing, also export the JSONL as a JSON array for inspection.",
    )
    parser.add_argument(
        "--strip-meta",
        action="store_true",
        help="Generate a clean JSONL copy without _meta fields (for HF upload).",
    )
    parser.add_argument(
        "-q", "--quiet",
        action="store_true",
        help="Suppress per-key output; show only summary.",
    )

    return parser.parse_args()


def main():
    args = parse_args()
    verbose = not args.quiet

    print(f"\n{'='*60}")
    print(f"  M3allem — Triplet Generator")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}")

    if args.all:
        process_all(args.output, dry_run=args.dry_run)

    elif args.input:
        # Resolve relative to script dir if not absolute
        json_path = args.input if args.input.is_absolute() else SCRIPT_DIR / args.input
        if not json_path.exists():
            print(f"❌ File not found: {json_path}")
            sys.exit(1)
        stats = process_exam_file(
            json_path, args.output,
            dry_run=args.dry_run,
            verbose=verbose,
        )
        print_summary(stats, args.output, args.dry_run)

    else:
        print("❌ Provide an input file or use --all.")
        print("   Run with -h for help.")
        sys.exit(1)

    # Post-processing options
    if not args.dry_run and args.output.exists():
        if args.export_json:
            jsonl_to_json_array(args.output)
        if args.strip_meta:
            strip_meta(args.output)


if __name__ == "__main__":
    main()
