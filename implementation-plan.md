# Rafiki — Phase 3: Fine-Tuning Implementation Plan

> **Project name:** Rafiki (Arabic: رفيقي — "my companion")
> **Architecture:** Vercel (Next.js) → Railway (FastAPI) → HuggingFace (model + data)

---

## Goal

Fine-tune `Qwen/Qwen2.5-1.5B-Instruct` via LoRA on ~150–400 Q-A-Reasoning triplets extracted from all 8 processed 2Bac documents (cours, exercices corrigés, cadre référenciel) for Maths, Physics, and English. The model learns *how* to answer in Moroccan 2Bac professor style (step-by-step, formal, LaTeX math, French/English), not *what* to answer (that's RAG's job).

### Constraints
- **HF Serverless Inference** with LoRA adapter only (base model + LoRA loaded together as a merged model)
- **Selected model:** `Qwen/Qwen2.5-1.5B-Instruct` for text generation; PDF/photo exercise uploads are extracted first by the VLM/OCR layer, then passed as text to this model.
- **Rank=16 LoRA**, thinking phase included via `<think>` tags
- **All 8 document sources** used for triplet generation
- **Dataset creation runs locally** (CPU), fine-tuning runs on **Kaggle** (T4 GPU, 16 GB VRAM)

---

## Two-Step Process

### Step A — Build the Q&A Dataset (Local, CPU)

**Script:** `src/phase3/dataset/build_dataset.py`

Reads all 8 `chunks.json` files from `output/phase1-extracted/` and generates `{input, thinking, output}` triplets using per-folder strategies:

| Document Type | Source Folder | Strategy | Actual Triplets |
|---|---|---|---|
| **Cours (Maths)** | `Maths-fonctions-cours` | Convert definitions, theorems, properties, examples → "Explique..." / "Définis..." questions; skip unsolved exercise-only chunks | 40 |
| **Cours (Physics)** | `Physique-lois-de-newton-cours-Exercices` | Concept Q&A; skip unsolved exercise-only chunks | 12 |
| **Cours (English)** | `English-cours` | English-learning Q&A: "Explain: ...", "Give an example: ..." | 70 |
| **Exercices corrigés (Maths)** | `Maths-fonctions-corrige-serie-d-exercices` | Conservative exercise↔solution pairing + concept Q&A for theorems/properties; known noisy source pairs filtered | 17 raw / 15 kept |
| **Cadre référenciel (English)** | `cadre-de-reference-english` | Competency-style: "Quels sont les objectifs d'apprentissage pour ...?" | 36 |
| **Cadre référenciel (Maths)** | `cadre-de-reference-maths` | Same competency style + definitions/examples | 38 |
| **Cadre référenciel (Physics)** | `cadre-de-reference-physique` | Same competency style + definitions/proofs | 55 |
| **Exam (English)** | `English-examen` | Exam-style Q&A: "Exam question: ..." | 11 |
| **Total** | | | **277 training-ready** |

#### Triplet format (raw stored locally)
```json
{
  "input": "Étudier la dérivabilité de f(x) = x² + 3x - 1",
  "thinking": "On utilise la définition du nombre dérivé. La fonction f est polynomiale donc dérivable sur ℝ...",
  "output": "f'(x) = 2x + 3\nD_f = ℝ",
  "subject": "mathematics",
  "language": "fr",
  "document_type": "course",
  "source": "Maths-fonctions-cours",
  "chunk_id": "maths_fonctions_cours_p04_c02",
  "content_type": "definition",
  "messages": [{"role": "system", "content": "..."}],
  "text": "<|im_start|>system\n..."
}
```

#### Key implementation details
- **Exercise–solution pairing (corrigés):** Walk chunks in order, ignore heading-only chunks, reset on new exercise headings, merge consecutive solution chunks, and reject oversized, multi-exercise, duplicate, or known noisy pairs.
- **Deduplication:** 100-char prefix dedup across chunks within each folder.
- **Training columns:** Local output includes raw fields plus `messages` and pre-formatted ChatML `text`, so Kaggle can train from either local JSON/JSONL or the pushed HF dataset.
- **Validation:** Rows with invalid subjects/languages, missing input/output, overlong outputs, bad exercise pairs, or duplicates are filtered before saving.
- **8 processed folders** in `output/phase1-extracted/`:
  - `cadre-de-reference-english/`, `cadre-de-reference-maths/`, `cadre-de-reference-physique/`
  - `English-cours/`, `English-examen/`
  - `Maths-fonctions-corrige-serie-d-exercices/`, `Maths-fonctions-cours/`
  - `Physique-lois-de-newton-cours-Exercices/`
- **Known artifact:** `cadre-de-reference-english` has 13 duplicate "example" chunks (over-splitting in Phase 1), filtered by dedup.

#### ChatML format
```text
<|im_start|>system
You are Rafiki, a Moroccan 2Bac professor. Explain concepts clearly and step by step, using appropriate terminology for the Moroccan baccalaureate curriculum.<|im_end|>
<|im_start|>user
{input}<|im_end|>
<|im_start|>assistant
<think>
{thinking}
</think>
{output}<|im_end|>
```

- The `messages` column (OpenAI format, for HF trainers) and `text` column (pre-formatted ChatML string) are generated locally before saving and are also pushed to HuggingFace.
- If `thinking` is empty, the `<think>` block is omitted entirely.

