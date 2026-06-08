# **Project Description: Rafiki — رفيقي — Moroccan Adaptive AI Tutor Platform**

---

## **1. Core Vision & Features**

### **Overview**
Rafiki — رفيقي — is an Adaptive AI tutor designed specifically for Moroccan students. The **MVP targets 2ème Bac** (Year 12) with three subjects: **Mathématiques, Physique-Chimie, and English**. It operates in **French** (for Maths/Physics) or **English** (for the English subject). Arabic-language subjects (Philosophie, Arabe, Éducation Islamique) are planned for a post-MVP phase.

### **Standard Student Tier (MVP Target)**
* **Pre-Loaded Knowledge Base:** The app ships with a pre-built ChromaDB built from all 2Bac PDFs — students can ask questions **immediately, without uploading anything**.
* **Temporary Session RAG:** Students can upload their own PDFs or images. The backend extracts the text via OCR (Qwen2.5-VL) and temporarily merges it into the knowledge base for that specific chat session.
* **AI Features (MVP):**
  * ✅ **Q&A Chat** — Step-by-step answers grounded in the pre-built 2Bac knowledge base (RAG + fine-tuned LLM), in French or English.
  * ✅ **Exercise Correction** — Student uploads a blank exercise or one with their own answers; AI corrects it like a professor with full step-by-step solutions.
  * 🔶 **Cadre Référenciel (الإطار المرجعي)** — UI exists in MVP to display extracted learning objectives.
  * 🔶 **Exercise Generation** — UI placeholder in MVP; connected to AI post-MVP.
  * 🔶 **Resume Generation** — UI placeholder in MVP; connected to AI post-MVP.
  * 🔶 **Exam Generation & Correction** — UI placeholders in MVP; connected to AI post-MVP.
* **Data Persistence & Memory:** 
  * The MVP uses strict session-based temporary memory (clears on restart). 
  * Post-MVP, we will integrate a free external database like Supabase (PostgreSQL) to store student accounts, chat histories, and uploaded document RAG indexes persistently.
* **RAG is permanent:** Fine-tuning teaches the model *how* to answer (style, format, step-by-step reasoning). RAG provides *what* to answer about (specific theorems, formulas, examples). Both are always used together at inference time.

---

## **2. Production Architecture (3-Server Split)**

The project uses a professional **3-server architecture** — each layer has its own dedicated hosting platform, all free-tier for the MVP.

### **Architecture Diagram**

```
STUDENT'S BROWSER
        │  HTTPS
        ▼
┌─────────────────────────────────────────────┐
│  VERCEL — Frontend                          │
│  Next.js 16 · JavaScript · Tailwind CSS     │
│  (UI styled with premium Stitch templates)  │
│  / → Landing page                           │
│  /chat → Q&A Chat                           │
│  /correction → Exercise Correction          │
└─────────────────┬───────────────────────────┘
                  │  POST /api/upload
                  │  POST /api/ask
                  │  POST /api/correct
                  ▼
┌─────────────────────────────────────────────┐
│  KAGGLE — Backend & AI Layer            ✅  │
│  Python 3.11 · FastAPI · Uvicorn            │
│  Dual T4 GPUs (15GB each) + Localtunnel     │
│  GPU 0: Text Model (4-bit quant)            │
│  GPU 1: Vision Model (4-bit quant)          │
└─────────────────┬───────────────────────────┘
                  │  Model Weights
                  ▼
┌─────────────────────────────────────────────┐
│  HUGGINGFACE — Model Storage                │
│  Model (Text): rafiki-qwen-2.5-finetune     │
│  Model (Vision): Qwen2.5-VL-3B-Instruct     │
│  Dataset: ChromaDB index                    │
└─────────────────────────────────────────────┘
```

### **Component Overview**

