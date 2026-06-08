# Phase 4 & 5: Backend & Frontend Deployment

The model fine-tuning is officially complete, and the model `Saad-Elouakate/rafiki-qwen-2.5-finetune` is now hosted on Hugging Face. We will now move forward to Phase 4 (FastAPI Backend) and Phase 5 (Next.js Frontend) to deploy the actual M3allem application.

## Goal

Create a production-ready infrastructure with a 3-server split:
1. **HuggingFace Serverless Inference API**: Hosts the fine-tuned model (already completed).
2. **FastAPI Backend (Railway)**: Handles the RAG pipeline (retrieving chunks from ChromaDB) and acts as the bridge between the frontend and the HuggingFace AI.
3. **Next.js Frontend (Vercel)**: The web UI for students to ask questions and upload exercises for correction.

---

## User Review Required

> [!IMPORTANT]
> **API Key Setup:** Before we begin executing this phase, you will need a free Hugging Face token with **Read** access (your current write token is fine) to call the Serverless API. We will use environment variables for this.
> **Frontend Design:** For the Next.js frontend, do you have the "Figma/Stitch design template" mentioned in the project description exported as CSS, or should I generate a modern, responsive UI using standard CSS/Tailwind?

---

## Proposed Changes

### Phase 4: Backend (FastAPI)

#### [NEW] src/phase4_backend/requirements.txt
Add dependencies for the backend: `fastapi`, `uvicorn`, `huggingface_hub`, `pydantic`, `chromadb`, and `sentence-transformers`.

#### [NEW] src/phase4_backend/llm_service.py
Service that uses `huggingface_hub.InferenceClient` to send requests to `Saad-Elouakate/rafiki-qwen-2.5-finetune`. It will format the chat template to include the RAG context inside the system prompt and append the user's question.

#### [NEW] src/phase4_backend/rag_service.py
Service that wraps the existing `src.phase2_rag.RAGRetriever`. It will load the persistent ChromaDB index from disk or download it if necessary.

#### [NEW] src/phase4_backend/main.py
The core FastAPI application.
It will expose the following endpoints:
- `GET /health` (For Railway health checks)
- `POST /api/ask` (Accepts `{"question": "...", "subject": "Mathématiques"}`)
- `POST /api/correct` (Accepts an exercise body or parsed text + subject)

#### [NEW] Procfile / railway.json
Configuration to tell Railway how to start the Uvicorn server (e.g., `uvicorn src.phase4_backend.main:app --host 0.0.0.0 --port $PORT`).

---

### Phase 5: Frontend (Next.js)

#### [NEW] frontend/ (Next.js App Router)
We will initialize a new Next.js 14+ application in the `frontend` directory using `npx create-next-app` (using Javascript and Vanilla CSS).

#### [NEW] frontend/app/page.js
Landing page explaining what Rafiki is, with buttons to navigate to the Chat and Correction interfaces.

#### [NEW] frontend/app/chat/page.js
Interactive Chat UI where students can select a subject and type their questions. It will stream or display the response, parsing the `<think>` block as an expandable "Professor's Reasoning" accordion, and formatting LaTeX math using `react-markdown` and `rehype-katex`.

#### [NEW] frontend/app/correction/page.js
Interface for students to paste or upload their exercise and get a step-by-step correction from the AI.

---

## Verification & Deployment Plan

### 1. Local Backend Verification
- Start the FastAPI server locally.
- Send a `cURL` request to `http://localhost:8000/api/ask` with a test Maths question.
- Verify ChromaDB retrieval and Hugging Face Serverless API response.

### 2. Railway Deployment
- Push the backend code to GitHub.
- Link the repository to Railway and set environment variables (`HF_TOKEN`, etc.).
- Verify the `/health` endpoint is live on the public Railway URL.

### 3. Local Frontend Verification
- Set `NEXT_PUBLIC_API_URL` to point to the local or Railway backend.
- Run the Next.js dev server (`npm run dev`).
- Ask a question via the web UI and ensure the math formulas render correctly.

### 4. Vercel Deployment
- Push the frontend code to GitHub.
- Link to Vercel and set `NEXT_PUBLIC_API_URL` to the Railway production URL.
- Verify the end-to-end flow on the live Vercel domain.

---

## Execution Steps for the User

To proceed with this plan, please follow these steps:

1. **Provide HF Token:** Have your Hugging Face API token (with Read access) ready to use as an environment variable (`HF_TOKEN`). We will need this to test the backend locally and to deploy it on Railway.
2. **Clarify Design Assets:** Provide the "Figma/Stitch design template" CSS files mentioned in the project docs. If you don't have them handy, let me know, and I will build a premium Vanilla CSS design from scratch.
3. **Approve the Plan:** If you agree with this plan, reply with **"Approved"** or let me know if you want any modifications. Once approved, I will start by writing the FastAPI backend code.
