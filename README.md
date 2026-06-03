# M3allem — Moroccan Adaptive AI Tutor

> **An AI-powered study assistant for Moroccan 2ème Bac students.**
> The app comes with a pre-built knowledge base from the 2Bac curriculum (Maths, Physics, English).
> Students can ask questions immediately — no upload needed — and also add their own documents.
> Answers are always grounded in the curriculum via RAG, in **French** or **English** depending on the subject.

---

## Table of Contents

- [What It Does](#what-it-does)
- [Architecture Overview](#architecture-overview)
- [Project Structure](#project-structure)
- [Phase Roadmap](#phase-roadmap)
- [Current Status](#current-status)
- [Status Log](#status-log)

---

## What It Does

A student opens the app and can start immediately — **no upload required** — because the app ships with a pre-built 2Bac knowledge base.

### MVP Feature Tiers

| Feature | MVP State | Description |
|---|---|---|
| 💬 **Q&A Chat** | ✅ Fully working | Ask any question → RAG retrieves the relevant 2Bac course chunk → fine-tuned LLM generates a step-by-step answer in French or English |
| ✍️ **Exercise Correction** | ✅ Fully working | Student uploads a blank exercise OR one with their own answers → AI corrects it like a professor, step by step |
| 📝 **Generate Exercise** | 🔶 Frontend only | UI exists, shows a static placeholder — connected to AI post-MVP |
| 📋 **Generate Resume** | 🔶 Frontend only | UI exists, shows a static placeholder — connected to AI post-MVP |
| 📤 **Upload your own PDF** | 🔶 Frontend only | UI exists — document indexing connected to RAG post-MVP |
| 🎓 **Level / Subject selection** | 🔶 Frontend only | UI exists — backend filtering post-MVP |
| 📊 **Progress tracking** | 🔶 Frontend only | UI exists — history and analytics post-MVP |

### Two-layer knowledge architecture

```
App startup
    │
    ▼
Load pre-built ChromaDB  ← built from YOUR 2Bac PDFs (Maths · Physics · English)
    │
    ├── Student asks a question (no upload needed)
    │       → RAG searches pre-built 2Bac knowledge base  ✅
    │
    └── Student uploads their own PDF
            → Also chunked + embedded
            → RAG searches BOTH (pre-built + uploaded)    ✅
```

> **RAG is permanent — not a workaround.** Fine-tuning teaches the model *how* to answer (style, format, reasoning). RAG gives it *what* to answer about (the specific theorem, formula, or exercise). Both work together at inference time — this is the industry-standard pattern for educational AI assistants.

---

## Architecture Overview

```
2Bac PDFs (Maths · Physics · English)
      │
      ▼
┌─────────────────────────────────┐
│  Phase 1 — PDF Extraction       │  Qwen2.5-VL-2B  (Kaggle T4 GPU)
│  PDF pages → Markdown chunks    │  PyMuPDF + PIL
└──────────────┬──────────────────┘
               │  chunks.json  (pre-built KB)
               ▼
┌─────────────────────────────────┐
│  Phase 2 — RAG Knowledge Base   │  sentence-transformers (CPU)
│  Embed chunks → ChromaDB        │  multilingual-MiniLM-L12-v2
│  (ships with the app)           │  ChromaDB on-disk
└──────────────┬──────────────────┘
               │  vector store  ← also used at every query (permanent)
               ▼
┌─────────────────────────────────┐
│  Phase 3 — Fine-tuned LLM       │  Qwen2.5-1.5B + LoRA (Kaggle T4)
│  Teaches style, not content     │  Unsloth 4-bit quant
│  Fine-tuning data = Q&A pairs   │  ~50-200 triplets (Maths/Physics)
│  extracted from same PDFs       │
└──────────────┬──────────────────┘
               │  HF Serverless Inference API (free, rate-limited)
               ▼
┌─────────────────────────────────┐
│  Phase 4 — Gradio App           │  HuggingFace Spaces (CPU Basic, free)
│  Student-facing interface       │  Q&A + Exercise Correction (working)
│                                 │  Exercise/Resume/Upload (frontend only)
└─────────────────────────────────┘
```

**Total MVP cost: $0** — all components run on free-tier Kaggle, HuggingFace Spaces, and HuggingFace Serverless Inference.

---

## Project Structure

```
src/
├── requirements-phase1.txt      pip install -r this before running Phase 1
│
└── phase1_extraction/           Phase 1 Python package
    ├── __init__.py              Package exports (PipelineConfig, M3allemPDFPipeline)
    │
    ├── config.py                All settings + Moroccan Bac curriculum taxonomy
    │                              BacLevel    — TC / 1Bac / 2Bac
    │                              Subject     — Maths, Physics, English, …
    │                              Specialization — Sciences Maths A/B, PC, …
    │                              PipelineConfig  — model path, DPI, HF token, …
    │                              FileMetadata    — auto-detects subject & level
    │                                               from PDF filename convention
    │
    ├── pdf_processor.py         PyMuPDF (fitz) wrapper
    │                              → PDFProcessor(path, dpi) context manager
    │                              → iter_pages() → (page_num, PIL.Image, raw_text)
    │                              → page_to_image() / page_to_text()
    │
    ├── extractor.py             Two pluggable extraction strategies
    │                              VLMExtractor  — Qwen2.5-VL-2B (GPU / Kaggle)
    │                                             loads model once, reuses per page
    │                              TextExtractor — PyMuPDF text dump (CPU, no GPU)
    │                                             fast fallback for local testing
    │                              BaseExtractor — shared interface (ABC)
    │
    ├── structurer.py            Markdown post-processing & chunking
    │                              clean_markdown()       strips VLM artifacts,
    │                                                     normalises LaTeX delimiters
    │                              chunk_by_headings()    splits on ## / ### headings
    │                              detect_content_type()  classifies each chunk:
    │                                  definition / theorem / proof / example /
    │                                  exercise / solution / property / remark /
    │                                  method / formula / summary / course_content
    │                              make_chunk_id()        unique ID per chunk
    │                                  e.g. maths_2bac_p03_c02
    │                              extract_math_formulas() pulls all $...$ / $$...$$
    │                              build_page_entry()     assembles the full record
    │                                  with metadata ready for Phase 2 ChromaDB
    │
    ├── pipeline.py              End-to-end orchestrator
    │                              M3allemPDFPipeline(config)
    │                                  .run_file(pdf_path)   — single PDF
    │                                  .run_folder(folder)   — batch all PDFs
    │                              Saves per PDF inside output_dir/<pdf_stem>/:
    │                                  pages/page_XX.md       per-page Markdown
    │                                  full_course.md         combined Markdown
    │                                  structured_data.json   per-page entries
    │                                  chunks.json            flat chunk list
    │                                                         ← Phase 2 input
    │                                  summary.json           run statistics
    │                              Optional HuggingFace Hub push
    │
    └── main.py                  CLI entry point
                                   python -m src.phase1_extraction.main [options]
                                   --input  path/to/file.pdf OR path/to/folder/
                                   --output data/extracted/
                                   --no-vlm   CPU text-only (no GPU needed)
                                   --push-to-hub
                                   --subject / --level overrides
```


---

## Phase Roadmap

| Phase | Objective | Tools | Status |
|---|---|---|---|
| **1 — PDF Extraction** | 2Bac PDFs (Maths/Physics/English) → Markdown chunks | Qwen2.5-VL-2B, PyMuPDF, Kaggle T4 | 🟡 In Progress |
| **2 — RAG Knowledge Base** | Embed all chunks → persistent ChromaDB (pre-built KB) | multilingual-MiniLM-L12-v2, ChromaDB | ⬜ Not started |
| **3 — Fine-Tuning** | Train Qwen on 2Bac Q&A style (French/English) | Qwen2.5-1.5B, LoRA, Unsloth, Kaggle T4 | ⬜ Not started |
| **4 — Gradio App** | Q&A Chat + Exercise Correction (working); other tabs as UI placeholders | Gradio, HuggingFace Spaces | ⬜ Not started |
| **5 — Integration** | Wire all phases, end-to-end test with real 2Bac questions | All of the above | ⬜ Not started |

---

## Current Status

**Active phase:** Phase 1 — PDF Extraction Pipeline

### ✅ Completed
- Project architecture finalised (`Project-Description.md`)
- HuggingFace Space created (Gradio, CPU Basic, public)
- GitHub repository initialised
- Raw Bac PDF dataset assembled (`Document-Data-Set/`)
- **Kaggle pipeline script** written and tested:
  - `kaggle/pdf_to_markdown_pipeline.py` — processes PDFs with Qwen2.5-VL-2B on T4
  - Tested on 6-page probability PDF → `kaggle/output/` contains verified results
- **Local `src/` module** created (production-quality, modular code):
  - `src/phase1_extraction/` — 6-module Python package
  - CPU fallback mode (`--no-vlm`) for local testing without a GPU
  - Supports batch-processing a folder of PDFs
  - Auto-detects subject/level from filename conventions
  - Enriched chunk schema with unique `chunk_id`s for Phase 2 traceability

### 🔴 Previous Blocker (resolved)
- **OOM on T4:** Original script used `Qwen2.5-VL-7B-Instruct` in bfloat16 → 14.5 GB VRAM, only 0.5 GB headroom.
- **Fix:** Switched to `Qwen2.5-VL-2B-Instruct` → ~4 GB VRAM, 12 GB headroom for images. ✅

### ⏳ Next Action
Run `kaggle/pdf_to_markdown_pipeline.py` on **all 5 PDFs in `Document-Data-Set/2bac/`** on Kaggle
(Maths, Physics, English — cours + exercices). Verify `chunks.json` quality for all 3 subjects,
then move to Phase 2 to build the persistent 2Bac ChromaDB knowledge base.

---

## Status Log

```
[2026-06-03]  MVP scope finalised via questionnaire
              - Target year: 2ème Bac only
              - Target subjects: Mathématiques · Physique-Chimie · English
              - Language: French (Maths/Physics), English (English subject)
              - Fully working in MVP: Q&A Chat + Exercise Correction
              - Frontend-only placeholders: Generate Exercise, Generate Resume,
                Upload PDF, Level selection, Progress tracking
              - Architecture: pre-built 2Bac ChromaDB (no upload needed to use app)
              - RAG is permanent (also used after fine-tuning, not replaced by it)
              - Model: Qwen2.5 only for MVP (no separate Arabic model)

[2026-06-03]  Created src/phase1_extraction/ module (6 files)
              - config.py: BacLevel / Subject / Specialization enums,
                           PipelineConfig, FileMetadata with auto-detection
              - pdf_processor.py: context-manager PDF wrapper
              - extractor.py: VLMExtractor (Qwen) + TextExtractor (CPU fallback)
              - structurer.py: chunker, content-type detector, chunk_id generator
              - pipeline.py: run_file() / run_folder() orchestrator
              - main.py: CLI with argparse (--no-vlm, --input, --push-to-hub)
              - src/requirements-phase1.txt added

[2026-06-03]  Fixed kaggle/pdf_to_markdown_pipeline.py
              - _pip_install() silenced stderr → errors were invisible
              - Fixed: stderr now shown on failure ([pip ERROR] prefix)

[2026-06-03]  Assembled Document-Data-Set/ with Bac PDFs
              - 6 probability/statistics PDFs (root level, legacy test data)
              - 5 multi-subject 2Bac PDFs (2bac/ subfolder) ← PRIMARY MVP INPUT
                Subjects: Maths (cours + exercices), Physics (cours), English (cours + examen)

[2026-06-03]  Verified Phase 1 output (kaggle/output/)
              - 6-page PDF → full_course.md (241 lines clean Markdown + LaTeX)
              - chunks.json generated and ready for Phase 2 schema

[2026-06-01]  Initial commit — project architecture confirmed
              - Project-Description.md written
              - kaggle/pdf_to_markdown_pipeline.py written (initial version)
              - Model switched: 7B → 2B to fix T4 OOM
```
