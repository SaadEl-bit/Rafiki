# **Project Description: M3allem — Moroccan Adaptive AI Tutor Platform**

---

## **1. Core Vision & Features**

### **Overview**
M3allem is an Adaptive AI tutor designed specifically for Moroccan students. The **MVP targets 2ème Bac** (Year 12) with three subjects: **Mathématiques, Physique-Chimie, and English**. It operates in **French** (for Maths/Physics) or **English** (for the English subject). Arabic-language subjects (Philosophie, Arabe, Éducation Islamique) are planned for a post-MVP phase.

### **Standard Student Tier (MVP Target)**
* **Pre-Loaded Knowledge Base:** The app ships with a pre-built ChromaDB built from all 2Bac PDFs — students can ask questions **immediately, without uploading anything**.
* **Custom Workspace (post-MVP):** Students will also be able to upload their own PDFs, which will be indexed and merged into the knowledge base for that session. *UI is present in MVP but not connected to RAG yet.*
* **AI Features (MVP):**
  * ✅ **Q&A Chat** — Step-by-step answers grounded in the pre-built 2Bac knowledge base (RAG + fine-tuned LLM), in French or English
  * ✅ **Exercise Correction** — Student uploads a blank exercise or one with their own answers; AI corrects it like a professor with full step-by-step solution
  * 🔶 **Exercise Generation** — UI placeholder in MVP; connected to AI post-MVP
  * 🔶 **Resume Generation** — UI placeholder in MVP; connected to AI post-MVP
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
│  Next.js 14+ · JavaScript                  │
│  / → Landing page                          │
│  /app/chat → Q&A Chat                      │
│  /app/correction → Exercise Correction     │
│  /app/exercise → Generate Exercise (later) │
│  /app/resume → Generate Resume (later)     │
└─────────────────┬───────────────────────────┘
                  │  POST /api/ask
                  │  POST /api/correct
                  ▼
┌─────────────────────────────────────────────┐
│  RAILWAY — Backend                          │
│  Python 3.11 · FastAPI · Uvicorn            │
│  RAGRetriever (Phase 2, reused as-is)       │
│  HuggingFace Inference API client           │
└─────────────────┬───────────────────────────┘
                  │  HF Serverless Inference API
                  ▼
┌─────────────────────────────────────────────┐
│  HUGGINGFACE — AI Layer                     │
│  Dataset: chunks (Phase 1 output)           │
│  Dataset: ChromaDB index (Phase 2 output)   │
│  Model: Qwen2.5-1.5B fine-tuned (Phase 3)  │
└─────────────────────────────────────────────┘
```

### **Component Overview**

| Component | Model / Tool | Purpose | Runs On |
|---|---|---|---|
| **PDF Parser** | `Qwen2.5-VL-2B-Instruct` | Reads PDF page images, extracts math, diagrams, and text as structured Markdown | Kaggle (free T4 GPU) |
| **Embedding Model** | `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | Converts text chunks to vectors for semantic search (supports French + English) | CPU (Kaggle / local) |
| **Vector Database** | `ChromaDB` | Stores and searches embedded 2Bac course chunks — pre-built KB downloaded at backend startup | On-disk, Railway |
| **Fine-tuned LLM** | `Qwen2.5-1.5B-Instruct` (LoRA fine-tuned) | Generates step-by-step Q&A answers and exercise corrections in Moroccan 2Bac curriculum style | HuggingFace Serverless Inference API (free) |
| **Backend API** | `FastAPI` on Railway | Exposes `/api/ask` and `/api/correct` — handles RAG retrieval and LLM calls | Railway (free tier) |
| **Frontend App** | `Next.js` on Vercel | Student-facing interface: Landing page + Q&A Chat + Exercise Correction + UI placeholders | Vercel (free tier) |

### **How HuggingFace Serverless Inference API Works (Step by Step)**

This is how the fine-tuned model is served to users **without any GPU server cost**:

