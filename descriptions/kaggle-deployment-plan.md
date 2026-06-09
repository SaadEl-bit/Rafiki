# Kaggle Deployment — Rafiki Backend

> **Steps to run the backend on Kaggle with Dual T4 GPU. All latest code is on GitHub — just clone and override 2 files.**

> **⚠️ BEFORE YOU START — verify these values against YOUR accounts:**
> | Check | Your Value | Where to find it |
> |-------|-----------|-----------------|
> | **GitHub username** | `SaadEl-bit` | Your GitHub profile URL: `github.com/…` |
> | **GitHub repo** | `M3allem` | The remote in `git remote -v` |
> | **GitHub email** | `saadelouakate7@gmail.com` | `git config user.email` |
> | **Kaggle dataset slug** | `rafiki-models` | The dataset you created in Kaggle |
> | **Kaggle dataset owner** | `saadelouakate` | Your Kaggle username |
> | **HuggingFace username** | `Saad-Elouakate` (for HF model refs) | Your HF profile |
> | **Localtunnel password** | Your Kaggle notebook's public IP | Generated automatically in Cell 3 |

---

## 1. Prerequisites (ONE TIME)

### Kaggle Dataset
Upload `rafiki_models_for_kaggle.zip` as a Kaggle Dataset named `rafiki-models`:
```
/kaggle/input/rafiki-models/
├── text-model/     (fine-tuned Qwen2.5-1.5B)
└── vision-model/   (Qwen2.5-VL-3B-Instruct)
```

### Kaggle Secrets
Set these in Kaggle Notebook → **Add-ons → Secrets**:
| Secret | Your Value | How to get it |
|--------|-----------|---------------|
| `GITHUB_EMAIL` | `saadelouakate7@gmail.com` | `git config user.email` |
| `GITHUB_TOKEN` | `ghp_xxxx...` | GitHub → Settings → Developer settings → Personal access tokens (classic, `repo` scope) |
| `GITHUB_USER` | `SaadEl-bit` | Your GitHub username |
| `HF_TOKEN` | `hf_xxxx...` | HuggingFace → Settings → Access Tokens |

---

## 2. Notebook Cells

### CELL 0 — Config
```python
# ── 🔍 VERIFY these values match YOUR accounts ──────────────────────
GITHUB_USER = "SaadEl-bit"       # Your GitHub username
REPO_NAME   = "M3allem"          # Your GitHub repository name
REPO_URL    = f"https://github.com/{GITHUB_USER}/{REPO_NAME}.git"
KAGGLE_DATASET = "rafiki-models"  # Your Kaggle dataset slug
API_PORT    = 8000
# ─────────────────────────────────────────────────────────────────────
```

### CELL 1 — Setup & Clone
```python
import os
from kaggle_secrets import UserSecretsClient

user_secrets = UserSecretsClient()
github_email = user_secrets.get_secret("GITHUB_EMAIL")
github_token = user_secrets.get_secret("GITHUB_TOKEN")
github_user  = user_secrets.get_secret("GITHUB_USER")
hf_token     = user_secrets.get_secret("HF_TOKEN")

repo_url = f"https://{github_token}@github.com/{github_user}/M3allem.git"
os.system(f"git clone {repo_url} /kaggle/working/app")
os.chdir("/kaggle/working/app")

# Set git identity (useful if you ever commit from Kaggle)
os.system(f'git config user.email "{github_email}"')
os.system(f'git config user.name "{github_user}"')

with open(".env", "w") as f:
    f.write(f"HF_TOKEN={hf_token}\nCHROMA_DB_DIR=./chroma_db_cache\nVL_MODEL_ID=Qwen/Qwen2.5-VL-3B-Instruct\n")

!pip install -q -r requirements_all.txt
!pip install -q transformers accelerate bitsandbytes qwen-vl-utils torchvision
!npm install -g localtunnel
print("✅ Done")
```

### CELL 2 — Override for Local Dual-GPU (NECESSARY)
> Replaces HF Inference API calls with direct model loading from Kaggle dataset.

> **⚠️ First run discovers the actual dataset path & handles nested model directories.**

