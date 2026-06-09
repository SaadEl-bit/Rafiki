# Kaggle Deployment — Rafiki Backend

> **Steps to run the backend on Kaggle with Dual T4 GPU. All latest code is on GitHub — just clone and override 2 files.**

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
| Secret | Value |
|--------|-------|
| `GITHUB_TOKEN` | `ghp_xxxx...` (classic, repo scope) |
| `HF_TOKEN` | `hf_xxxx...` |

---

## 2. Notebook Cells

### CELL 0 — Config
```python
REPO_URL = "https://github.com/Saad-Elouakate/Rafiki.git"
KAGGLE_DATASET = "rafiki-models"
TEXT_MODEL_PATH = f"/kaggle/input/{KAGGLE_DATASET}/text-model"
VISION_MODEL_PATH = f"/kaggle/input/{KAGGLE_DATASET}/vision-model"
API_PORT = 8000
```

### CELL 1 — Setup & Clone
```python
import os
from kaggle_secrets import UserSecretsClient

user_secrets = UserSecretsClient()
github_token = user_secrets.get_secret("GITHUB_TOKEN")
hf_token = user_secrets.get_secret("HF_TOKEN")

repo_url = f"https://{github_token}@github.com/Saad-Elouakate/Rafiki.git"
os.system(f"git clone {repo_url} /kaggle/working/app")
os.chdir("/kaggle/working/app")

with open(".env", "w") as f:
    f.write(f"HF_TOKEN={hf_token}\nCHROMA_DB_DIR=./chroma_db_cache\nVL_MODEL_ID=Qwen/Qwen2.5-VL-3B-Instruct\n")

!pip install -q -r requirements_all.txt
!pip install -q transformers accelerate bitsandbytes qwen-vl-utils torchvision
!npm install -g localtunnel
print("✅ Done")
```

### CELL 2 — Override for Local Dual-GPU (NECESSARY)
> Replaces HF Inference API calls with direct model loading from `/kaggle/input/rafiki-models/`.

```python
import os

llm_code = '''
import logging, torch
from transformers import pipeline, BitsAndBytesConfig

logger = logging.getLogger(__name__)
TEXT_MODEL_PATH = "/kaggle/input/rafiki-models/text-model"
logger.info("Loading text model from %s on GPU 0 (4-bit)", TEXT_MODEL_PATH)

quant_config = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_compute_dtype=torch.float16)
generator = pipeline("text-generation", model=TEXT_MODEL_PATH, device_map="cuda:0", model_kwargs={"quantization_config": quant_config})
logger.info("Text model loaded on GPU 0")

def generate_answer(context: str, question: str, history: list = None) -> str:
    system = "Vous etes Rafiki, un tuteur IA pour les etudiants marocains (2eme Bac). Utilisez le contexte fourni. Vous avez une conversation avec l'etudiant."
    prompt = f"<|im_start|>system\\n{system}\\nContexte du cours:\\n{context}<|im_end|>\\n"
    if history:
        for msg in history:
            role = "user" if msg["role"] == "user" else "assistant"
            prompt += f"<|im_start|>{role}\\n{msg['content']}<|im_end|>\\n"
    prompt += f"<|im_start|>user\\n{question}<|im_end|>\\n<|im_start|>assistant\\n"
    res = generator(prompt, max_new_tokens=1500, temperature=0.3)
    return res[0]["generated_text"].split("<|im_start|>assistant\\n")[-1]

def correct_exercise(context: str, exercise_text: str) -> str:
    system = "Vous etes Rafiki. Corrigez cet exercice etape par etape."
    prompt = f"<|im_start|>system\\n{system}\\nContexte:\\n{context}<|im_end|>\\n<|im_start|>user\\n{exercise_text}<|im_end|>\\n<|im_start|>assistant\\n"
    res = generator(prompt, max_new_tokens=2000, temperature=0.3)
    return res[0]["generated_text"].split("<|im_start|>assistant\\n")[-1]
'''

vision_code = '''
import logging
from typing import List
import torch
from transformers import Qwen2_5_VLForConditionalGeneration, AutoProcessor, BitsAndBytesConfig
from qwen_vl_utils import process_vision_info

logger = logging.getLogger(__name__)
VISION_MODEL_PATH = "/kaggle/input/rafiki-models/vision-model"
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
        extracted += f"\\n\\n--- Page {idx+1} ---\\n\\n" + processor.decode(out[0], skip_special_tokens=True)
    return extracted.strip()
'''

with open("src/phase4_backend/services/llm_service.py", "w", encoding="utf-8") as f:
    f.write(llm_code)
with open("src/phase4_backend/services/extraction_service.py", "w", encoding="utf-8") as f:
    f.write(vision_code)

print("✅ Override: llm_service.py → GPU 0 | extraction_service.py → GPU 1")
```

### CELL 3 — Start Server + Localtunnel
```python
import subprocess, time, urllib.request

subprocess.Popen(["python", "-m", "uvicorn", "src.phase4_backend.main:app", "--host", "0.0.0.0", "--port", "8000", "--log-level", "info"])
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
|---------|-----|
| CUDA OOM | Use GPU T4 x2 (not x1) |
| Dataset not found | Add `rafiki-models` in notebook Data panel |
| Localtunnel dead | Re-run Cell 3 |
| Model not loading | Verify `/kaggle/input/rafiki-models/` structure |
