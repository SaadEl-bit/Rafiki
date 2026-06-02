# **Project Description: M3allem — Moroccan Adaptive AI Tutor Platform**

---

## **1. Core Vision & Features**

### **Overview**
M3allem is an Adaptive AI tutor designed specifically for Moroccan students, covering all educational levels from Primary School through High School (2Bac). It operates in both **Modern Standard Arabic (MSA)** and **French**, depending on the subject matter.

### **Standard Student Tier (MVP Target)**
* **Curriculum Alignment:** The AI's knowledge base is strictly linked to the Moroccan core program — the Pedagogy (البيداغوجية) and the Frame of Reference (الإطار المرجعي).
* **Pre-Loaded Knowledge:** Students select their educational level and specialization to access courses, exercises, and exam examples from a proprietary dataset.
* **Custom Workspace:** Students upload their own PDFs/course documents, which are indexed and made queryable.
* **AI Features:**
  * **Q&A Chat** — Step-by-step answers grounded in uploaded content (French or MSA)
  * **Exercise Generation** — AI generates similar exercises, with an option to reveal the full solution after the student attempts it
  * **Resume Generation** — AI summarizes a chapter or course into a structured revision sheet

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
| **Embedding Model** | `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | Converts text chunks to vectors for semantic search (supports French + Arabic) | CPU (Kaggle / local) |
| **Vector Database** | `ChromaDB` | Stores and searches embedded course chunks (RAG retrieval) | In-memory or on-disk, CPU |
| **Fine-tuned LLM** | `Qwen2.5-1.5B-Instruct` (LoRA fine-tuned) | Generates step-by-step answers, exercises, and resumes in Moroccan curriculum style | HuggingFace Serverless Inference API (free) |
| **Frontend App** | `Gradio` on HuggingFace Spaces | Student-facing chat, upload, and output interface | HuggingFace Spaces (CPU Basic, free) |

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

### **A. MVP Sample Dataset (Build First)**
The MVP is validated on a **minimal but real sample** of Moroccan curriculum data:

* **Phase 1 test:** 1 PDF document (6 pages) from the Probability & Statistics course (`Cours_Proba-Statistiques-1-26.pdf`, pages 1–6).
* **Phase 3 test:** A small hand-crafted or extracted dataset of ~50–200 `(question, reasoning_steps, answer)` triplets from the same subject — enough to observe whether fine-tuning changes the model's output style.
* **Format for fine-tuning:**
  ```json
  {
    "input": "Calculer P(A∪B) sachant que P(A)=0.4, P(B)=0.3, P(A∩B)=0.1",
    "thinking": "J'applique la formule de l'union: P(A∪B) = P(A) + P(B) - P(A∩B)...",
    "output": "**Solution:**\nP(A∪B) = 0.4 + 0.3 - 0.1 = **0.6**"
  }
  ```

### **B. Full Production Dataset (Post-MVP)**
After the MVP pipeline is validated:
* Scrape national education portals for all subjects (Primary → 2Bac).
* Process full exam archives with the Qwen2.5-VL-3B extraction pipeline.
* Scale fine-tuning to the full dataset using a larger model (DeepSeek-R1-14B) on RunPod.

### **C. Ready-to-Use Base Models**
The models selected (`Qwen2.5` family) already have strong pre-trained knowledge of:
* French and Modern Standard Arabic (MSA)
* General mathematics and scientific reasoning
* Instruction-following (answering questions, following formatting rules)

---

## **4. MVP Build Roadmap**

### **Phase 1 — PDF Extraction Pipeline**
> **Objective:** Convert raw Moroccan curriculum PDFs → structured Markdown chunks.

**Tools:** `Qwen2.5-VL-2B-Instruct`, Kaggle (free T4 GPU), HuggingFace Datasets

**MVP Test:** Process a single 6-page PDF.

**Actions:**
1. Pipeline script uses `Qwen2.5-VL-2B-Instruct` to stay well within T4 VRAM limits (~4 GB model size, ~12 GB headroom for images).
2. Render each PDF page as an image (150 DPI to save VRAM).
3. Feed each page image to the model with the extraction prompt.
4. Save output as structured Markdown with LaTeX math preserved.
5. Push extracted chunks to a **private HuggingFace Dataset** repository.

**Success Condition:** 6-page PDF → clean Markdown file with correct math notation, pushed to HuggingFace. ✅

---

### **Phase 2 — RAG Knowledge Base**
> **Objective:** Make the AI able to retrieve the exact relevant lesson when a student asks a question.

**Tools:** `ChromaDB`, `sentence-transformers` multilingual embedding model, CPU (Kaggle or local)

**MVP Test:** Index the chunks from the 6-page Phase 1 output.

**Actions:**
1. Load the Markdown chunks from the HuggingFace dataset.
2. Use the multilingual embedding model to convert each chunk to a vector.
3. Store all vectors + original text + metadata (subject, level, chapter) in ChromaDB.
4. Write and test a retrieval function: given a student query, return the top-3 most relevant chunks.
5. Save the ChromaDB collection to disk and upload it to HuggingFace as a dataset artifact.

**Success Condition:** Query `"Comment calculer P(A∩B)?"` → returns the correct lesson chunks. ✅

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

**MVP Test:** A working Gradio app with all 4 features connected to mock/placeholder model output.

**Actions:**
1. Create a HuggingFace Space (Gradio, Blank template, CPU Basic, Public).
2. Build the Gradio interface with 4 tabs:
   * 📤 **Upload PDF** — Student uploads a document, it gets indexed into ChromaDB on the fly.
   * 💬 **Ask a Question** — Chat interface. Student types a question → RAG retrieves context → answer generated.
   * 📝 **Generate Exercise** — AI generates a similar exercise. Button: "Show Solution" reveals the answer.
   * 📋 **Generate Resume** — AI creates a structured chapter summary/revision sheet.
3. Store the HuggingFace API token as a **Secret** in Space settings (not in code).
4. Connect the Space's ChromaDB to the pre-built knowledge base from Phase 2.

**Success Condition:** App loads, student can upload a PDF, ask a question, and see a response. ✅

---

### **Phase 5 — Full Integration & End-to-End Test**
> **Objective:** Wire all components together and validate the complete pipeline works with real data.

**Tools:** All components from Phases 1–4.

**MVP Test:** One complete flow: upload 6-page PDF → index → ask question → exercise → resume.

**Actions:**
1. Upload the Phase 3 fine-tuned model to HuggingFace and enable the Serverless Inference API.
2. Replace placeholder model output in the Gradio app with real HuggingFace Inference API calls.
3. Test the complete user flow end-to-end:
   - Upload the 6-page Probability PDF
   - Ask: *"Explique-moi la formule de Bayes"*
   - Generate a similar exercise → reveal solution
   - Generate a resume of the chapter
4. Fix any prompt formatting, retrieval quality, or API latency issues.

**Success Condition:** A working end-to-end demo with real AI responses grounded in the uploaded course content. ✅

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
* Project architecture finalized and confirmed.
* HuggingFace Space created (Gradio, Blank, CPU Basic, Public).
* GitHub repository initialized.
* Kaggle pipeline script (`pdf_to_markdown_pipeline.py`) written.
* Kaggle notebook created with `Cours_Proba-Statistiques-1-26.pdf` uploaded as a dataset.

### **Current Blocker:**
* Original script used `Qwen2.5-VL-7B-Instruct` in bfloat16 → **OOM on T4** (model uses 14.5 GB, leaves only 0.5 GB for inference).
* **Fix:** Using `Qwen2.5-VL-2B-Instruct` → model uses ~4 GB VRAM, leaving ~12 GB headroom for image inputs. ✅

### **Next Action:**
Run `pdf_to_markdown_pipeline.py` on Kaggle with `Qwen2.5-VL-2B-Instruct` (already set in script) against the 6-page test PDF and verify clean Markdown output is produced and pushed to HuggingFace.