```python
import os, glob

# ── Discover dataset paths ──────────────────────────────────────────
# Try common Kaggle mount points
CANDIDATES = [
    "/kaggle/input/rafiki-models",
    "/kaggle/input/datasets/saadelouakate/rafiki-models",
]
DATASET_ROOT = None
for p in CANDIDATES:
    if os.path.isdir(p):
        DATASET_ROOT = p
        break

if DATASET_ROOT is None:
    raise FileNotFoundError(
        "❌ Dataset not found at any expected path. "
        "Make sure 'rafiki-models' is added in the Data panel."
    )

print(f"📂 Dataset root: {DATASET_ROOT}")

# Find actual model dirs (handles nested subdirectory)
def find_model_dir(base_dir: str, name: str) -> str:
    """Find the actual model directory that contains config.json."""
    candidate = os.path.join(base_dir, name)
    if os.path.isfile(os.path.join(candidate, "config.json")):
        return candidate
    # Look one level deeper (Kaggle zip nesting)
    subs = sorted(os.listdir(candidate))
    for sub in subs:
        subpath = os.path.join(candidate, sub)
        if os.path.isdir(subpath) and os.path.isfile(os.path.join(subpath, "config.json")):
            print(f"  ↳ Found {name} nested at: {subpath}")
            return subpath
    return candidate  # fallback

TEXT_MODEL_PATH = find_model_dir(DATASET_ROOT, "text-model")
VISION_MODEL_PATH = find_model_dir(DATASET_ROOT, "vision-model")
print(f"📝 TEXT_MODEL_PATH  = {TEXT_MODEL_PATH}")
print(f"📝 VISION_MODEL_PATH = {VISION_MODEL_PATH}")

# ── Write override files ────────────────────────────────────────────

# Build the code strings with correct escaping using .replace()
_LLM_TEMPLATE = r'''
import logging, torch
from transformers import pipeline, BitsAndBytesConfig

logger = logging.getLogger(__name__)
TEXT_MODEL_PATH = "__TEXT_MODEL_PATH__"
logger.info("Loading text model from %s on GPU 0 (4-bit)", TEXT_MODEL_PATH)

quant_config = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_compute_dtype=torch.float16)
generator = pipeline("text-generation", model=TEXT_MODEL_PATH, device_map="cuda:0", model_kwargs={"quantization_config": quant_config})
logger.info("Text model loaded on GPU 0")

def generate_answer(context: str, question: str, history: list = None) -> str:
    system = "Vous etes Rafiki, un tuteur IA pour les etudiants marocains (2eme Bac). Utilisez le contexte fourni. Vous avez une conversation avec l'etudiant."
    prompt = f"<|im_start|>system\n{system}\nContexte du cours:\n{context}<|im_end|>\n"
    if history:
        for msg in history:
            role = "user" if msg["role"] == "user" else "assistant"
            prompt += f"<|im_start|>{role}\n{msg['content']}<|im_end|>\n"
    prompt += f"<|im_start|>user\n{question}<|im_end|>\n<|im_start|>assistant\n"
    res = generator(prompt, max_new_tokens=1500, temperature=0.3)
    return res[0]["generated_text"].split("<|im_start|>assistant\n")[-1]

def correct_exercise(context: str, exercise_text: str) -> str:
    system = "Vous etes Rafiki. Corrigez cet exercice etape par etape."
    prompt = f"<|im_start|>system\n{system}\nContexte:\n{context}<|im_end|>\n<|im_start|>user\n{exercise_text}<|im_end|>\n<|im_start|>assistant\n"
    res = generator(prompt, max_new_tokens=2000, temperature=0.3)
    return res[0]["generated_text"].split("<|im_start|>assistant\n")[-1]

def generate_content(context: str, instruction: str, system_prompt: str, max_tokens: int = 2000, temperature: float = 0.3) -> str:
    prompt = f"<|im_start|>system\n{system_prompt}<|im_end|>\n<|im_start|>user\nContexte du cours:\n{context}\n\n{instruction}<|im_end|>\n<|im_start|>assistant\n"
    res = generator(prompt, max_new_tokens=max_tokens, temperature=temperature)
    return res[0]["generated_text"].split("<|im_start|>assistant\n")[-1]
'''
llm_code = _LLM_TEMPLATE.replace("__TEXT_MODEL_PATH__", TEXT_MODEL_PATH)

_VISION_TEMPLATE = r'''
import logging
from typing import List
import torch
from transformers import Qwen2_5_VLForConditionalGeneration, AutoProcessor, BitsAndBytesConfig
from qwen_vl_utils import process_vision_info

logger = logging.getLogger(__name__)
VISION_MODEL_PATH = "__VISION_MODEL_PATH__"
logger.info("Loading vision model from %s on GPU 1 (4-bit)", VISION_MODEL_PATH)

quant_config = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_compute_dtype=torch.float16)
model = Qwen2_5_VLForConditionalGeneration.from_pretrained(VISION_MODEL_PATH, quantization_config=quant_config, device_map="cuda:1")
processor = AutoProcessor.from_pretrained(VISION_MODEL_PATH)
logger.info("Vision model loaded on GPU 1")

def file_to_base64_images(file_bytes: bytes, filename: str) -> List[str]:
    import fitz, base64
    images = []
    if filename.lower().endswith(".pdf"):
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        for p in range(len(doc)):
            page = doc.load_page(p)
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
            images.append(base64.b64encode(pix.tobytes("png")).decode("utf-8"))
    return images

def extract_text_via_vl(base64_images: List[str]) -> str:
    extracted = ""
    for idx, b64 in enumerate(base64_images):
        messages = [{"role": "user", "content": [{"type": "image", "image": f"data:image/png;base64,{b64}"}, {"type": "text", "text": "Extract all text and math. Use LaTeX for math."}]}]
        text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        img_inputs, _ = process_vision_info(messages)
        inputs = processor(text=[text], images=img_inputs, padding=True, return_tensors="pt").to("cuda:1")
        out = model.generate(**inputs, max_new_tokens=2000)
        out = out[:, inputs.input_ids.shape[1]:]
        extracted += f"\n\n--- Page {idx+1} ---\n\n" + processor.decode(out[0], skip_special_tokens=True)
    return extracted.strip()
'''
vision_code = _VISION_TEMPLATE.replace("__VISION_MODEL_PATH__", VISION_MODEL_PATH)

with open("src/phase4_backend/services/llm_service.py", "w", encoding="utf-8") as f:
    f.write(llm_code)
with open("src/phase4_backend/services/extraction_service.py", "w", encoding="utf-8") as f:
    f.write(vision_code)

print("✅ Override: llm_service.py → GPU 0 | extraction_service.py → GPU 1")
```

