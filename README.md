# Rafiki — رفيقي — Moroccan Adaptive AI Tutor

> **An AI-powered study companion for Moroccan 2ème Bac students.**
> *"رفيقك في الدراسة — Ton compagnon pour le Bac"*
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
               │  chunks.json  (pushed to HuggingFace Dataset)
               ▼
┌─────────────────────────────────┐
│  Phase 2 — RAG Knowledge Base   │  sentence-transformers (CPU)
│  Embed chunks → ChromaDB        │  multilingual-MiniLM-L12-v2
│  (pushed to HuggingFace Dataset)│  ChromaDB on-disk
└──────────────┬──────────────────┘
               │  vector store ← used at every query (permanent)
               ▼
┌─────────────────────────────────┐
│  Phase 3 — Fine-tuned LLM       │  Qwen2.5-1.5B + LoRA (Kaggle T4)
│  Teaches style, not content     │  Unsloth 4-bit quant
│  Fine-tuning data = Q&A pairs   │  ~50-200 triplets (Maths/Physics)
│  (pushed to HuggingFace Model)  │
└──────────────┬──────────────────┘
               │  HF Serverless Inference API
               ▼
┌─────────────────────────────────┐
│  Phase 4 — FastAPI Backend      │  Python 3.11 + FastAPI
│  POST /api/ask                  │  Railway (free tier)
│  POST /api/correct              │  RAGRetriever + HF API client
└──────────────┬──────────────────┘
               │  JSON responses
               ▼
┌─────────────────────────────────┐
│  Phase 5 — Next.js Frontend     │  Next.js 14+ (App Router)
│  / → Landing page (Rafiki)        │  Vercel (free tier)
│  /app/chat → Q&A Chat          │  CSS from Figma/Stitch template
│  /app/correction → Correction  │
└─────────────────────────────────┘
```

**Total MVP cost: ~$0** — PDF extraction on Kaggle, AI hosting on HuggingFace, backend on Railway free tier, frontend on Vercel free tier.

---

## Project Structure

```
src/
├── requirements-phase1.txt      pip install -r this before running Phase 1
├── requirements-phase4.txt      pip install -r this before running the backend
│
├── phase1_extraction/           Phase 1 Python package ✅ Done
│   ├── __init__.py
│   ├── config.py                BacLevel / Subject / Specialization enums,
│   │                              PipelineConfig, FileMetadata with auto-detection
│   ├── pdf_processor.py         PyMuPDF (fitz) wrapper
│   ├── extractor.py             VLMExtractor (Qwen) + TextExtractor (CPU fallback)
│   ├── structurer.py            Markdown chunker, content-type detector, chunk_id generator
│   ├── pipeline.py              run_file() / run_folder() orchestrator
│   └── main.py                  CLI: --input, --output, --no-vlm, --push-to-hub
│
├── phase2_rag/                  Phase 2 Python package ✅ Done
│   ├── __init__.py              Exports RAGRetriever
│   ├── config.py                Settings (embedding model, ChromaDB path, HF repos)
│   ├── embedder.py              build_index(): downloads HF chunks, embeds into ChromaDB
│   ├── retriever.py             RAGRetriever: loads ChromaDB, returns top-K chunks
│   └── main.py                  Kaggle entry point: python -m src.phase2_rag.main --push-to-hub
│
├── phase3_finetune/             Phase 3 — Kaggle fine-tuning script ⏯ To build
│
└── phase4_backend/              Phase 4 — FastAPI server (Railway) 🆕 New
    ├── __init__.py
    ├── main.py                  FastAPI app entry point
    ├── routers/
    │   ├── ask.py               POST /api/ask endpoint
    │   └── correct.py           POST /api/correct endpoint
    ├── services/
    │   ├── rag_service.py       Wraps RAGRetriever from phase2_rag (unchanged)
    │   └── llm_service.py       HuggingFace Inference API client
    └── models/
        ├── request_models.py   Pydantic request schemas
        └── response_models.py  Pydantic response schemas

frontend/                        Phase 5 — Next.js app (Vercel) 🆕 New
├── app/                         Next.js App Router
│   ├── layout.js               Root layout (fonts, global styles)
│   ├── page.js                 Landing page (/)
│   └── app/                    Student interface (/app)
│       ├── chat/page.js        Q&A Chat
│       ├── correction/page.js  Exercise Correction
│       ├── exercise/page.js    Generate Exercise (placeholder)
│       └── resume/page.js      Generate Resume (placeholder)
├── components/
│   ├── ui/                     Base components (Button, Card, Input…)
│   ├── chat/                   ChatWindow, MessageBubble, InputBar
│   ├── correction/             FileUpload, CorrectionResult
│   └── layout/                 Sidebar, SubjectSelector
├── lib/api.js                   API call functions (fetch to Railway backend)
├── styles/globals.css           Global CSS (from Figma/Stitch template)
├── public/                      Static assets (logo, icons)
├── package.json
└── next.config.js
```


---

## Phase Roadmap

| Phase | Objective | Tools | Status |
|---|---|---|---|
| **1 — PDF Extraction** | 2Bac PDFs → Markdown chunks | Qwen2.5-VL-2B, PyMuPDF, Kaggle T4 | ✅ Complete |
| **2 — RAG Knowledge Base** | Embed all chunks → persistent ChromaDB | multilingual-MiniLM-L12-v2, ChromaDB | 🟡 In Progress |
| **3 — Fine-Tuning** | Train Qwen on 2Bac Q&A style (French/English) | Qwen2.5-1.5B, LoRA, Unsloth, Kaggle T4 | ⬜ Not started |
| **4 — FastAPI Backend** | Wrap RAG + LLM into a REST API | FastAPI, Uvicorn, Railway | ⬜ Not started |
| **5 — Next.js Frontend** | Landing page + student app UI | Next.js, Vercel, CSS from design template | ⬜ Not started |
| **6 — Integration** | Wire all 3 servers, end-to-end test | All of the above | ⬜ Not started |

---

## Current Status

**Active phase:** Phase 2 — RAG Knowledge Base

### ✅ Completed
- **Architecture upgraded:** 3-server split confirmed — Vercel (Next.js) + Railway (FastAPI) + HuggingFace (model + data).
- **Phase 1 (Extraction):** Successfully extracted all 2Bac PDFs on Kaggle and pushed 965 structured chunks to HuggingFace dataset `Saad-Elouakate/AI-Adaptive-Learning`.
- **Phase 2 (RAG):** Created the `src/phase2_rag/` module:
  - `config.py` — embedding model and repository settings
  - `embedder.py` — logic to download chunks from HF and embed into ChromaDB
  - `retriever.py` — RAGRetriever wrapper for the FastAPI backend
  - `main.py` — Kaggle script to orchestrate indexing and pushing

### ⏳ Next Action
Run `src/phase2_rag/main.py` on Kaggle to process the 965 chunks, build the ChromaDB vector index, and push it to the new `Saad-Elouakate/AI-Adaptive-Learning-Index` dataset on HuggingFace.

---

## Status Log

[2026-06-05]  Architecture upgraded to 3-server strategy
              - Dropped Gradio / HuggingFace Spaces approach
              - New stack: Vercel (Next.js) + Railway (FastAPI) + HuggingFace (AI)
              - Added Phase 4 (FastAPI Backend) and Phase 5 (Next.js Frontend)
              - Frontend styling will follow a Figma/Stitch design template
              - Streaming responses deferred (full answer at once for MVP)
              - Private school / educator tier removed from this project

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