#### Pushing to HuggingFace
```bash
set HF_TOKEN=hf_your_token_here    # Windows CMD
# or: $env:HF_TOKEN="..."          # PowerShell
# or: export HF_TOKEN="..."        # Git Bash / WSL
python -m src.phase3.dataset.build_dataset --push-to-hub
```

**Dataset repo:** `Saad-Elouakate/rafiki-qna-triplets` (private)

---

### Step B — Fine-Tune on Kaggle (T4 GPU)

**Selected model:** `Qwen/Qwen2.5-1.5B-Instruct`

| Model | Params | Type | T4 VRAM | Notes |
|---|---|---|---|---|
| `Qwen/Qwen2.5-1.5B-Instruct` | 1.5B | Text-only LLM | ~3 GB in 4-bit | Final MVP choice: simple Kaggle T4 LoRA path, multilingual, good math/instruction behavior |
| `Qwen/Qwen3-VL-2B-Instruct` | 2B | Vision-Language | Higher memory/complexity | Not selected for fine-tuning; use a VLM/OCR stage separately for PDF/photo extraction |

**Training pipeline:**
1. **Load model** in 4-bit (NF4) via Unsloth or bitsandbytes
2. **Attach LoRA:** rank=16, target Q/K/V/O projections (~12 MB adapter size)
3. **Load dataset:** `Saad-Elouakate/rafiki-qna-triplets` from HuggingFace
4. **Tokenize** using `text` column (pre-formatted ChatML) — the tokenizer's `apply_chat_template` or direct tokenization
5. **Train:** 1-3 epochs (~10-30 min on T4)
6. **Merge & Push:** Merge LoRA weights into the base model and push the **full merged model** (~3 GB) → private HF repo. Required because HF Serverless Inference API cannot load adapters dynamically.

#### Known blocker
`DatasetDict.push_to_hub()` triggers `UnboundLocalError` on Kaggle's `datasets` library (v2.19–2.20).
**Workaround:** `!pip install -U datasets` at the top of the Kaggle notebook, or push individual splits with `Dataset.push_to_hub(split=...)`.

---

## File Structure

```
src/
├── phase1_extraction/
│   ├── pipeline.py          # Phase 1: PDF → Markdown → chunks (DONE)
│   └── pdf_extractor.py     # Core extraction logic (DONE)
├── phase2_rag/
│   ├── embedder.py          # Embedding generation (DONE)
│   ├── retriever.py         # ChromaDB retrieval (DONE)
│   └── config.py            # Phase 2 config (DONE)
├── phase3/
│   └── dataset/
│       ├── build_dataset.py # Step A: scans chunks.json, builds 277 training-ready triplets, pushes to HF
│       └── __init__.py
└── phase3_finetune/         # Step B: Kaggle notebook (TO BUILD)
    ├── config.py            # Model name, LoRA params, training hyperparams, HF repos
    ├── dataset.py           # Load HF/local dataset using preformatted ChatML text
    ├── train.py             # Training loop (Unsloth / bitsandbytes + PEFT)
    ├── inference_test.py    # Compare pre/post outputs on held-out questions
    ├── main.py              # Kaggle entry point
    └── requirements.txt     # Dependencies

output/
└── phase3/
    ├── triplets.json        # Training-ready triplets with messages + ChatML text
    └── triplets.jsonl       # Same data as JSONL (one JSON object per line)
```

---

## Key Decisions

| Decision | Choice | Why |
|---|---|---|
| Base model | `Qwen/Qwen2.5-1.5B-Instruct` | Best fit for text-only LoRA on Kaggle T4; PDF/photo input is handled before generation by extraction/OCR |
| LoRA rank | 16 | Balanced capacity for ~200 examples, ~12 MB adapter, fits T4 16 GB VRAM |
| Thinking field | Included as `<think>` tags | Exercise corrections already have step-by-step reasoning; teaches the model to reason before answering |
| Output format | Direct answer only (no separate CoT visible to student) | Thinking is internal reasoning; student sees only the final answer |
| Data sources | ALL 8 documents | Diversity prevents overfitting to one style/subject |
| Dataset repo | `Saad-Elouakate/rafiki-qna-triplets` | Private HF dataset |
| Model repo | `Saad-Elouakate/rafiki-qwen-finetune` | Private HF model — **full merged model** for Serverless API compatibility |
| Training epochs | 1-3 | Small dataset; more epochs risk overfitting |
| Chat template | ChatML (`<|im_start|>` / `<|im_end|>`) with system prompt naming "Rafiki" | Required for Qwen instruction-tuned models; project name embedded in system prompt |
| HF Token | `HF_TOKEN` environment variable | Avoids hardcoded secrets in notebooks/scripts |

---

## Success Check

After fine-tuning, the model should:
- Answer in **step-by-step** format (not one-line)
- Use proper **French/English** for the right subject
- Include **LaTeX math** for formulas
- Sound like a **Moroccan 2Bac professor** (not generic ChatGPT)
- Begin responses with `<think>` reasoning when appropriate

---

## Remaining Questions

1. **Fine-tuning framework:** Unsloth vs bitsandbytes + PEFT (Unsloth is faster on T4)
2. **Push flow:** Should we merge LoRA → full model on Kaggle T4 (3 GB, feasible) or separately?
3. **Inference deployment:** After push to private HF, test via Serverless Inference API before wiring to Railway
