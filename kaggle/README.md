# M3allem - Kaggle PDF Processing Pipeline

## Objective
Parse Moroccan curriculum PDFs using **Qwen2.5-VL-7B-Instruct** (vision-language model) into structured Markdown with LaTeX math, then chunk them into a curriculum dataset.

## Files

| File | Purpose |
|------|---------|
| `pdf_to_markdown_pipeline.py` | Main pipeline script (upload to Kaggle as Notebook) |
| `prepare_kaggle_dataset.py` | Packages the PDF + script for Kaggle dataset upload |

## How to Use on Kaggle

### Option A: Quick Start (Notebook)
1. Go to [Kaggle](https://kaggle.com) → Create → New Notebook
2. Upload `pdf_to_markdown_pipeline.py` as the notebook source
3. Add the PDF as a dataset input:
   - Click "Add Data" → "Upload" → select the PDF
   - Or upload to a Kaggle Dataset first, then add it
4. Update `config.pdf_path` in the script to match your dataset path
5. Select a GPU accelerator (T4 x2 recommended)
6. Run all cells

### Option B: Using the Dataset Prep Script
1. Run `prepare_kaggle_dataset.py` locally to create a zip
2. Upload the zip to Kaggle as a Dataset
3. Create a notebook using that dataset as input

## Expected Outputs

After processing, the `/kaggle/working/extracted_markdown/` directory contains:
- `pages/page_XX.md` — Per-page markdown extraction
- `full_course.md` — Complete course in one file
- `structured_data.json` — Full structured data with metadata
- `chunks.json` — Flattened chunks (ready for RAG ingestion)
- `summary.json` — Processing statistics

## Notes
- First run installs dependencies (~5 mins)
- Processing 26 pages on T4 takes ~20-30 mins
- Set `push_to_hub: True` + `HF_TOKEN` secret to auto-push to Hugging Face
- The model requires ~14GB VRAM in bfloat16 (fits T4 with flash_attention_2)
