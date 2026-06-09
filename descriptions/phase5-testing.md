# Phase 5 Testing: Running Your Custom Model on Kaggle GPU

This guide explains how to bypass Hugging Face's API limits by running your **FastAPI Backend and Fine-Tuned Model directly inside a free Kaggle T4 GPU**, and securely connecting it to your Vercel/Next.js frontend.

This is the ultimate setup for your presentation because it guarantees zero API blocks, massive GPU speed, and completely free hosting of your custom `rafiki-qwen-2.5-finetune` model.

---

## Step 0: Upload Models to Kaggle as a Dataset

Before starting, upload your downloaded models to Kaggle:

1. Go to [kaggle.com/datasets](https://www.kaggle.com/datasets) → **New Dataset**
2. Upload the file `models/rafiki_models_for_kaggle.zip`
3. Set:
   - **Title:** `rafiki-models`
   - **Visibility:** Private (or Public)
4. Click **Create**
5. Note your dataset slug: `your-username/rafiki-models`

When added as input in a notebook, the models will be at:
```
/kaggle/input/rafiki-models/
├── text-model/
└── vision-model/
```

---

## Step 1: Prepare the Kaggle Environment

1. Open [Kaggle](https://www.kaggle.com/) and create a **New Notebook**.
2. On the right-hand panel, under **Session Options**:
   - **Accelerator:** Set to `GPU T4 x2` (or `GPU T4 x1`).
   - **Internet:** Ensure it is turned `ON`.
3. On the right-hand panel, under **Data**:
   - Click **Add Data** → Search for `rafiki-models` (your uploaded dataset)
   - Add it. This makes the models available at `/kaggle/input/rafiki-models/`

---

## Step 2: Securely Clone Repo & Setup Environment

Create the first code cell. This securely accesses your Kaggle Secrets to clone your private GitHub repository and set up your `.env` file automatically.

```python
# CELL 1: Setup Environment and Secrets
import os
from kaggle_secrets import UserSecretsClient

# 1. Load Secrets
user_secrets = UserSecretsClient()
github_email = user_secrets.get_secret("GITHUB_EMAIL")
github_user = user_secrets.get_secret("GITHUB_USER")
github_token = user_secrets.get_secret("GITHUB_TOKEN")
hf_token = user_secrets.get_secret("HF_TOKEN")

# 2. Securely clone your github repository
repo_url = f"https://{github_token}@github.com/{github_user}/M3allem.git"
os.system(f"git clone {repo_url} app")
os.chdir('/kaggle/working/app')

# Set git identity (useful if you ever commit from Kaggle)
os.system(f'git config user.email "{github_email}"')
os.system(f'git config user.name "{github_user}"')

# 3. Create .env file dynamically
env_content = f"""
HF_TOKEN={hf_token}
CHROMA_DB_DIR=./chroma_db_cache
VL_MODEL_ID=Qwen/Qwen2.5-VL-3B-Instruct
"""
with open(".env", "w") as f:
    f.write(env_content)
print(".env file created securely!")

# 4. Install backend requirements
!pip install -r requirements_all.txt

# 5. Install GPU local model dependencies (Transformers & Vision Utils)
!pip install transformers accelerate bitsandbytes qwen-vl-utils torchvision

# 6. Install Localtunnel (to create a public URL)
!npm install -g localtunnel

# 7. Discover & define model paths from Kaggle Dataset Input
import os

CANDIDATES = [
    "/kaggle/input/rafiki-models",
    "/kaggle/input/datasets/saadelouakate/rafiki-models",
]
DATASET_ROOT = next((p for p in CANDIDATES if os.path.isdir(p)), None)
if DATASET_ROOT is None:
    raise FileNotFoundError("Dataset 'rafiki-models' not found — add it in the Data panel.")

def _find_subdir(base, name):
    cand = os.path.join(base, name)
    if os.path.isfile(os.path.join(cand, "config.json")):
        return cand
    for sub in sorted(os.listdir(cand)):
        sp = os.path.join(cand, sub)
        if os.path.isdir(sp) and os.path.isfile(os.path.join(sp, "config.json")):
            return sp
    return cand

TEXT_MODEL_PATH = _find_subdir(DATASET_ROOT, "text-model")
VISION_MODEL_PATH = _find_subdir(DATASET_ROOT, "vision-model")
print(f"Text model path: {TEXT_MODEL_PATH}")
print(f"Vision model path: {VISION_MODEL_PATH}")
```
*Run this cell and wait for the installations to complete.*

---

## Step 3: Override API to Use Dual Kaggle GPUs

By default, your code tries to call the Hugging Face Serverless APIs. We need to tell it to load the models **directly into the Kaggle GPUs** from the dataset input instead.

Create a second code cell. This script will overwrite both `llm_service.py` and `extraction_service.py` to utilize Kaggle's dual T4 setup:
- **GPU 0** will run your Fine-Tuned Text Model (loaded from `/kaggle/input/rafiki-models/text-model`).
- **GPU 1** will run your Vision Model (loaded from `/kaggle/input/rafiki-models/vision-model`).

```python
# CELL 2: Override Backend Services to Use Dual Kaggle GPUs

# ── Discovered paths from CELL 1 ──────────────────────────────────
# (re-run if paths are empty)
import os
CANDIDATES = [
    "/kaggle/input/rafiki-models",
    "/kaggle/input/datasets/saadelouakate/rafiki-models",
]
DATASET_ROOT = next((p for p in CANDIDATES if os.path.isdir(p)), None)
if DATASET_ROOT is None:
    raise FileNotFoundError("Dataset 'rafiki-models' not found.")

def _find_subdir(base, name):
    cand = os.path.join(base, name)
    if os.path.isfile(os.path.join(cand, "config.json")):
        return cand
    for sub in sorted(os.listdir(cand)):
        sp = os.path.join(cand, sub)
        if os.path.isdir(sp) and os.path.isfile(os.path.join(sp, "config.json")):
            return sp
    return cand

TEXT_MODEL_PATH = _find_subdir(DATASET_ROOT, "text-model")
VISION_MODEL_PATH = _find_subdir(DATASET_ROOT, "vision-model")

# ====================================================================
# 1. OVERRIDE LLM SERVICE (TEXT MODEL ON GPU 0)
# ====================================================================
_LLM = r"""
import os
import logging
import torch
from transformers import pipeline, BitsAndBytesConfig

logger = logging.getLogger(__name__)

TEXT_MODEL_PATH = "__TEXT_MODEL_PATH__"
logger.info(f"Loading text model from {TEXT_MODEL_PATH} into GPU 0 in 4-bit...")

quant_config = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_compute_dtype=torch.float16)
generator = pipeline("text-generation", model=TEXT_MODEL_PATH, device_map="cuda:0", model_kwargs={"quantization_config": quant_config})
logger.info("Text Model loaded successfully in 4-bit!")

def generate_answer(context: str, question: str) -> str:
    system_prompt = "Vous \u00eates Rafiki, un tuteur IA pour les \u00e9tudiants marocains (2\u00e8me Bac). Utilisez le contexte fourni."
    prompt = f"<|im_start|>system\n{system_prompt}\nContexte:\n{context}<|im_end|>\n<|im_start|>user\n{question}<|im_end|>\n<|im_start|>assistant\n"
    res = generator(prompt, max_new_tokens=1500, temperature=0.3)
    return res[0]['generated_text'].split("<|im_start|>assistant\n")[-1]

def correct_exercise(context: str, exercise_text: str) -> str:
    system_prompt = "Vous \u00eates Rafiki... Corrigez cet exercice \u00e9tape par \u00e9tape."
    prompt = f"<|im_start|>system\n{system_prompt}\nContexte:\n{context}<|im_end|>\n<|im_start|>user\n{exercise_text}<|im_end|>\n<|im_start|>assistant\n"
    res = generator(prompt, max_new_tokens=2000, temperature=0.3)
    return res[0]['generated_text'].split("<|im_start|>assistant\n")[-1]
"""
override_llm = _LLM.replace("__TEXT_MODEL_PATH__", TEXT_MODEL_PATH)
with open("src/phase4_backend/services/llm_service.py", "w", encoding="utf-8") as f:
    f.write(override_llm)


# ====================================================================
# 2. OVERRIDE EXTRACTION SERVICE (VISION MODEL ON GPU 1)
# ====================================================================
_VISION = r"""
import logging
from typing import List
from transformers import Qwen2_5_VLForConditionalGeneration, AutoProcessor, BitsAndBytesConfig
from qwen_vl_utils import process_vision_info
import torch

logger = logging.getLogger(__name__)

VISION_MODEL_PATH = "__VISION_MODEL_PATH__"
logger.info(f"Loading vision model from {VISION_MODEL_PATH} into GPU 1 in 4-bit...")

quant_config = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_compute_dtype=torch.float16)
model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
    VISION_MODEL_PATH, 
    quantization_config=quant_config, 
    device_map="cuda:1"
)
processor = AutoProcessor.from_pretrained(VISION_MODEL_PATH)
logger.info("Vision Model loaded successfully in 4-bit!")

def file_to_base64_images(file_bytes: bytes, filename: str) -> List[str]:
    import fitz, base64
    base64_images = []
    if filename.lower().endswith('.pdf'):
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
            base64_images.append(base64.b64encode(pix.tobytes("png")).decode('utf-8'))
    return base64_images

def extract_text_via_vl(base64_images: List[str]) -> str:
    extracted_text = ""
    for idx, b64_img in enumerate(base64_images):
        messages = [{"role": "user", "content": [
            {"type": "image", "image": f"data:image/png;base64,{b64_img}"},
            {"type": "text", "text": "Extract all text and math. Use LaTeX for math."}
        ]}]
        
        text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        image_inputs, video_inputs = process_vision_info(messages)
        inputs = processor(
            text=[text], images=image_inputs, videos=video_inputs, padding=True, return_tensors="pt"
        ).to("cuda:1")

        generated_ids = model.generate(**inputs, max_new_tokens=2000)
        generated_ids_trimmed = [out_ids[len(in_ids):] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)]
        output_text = processor.batch_decode(generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False)
        extracted_text += f"\n\n--- Page {idx+1} ---\n\n" + output_text[0]
        
    return extracted_text.strip()
"""
override_vision = _VISION.replace("__VISION_MODEL_PATH__", VISION_MODEL_PATH)
with open("src/phase4_backend/services/extraction_service.py", "w", encoding="utf-8") as f:
    f.write(override_vision)

print("Services successfully overridden for Dual Kaggle GPUs!")
```
*Run this cell to save the GPU configurations.*

---

## Step 4: Start Server & Expose to the Internet

Create the third code cell. This will start your FastAPI server in the background and expose it using Localtunnel.

```python
# CELL 3: Start Uvicorn and Localtunnel
import os, subprocess, time, urllib.request

# ── Verify override files have valid model paths ────────────────────
for fname, label in [("llm_service.py", "Text"), ("extraction_service.py", "Vision")]:
    fpath = f"src/phase4_backend/services/{fname}"
    if not os.path.isfile(fpath):
        print(f"❌ Override file missing: {fpath} — run Cell 2 first!")
        raise SystemExit(1)
    with open(fpath) as f:
        content = f.read()
    for line in content.splitlines():
        if "MODEL_PATH" in line and "=" in line and not line.strip().startswith("#"):
            val = line.split("=", 1)[1].strip().strip('"').strip("'")
            if os.path.isdir(val) or os.path.isfile(os.path.join(val, "config.json")):
                print(f"  ✅ {label} model path OK: {val}")
            else:
                print(f"  ⚠️ {label} model path may be invalid: {val}")

# 1. Start FastAPI server in the background
print("Starting FastAPI Server...")
subprocess.Popen(["python", "-m", "uvicorn", "src.phase4_backend.main:app", "--host", "0.0.0.0", "--port", "8000"])

# Give the server 20 seconds to boot up, load models from dataset into VRAM
time.sleep(20) 

# 2. Get the public IP address (you will need this password for localtunnel)
ip = urllib.request.urlopen('https://ipv4.icanhazip.com').read().decode('utf8').strip("\n")
print(f"\n==============================================")
print(f"YOUR LOCALTUNNEL PASSWORD IS: {ip}")
print(f"==============================================\n")

# 3. Start Localtunnel to generate the public HTTPS link
!npx localtunnel --port 8000
```

### What happens when you run Cell 3:
1. **Model Loading Phase:** FastAPI boots up and loads both models from the Kaggle Dataset Input directly into GPU VRAM. This is much faster than downloading (~30 seconds vs ~5 minutes).
2. It will print a password (an IP address). **Copy this password**.
3. It will output a URL that looks like `https://funny-words-go.loca.lt`.
4. Click that link. It will ask for a password. Paste the IP address.
5. **Congratulations!** Your Kaggle API (powered by two dedicated GPUs) is now live to the internet!

---

## Step 5: Connect your Frontend to the Kaggle API

Now that your API is running on a public link, you can connect your Next.js app to it.

1. Go to your local machine (where you run your frontend).
2. Open the Next.js `frontend/.env` file (or create it if it doesn't exist).
3. Add the Localtunnel URL you got from Kaggle:
   ```env
   NEXT_PUBLIC_API_URL=https://funny-words-go.loca.lt
   ```
4. Run your frontend:
   ```bash
   npm run dev
   ```

**The Magic:** When you ask a question in your local frontend, it sends a request across the internet to the Kaggle GPU, processes it through your custom fine-tuned model and RAG database, and sends the answer back! 

*(Note: Every time you restart the Kaggle notebook, the Localtunnel URL changes, so just update your `NEXT_PUBLIC_API_URL` before your presentation).*
