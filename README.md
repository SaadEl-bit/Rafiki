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
| 📄 **Exam Generation** | 🔶 Frontend only | UI exists — generates mock exams matching national Bac structure |
| 📄 **Exam Correction** | 🔶 Frontend only | UI exists — submits exams for grading and detailed feedback |
| 📚 **Cadre Référenciel** | 🔶 Frontend only | UI exists — displays official 2Bac curriculum and exam weighting |

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
│  Phase 3 — Fine-tuned LLM       │  Qwen/Qwen2.5-1.5B-Instruct + LoRA (Kaggle T4)
│  Teaches style, not content     │  Unsloth 4-bit quant
│  Fine-tuning data = Q&A pairs   │  277 training-ready triplets (Maths/Physics/English)
│  (pushed to HuggingFace Model)  │
└──────────────┬──────────────────┘
               │  HF Serverless Inference API
               ▼
┌─────────────────────────────────┐
│  Phase 4 — FastAPI Backend  ✅  │  Python 3.11 + FastAPI
│  POST /api/ask                  │  Railway (free tier)
│  POST /api/correct              │  RAGRetriever + HF API client
│  GET /health                    │
└──────────────┬──────────────────┘
               │  JSON responses
               ▼
┌─────────────────────────────────┐
│  Phase 5 — Next.js Frontend  ✅ │  Next.js 16 (App Router)
│  / → Landing page (Rafiki)        │  Vercel (free tier)
│  /chat → Q&A Chat               │  Tailwind CSS
│  /correction → Exercise Correction│  Sidebar + Topbar layout
│  /exercise → Generate Exercise   │
│  /resume → Generate Resume       │
│  /exam-gen → Exam Generation     │
│  /exam-correction → Exam Correction│
│  /cadre → Cadre Référenciel      │
└─────────────────────────────────┘
```

**Total MVP cost: ~$0** — PDF extraction on Kaggle, AI hosting on HuggingFace, backend on Railway free tier, frontend on Vercel free tier.

---

## Project Structure

```
src/
├── requirements.txt             Root requirements (delegates to phase4_backend)
├── requirements-phase1.txt      pip install -r this before running Phase 1
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
├── phase3/                      Phase 3 — Dataset building + Kaggle fine-tuning
│   └── dataset/
│       ├── build_dataset.py     Builds {input, thinking, output} triplets from Phase 1 chunks
│       └── push_data.py         Pushes triplets to HuggingFace Hub
│
└── phase4_backend/              Phase 4 — FastAPI server (Railway) ✅ Done
    ├── __init__.py
    ├── main.py                  FastAPI app entry point (CORS, routers, health check)
    ├── requirements.txt         fastapi, uvicorn, huggingface_hub, chromadb, etc.
    ├── routers/
    │   ├── __init__.py
    │   ├── ask.py               POST /api/ask endpoint
    │   └── correct.py           POST /api/correct endpoint
    ├── services/
    │   ├── __init__.py
    │   ├── rag_service.py       Downloads ChromaDB from HF, wraps RAGRetriever
    │   └── llm_service.py       HuggingFace Inference API client (InferenceClient)
    └── models/
        ├── __init__.py
        ├── request_models.py    Pydantic request schemas (AskRequest, CorrectRequest)
        └── response_models.py   Pydantic response schemas (AskResponse, CorrectResponse)