| Component | Model / Tool | Purpose | Runs On |
|---|---|---|---|
| **Backend API** | `FastAPI` + `Localtunnel` | Orchestrates OCR, RAG, and serves the public URL. | Kaggle Notebook |
| **Backend OCR** | `Qwen2.5-VL-3B-Instruct` (4-bit) | Live OCR for student-uploaded PDFs/Images. | Kaggle GPU 1 |
| **Fine-tuned LLM** | `rafiki-qwen-2.5-finetune` (4-bit)| Generates step-by-step Q&A answers and corrections. | Kaggle GPU 0 |
| **Vector Database** | `ChromaDB` | Stores global 2Bac chunks AND temporary session chunks. | Kaggle Disk |
| **Frontend App** | `Next.js` | Student-facing interface with modern, premium UI/UX. | Vercel (free tier) |

---

## **3. MVP Build Roadmap**

### **Phase 1 — PDF Extraction Pipeline**
> **Objective:** Convert raw Moroccan curriculum PDFs → structured Markdown chunks.
**Success Condition:** All 8 PDFs/documents → clean Markdown + `chunks.json` per subject, pushed to HuggingFace. ✅

### **Phase 2 — RAG Knowledge Base**
> **Objective:** Build a semantic index for instant lesson retrieval.
**Success Condition:** Query `"How to find the derivative of a polynomial?"` returns the correct lesson chunks. ✅

### **Phase 3 — Model Fine-Tuning**
> **Objective:** Teach a small LLM the style and format of Moroccan curriculum Q&A.
**Success Condition:** Fine-tuned model answers in the correct Moroccan curriculum style. ✅

### **Phase 4 & 4.5 — FastAPI Backend + Live OCR**
> **Objective:** Expose RAG retrieval and LLM inference, and handle live user uploads.
**Actions:**
1. Implemented `/api/ask` and `/api/correct` utilizing HuggingFace Inference API.
2. Added `/api/upload` endpoint using `PyMuPDF` and `Qwen2.5-VL` Serverless API for OCR.
3. Added Ephemeral In-Memory ChromaDB for temporary session RAG.
**Success Condition:** Uploading a PDF returns extracted text, and asking a question retrieves context from it. ✅

### **Phase 5 — Next.js Frontend**
> **Objective:** Build the student-facing web interface and deploy to Vercel.
**Success Condition:** Student interface fully styled using premium templates (Stitch) and navigation fixed. ✅

### **Phase 6 — Full Integration & End-to-End Test**
> **Objective:** Validate the complete 3-server pipeline works together.
**Success Condition:** End-to-end testing successful with frontend talking to the deployed backend. ⬜ Not started

---

## **4. Status Log**

[2026-06-08]  Phase 4.5 (Backend OCR & Session RAG) Completed
              - Shifted backend deployment to Kaggle Notebooks utilizing Dual T4 GPUs.
              - Implemented 4-bit Quantization for both Text and Vision models to prevent OOM.
              - Exposed FastAPI to the frontend using Localtunnel.
              - extraction_service.py now runs Qwen2.5-VL-3B locally on GPU 1.
              - llm_service.py now runs the fine-tuned text model locally on GPU 0.

[2026-06-07]  Frontend UX Refinements & Bug Fixes
              - Applied premium Stitch design exports to the UI.
              - Fixed scroll, margin, and overflow bugs on all dashboard pages.
              - Resolved routing and 404 errors on the landing page.

[2026-06-07]  Phase 4 (Backend) and Phase 5 (Frontend) MVP code complete
              - FastAPI backend fully implemented.
              - Next.js frontend built with Tailwind CSS.

[2026-06-06]  Phase 3 model and dataset selected
              - Selected Qwen/Qwen2.5-1.5B-Instruct for text LoRA fine-tuning.

[2026-06-05]  Architecture upgraded to 3-server strategy
              - Dropped Gradio / HuggingFace Spaces approach.
              - New stack: Vercel (Next.js) + Railway (FastAPI) + HuggingFace (AI).

[2026-06-03]  MVP scope finalised
              - Target year: 2ème Bac only.
              - Subjects: Mathématiques · Physique-Chimie · English.