1. **You fine-tune** the `Qwen2.5-1.5B-Instruct` model using LoRA on Kaggle (Phase 3).
2. **You upload** the fine-tuned model weights to your private HuggingFace model repository.
3. **HuggingFace hosts** the model on their own servers (free tier, with rate limits).
4. **Your FastAPI backend** (on Railway) sends a request to the HuggingFace Inference API:
   ```
   POST https://api-inference.huggingface.co/models/Saad-Elouakate/m3allem-qwen
   Headers: { Authorization: "Bearer HF_TOKEN" }
   Body: { inputs: "[RAG context chunks] + [student question]" }
   ```
5. **HuggingFace runs** the model and returns the generated answer.
6. **FastAPI** returns the answer to the Next.js frontend, which displays it to the student.

> **Free tier limits:** ~1,000 requests/day, cold start possible (model loads in ~20 sec if idle). Sufficient for MVP testing.

---

## **3. Data Strategy**

### **A. MVP Dataset (2Bac — 3 subjects)**
The MVP is built and validated on the **2ème Bac PDFs already collected** in `Document-Data-Set/2bac/`:

| File | Subject | Use |
|---|---|---|
| `Maths-fonctions-cours.pdf` | Mathématiques | Pre-built KB |
| `Maths-fonctions-corrige-serie-d-exercices.pdf` | Mathématiques | Pre-built KB + fine-tuning Q&A pairs |
| `Physique-lois-de-newton-cours.pdf` | Physique-Chimie | Pre-built KB |
| `English-cours.pdf` | English | Pre-built KB |
| `English-examen.pdf` | English | Pre-built KB + fine-tuning Q&A pairs |

* **Phase 1:** All 5 PDFs → Markdown chunks via Qwen2.5-VL-2B on Kaggle.
* **Phase 2:** All chunks → persistent ChromaDB (this becomes the pre-built KB that ships with the app).
* **Phase 3:** Extract ~50–200 `(question, reasoning_steps, answer)` triplets from the exercise PDFs for fine-tuning style:
  ```json
  {
    "input": "Déterminer la dérivée de f(x) = x³ + 2x",
    "thinking": "J'applique la règle de dérivation: (x^n)' = n·x^(n-1)...",
    "output": "**Solution:**\nf'(x) = 3x² + 2"
  }
  ```

### **B. Full Production Dataset (Post-MVP)**
After the MVP pipeline is validated:
* Expand to other 2Bac subjects: SVT, Physique-Chimie full programme, Arabic subjects (Arabe, Philosophie, Éducation Islamique).
* Add Tronc Commun and 1ère Bac levels.
* Scrape national education portals for all subjects.
* Scale fine-tuning to the full dataset using a larger model (DeepSeek-R1-14B) on RunPod.
* For Arabic-language subjects, evaluate `Jais-13B` (Arabic-native LLM) as an alternative to Qwen.

### **C. Ready-to-Use Base Models**
The model selected (`Qwen2.5` family) already has strong pre-trained knowledge of:
* French and English (primary MVP languages)
* General mathematics, physics, and scientific reasoning
* Instruction-following (step-by-step answers, formatting rules)
* Modern Standard Arabic (MSA) — available for post-MVP Arabic subjects without switching models

---

## **4. MVP Build Roadmap**

### **Phase 1 — PDF Extraction Pipeline**
> **Objective:** Convert raw Moroccan curriculum PDFs → structured Markdown chunks.

**Tools:** `Qwen2.5-VL-2B-Instruct`, Kaggle (free T4 GPU), HuggingFace Datasets

**MVP Target:** Process all 5 PDFs in `Document-Data-Set/2bac/` (Maths · Physics · English).

**Actions:**
1. Pipeline uses `Qwen2.5-VL-2B-Instruct` to stay well within T4 VRAM limits (~4 GB model, ~12 GB headroom for images).
2. Render each PDF page as an image (150 DPI).
3. Feed each page image to the model with the extraction prompt.
4. Save output as structured Markdown with LaTeX math preserved.
5. Push extracted chunks to a **private HuggingFace Dataset** repository.

**Success Condition:** All 5 PDFs → clean Markdown + `chunks.json` per subject, pushed to HuggingFace. ✅

---

### **Phase 2 — RAG Knowledge Base**
> **Objective:** Make the AI able to retrieve the exact relevant lesson when a student asks a question.

