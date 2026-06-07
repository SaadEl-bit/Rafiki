# Phase 3 Fine-Tuning — Recovery & Improvement Plan

> **Status:** Initial training run completed (loss 1.25 -> 0.44 in 3 epochs / 105 steps on 277 examples), but inference outputs show **memorization artifacts** (regurgitated `[Diagram: ...]` blocks, unrelated training chunks, broken LaTeX tables) on out-of-distribution queries. Cleanup + retraining required before pushing to HuggingFace.

---

## What Went Wrong

After the first fine-tuning run on Kaggle, the model produces clean answers for **seen patterns** (e.g. `f(x) = x^2 + 3x` derivative) but **hallucinated/regurgitated** chunks on **unseen queries** (e.g. "Donner la definition d'une fonction derivable").

### Root causes (in order of impact)

1. **Phase 1 VLM extraction artifacts leaked into training data.** The VLM (`Qwen2.5-VL-2B-Instruct`) used in Phase 1 to extract PDFs could not OCR diagrams cleanly, so it inserted text descriptions in brackets like `[Diagram: A graph showing ...]`. These descriptions were saved verbatim into `chunks.json` files, then into our Q&A triplets, and now the model **memorizes and regurgitates** them when it cannot find a clean training pattern.
2. **3 epochs on 277 examples is borderline memorization territory.** Loss went down smoothly (1.25 -> 0.44), which is the *right direction*, but the model with 1.18% trainable parameters (18.5M LoRA params) had enough exposure to memorize individual chunks.
3. **Learning rate 2e-4 is high** for style transfer on small data. Encourages the model to lock onto specific examples rather than learn the general pattern.
4. **No quality filter on the dataset.** Some triplets contain raw LaTeX tables, broken LaTeX, or "Sommaire" / table-of-contents content with no real prose.
5. **Inference temperature 0.7 is too "creative"** for a memorization-prone model on a small dataset.
6. **The test queries are out-of-distribution.** "Definition d'une fonction derivable" does not match any verbatim training pattern, so the model falls back to nearest memorized chunks.

---

## The Vision

A fine-tuned `rafiki-qwen-finetune` model that:
- Answers **cleanly** (no bracket-text, no random LaTeX tables, no regurgitated chunks)
- Uses the `<think>` block for **genuine step-by-step reasoning** before the final answer
- Speaks proper **French for Maths/Physics** and proper **English for the English subject**
- Handles **slight variations** of questions, not just verbatim matches
- Falls back to a clean `Je ne suis pas sur.` rather than regurgitating random training chunks when uncertain

---

## 3-Phase Plan

### Phase 1 — Clean the Dataset (Local, ~10 min)

Apply quality filters to the triplet builder **before** pushing to HuggingFace. Add a `validate_and_prepare()` step in `src/phase3/dataset/build_dataset.py` that drops:

| Filter | Reason |
|---|---|
| Rows containing `[Diagram:`, `[Graph:`, `[Figure:`, `[Image:`, `[Schema:` (case-insensitive) | Phase 1 VLM artifacts the model memorizes |
| Rows where the content is mostly a LaTeX table with no real prose | The model regurgitates the raw LaTeX table |
| Rows with broken LaTeX (unmatched `$` signs, malformed `\begin{}` blocks) | The model copies the broken LaTeX verbatim |
| "Sommaire" / table-of-contents / purely-heading rows | Not real Q&A content |
| Outputs longer than 4000 chars (down from 7000) | Some triplets span multiple unrelated sections |
| Already-existing filters: invalid subject/language, missing input/output, dupes, input==output, known-bad chunk_ids | (Already in code) |

**Expected result:** 277 raw -> ~180-220 cleaner training-ready triplets.

**Validation step after filtering:**
- Sample 10 random triplets and visually confirm they look like real Q&A
- If < 150 remain, lower the output-length cap to 3000 chars
- Re-run `python -m src.phase3.dataset.build_dataset` to regenerate `output/phase3/triplets.{json,jsonl}`
- Re-push with the `push_data.py` script (or `--push-to-hub` flag)

