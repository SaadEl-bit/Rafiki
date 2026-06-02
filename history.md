# history.md: Moroccan Adaptive AI Tutor - Conversation & Progress Log

## 1. Project Vision & Scope
* **Goal:** Build an Adaptive AI guide for Moroccan students (Primary to High School / 2Bac).
* **Capabilities:** Bilingual (MSA and French), logic resolution for Math, Physics, and Sciences, and curriculum alignment with the official Moroccan Pedagogy and Frame of Reference (الإطار المرجعي).
* **Tiers:** * *Standard Student:* Access to curriculum, document upload, and AI reasoning.
    * *Private School/Educator:* Level detection via diagnostic quizzes, classroom creation, and student progress analytics.

## 2. Core AI Architecture & Logic
We established a 4-step modern AI stack to handle complex Moroccan curricula:
1.  **Data Extraction (The Parser):** Use **`Qwen2.5-VL-7B`** to process complex PDFs (reading math formulas, physics diagrams, and text) and convert them to clean Markdown.
2.  **Knowledge Base (RAG):** Store the parsed curriculum in a vector database (`ChromaDB` or `FAISS`) to force the AI to use Moroccan context and prevent hallucination.
3.  **Reasoning Engine:** Fine-tune **`DeepSeek-R1-Distill-Qwen-14B`** using LoRA via the `Unsloth` library on Moroccan QA pairs.
4.  **Frontend/UI:** Use `Gradio` or `Streamlit` to build the student and teacher dashboards.

## 3. Infrastructure & Cloud GPU Decisions
We analyzed cloud GPU options and assigned them specific roles:
* **Kaggle:** Selected as the primary environment for Phase 1 (Data Engineering). It provides reliable free GPUs (30h/week T4 x2) and seamless dataset hosting.
* **Hugging Face:** Used for storing the private dataset (parsed PDFs) and hosting the final fine-tuned model weights.
* **RunPod:** Selected for Phase 3 (Model Fine-Tuning). It provides cost-effective, heavy-duty GPUs (RTX 3090/4090) required to run Unsloth and train the 14B DeepSeek model.

## 4. Documentation Generated
* We generated a complete, formal `project_description.md` file outlining the core concepts, model architecture, data strategy (proprietary vs. open-source datasets), and a 5-Phase standard MVP Build Plan. 

## 5. Technical Setup & Coding Progress
* **Hugging Face Authentication:** Successfully generated a Hugging Face Access Token with `WRITE` permissions (named *M3ellem-AI*).
* **Kaggle Setup:** Successfully stored the HF Token securely in the Kaggle Notebook's "Secrets" tab (`HF_TOKEN`) to allow automated dataset uploads. 
* **Library Context:** Clarified the difference between `Transformers` (the Hugging Face Python library used to run the models) and `ModelScope` (Alibaba's open-source model hub/library).

## 6. Current Status & Troubleshooting (Where we left off)
* **Task:** Writing the Python script in Kaggle to extract text/math from a 109-page College Probability & Statistics PDF using `Qwen2.5-VL-7B`.
* **Issue 1 (OOM Warning):** Feeding a 109-page PDF directly to a 16GB Kaggle GPU will cause an Out-Of-Memory crash. The strategy shifted to slicing 1-2 pages at a time for testing.
* **Issue 2 (AI Hallucination):** The initial script failed and the AI hallucinated an apology ("I haven't provided any document"). This happened because `qwen_vl_utils` only understands images, not direct PDF files. 
* **The Fix:** We implemented a new script using the `pdf2image` library (and `poppler-utils`) to slice the PDF into images first, and then pass those images to Qwen's vision processor.

**Next Immediate Step:** Run the corrected `pdf2image` Python script in Kaggle on a 2-page slice of the Probability PDF to verify that Qwen correctly extracts the math formulas into Markdown.