### CELL 3 — Start Server + Localtunnel
```python
import os, subprocess, time, urllib.request

# ── Verify model paths in override files ────────────────────────────
for fname, label in [("llm_service.py", "Text"), ("extraction_service.py", "Vision")]:
    fpath = f"src/phase4_backend/services/{fname}"
    if not os.path.isfile(fpath):
        print(f"❌ Override file missing: {fpath} — run Cell 2 first!")
        raise SystemExit(1)
    with open(fpath) as f:
        content = f.read()
    # Quick sanity: model path should be an absolute existing directory
    import re
    for line in content.splitlines():
        m = re.match(r'^\s*(\w*MODEL_PATH\w*)\s*=\s*["\']([^"\']+)["\']', line)
        if m:
            val = m.group(2)
            if os.path.isdir(val):
                print(f"  ✅ {label} model path OK: {val}")
            else:
                # Maybe nested — look for config.json
                if os.path.isfile(os.path.join(val, "config.json")):
                    print(f"  ✅ {label} model path OK: {val}")
                else:
                    print(f"  ⚠️ {label} model path may be invalid: {val}")

# ── Start uvicorn ───────────────────────────────────────────────────
proc = subprocess.Popen(
    ["python", "-m", "uvicorn", "src.phase4_backend.main:app",
     "--host", "0.0.0.0", "--port", "8000", "--log-level", "info"]
)
print("⏳ Loading models into VRAM (~40s)...")
time.sleep(40)

try:
    import requests
    r = requests.get("http://localhost:8000/health", timeout=5)
    print(f"✅ Server OK: {r.status_code}")
except:
    print("⚠️ Still starting...")
    time.sleep(20)

ip = urllib.request.urlopen("https://ipv4.icanhazip.com").read().decode("utf8").strip()
print(f"\n{'='*50}")
print(f"🔑 LOCALTUNNEL PASSWORD: {ip}")
print(f"{'='*50}")
!npx localtunnel --port 8000
```

---

## 3. Quick Reference

| Step | What happens | Time |
|------|-------------|------|
| Cell 1 | Clone repo + install deps | ~3 min |
| Cell 2 | Override 2 files for local GPU | ~1 sec |
| Cell 3 | Load models from dataset + expose API | ~2 min |

**On each session:** Same steps. Pip packages are cached → faster.

**Notes:**
- Localtunnel URL changes on every restart → update `NEXT_PUBLIC_API_URL` in frontend
- ChromaDB RAG index downloads from HuggingFace on first `/ask` call (one-time, needs Internet ON)
- Kaggle disconnects after ~9h inactivity