---

### Phase 2 — Retrain with Conservative Hyperparameters (Kaggle, ~10 min)

Replace the current Cell 4 in the Kaggle notebook with:

| Setting | Old | New | Why |
|---|---|---|---|
| `num_train_epochs` | 3 | **1** | 277 clean examples only need 1 pass for style transfer |
| `learning_rate` | 2e-4 | **5e-5** | 4x lower = smaller per-step changes = less overfitting |
| `warmup_steps` | 5 | **10** | Smoother LR ramp-up at lower LR |
| Everything else | unchanged | unchanged | LoRA rank 16, batch 2x4, cosine scheduler, packing=False |

Cell 4 replacement code (matches what the user already validated works):

```python
from trl import SFTTrainer
from trl import SFTConfig
from unsloth import is_bfloat16_supported

trainer = SFTTrainer(
    model = model,
    processing_class = tokenizer,
    train_dataset = dataset,
    args = SFTConfig(
        dataset_text_field = "text",
        max_seq_length = 2048,
        dataset_num_proc = 2,
        packing = False,
        per_device_train_batch_size = 2,
        gradient_accumulation_steps = 4,
        warmup_steps = 10,
        num_train_epochs = 1,
        learning_rate = 5e-5,
        fp16 = not is_bfloat16_supported(),
        bf16 = is_bfloat16_supported(),
        logging_steps = 10,
        optim = "adamw_8bit",
        weight_decay = 0.01,
        lr_scheduler_type = "linear",
        seed = 3407,
        output_dir = "outputs",
        report_to = "none",
    ),
)

trainer_stats = trainer.train()
```

**Expected training time:** ~2 minutes (1 epoch = 35 steps instead of 105).

**Expected loss curve:** should land around 0.5-0.7 (slightly higher than the 0.44 we got from 3 epochs, but that 0.44 was *memorization*; the new 0.5-0.7 represents actual *style learning*).

---

### Phase 3 — Better Inference Settings (Kaggle, ~1 min)

Replace the `model.generate(...)` call in Cell 5 with:

```python
outputs = model.generate(
    **inputs,
    max_new_tokens = 600,         # hard cap (was 512)
    use_cache = True,
    temperature = 0.3,            # was 0.7 - less randomness
    top_p = 0.9,                  # tighter nucleus sampling
    repetition_penalty = 1.1,     # prevents loops / memorization spirals
    do_sample = True,
)
```

**Why these settings:**
- `temperature=0.3`: keeps the model close to the high-probability path it learned during training, instead of wandering into memorized chunks
- `repetition_penalty=1.1`: penalizes token-level repetition, which is what happens when the model starts regurgitating
- `max_new_tokens=600`: prevents runaway generation if the model gets stuck

---

### Phase 4 — Validation Before Push (Kaggle, ~5 min)

Before running Cell 6 (push to `rafiki-qwen-finetune`), test the model on a held-out set. Add a new cell:

```python
FastLanguageModel.for_inference(model)

test_questions = [
    # Maths
    "Donner la definition d'une fonction derivable en un point.",
    "Calculer la derivee de f(x) = x^3 - 2x + 1.",
    "Explique le theoreme des accroissements finis.",
    # Physics
    "Enonce la deuxieme loi de Newton.",
    # English
    "What is the difference between present perfect and past simple?",
]

SYSTEM = "You are Rafiki, a Moroccan 2Bac professor. Explain concepts clearly and step by step, using appropriate terminology for the Moroccan baccalaureate curriculum."

for q in test_questions:
    prompt = f"<|im_start|>system\n{SYSTEM}<|im_end|>\n<|im_start|>user\n{q}<|im_end|>\n<|im_start|>assistant\n"
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    outputs = model.generate(
        **inputs, max_new_tokens=600, use_cache=True,
        temperature=0.3, top_p=0.9, repetition_penalty=1.1, do_sample=True,
    )
    response = tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True)
    print(f"Q: {q}\nA: {response}\n{'-'*60}")

    # Quality gate
    flags = []
    if "[diagram:" in response.lower(): flags.append("ARTIFACT")
    if "the graph" in response.lower() or "as shown" in response.lower(): flags.append("MEMORIZATION")
    if "$$" in response and "\\\\" in response: flags.append("BROKEN_LATEX")
    if not flags:
        flags = ["OK"]
    print(f"FLAGS: {flags}\n")
```

