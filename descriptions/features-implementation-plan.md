# Implementation Plan — Remaining Features

> **Plan for building: Cadre Référenciel · Course Notes Viewer · Exercise Generation · Exam Generation**
> *Exam Correction postponed for later.*

---

## 1. Cadre Référenciel (الإطار المرجعي)

### Status
Frontend placeholder exists. Data already extracted as `.md` files.

### Data source (READY ✅)
`Dataset/*-cadre-reference.md` — already structured with hierarchy:
```
# Premier domaine : Analyse          → Domain
## Premier sous-domaine : Suites     → Sub-domain
### 1.1.1. Utiliser les suites...    → Objective (with code)
```

### What to build

**Backend — New endpoint: `GET /api/cadre`**
- Parses the 3 markdown files into JSON structure
- Returns structured data:
```json
[
  {
    "subject": "Mathématiques",
    "domains": [
      {
        "name": "Premier domaine : Analyse",
        "sub_domains": [
          {
            "name": "Suites numériques",
            "objectives": [
              { "code": "1.1.1", "text": "Utiliser les suites..." }
            ]
          }
        ]
      }
    ]
  }
]
```
- Parsing logic: split by `# ` (domain), `## ` (sub-domain), `### ` (objective)
- Store as static JSON file loaded at startup (no DB needed)
- One-time parse, cache in memory

**Frontend — Page: `/cadre`**
- Expandable tree: Subject → Domain → Sub-domain → Objective
- Each objective has an "Ask AI" button
- Search bar filters objectives by keyword (live filter)
- Click "Ask AI" → navigate to `/chat?q=objectif-1.1.1`

**Frontend — Chat page modification**
- Detect `?q=objectif-X.Y.Z` URL parameter
- Auto-send question: *"Explique l'objectif 1.1.1 du programme de Mathématiques : [objective text]"*
- Show AI response in chat

### Files to create/modify
| File | Action |
|------|--------|
| `src/phase4_backend/routers/cadre.py` | **New** — `GET /api/cadre` endpoint |
| `src/phase4_backend/main.py` | Register cadre router |
| `src/phase4_backend/services/cadre_service.py` | **New** — Parse logic + cache |
| `frontend/app/(dashboard)/cadre/page.js` | **New** — Tree view page |
| `frontend/app/(dashboard)/chat/page.js` | Modify — Handle `?q=` parameter |

### Data dependencies
- `Dataset/Maths-cadre-reference.md` ✅
- `Dataset/Physics-cadre-reference.md` ✅
- `Dataset/English-cadre-reference.md` ✅

---

## 2. Course Notes Viewer (formerly Resume Generation)

### Status
UI placeholder exists for "Resume Generation." Repurposing into Course Notes Viewer.

### Data source (READY ✅)
`Dataset/*-course.md` files:
- `Dataset/Maths-course.md` (1289 lines)
- `Dataset/English-course.md`
- `Dataset/Physics-course-exercices.md`

### What to build

**Backend — New endpoint: `GET /api/course/{subject}`**
- Reads the corresponding markdown file
- Returns raw markdown content
- Subject mapping: `mathematiques → Maths-course.md`, `physique → Physics-course-exercices.md`, `anglais → English-course.md`

**Frontend — Repurpose `/generators` page (or new page: `/course`)**
- Subject selector (Maths/Physics/English)
- Markdown renderer with proper LaTeX rendering (use `react-markdown` + `remark-math` + `rehype-katex`)
- Sidebar with chapter navigation (generated from `##` headings in the markdown)
- Scrollable content area

### Files to create/modify
| File | Action |
|------|--------|
| `frontend/app/(dashboard)/course/page.js` | **New** — Course viewer page |
| `frontend/components/layout/Sidebar.jsx` | Modify — Repurpose "Resume Generation" link → "Course Notes" |
| `src/phase4_backend/routers/course.py` | **New** — `GET /api/course/{subject}` |
| `src/phase4_backend/main.py` | Register course router |
| `package.json` | Add: `react-markdown`, `remark-math`, `rehype-katex`, `katex` |

### What's needed from you
- Nothing — data already exists ✅

---

## 3. Exercise Generation

### Status
UI placeholder exists. AI generation — new backend endpoint needed.