**Concepts:**
* **Embeddings:** The `sentence-transformers` model converts extracted text into a list of numbers (a vector) where similar meanings have similar numbers.
* **ChromaDB:** A specialized Vector Database that stores these vectors and quickly searches for the closest match to a student's question.

**Tools:** `ChromaDB`, `sentence-transformers/all-MiniLM-L6-v2`, CPU (Kaggle)

**MVP Target:** Index all chunks from the Phase 1 HuggingFace dataset into a single persistent ChromaDB.

**Actions:**
1. Load all Markdown chunks from the HuggingFace dataset (e.g., `Saad-Elouakate/AI-Adaptive-Learning`).
2. Use the multilingual embedding model to convert each chunk's `content_string` to a vector.
3. Store all vectors + original text + metadata (subject, level, chapter) in a local ChromaDB folder.
4. Write and test a retrieval function: given a student query, return the top-5 most relevant chunks.
5. Save the ChromaDB collection to disk — this is the **pre-built KB that ships with the Gradio app**.
6. Upload the ChromaDB artifact to a **new HuggingFace dataset** (e.g., `Saad-Elouakate/AI-Adaptive-Learning-Index`).

**Success Condition:** Query `"How to find the derivative of a polynomial?"` or `"Loi de Newton?"` → returns the correct lesson chunks from the right subject. 

---

### **Phase 3 — Model Fine-Tuning**
> **Objective:** Teach a small LLM the style and format of Moroccan curriculum Q&A.

**Tools:** `Unsloth`, `LoRA`, `Qwen2.5-1.5B-Instruct`, Kaggle (free T4 GPU)

**MVP Test:** Fine-tune on a small sample (~50–200 Q-A-Reasoning triplets) just to confirm training runs and the model output style changes.

**Actions:**
1. Load `Qwen2.5-1.5B-Instruct` in 4-bit quantization using Unsloth (fits comfortably on T4).
2. Attach LoRA adapters (low memory overhead, trains only the adapter layers).
3. Load the small Q-A-Reasoning dataset from HuggingFace.
4. Run a short training loop (1–3 epochs, just to observe results).
5. Compare model output before vs. after fine-tuning on a few test questions.
6. Push the fine-tuned LoRA weights to a **private HuggingFace Model** repository.

**Success Condition:** Fine-tuned model answers in the correct Moroccan curriculum style (step-by-step, proper French/MSA formatting). ✅

---

### **Phase 4 — FastAPI Backend**
> **Objective:** Expose RAG retrieval and LLM inference as a REST API that the frontend can call.

**Tools:** `FastAPI`, `Uvicorn`, `Pydantic`, Railway (free tier)

**MVP Target:** A deployed Railway API with two working endpoints: `/api/ask` and `/api/correct`.

**Actions:**
1. Create `src/phase4_backend/` with FastAPI app structure (routers, services, models).
2. Wrap `RAGRetriever` (Phase 2) into a `rag_service.py` — no code changes to Phase 2.
3. Create `llm_service.py` — calls the HuggingFace Inference API with the RAG context + student question.
4. Implement endpoints:
   * `POST /api/ask` — receives question + subject → returns AI answer
   * `POST /api/correct` — receives uploaded file + subject → returns step-by-step correction
   * `GET /health` — health check for Railway
5. Set environment variables on Railway (HF_TOKEN, HF_MODEL_ID, ALLOWED_ORIGINS).
6. Deploy to Railway via Git push.

**Success Condition:** `POST /api/ask` with a 2Bac Maths question returns a correct, formatted answer. ✅

---

### **Phase 5 — Next.js Frontend**
> **Objective:** Build the student-facing web interface and deploy to Vercel.

**Tools:** `Next.js 14+`, JavaScript, CSS (from Figma/Stitch design template), Vercel

**MVP Target:** A deployed Vercel app with a landing page and the two working AI features.

