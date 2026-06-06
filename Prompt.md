**Build a web application called Rafiki — رفيقي — an AI-powered tutoring platform for Moroccan high school students (2ème Baccalauréat).**
**Slogan: "رفيقك في الدراسة — Ton compagnon pour le Bac" (Your study companion for the Bac)**

The app has two main sections: a Landing Page and a Student App.

---

## Landing Page (`/`)

The landing page is the first thing a student sees. It must communicate the value proposition immediately and guide the student into the app.

**Required sections, in order:**

1. **Hero Section**
   - App name: Rafiki (رفيقي)
   - Slogan: "رفيقك في الدراسة — Ton compagnon pour le Bac"
   - A one-line tagline that explains what the app does (AI tutor for Moroccan 2Bac students)
   - A clear primary CTA button: "Start Learning" or "Ask a Question" — clicking it goes to `/app/chat`
   - A secondary link: "Correct my Exercise" — goes to `/app/correction`

2. **Features Overview Section**
   - Three feature cards explaining the three main capabilities:
     - **Q&A Chat**: Ask any question about your 2Bac curriculum and get a step-by-step answer
     - **Exercise Correction**: Upload a photo or PDF of your exercise and get a full professor-style correction
     - **Resume Generation** *(coming soon — greyed out, not clickable)*: Auto-generate a structured summary of any chapter
   - Each card has an icon, a short title, and 1-2 sentences of description

3. **How It Works Section**
   - 3 steps shown horizontally:
     1. Choose your subject (Maths, Physics, English)
     2. Ask your question or upload your exercise
     3. Get a detailed, step-by-step answer instantly
   - No signup required — the AI works immediately

4. **Subjects Section**
   - Show the 3 supported subjects: Mathématiques, Physique-Chimie, English
   - Each shows an icon/badge and the label
   - Small note: "2ème Baccalauréat — Moroccan Curriculum"

5. **Footer**
   - App name + slogan: "رفيقك في الدراسة — Ton compagnon pour le Bac"
   - Links: Chat, Exercise Correction
   - A "built for Moroccan students" note

---

## Student App

The app is accessible via a persistent top navigation bar with:
- App name/logo "Rafiki — رفيقي" (links back to landing page)
- Navigation tabs: **Chat**, **Correction**, **Exercises** *(disabled)*, **Résumé** *(disabled)*
- A subject selector (dropdown or tabs): **Mathématiques · Physique-Chimie · English** — this selection persists across all pages

---

### Page 1 — Q&A Chat (`/app/chat`)

**Purpose:** Student types a question about their curriculum and gets a structured, step-by-step answer from the AI.

**Layout:**
- A subject selector at the top if not already chosen (Maths / Physics / English)
- A scrollable chat conversation area in the middle taking up most of the screen
  - Messages alternate between student (right-aligned) and AI (left-aligned)
  - AI responses render **formatted Markdown** including headings, bullet points, bold text, numbered steps
  - Math formulas render in **LaTeX** (not raw `$...$` strings — they must display as proper symbols)
  - Each AI response has a small "Copy" button
- A fixed input bar at the bottom:
  - Text input field: placeholder text "Pose ta question ici... / Ask your question here..."
  - A Send button
  - Pressing Enter also sends
- While the AI is generating: show a typing indicator (animated dots or a spinner)
- The conversation is stateless per session (no history saved between visits)

**User experience notes:**
- The student does not need to log in
- The student should be able to ask in French or English — no need to switch modes manually
- If the AI is loading (cold start), show a clear loading state: "The AI is waking up, this may take up to 20 seconds..."
- Show an error message if the API call fails, with a "Try again" button

---

### Page 2 — Exercise Correction (`/app/correction`)

**Purpose:** Student uploads a photo or PDF of an exercise (with or without their own answers written on it) and gets a complete, step-by-step correction.

**Layout:**
- A subject selector at the top (Maths / Physics / English)
- A large upload area in the center:
  - Drag-and-drop zone with text: "Drop your exercise here (PDF or image)"
  - A "Browse files" button as fallback
  - Accepted formats displayed: PDF, JPG, PNG
  - File size limit shown: e.g. "Max 10MB"
  - After a file is selected, show the filename and a small preview thumbnail (if image) or a PDF icon
  - A "Remove" button to change the file
- An optional text field below the upload: "Add a note (optional) — e.g. 'I'm stuck on question 2'"
- A large "Correct my Exercise" submit button
- After submission:
  - Show a loading state: "Analysing your exercise..."
  - The correction result appears below the upload area (or replaces it):
    - Rendered in formatted Markdown with numbered steps
    - Math formulas rendered as LaTeX
    - Sections clearly labelled: e.g. "Question 1 — Solution", "Question 2 — Solution"
  - A "Correct another exercise" button resets the form

**User experience notes:**
- No login required
- The page must handle large files gracefully (show an error if file is too large)
- If the API fails, show a friendly error with a "Try again" option
- The student's uploaded file is never stored permanently

---

### Pages 3 & 4 — Exercise Generation and Resume Generation (`/app/exercise`, `/app/resume`)

**These pages exist in the MVP but are not yet connected to AI.**

- Show the page layout with the input fields (e.g., "Choose a chapter", "Choose difficulty level") but all interactive elements are visually disabled
- Display a clear banner: "This feature is coming soon — stay tuned!"
- The navigation tab for these pages is visible but shows a "Coming Soon" badge

---

## Global UX Requirements

- **No login or registration required** for any MVP feature — the app is fully open
- **Fully responsive** — works well on mobile phones (students primarily use phones)
- **Bilingual**: UI labels and placeholders in both French and English where possible (French-first since Maths and Physics are in French, English-first for the English subject)
- **LaTeX rendering**: All math formulas in AI responses must render as proper mathematical notation, not raw strings
- **Loading states**: Every AI call must have a clear loading indicator and a timeout/error fallback
- **Fast initial load**: The landing page must load instantly; the AI cold start delay (up to 20 seconds) is expected only after the student submits their first request