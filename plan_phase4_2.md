# Phase 4.5: Backend Enhancements (OCR & Temporary RAG)

This plan outlines how to complete the backend to support dynamic document uploads, optical character recognition (OCR), and session-based RAG before connecting to the frontend.

## Approved Strategy

> [!TIP]
> **OCR Strategy (Approved):** We will use `Qwen/Qwen2.5-VL-7B-Instruct` (or similar VL model) hosted on the HuggingFace Serverless API. For PDFs, the backend will convert the pages to images using `PyMuPDF`, encode them as base64, and send them to the HuggingFace Vision API. The model will return the structured markdown/math text, which will then be chunked and added to the Temporary RAG.

> [!WARNING]
> **Data Persistence vs. Temporary Sessions:** You asked if it's easy to save documents and conversation memory for the MVP. **Yes, it is very easy!** We can use a lightweight SQLite database to store chat histories and save uploaded PDFs to a local folder. 
> *However*, because we are deploying on Railway's free tier, the server's hard drive resets every time the app restarts or redeploys, which would erase the SQLite database and saved files. 
> **Decision:** Should we (A) Stick to temporary memory for the MVP (clears on restart), (B) Use a free external database like Supabase (PostgreSQL) so memory is permanent, or (C) Keep it completely session-based (no memory between questions)?

## Proposed Changes

### 1. Document Upload & Extraction (OCR)
We will add dependencies for handling file uploads and parsing.
#### [MODIFY] src/phase4_backend/requirements.txt
- Add `python-multipart` (for FastAPI file uploads).
- Add `PyMuPDF` (for converting PDFs to images).
- Add `Pillow` (for image processing).

#### [NEW] src/phase4_backend/services/extraction_service.py
- A new service to handle extracting text from uploaded `PDF`, `PNG`, and `JPG` files.
- It will convert PDFs to base64 images and send them to `Qwen/Qwen2.5-VL-7B-Instruct` on HuggingFace via the InferenceClient.
- It will return the extracted Markdown/LaTeX text.

### 2. Temporary Session RAG Concept
We will modify the RAG service to support temporary collections.
#### [MODIFY] src/phase4_backend/services/rag_service.py
- Add functionality to chunk the extracted text from user uploads.
- Embed the chunks and store them in an **in-memory ChromaDB collection** (tied to a specific `session_id`).
- Modify the `retrieve_context` function to query **both** the global 2Bac database AND the temporary session database. It will merge the top results from both sources.

### 3. Conversation Memory (Optional MVP Feature)
If we decide to keep conversation memory:
#### [NEW] src/phase4_backend/services/memory_service.py
- Use SQLite (or in-memory lists for temporary sessions) to store past Q&A pairs linked to a `session_id`.
- Update `llm_service.py` to inject the past 3-4 messages into the prompt so Rafiki remembers the context of the conversation.

### 4. API Endpoints Update
We will update the routers to accept files and session IDs.
#### [MODIFY] src/phase4_backend/routers/ask.py
- Add a new endpoint `POST /api/upload` that accepts a file, extracts its text, creates the temporary RAG, and returns a `session_id`.
- Update `POST /api/ask` to accept an optional `session_id`. If provided, it will search the temporary RAG alongside the main RAG.

#### [MODIFY] src/phase4_backend/routers/correct.py
- Update `POST /api/correct` to accept either raw `exercise_text` OR an uploaded file (Multipart form data). If a file is provided, it extracts the text first before running the correction RAG pipeline.

## Verification Plan

### Automated Tests
- Test the new `/api/upload` endpoint using `curl` with a sample PDF.
- Test `/api/ask` with the returned `session_id` to ensure it retrieves content from the uploaded PDF.
- Test `/api/correct` with an image file to ensure the text is extracted and corrected properly.

### Manual Verification
- Deploy the updated backend to Railway.
- Use Postman to simulate a full session: Upload a document -> Ask a question about it -> Verify the HuggingFace model uses both the document and the global knowledge base.

---

## Step-by-Step Execution Plan

Here are the precise steps we will follow to build this out:

### **Step 1: Environment & Dependencies Setup**
- **Description:** Update `src/phase4_backend/requirements.txt` to include the new packages required for file processing.
- **Actions:** Add `python-multipart` (for receiving files), `PyMuPDF` (for splitting PDFs into images), and `Pillow` (for handling raw images).

### **Step 2: Build the Extraction Service (OCR)**
- **Description:** Create `src/phase4_backend/services/extraction_service.py` to handle incoming files and talk to HuggingFace.
- **Actions:** 
  - Write a function `process_upload(file)` that converts uploaded PDFs/images into base64 format.
  - Write a function `extract_text_via_vl(base64_images)` that sends the images to `Qwen/Qwen2.5-VL-7B-Instruct` on HuggingFace and returns the raw Markdown/math text.

### **Step 3: Implement Temporary Session RAG**
- **Description:** Update `src/phase4_backend/services/rag_service.py` to allow creating and querying temporary databases.
- **Actions:**
  - Add logic to chunk the text returned from Step 2.
  - Create a temporary, in-memory ChromaDB collection labeled with a generated `session_id`.
  - Modify the `retrieve_context` function so that if a `session_id` is passed, it pulls relevant chunks from BOTH the permanent 2Bac database and the temporary session database.

### **Step 4: Update the Ask & Correct API Routers**
- **Description:** Expose the new functionality through FastAPI endpoints in `ask.py` and `correct.py`.
- **Actions:**
  - Create a new endpoint `POST /api/upload` that receives a file, runs Step 2 and Step 3, and returns the `session_id`.
  - Update `POST /api/ask` and `POST /api/correct` to accept an optional `session_id`. If the ID is present, the backend will feed the temporary RAG context into the `generate_answer` function.

### **Step 5: Testing & Validation**
- **Description:** Verify the complete backend pipeline locally before linking the frontend.
- **Actions:** Run the FastAPI server and perform test requests (simulating an upload and a follow-up question) to ensure the OCR and temporary RAG are working perfectly.

---

## How to Test the Full Pipeline (Phase 1 to 4)

1. **Install All Requirements:**
   Run the following command from the root of the project to install all dependencies for Phase 1 through 4:
   ```bash
   pip install -r requirements_all.txt
   ```

2. **Set Environment Variables:**
   Create a `.env` file or export the following variables:
   ```bash
   HF_TOKEN=your_huggingface_token
   CHROMA_DB_DIR=./chroma_db_cache
   VL_MODEL_ID=Qwen/Qwen2.5-VL-7B-Instruct
   ```

3. **Start the Backend Server (Phase 4):**
   ```bash
   python -m uvicorn src.phase4_backend.main:app --host 0.0.0.0 --port 8000 --reload
   ```

4. **Test the `/api/upload` Endpoint (OCR & RAG):**
   Use Postman or `curl` to upload a test PDF:
   ```bash
   curl -X POST "http://localhost:8000/api/upload" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@/path/to/test_exercise.pdf" \
     -F "subject=Mathématiques"
   ```
   **Expected Result:** A JSON response containing the extracted Markdown text and a `session_id`.

5. **Test the `/api/ask` Endpoint (With Session Memory):**
   Use the `session_id` you received from the upload to ask a question:
   ```bash
   curl -X POST "http://localhost:8000/api/ask" \
     -H "Content-Type: application/json" \
     -d '{"question": "How do I solve the first equation in the document?", "subject": "Mathématiques", "session_id": "YOUR_SESSION_ID"}'
   ```
   **Expected Result:** A detailed step-by-step mathematical explanation using the uploaded document context.
