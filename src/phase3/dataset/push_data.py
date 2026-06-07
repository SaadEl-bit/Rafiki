from datasets import load_dataset
from huggingface_hub import login

# 1. Login to Hugging Face
login("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")

# 2. Load the dataset you just built
print("Loading local dataset...")
dataset = load_dataset("json", data_files="h:/Study/Projects/M3allem/Github/M3allem/output/phase3/triplets.jsonl", split="train")

# 3. Push to your private Hub
print("Pushing to HuggingFace...")
dataset.push_to_hub("Saad-Elouakate/rafiki-qna-triplets", private=True)

print("Done! Dataset is ready.")