frontend/                        Phase 5 — Next.js app (Vercel) ✅ Built (UI only)
├── app/
│   ├── layout.js               Root layout (fonts, global styles)
│   ├── page.js                 Landing page (/)
│   ├── globals.css             Global CSS (Tailwind + custom tokens)
│   └── (dashboard)/            Route group for student interface
│       ├── layout.js           Dashboard layout (Sidebar + Topbar)
│       ├── chat/page.js        Q&A Chat (/chat)
│       ├── correction/page.js  Exercise Correction (/correction)
│       ├── exercise/page.js    Generate Exercise (/exercise) — placeholder
│       ├── resume/page.js      Generate Resume (/resume) — placeholder
│       ├── exam-gen/page.js    Exam Generation (/exam-gen) — placeholder
│       ├── exam-correction/page.js  Exam Correction (/exam-correction) — placeholder
│       └── cadre/page.js       Cadre Référenciel (/cadre) — curriculum info
├── components/
│   └── layout/
│       ├── Sidebar.jsx         Navigation sidebar with all routes
│       └── Topbar.jsx          Top bar with search and page title
├── package.json                Next.js 16.2.7, React 19, Tailwind CSS
├── tailwind.config.js          Tailwind configuration
├── next.config.mjs             Next.js configuration
└── public/                     Static assets (logo, icons)
```

> **Note:** Frontend is UI-only — not yet connected to the Railway backend. No `lib/api.js` exists yet.


---

## Phase Roadmap

| Phase | Objective | Tools | Status |
|---|---|---|---|
| **1 — PDF Extraction** | 2Bac PDFs → Markdown chunks | Qwen2.5-VL-2B, PyMuPDF, Kaggle T4 | ✅ Complete |
| **2 — RAG Knowledge Base** | Embed all chunks → persistent ChromaDB | multilingual-MiniLM-L12-v2, ChromaDB | ✅ Complete |
| **3 — Fine-Tuning** | Train Qwen on 2Bac Q&A style (French/English) | Qwen/Qwen2.5-1.5B-Instruct, LoRA, Unsloth, Kaggle T4 | 🟡 In Progress |
| **4 — FastAPI Backend** | Wrap RAG + LLM into a REST API | FastAPI, Uvicorn, Railway | ✅ Complete |
| **5 — Next.js Frontend** | Landing page + student app UI | Next.js 16, Tailwind CSS, Vercel | ✅ Built (UI only) |
| **6 — Integration** | Wire frontend to backend, end-to-end test | All of the above | ⬜ Not started |

---

## Current Status

**Active phase:** Phase 6 — Integration (wire frontend to backend)

### ✅ Completed
- **Architecture upgraded:** 3-server split confirmed — Vercel (Next.js) + Railway (FastAPI) + HuggingFace (model + data).
- **Phase 1 (Extraction):** Successfully extracted all 2Bac PDFs on Kaggle and pushed 965 structured chunks to HuggingFace dataset `Saad-Elouakate/AI-Adaptive-Learning`.
- **Phase 2 (RAG):** Created the `src/phase2_rag/` module:
  - `config.py` — embedding model and repository settings
  - `embedder.py` — logic to download chunks from HF and embed into ChromaDB
  - `retriever.py` — RAGRetriever wrapper for the FastAPI backend
  - `main.py` — Kaggle script to orchestrate indexing and pushing
  - ChromaDB index built and pushed to `Saad-Elouakate/AI-Adaptive-Learning-Index`
- **Phase 3 (Dataset):** Generated 277 training-ready triplets in `output/phase3/` with raw fields, `messages`, and ChatML `text`. Dataset builder script complete at `src/phase3/dataset/build_dataset.py`.
- **Phase 4 (Backend):** FastAPI backend fully implemented at `src/phase4_backend/`:
  - `POST /api/ask` — receives question + subject → returns AI answer
  - `POST /api/correct` — receives exercise text + subject → returns step-by-step correction
  - `GET /health` — Railway health check
  - `rag_service.py` — auto-downloads ChromaDB from HuggingFace on startup
  - `llm_service.py` — uses `huggingface_hub.InferenceClient` for model inference
  - Railway deployment configured via `railway.json`
- **Phase 5 (Frontend):** Next.js app built at `frontend/`:
  - Landing page (`/`) with hero section, feature cards, "How It Works" steps
  - Student dashboard with Sidebar + Topbar layout
  - 8 pages: Chat, Correction, Exercise, Resume, Exam-Gen, Exam-Correction, Cadre
  - Tailwind CSS styling (Material Design-inspired tokens)
  - **Note:** UI is complete but not connected to backend yet

### ⏳ Next Action
**Phase 6 — Integration:** Connect the Next.js frontend to the Railway backend:
1. Create `frontend/lib/api.js` with API call functions
2. Wire Chat page to `POST /api/ask`
3. Wire Correction page to `POST /api/correct`
4. Set `NEXT_PUBLIC_API_URL` environment variable on Vercel
5. Deploy and test end-to-end

---

## Status Log

[2026-06-07]  Phase 4 (Backend) and Phase 5 (Frontend) completed
              - FastAPI backend fully implemented at src/phase4_backend/
              - POST /api/ask and POST /api/correct endpoints working
      - rag_service.py auto-downloads ChromaDB from HuggingFace on startup
      - llm_service.py uses huggingface_hub.InferenceClient
              - Railway deployment configured via railway.json
      - Next.js frontend built at frontend/ (Next.js 16, Tailwind CSS)
      - 8 pages implemented: Chat, Correction, Exercise, Resume, Exam-Gen, Exam-Correction, Cadre
      - Landing page with hero, features, and "How It Works" section
      - Sidebar + Topbar dashboard layout
      - UI is complete but NOT connected to backend yet

[2026-06-06]  Phase 3 model and dataset selected
              - Selected Qwen/Qwen2.5-1.5B-Instruct for text LoRA fine-tuning
              - Kept PDF/photo exercise support as a separate extraction/OCR step before RAG + LLM
              - Regenerated output/phase3 with 277 training-ready triplets
              - Local dataset now includes messages and ChatML text columns

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

[2026-06-03]  Created src/phase1_extraction/ module (7 files)
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