### Data source
- Subject list from you (you said you'll provide)
- RAG ChromaDB index provides course context for the AI

### What to build

**Backend — New endpoint: `POST /api/generate/exercise`**
```json
// Request
{
  "subject": "Mathématiques",
  "topic": "Dérivation — étude des fonctions"
}

// Response
{
  "exercise": "... exercise statement with LaTeX ...",
  "solution": "... step-by-step solution ..."
}
```
- Uses fine-tuned LLM (same as chat)
- RAG retrieves relevant course chunks as context
- Prompt example:
  ```
  "Génère UN exercice de Mathématiques sur le thème 'Dérivation'
   avec sa solution détaillée étape par étape.
   Utilise le contexte du cours fourni pour t'assurer que
   l'exercice correspond au programme 2ème Bac.
   Format : d'abord l'énoncé, puis la solution complète."
  ```

**Frontend — Page: `/generate/exercise`**
- Subject dropdown (from a list you provide)
- Topic dropdown (list of topics per subject — you provide)
- "Generate Exercise" button
- Loading state
- Result display: markdown with LaTeX rendering
- "Generate Another" button

### Files to create/modify
| File | Action |
|------|--------|
| `src/phase4_backend/routers/generate.py` | **New** — `POST /api/generate/exercise` |
| `src/phase4_backend/main.py` | Register generate router |
| `frontend/app/(dashboard)/generate/exercise/page.js` | **New** |
| `frontend/components/layout/Sidebar.jsx` | Modify — Update link |

### What's needed from you
- **Subject list** + **Topic list per subject** (the courses/topics the user can choose from)
  - Example: `{ "Mathématiques": ["Dérivation", "Suites numériques", "Nombres complexes", ...], "Physique-Chimie": [...], "Anglais": [...] }`
  - Can be extracted from the `##` headings in the course `.md` files, or you can provide manually

---

## 4. Exam Generation

### Status
UI placeholder exists. Data already extracted in JSON format.

### Data source (READY ✅)
`Document-Data-Set/Fine-Tuning/**/*.json` — existing exam files with Q/Corr pairs:
- `Maths/Maths-examen-{1,2,3}.json`
- `Physics/physics-exam-{1,2}.json`
- `English/english_exam_{1,2}.json`

### How the AI generates exams
```
User: "Generate Maths exam on Analysis"
  → Backend loads 1 real Maths exam JSON as format reference
  → RAG retrieves course chunks on "Analyse" for content
  → LLM prompt:
      "Voici un exemple d'examen réel du Bac Mathématiques:
       [real exam JSON as text]
       
       Génère un NOUVEL examen sur le thème 'Analyse'
       en suivant EXACTEMENT le même format.
       Chaque question doit avoir sa correction détaillée."
  → Response: new exam in same format
```

**Backend — New endpoint: `POST /api/generate/exam`**
```json
// Request
{
  "subject": "Mathématiques",
  "topic": "Analyse"  // optional, omit for full subject review
}

// Response
{
  "exam": {
    "subject": "Examen National Mathématiques (Généré)",
    "Ex1.Q1": "...",
    "Corr Ex1.Q1": "...",
    ...
  }
}
```

**Frontend — Page: `/generate/exam`**
- Subject dropdown
- Optional topic focus dropdown
- "Generate Exam" button
- Loading state (longer — generates multiple questions)
- Result: exam displayed with all Q/Corr pairs
- Each exercise in a collapsible section (question visible, correction hidden by default — toggle to reveal)

### Files to create/modify
| File | Action |
|------|--------|
| `src/phase4_backend/routers/generate.py` | Extend — Add `POST /api/generate/exam` |
| `frontend/app/(dashboard)/generate/exam/page.js` | **New** |
| `frontend/components/layout/Sidebar.jsx` | Modify — Update links |

### What's needed from you
- Nothing — exam data already in repo ✅

---

## 5. Exam Correction

### Status
**Postponed.** Will be planned in a future round.

---

## Implementation Order (Recommended)

| Priority | Feature | Why first |
|----------|---------|-----------|
| 1 | **Cadre Référenciel** | Data ready, no AI dependency, quick win |
| 2 | **Course Notes Viewer** | Data ready, display-only, same approach |
| 3 | **Exercise Generation** | Core AI feature, single exercise = simpler to build |
| 4 | **Exam Generation** | More complex, built after exercise gen is validated |
| — | Exam Correction | Postponed |

---

## Summary: What's needed from you

| Feature | Data needed | Status |
|---------|-------------|--------|
| Cadre Référenciel | None — `.md` files exist | ✅ Ready |
| Course Notes Viewer | None — `.md` files exist | ✅ Ready |
| Exercise Generation | **Subject list + Topic list per subject** | ⏳ You provide |
| Exam Generation | None — JSON exam files exist | ✅ Ready |
| Exam Correction | Postponed | — |

---

## Appendix: Topic list for Exercise Generation

If you want me to auto-extract topics from the course `.md` files rather than you typing them manually, the `##` headings in each course file give the chapter/topic names directly. For example from `Maths-course.md`:

```
## dérivation – étude des fonctions
## Les suites numériques
## Fonctions logarithmes
## Fonctions exponentielles
## Calcul des primitives
...etc
```

**This would save you from manually writing a topic list.** I can parse the `##` headings from the course files automatically. Do you want me to do that?
