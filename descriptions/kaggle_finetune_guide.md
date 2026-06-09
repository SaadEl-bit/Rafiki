# Phase 3 Fine-Tuning Guide

Everything looks perfectly ready! Your Phase 1 and 2 pipelines successfully built the datasets, and your `build_dataset.py` accurately created the training-ready Q&A triplets in `output/phase3/triplets.jsonl`. 

> [!NOTE]
> ### 💡 How Model Handling is Different from Phase 1
> Because you used **Qwen2.5-VL-2B** previously, you likely had to manually download it as a Kaggle Dataset, attach it to your notebook, and load it from a local folder like `/kaggle/input/`. 
> 
> **For Phase 3, you do NOT need to do that!**
> 
> * **How to download the new model?** The python code below (`FastLanguageModel.from_pretrained`) automatically downloads the model directly from HuggingFace when you run the cell. You just need to ensure the **"Internet"** toggle is switched ON in your Kaggle notebook settings.
> * **Where is it put?** Kaggle temporarily saves it in the hidden `~/.cache/huggingface/` folder. You don't need to touch or manage these files.
> * **How to extract it after training?** You don't! The script keeps everything in memory and temporary folders.
> * **How to push it to HuggingFace?** The final cell (`model.push_to_hub_merged`) automatically takes the base model, merges your trained changes into it, and uploads the final model straight to your HuggingFace account over the internet.

---

## Part 1: Push Your Dataset to HuggingFace (Locally)

Before going to Kaggle, you need to push the `triplets.jsonl` file to your private HuggingFace account so Kaggle can download it easily.

Create a temporary file named `push_data.py` on your computer and run it. **Make sure to replace `YOUR_HF_TOKEN` with your actual token.**

```python
from datasets import load_dataset
from huggingface_hub import login

# 1. Login to Hugging Face
login("YOUR_HF_TOKEN")

# 2. Load the dataset you just built
print("Loading local dataset...")
dataset = load_dataset("json", data_files="output/phase3/triplets.jsonl", split="train")

# 3. Push to your private Hub
print("Pushing to HuggingFace...")
dataset.push_to_hub("Saad-Elouakate/rafiki-qna-triplets", private=True)

print("Done! Dataset is ready.")
```

Run this in your terminal: `python push_data.py`. 
*Note: Check your HuggingFace account to verify the dataset `rafiki-qna-triplets` exists and is set to Private.*

---

## Part 2: Kaggle Fine-Tuning Notebook Cells

Create a new Notebook on Kaggle, turn on the **T4 GPU** accelerator, **Turn ON Internet**, and add the following code cells. We will use **Unsloth** because it makes training 2x faster and uses 50% less VRAM.

### Cell 1: Install Dependencies
```python
%%capture
!pip install -U unsloth
!pip install -U datasets accelerate bitsandbytes
```

Do **not** install `transformers`, `peft`, or `trl` directly from GitHub for this notebook. The live GitHub versions can become incompatible with the Unsloth trainer wrapper and trigger errors like:

```text
TypeError: SFTConfig.__init__() got an unexpected keyword argument 'push_to_hub_token'
```

### Cell 2: Login & Load the Base Model
*Replace `YOUR_HF_TOKEN` with your write-access token (or use Kaggle Secrets).*
```python
from unsloth import FastLanguageModel
import torch
from huggingface_hub import login

login("YOUR_HF_TOKEN") # Required to push later

# Automatically downloads the base model from HuggingFace to Kaggle's cache!
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "Qwen/Qwen2.5-1.5B-Instruct",
    max_seq_length = 2048, # Supports long questions/answers
    dtype = None, # Auto-detect
    load_in_4bit = True, 
)

# Apply LoRA Adapters (Rank = 16)
model = FastLanguageModel.get_peft_model(
    model,
    r = 16, 
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj"],
    lora_alpha = 16,
    lora_dropout = 0, # 0 is optimized for Unsloth
    bias = "none",
    use_gradient_checkpointing = "unsloth",
    random_state = 3407,
)
```

### Cell 3: Load Your Dataset
```python
from datasets import load_dataset

# Load your private dataset from HuggingFace
dataset = load_dataset("Saad-Elouakate/rafiki-qna-triplets", split="train")

# Verify the ChatML format looks correct
print(dataset[0]["text"])
```

### Cell 4: Train the Model
```python
from trl import SFTTrainer
from trl import SFTConfig
from unsloth import is_bfloat16_supported

trainer = SFTTrainer(
    model = model,
    processing_class = tokenizer,
    train_dataset = dataset,
    args = SFTConfig(
        dataset_text_field = "text", # We use the pre-formatted ChatML column!
        max_seq_length = 2048,
        dataset_num_proc = 2,
        packing = False,
        per_device_train_batch_size = 2,
        gradient_accumulation_steps = 4,
        warmup_steps = 5,
        num_train_epochs = 3, # Training for 3 passes over your ~277 rows
        learning_rate = 2e-4,
        fp16 = not is_bfloat16_supported(),
        bf16 = is_bfloat16_supported(),
        logging_steps = 10,
        optim = "adamw_8bit",
        weight_decay = 0.01,
        lr_scheduler_type = "linear",
        seed = 3407,
        output_dir = "outputs",
        report_to = "none", # Disable wandb logging
    ),
)

# Start training! (Should take ~5 to 15 minutes)
trainer_stats = trainer.train()
```

### Cell 5: Test the Model Locally
Let's ask it a question to see its Moroccan Professor style.
```python
# Enable native 2x faster inference
FastLanguageModel.for_inference(model) 

test_prompt = """<|im_start|>system
You are Rafiki, a Moroccan 2Bac professor. Explain concepts clearly and step by step, using appropriate terminology for the Moroccan baccalaureate curriculum.<|im_end|>
<|im_start|>user
Comment calculer la dérivée de f(x) = x^2 + 3x ?<|im_end|>
<|im_start|>assistant
"""

inputs = tokenizer([test_prompt], return_tensors = "pt").to("cuda")

# Generate response
outputs = model.generate(**inputs, max_new_tokens = 512, use_cache = True)
response = tokenizer.batch_decode(outputs, skip_special_tokens = False)[0]

print(response)
```

### Cell 6: Merge & Push to HuggingFace
**This is the most critical step for Phase 4.** Because the Hugging Face Serverless API cannot easily attach an adapter to a base model dynamically, we use Unsloth's `merged_16bit` method. This physically merges your LoRA weights into the Qwen weights, creating a brand new, standalone ~3GB model.

```python
# Merge the LoRA adapter into the base model and push the full model directly to HuggingFace
print("Merging and pushing to HuggingFace... (This might take a few minutes)")

model.push_to_hub_merged(
    "Saad-Elouakate/rafiki-qwen-finetune", 
    tokenizer, 
    save_method = "merged_16bit", # Combines base model + LoRA
    token = "YOUR_HF_TOKEN"
)

print("Successfully pushed! Your model is now ready for the Serverless API.")
```