**Actions:**
1. Initialize `frontend/` as a Next.js 14+ project (App Router, JavaScript).
2. Build the landing page (`/`) — hero section, feature overview, CTA button.
3. Build the student app interface (`/app`) with:
   * ✅ **Q&A Chat** (`/app/chat`) — text input → calls `POST /api/ask` → displays formatted answer with LaTeX math.
   * ✅ **Exercise Correction** (`/app/correction`) — drag-and-drop PDF/image upload → calls `POST /api/correct` → displays step-by-step correction.
   * 🔶 **Generate Exercise** (`/app/exercise`) — UI placeholder, connected to AI post-MVP.
   * 🔶 **Generate Resume** (`/app/resume`) — UI placeholder, connected to AI post-MVP.
4. Apply the CSS design from the provided Figma/Stitch template.
5. Set `NEXT_PUBLIC_API_URL` environment variable on Vercel pointing to the Railway backend.
6. Deploy to Vercel via Git push.

**Success Condition:** Student opens the Vercel URL, navigates to Chat, asks a 2Bac question, gets a formatted answer from the Railway backend. ✅

---

### **Phase 6 — Full Integration & End-to-End Test**
> **Objective:** Validate the complete 3-server pipeline works together with real 2Bac data.

**Tools:** All components from Phases 1–5.

**Actions:**
1. Test the complete user flow:
   - Open the Vercel URL (no upload needed)
   - Ask: *"Explique-moi comment dériver f(x) = x³ + 2x"*
   - Upload an exercise PDF → get professor-style correction
   - Verify answers are grounded in the pre-built 2Bac knowledge base
2. Fix any CORS issues, prompt formatting, retrieval quality, or API latency issues.
3. Verify Railway cold-start time is acceptable; add a loading indicator in the frontend.

**Success Condition:** Full end-to-end demo working: student opens Vercel app, asks a 2Bac question, gets a correct answer served via Railway + HuggingFace. ✅

---

## **5. Free-Tier Resource Map**

| Task | Platform | Cost |
|---|---|---|
| PDF extraction (Phase 1) | Kaggle (T4 GPU, 30 hrs/week) | Free |
| RAG index building (Phase 2) | Kaggle or local laptop (CPU) | Free |
| Model fine-tuning (Phase 3) | Kaggle (T4 GPU) | Free |
| Dataset & model hosting | HuggingFace (free account) | Free |
| LLM inference (Phase 4 backend calls) | HuggingFace Serverless Inference API | Free (rate-limited) |
| Backend API hosting (Phase 4) | Railway (free $5/month credit) | ~Free for MVP |
| Frontend hosting (Phase 5) | Vercel (free tier) | Free |
| **TOTAL MVP COST** | | **~$0** |

> **Post-MVP (Production):** Migrate fine-tuning to RunPod (RTX 3090, ~$0.34/hr) for the full dataset. Upgrade Railway to a paid plan (~$5–20/month) for production traffic. Add Supabase (free tier) for user accounts and progress tracking when authentication is needed.

---

## **6. Project Status**

### **Current Phase:** Phase 2 — RAG Knowledge Base

### **Completed:**
* MVP scope finalised: **2ème Bac only**, subjects: **Mathématiques · Physique-Chimie · English**.
* Architecture upgraded: **3-server split** — Vercel (Next.js) + Railway (FastAPI) + HuggingFace (model + data).
* Deployment strategy confirmed: no Gradio, full professional stack with a landing page.
* Phase 1 complete: 965 structured chunks pushed to `Saad-Elouakate/AI-Adaptive-Learning` on HuggingFace.
* `src/phase1_extraction/` module written (6 files, CPU fallback mode, batch folder support).
* `src/phase2_rag/` module created (embedder, retriever, config, main).
* GitHub repository initialized.

### **Resolved Blockers:**
* Original script used `Qwen2.5-VL-7B-Instruct` in bfloat16 → **OOM on T4** (14.5 GB VRAM).
* **Fix:** Using `Qwen2.5-VL-2B-Instruct` → ~4 GB VRAM, ~12 GB headroom. ✅

### **Next Action:**
Run `src/phase2_rag/main.py` on Kaggle to embed the 965 chunks into ChromaDB and push the index to `Saad-Elouakate/AI-Adaptive-Learning-Index` on HuggingFace.