"""
M3allem - Kaggle Dataset Preparation Script
=============================================
Packages the PDF + pipeline script into a zip file
ready for upload to Kaggle as a Dataset.

Usage:
    python prepare_kaggle_dataset.py
"""

import os
import zipfile
from pathlib import Path
import datetime

# Paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
KAGGLE_DIR = PROJECT_ROOT / "kaggle"
DATA_DIR = PROJECT_ROOT / "Document-Data-Set"
OUTPUT_ZIP = KAGGLE_DIR / "m3allem_kaggle_dataset.zip"

def prepare():
    files_to_package = []

    # 1. Pipeline script
    script_path = KAGGLE_DIR / "pdf_to_markdown_pipeline.py"
    if script_path.exists():
        files_to_package.append((script_path, "pdf_to_markdown_pipeline.py"))
        print(f"  ✓ {script_path.name}")
    else:
        print(f"  ✗ {script_path.name} not found")

    # 2. PDFs from Document-Data-Set
    if DATA_DIR.exists():
        for pdf_file in sorted(DATA_DIR.glob("*.pdf")):
            target = f"data/{pdf_file.name}"
            files_to_package.append((pdf_file, target))
            print(f"  ✓ {pdf_file.name}")
    else:
        print(f"  ✗ Document-Data-Set directory not found")

    # 3. README
    readme_path = KAGGLE_DIR / "README.md"
    if readme_path.exists():
        files_to_package.append((readme_path, "README.md"))
        print(f"  ✓ {readme_path.name}")

    # Create zip
    print(f"\nCreating {OUTPUT_ZIP.name}...")
    with zipfile.ZipFile(OUTPUT_ZIP, "w", zipfile.ZIP_DEFLATED) as zf:
        for filepath, arcname in files_to_package:
            zf.write(filepath, arcname)

    size_mb = os.path.getsize(OUTPUT_ZIP) / (1024 * 1024)
    print(f"\n✅ Done! Created {OUTPUT_ZIP.name} ({size_mb:.1f} MB)")
    print(f"   Upload this file to Kaggle as a Dataset, then use it in your notebook.")

if __name__ == "__main__":
    prepare()