**Push only if all 5 outputs have `OK` flag.** If any show `ARTIFACT` or `MEMORIZATION`, do not push - iterate on Phase 1 (cleaner data) and Phase 2 (lower LR, fewer epochs).

---

### Phase 5 — Push to HuggingFace (Kaggle, ~3 min)

Once the quality gate passes, run Cell 6 as in the guide. Replace `"YOUR_HF_TOKEN"` with the actual token (or use Kaggle Secrets):

```python
import os
from huggingface_hub import login

# Option A: hardcode
login("hf_your_token_here")

# Option B: Kaggle Secrets (recommended)
# from kaggle_secrets import UserSecretsClient
# login(UserSecretsClient().get_secret("HF_TOKEN"))

print("Merging and pushing to HuggingFace...")
model.push_to_hub_merged(
    "Saad-Elouakate/rafiki-qwen-finetune",
    tokenizer,
    save_method = "merged_16bit",
    token = os.environ.get("HF_TOKEN", "hf_your_token_here"),
)
print("Done: https://huggingface.co/Saad-Elouakate/rafiki-qwen-finetune")
```

---

## Optional — Phase 6: Add a "Golden Set" Anchor (only if Phases 1-5 still fail)

If after cleaning and retraining, the model still produces poor outputs on common queries (definitions, simple explanations):

1. Hand-write 30-50 high-quality Q&A examples for common 2Bac patterns:
   - "Donner la definition d'une fonction derivable en un point" (3-5 ways to phrase it)
   - "Donner la definition d'une fonction continue" (3-5 ways)
   - "Quelle est la difference entre X et Y" (various)
   - "Enonce la loi/le theoreme/le principe" (common ones)
2. Append to the training set (bringing it from ~200 to ~250)
3. Retrain with same conservative hyperparams (1 epoch, LR 5e-5)

This acts as **anchors** that teach the model "for vague definitions, give a clean structured answer, not a regurgitated chunk."

---

## Connection Back to Phase 1

This recovery plan **originates from Phase 1 extraction artifacts.** The VLM in Phase 1 produced:
- Bracket-text diagram descriptions (`[Diagram: ...]`)
- Broken LaTeX tables
- "Sommaire" / heading-only chunks

These were **invisible** in Phase 1's success criteria (it correctly extracted *most* content as Markdown) but became visible during Phase 3 fine-tuning when the model memorized them.

**Recommendation for future Phase 1 work:** add a post-extraction filter in `src/phase1_extraction/pipeline.py` that strips:
- Lines containing `[Diagram:`, `[Figure:`, `[Image:`
- Lines that are pure LaTeX tables with no prose
- "Sommaire" / TOC chunks

This would prevent the same issue from happening when we scale to more subjects post-MVP (SVT, Arabic, Tronc Commun, etc.).

---

## Quick Reference — Total Time & Cost

| Phase | Where | Time | GPU |
|---|---|---|---|
| 1. Clean dataset | Local | ~10 min | None |
| 2. Retrain (1 epoch) | Kaggle | ~2 min | T4 |
| 3. Better inference | Kaggle | ~1 min | T4 |
| 4. Validation | Kaggle | ~5 min | T4 |
| 5. Push | Kaggle | ~3 min | T4 (CPU mostly) |
| **Total** | | **~20 min** | **1 T4 session** |

---

## Decision Log

| Date | Decision | Rationale |
|---|---|---|
| First run | 3 epochs, LR 2e-4 | Default Unsloth settings, worked for similar Q&A tasks |
| After first run | 1 epoch, LR 5e-5, temp 0.3 | Memorization observed; need to reduce training intensity and inference creativity |
| TBD | Add golden set of 30-50 examples | Only if Phases 1-5 still produce artifacts |