### Troubleshooting

| Problem | Fix |
|---------|------|
| CUDA OOM | Use GPU T4 x2 (not x1) |
| Dataset not found | Add `rafiki-models` in notebook Data panel |
| Localtunnel dead | Re-run Cell 3 |
| Model not loading / `HFValidationError` | Run **Cell 2** first — it discovers the correct path & handles nested subdirs |
| `Repo id must be in the form...` | Same fix — the model dir has an extra nesting level; Cell 2 now finds it automatically |

---

## 4. Adding the RAG Index as a Kaggle Dataset

The ChromaDB index (`maths_2bac`, `physics_2bac`, `english_2bac`) normally downloads from HuggingFace on first `/ask` call (~500MB, needs Internet ON).  
To avoid download failures and speed up startup, upload it as a **second Kaggle dataset**.

### Step 4.1 — Prepare the index locally

From your **local machine** where you built the index (Phase 2), locate the ChromaDB folder:

```bash
# Default location from Phase 2 (adjust if you used a different path)
ls /kaggle/working/chromadb/
# Should contain: chroma.sqlite3 + subdirs
```

Zip it:

```bash
# On your local machine (Windows PowerShell or CMD):
# Navigate to the folder CONTAINING the chromadb directory
# e.g. if chromadb is at C:\Users\you\M3allem\chromadb
cd C:\Users\you\M3allem
Compress-Archive -Path chromadb -DestinationPath rag_index.zip

# Or on macOS / Linux:
# zip -r rag_index.zip chromadb/
```

### Step 4.2 — Upload to Kaggle

1. Go to [kaggle.com/datasets](https://www.kaggle.com/datasets) → **New Dataset**
2. Upload `rag_index.zip`
3. Set:
   - **Title:** `rag-index`
   - **Visibility:** Private
4. Click **Create**
5. Note the slug: `saadelouakate/rag-index` (your-username/rag-index)

### Step 4.3 — Add dataset to the notebook

Before running any cells:
1. In your Kaggle notebook, click **Add Data** (right panel)
2. Search for `rag-index`
3. Add it

The index will be mounted at:
```
/kaggle/input/rag-index/
└── chromadb/
    ├── chroma.sqlite3
    └── ... (subdirs)
```

### Step 4.4 — Auto-detect in Cell 1

Update **CELL 1** so it detects the local RAG index and points to it instead of downloading:

```python
# ── Add this AFTER the .env file creation in CELL 1 ──────────────────

# Detect local RAG index dataset (skip HF download)
RAG_INDEX_CANDIDATES = [
    "/kaggle/input/rag-index",
    "/kaggle/input/datasets/saadelouakate/rag-index",
]
local_rag = None
for p in RAG_INDEX_CANDIDATES:
    chroma_subdir = os.path.join(p, "chromadb")
    if os.path.isdir(chroma_subdir) and os.path.isfile(os.path.join(chroma_subdir, "chroma.sqlite3")):
        local_rag = chroma_subdir
        break

if local_rag:
    print(f"📂 Found local RAG index at: {local_rag}")
    # Update .env to use the local path
    with open(".env", "a") as f:
        f.write(f"CHROMA_DB_DIR={local_rag}\n")
else:
    print("ℹ️  No local RAG index dataset found — will download from HuggingFace on first request")
```

Place this snippet right after the `.env` creation block (after line 72 in the current CELL 1).

### Step 4.5 — What changes?

| Without dataset | With dataset |
|---|---|
| Downloads ~500MB from HF on first `/ask` | Uses files directly from Kaggle disk |
| Needs Internet ON | Works even if Internet is OFF |
| ~30s download delay on first call | Instant retrieval |
| Can fail if HF repo is missing | Always works |

### Verify it works

After starting the server (Cell 3), send a test request:

```bash
# From another terminal, or use the Localtunnel URL in your browser:
curl -X POST "https://your-tunnel-url.loca.lt/api/ask" \
  -H "Content-Type: application/json" \
  -d '{"question": "Comment calculer la dérivée?", "subject": "Mathématiques"}'
```

If the RAG index is loaded, you should **not** see the error:
```
Collection 'maths_2bac' not found in ChromaDB...
```

Instead you should see in the logs:
```
INFO:src.phase2_rag.retriever:Loading retriever from: /kaggle/input/rag-index/chromadb
```
