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

### **Private School & Educator Tier (Post-MVP)**
* **Student Level Detection** — Diagnostic questions to evaluate baseline understanding upon registration.
* **Teacher Dashboard** — Create virtual classrooms, invite students, track scores and progress.
* **Adaptive Teaching** — Analytics help teachers adapt their methods per student.

---

## **2. MVP Model Architecture**

The MVP uses a lean, **100% free-tier** AI stack. The goal is to validate the full pipeline with small samples before scaling.

### **Component Overview**

| Component | Model / Tool | Purpose | Runs On |
|---|---|---|---|
| **PDF Parser** | `Qwen2.5-VL-2B-Instruct` | Reads PDF page images, extracts math, diagrams, and text as structured Markdown | Kaggle (free T4 GPU) |
| **Embedding Model** | `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | Converts text chunks to vectors for semantic search (supports French + English) | CPU (Kaggle / local) |
| **Vector Database** | `ChromaDB` | Stores and searches embedded 2Bac course chunks — **ships with the app as the pre-built KB** | On-disk, CPU |
| **Fine-tuned LLM** | `Qwen2.5-1.5B-Instruct` (LoRA fine-tuned) | Generates step-by-step Q&A answers and exercise corrections in Moroccan 2Bac curriculum style | HuggingFace Serverless Inference API (free) |
| **Frontend App** | `Gradio` on HuggingFace Spaces | Student-facing interface: Q&A Chat (working), Exercise Correction (working), other tabs as UI placeholders | HuggingFace Spaces (CPU Basic, free) |

### **How HuggingFace Serverless Inference API Works (Step by Step)**

This is how the fine-tuned model is served to users **without any GPU server cost**:

1. **You fine-tune** the `Qwen2.5-1.5B-Instruct` model using LoRA on Kaggle (Phase 3).
2. **You upload** the fine-tuned model weights to your private HuggingFace model repository.
3. **HuggingFace hosts** the model on their own servers (free tier, with rate limits).
4. **Your Gradio app** sends a request to the HuggingFace Inference API endpoint:
   ```
   POST https://api-inference.huggingface.co/models/your-username/m3allem-model
   Headers: { Authorization: "Bearer YOUR_HF_TOKEN" }
   Body: { inputs: "[RAG context] + [student question]" }
   ```
5. **HuggingFace runs** the model and returns the generated answer.
6. **Gradio displays** the answer to the student.

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

**Tools:** `ChromaDB`, `sentence-transformers` multilingual embedding model, CPU (Kaggle or local)

**MVP Target:** Index all chunks from the 5 Phase 1 PDFs into a single persistent ChromaDB.

**Actions:**
1. Load all Markdown chunks from the HuggingFace dataset.
2. Use the multilingual embedding model to convert each chunk to a vector.
3. Store all vectors + original text + metadata (subject, level, chapter) in ChromaDB.
4. Write and test a retrieval function: given a student query, return the top-3 most relevant chunks.
5. Save the ChromaDB collection to disk — this is the **pre-built KB that ships with the Gradio app**.
6. Upload the ChromaDB artifact to HuggingFace as a dataset.

**Success Condition:** Query `"How to find the derivative of a polynomial?"` or `"Loi de Newton?"` → returns the correct lesson chunks from the right subject. ✅

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

### **Phase 4 — Gradio App (Frontend)**
> **Objective:** Build the student-facing interface on HuggingFace Spaces.

**Tools:** `Gradio`, HuggingFace Spaces (CPU Basic, free), `chromadb`, `sentence-transformers`

**MVP Test:** A working Gradio app with Q&A Chat and Exercise Correction connected to real AI, and all other tabs as UI placeholders.

**Actions:**
1. Create a HuggingFace Space (Gradio, Blank template, CPU Basic, Public).
2. Load the pre-built ChromaDB (from Phase 2) at app startup — students can use the app without uploading anything.
3. Build the Gradio interface with tabs:
   * ✅ **Q&A Chat** — Student types a question → RAG retrieves top-3 chunks from the pre-built KB → fine-tuned LLM generates a step-by-step answer in French or English.
   * ✅ **Exercise Correction** — Student uploads a PDF or image of an exercise (blank or with their answers) → AI corrects it like a professor with full solution.
   * 🔶 **Generate Exercise** — UI tab exists, shows a static example placeholder.
   * 🔶 **Generate Resume** — UI tab exists, shows a static example placeholder.
   * 🔶 **Upload your own PDF** — UI exists, not connected to RAG yet.
   * 🔶 **Level / Subject selection** — UI exists, no backend filtering yet.
4. Store the HuggingFace API token as a **Secret** in Space settings (not in code).

**Success Condition:** App loads without upload, student asks a 2Bac Maths question, gets a correct step-by-step answer. Exercise correction also works. ✅

---

### **Phase 5 — Full Integration & End-to-End Test**
> **Objective:** Wire all components together and validate the complete pipeline works with real data.

**Tools:** All components from Phases 1–4.

**MVP Test:** One complete flow using 2Bac content: no upload → ask a Maths question → get answer → upload an exercise for correction.

**Actions:**
1. Upload the Phase 3 fine-tuned model to HuggingFace and enable the Serverless Inference API.
2. Replace placeholder model output in the Gradio app with real HuggingFace Inference API calls.
3. Test the complete user flow end-to-end:
   - Open the app (no upload needed)
   - Ask: *"Explique-moi comment dériver f(x) = x³ + 2x"*
   - Upload an exercise PDF → get professor-style correction
   - Verify answers are grounded in the pre-built 2Bac knowledge base
4. Fix any prompt formatting, retrieval quality, or API latency issues.

**Success Condition:** A working end-to-end demo: student opens app, asks a 2Bac question, gets a correct step-by-step answer without uploading anything. ✅

---

## **5. Free-Tier Resource Map**

| Task | Platform | Cost |
|---|---|---|
| PDF extraction (Phase 1) | Kaggle (T4 GPU, 30 hrs/week) | Free |
| RAG index building (Phase 2) | Kaggle or local laptop (CPU) | Free |
| Model fine-tuning (Phase 3) | Kaggle (T4 GPU) | Free |
| Dataset & model hosting | HuggingFace (free account) | Free |
| Gradio app hosting (Phase 4) | HuggingFace Spaces (CPU Basic) | Free |
| LLM inference for users (Phase 5) | HuggingFace Serverless Inference API | Free (rate-limited) |
| **TOTAL MVP COST** | | **$0** |

> **Post-MVP (Production):** Migrate fine-tuning to RunPod (RTX 3090, ~$0.34/hr) for the full dataset, and upgrade HuggingFace Space to GPU for lower latency inference.

---

## **6. Project Status**

### **Current Phase:** Phase 1 — PDF Extraction Pipeline

### **Completed:**
* MVP scope finalised: **2ème Bac only**, subjects: **Mathématiques · Physique-Chimie · English**.
* Architecture confirmed: pre-built ChromaDB as default KB (no upload required); RAG is permanent even after fine-tuning.
* Fully working MVP features: **Q&A Chat** and **Exercise Correction**. All other features are frontend-only placeholders.
* HuggingFace Space created (Gradio, Blank, CPU Basic, Public).
* GitHub repository initialized.
* Kaggle pipeline script (`pdf_to_markdown_pipeline.py`) written, tested on 6-page PDF → verified Markdown + chunks output.
* `src/phase1_extraction/` module written (6 files, CPU fallback mode, batch folder support).

### **Resolved Blockers:**
* Original script used `Qwen2.5-VL-7B-Instruct` in bfloat16 → **OOM on T4** (14.5 GB VRAM).
* **Fix:** Using `Qwen2.5-VL-2B-Instruct` → ~4 GB VRAM, ~12 GB headroom. ✅

### **Next Action:**
Run `pdf_to_markdown_pipeline.py` on Kaggle against **all 5 PDFs in `Document-Data-Set/2bac/`** (Maths, Physics, English), verify `chunks.json` quality for all three subjects, then move to Phase 2 to build the persistent 2Bac ChromaDB.