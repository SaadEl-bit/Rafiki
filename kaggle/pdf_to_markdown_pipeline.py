"""
================================================================================
  M3allem - Moroccan Adaptive AI Tutor Platform
  Phase 1: PDF to Structured Markdown Pipeline (Kaggle)
================================================================================
  Description: Parses Moroccan curriculum PDFs using Qwen2.5-VL-2B,
               extracts structured content (definitions, theorems,
               formulas, examples, exercises) into clean Markdown
               with LaTeX math notation.

  Target PDF: Cours_Proba-Statistiques-1-6.pdf
              (Probability & Statistics, FIGI-S1, FSTS Settat)

  Steps:
    1. Install dependencies
    2. Load PDF & convert pages to images
    3. Load Qwen2.5-VL-2B-Instruct
    4. Process each page with vision-language model
    5. Extract structured Markdown
    6. Chunk content by sections
    7. Save results & optionally push to Hugging Face
================================================================================
"""

# ==============================================================================
# CELL 1: Install dependencies
# ==============================================================================

import subprocess, sys

def _pip_install(*packages):
    """Install packages quietly via pip (works in Kaggle .py scripts)."""
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "-q", *packages],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT,
    )

print("Installing dependencies...")
_pip_install("PyMuPDF", "Pillow")
_pip_install("transformers>=4.49.0", "qwen-vl-utils", "accelerate")
_pip_install("datasets", "huggingface-hub")
_pip_install("sentencepiece", "einops")
print("Dependencies installed.")

# ==============================================================================
# CELL 2: Imports & Configuration
# ==============================================================================

import os
import json
import yaml
import time
import logging
import re
from pathlib import Path
from typing import List, Dict, Optional, Any
from dataclasses import dataclass, field, asdict
from PIL import Image

import torch
import fitz  # PyMuPDF
from transformers import AutoModelForImageTextToText, AutoProcessor
from datasets import Dataset, DatasetDict
from huggingface_hub import HfApi, login

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# ----------------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------------

@dataclass
class PipelineConfig:
    # --- PDF Source ---
    pdf_path: str = "/kaggle/input/datasets/saadelouakate/proba-raw-pdfs/Cours_Proba-Statistiques-1-6.pdf"
    pdf_output_dir: str = "/kaggle/working/extracted_markdown"

    # --- Model ---
    model_name: str = "/kaggle/input/models/qwen-lm/qwen-3-vl/transformers/2b-instruct/1"
    device: str = "cuda" if torch.cuda.is_available() else "cpu"
    max_new_tokens: int = 2048
    temperature: float = 0.1
    top_p: float = 0.9

    # --- Processing ---
    batch_size: int = 1       # Process pages sequentially with VL model
    dpi: int = 150            # PDF page render resolution (150 saves VRAM vs 200)
    start_page: int = 0       # 0-indexed, set to skip cover/toc
    end_page: int = 3         # First 3 pages for test (0-indexed: pages 0,1,2)

    # --- Output ---
    push_to_hub: bool = True
    hub_dataset_name: str = "Saad-Elouakate/AI-Adaptive-Learning"
    hub_token: Optional[str] = None  # Set via Kaggle Secrets or env var
    save_local: bool = True

    # --- Content Classification ---
    chapter_pattern: str = r"^(Chapitre|Chapter)\s+\d+|^\d+\s+[A-Z]"
    section_pattern: str = r"^\d+\.\d+\s+[A-Z]"

    # --- Metadata ---
    subject: str = "Probabilites & Statistiques"
    level: str = "FIGI-S1 (Bac+1)"
    language: str = "fr"
    curriculum: str = "Moroccan University - FSTS Settat"
    source_file: str = "Cours_Proba-Statistiques-1-6.pdf"


config = PipelineConfig()

# Create output directory
Path(config.pdf_output_dir).mkdir(parents=True, exist_ok=True)

# ==============================================================================
# CELL 3: PDF Processing Utilities
# ==============================================================================

class PDFProcessor:
    """Handles PDF loading, page extraction, and image conversion."""

    def __init__(self, pdf_path: str, dpi: int = 200):
        self.pdf_path = pdf_path
        self.dpi = dpi
        self.doc = None

    def open(self):
        """Open the PDF document."""
        if not Path(self.pdf_path).exists():
            raise FileNotFoundError(f"PDF not found: {self.pdf_path}")
        self.doc = fitz.open(self.pdf_path)
        logger.info(f"Opened PDF: {self.pdf_path} ({self.doc.page_count} pages)")
        return self

    def close(self):
        if self.doc:
            self.doc.close()

    @property
    def page_count(self) -> int:
        return len(self.doc) if self.doc else 0

    def get_page_text(self, page_num: int) -> str:
        """Extract raw text from a page (fallback / pre-processing)."""
        page = self.doc[page_num]
        return page.get_text()

    def page_to_image(self, page_num: int) -> Image.Image:
        """Render a PDF page as a PIL Image at the configured DPI."""
        page = self.doc[page_num]
        mat = fitz.Matrix(self.dpi / 72, self.dpi / 72)
        pix = page.get_pixmap(matrix=mat)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        return img

    def get_page_range(self, start: int = 0, end: Optional[int] = None):
        """Get the range of pages to process."""
        end = end or self.page_count
        return range(start, min(end, self.page_count))

    def extract_all_text(self, start: int = 0, end: Optional[int] = None) -> Dict[int, str]:
        """Extract raw text from all pages in range."""
        result = {}
        for i in self.get_page_range(start, end):
            result[i] = self.get_page_text(i)
        return result


# ==============================================================================
# CELL 4: Qwen2.5-VL Model Loader
# ==============================================================================

class VisionLanguageProcessor:
    """Handles loading Qwen2.5-VL-2B and processing page images."""

    def __init__(self, config: PipelineConfig):
        self.config = config
        self.model = None
        self.processor = None

    def load_model(self):
        """Load the model and processor."""
        logger.info(f"Loading model: {self.config.model_name}")
        attn = "flash_attention_2"
        try:
            import flash_attn
        except ImportError:
            attn = "sdpa"
            logger.info("flash_attn not installed, falling back to SDPA")

        # 2B model in bfloat16 = ~4GB — fits on T4 (16GB) with 12GB+ headroom.
        # AutoModelForImageTextToText correctly resolves Qwen2.5-VL without class mismatch.
        self.model = AutoModelForImageTextToText.from_pretrained(
            self.config.model_name,
            torch_dtype=torch.bfloat16,
            device_map="auto",
            attn_implementation=attn,
        )
        self.processor = AutoProcessor.from_pretrained(
            self.config.model_name,
            min_pixels=256 * 256,
            max_pixels=768 * 768,
        )
        logger.info("Model loaded successfully")
        return self

    def build_extraction_prompt(self, page_num: int, total_pages: int, raw_text_hint: str = "") -> str:
        """Build the prompt for extracting structured content from a PDF page image."""

        prompt = f"""You are an AI assistant for the M3allem project, extracting Moroccan curriculum content from PDF pages.

Page {page_num + 1} of {total_pages}

Your task is to extract ALL content from this page image and convert it to clean Markdown.

RULES:
- Preserve the exact academic content (definitions, theorems, formulas, proofs, examples)
- Write ALL mathematical formulas in LaTeX inline ($...$) or display ($$...$$) format
- Use proper Markdown headings (# for chapter, ## for section, ### for subsection)
- Format definitions as: **Definition:** ...
- Format theorems as: **Theorem:** ...
- Format proofs as: **Proof:** ...
- Format examples as: **Example X:** ...
- Format exercises/questions as: **Exercise X:** ...
- Keep the original French or Arabic text exactly as written
- If a table is present, format it as a Markdown table
- If a diagram is described, note it as [Diagram: description]
- Extract EVERYTHING — do not skip content

Output ONLY the Markdown content, no additional commentary."""

        if raw_text_hint.strip():
            prompt += f"\n\nRaw text extracted from this page (use as reference, but prefer what you see):\n{raw_text_hint[:500]}"

        return prompt

    def process_page(
        self,
        image: Image.Image,
        page_num: int,
        total_pages: int,
        raw_text_hint: str = "",
    ) -> str:
        """Process a single page image and return structured Markdown."""

        prompt_text = self.build_extraction_prompt(page_num, total_pages, raw_text_hint)

        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "image", "image": image},
                    {"type": "text", "text": prompt_text},
                ],
            }
        ]

        text = self.processor.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )

        inputs = self.processor(
            text=[text],
            images=[image],
            padding=True,
            return_tensors="pt",
        )

        if torch.cuda.is_available():
            inputs = inputs.to("cuda")

        generated_ids = self.model.generate(
            **inputs,
            max_new_tokens=self.config.max_new_tokens,
            temperature=self.config.temperature,
            top_p=self.config.top_p,
            do_sample=True,
        )

        # Strip input tokens from output
        generated_ids_trimmed = [
            out_ids[len(in_ids):]
            for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
        ]

        output_text = self.processor.batch_decode(
            generated_ids_trimmed,
            skip_special_tokens=True,
            clean_up_tokenization_spaces=False,
        )[0]

        return output_text.strip()

    def process_pages_batch(
        self,
        pages: List[int],
        pdf_processor: PDFProcessor,
    ) -> Dict[int, str]:
        """Process multiple pages sequentially."""
        results = {}
        total = len(pages)

        for idx, page_num in enumerate(pages):
            logger.info(f"Processing page {page_num + 1}/{total} ({idx + 1}/{total})")

            # Get image and raw text hint
            image = pdf_processor.page_to_image(page_num)
            raw_text = pdf_processor.get_page_text(page_num)

            try:
                markdown = self.process_page(
                    image=image,
                    page_num=page_num,
                    total_pages=total,
                    raw_text_hint=raw_text,
                )
                results[page_num] = markdown
                logger.info(f"Page {page_num + 1} -> {len(markdown)} chars extracted")
            except Exception as e:
                logger.error(f"Failed to process page {page_num + 1}: {e}")
                results[page_num] = f"<!-- ERROR: {e} -->\n\n{raw_text}"
                time.sleep(30)  # Cooldown on error

            # Small delay to avoid overwhelming the GPU
            time.sleep(1)

        return results


# ==============================================================================
# CELL 5: Content Structuring & Chunking
# ==============================================================================

class ContentStructuring:
    """Post-processes extracted Markdown into structured, chunked curriculum data."""

    @staticmethod
    def clean_markdown(text: str) -> str:
        """Clean up common issues in extracted Markdown."""
        # Remove multiple consecutive blank lines
        text = re.sub(r"\n{3,}", "\n\n", text)
        # Fix broken LaTeX delimiters
        text = text.replace("\\[", "$$").replace("\\]", "$$")
        text = text.replace("\\(", "$").replace("\\)", "$")
        # Fix common OCR issues
        text = text.replace("| |", "|")
        return text.strip()

    @staticmethod
    def detect_content_type(text: str) -> str:
        """Classify the content type of a chunk."""
        text_lower = text.lower()
        if any(kw in text_lower for kw in ["exercice", "exercise", "exercice"]):
            return "exercise"
        if any(kw in text_lower for kw in ["definition", "définition"]):
            return "definition"
        if any(kw in text_lower for kw in ["theoreme", "théorème", "theorem"]):
            return "theorem"
        if any(kw in text_lower for kw in ["demonstration", "démonstration", "proof"]):
            return "proof"
        if any(kw in text_lower for kw in ["exemple", "example"]):
            return "example"
        if any(kw in text_lower for kw in ["propriete", "propriété", "property"]):
            return "property"
        if any(kw in text_lower for kw in ["remarque", "note"]):
            return "remark"
        if any(kw in text_lower for kw in ["solution", "correction"]):
            return "solution"
        return "course_content"

    @staticmethod
    def extract_section_title(text: str) -> str:
        """Extract the section title from markdown content."""
        # Look for the first heading
        match = re.search(r"^#{1,3}\s+(.+)$", text, re.MULTILINE)
        if match:
            return match.group(1).strip()
        return "untitled"

    @staticmethod
    def extract_math_formulas(text: str) -> List[str]:
        """Extract all LaTeX math formulas from the text."""
        # Display math
        display = re.findall(r"\$\$(.*?)\$\$", text, re.DOTALL)
        # Inline math
        inline = re.findall(r"\$(.*?)\$", text)
        return display + inline

    @staticmethod
    def chunk_by_headings(markdown_text: str) -> List[Dict[str, Any]]:
        """Split a full markdown document into chunks by headings."""
        lines = markdown_text.split("\n")
        chunks = []
        current_chunk = []
        current_heading = "preamble"

        for line in lines:
            # Check if this is a heading (## or ### — not # which might be page title)
            heading_match = re.match(r"^(#{2,3})\s+(.+)$", line)
            if heading_match:
                # Save previous chunk
                if current_chunk:
                    chunk_text = "\n".join(current_chunk).strip()
                    if chunk_text:
                        chunks.append({
                            "section_title": current_heading,
                            "content_type": ContentStructuring.detect_content_type(chunk_text),
                            "content": chunk_text,
                            "math_formulas": ContentStructuring.extract_math_formulas(chunk_text),
                        })
                current_heading = heading_match.group(2).strip()
                current_chunk = [line]
            else:
                current_chunk.append(line)

        # Don't forget the last chunk
        if current_chunk:
            chunk_text = "\n".join(current_chunk).strip()
            if chunk_text:
                chunks.append({
                    "section_title": current_heading,
                    "content_type": ContentStructuring.detect_content_type(chunk_text),
                    "content": chunk_text,
                    "math_formulas": ContentStructuring.extract_math_formulas(chunk_text),
                })

        return chunks

    @staticmethod
    def build_curriculum_entry(
        page_num: int,
        raw_markdown: str,
        metadata: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Build a complete curriculum entry from a page's extracted content."""
        cleaned = ContentStructuring.clean_markdown(raw_markdown)
        chunks = ContentStructuring.chunk_by_headings(cleaned)

        return {
            "page_number": page_num + 1,
            "source_file": metadata.get("source_file", ""),
            "subject": metadata.get("subject", ""),
            "level": metadata.get("level", ""),
            "language": metadata.get("language", "fr"),
            "curriculum": metadata.get("curriculum", ""),
            "raw_markdown": cleaned,
            "chunks": chunks,
            "total_chunks": len(chunks),
            "math_formulas": ContentStructuring.extract_math_formulas(cleaned),
        }


# ==============================================================================
# CELL 6: Main Pipeline
# ==============================================================================

class M3allemPDFPipeline:
    """End-to-end pipeline: PDF -> Qwen2.5-VL -> Structured Markdown -> Dataset."""

    def __init__(self, config: PipelineConfig):
        self.config = config
        self.pdf_processor = None
        self.vl_processor = None
        self.results: List[Dict[str, Any]] = []

    def run(self):
        """Execute the full pipeline."""
        start_time = time.time()
        logger.info("=" * 60)
        logger.info("M3allem PDF -> Markdown Pipeline Started")
        logger.info("=" * 60)

        # Step 1: Open PDF
        logger.info("[Step 1/5] Opening PDF...")
        self.pdf_processor = PDFProcessor(
            pdf_path=self.config.pdf_path,
            dpi=self.config.dpi,
        ).open()
        total_pages = self.pdf_processor.page_count
        logger.info(f"Total pages: {total_pages}")

        # Step 2: Load Vision-Language Model
        logger.info("[Step 2/5] Loading Qwen2.5-VL-2B...")
        self.vl_processor = VisionLanguageProcessor(self.config)
        self.vl_processor.load_model()

        # Step 3: Process pages
        logger.info("[Step 3/5] Processing pages...")
        page_range = list(self.pdf_processor.get_page_range(
            start=self.config.start_page,
            end=self.config.end_page,
        ))
        extracted = self.vl_processor.process_pages_batch(
            pages=page_range,
            pdf_processor=self.pdf_processor,
        )

        # Step 4: Structure content
        logger.info("[Step 4/5] Structuring extracted content...")
        metadata = {
            "source_file": self.config.source_file,
            "subject": self.config.subject,
            "level": self.config.level,
            "language": self.config.language,
            "curriculum": self.config.curriculum,
        }

        for page_num, markdown in sorted(extracted.items()):
            entry = ContentStructuring.build_curriculum_entry(
                page_num=page_num,
                raw_markdown=markdown,
                metadata=metadata,
            )
            self.results.append(entry)

        # Step 5: Save outputs
        logger.info("[Step 5/5] Saving outputs...")
        self._save_outputs()

        # Cleanup
        self.pdf_processor.close()

        elapsed = time.time() - start_time
        logger.info("=" * 60)
        logger.info(f"Pipeline complete in {elapsed:.1f}s")
        logger.info(f"Processed {len(self.results)} pages")
        logger.info(f"Output: {self.config.pdf_output_dir}")
        logger.info("=" * 60)

        return self.results

    def _save_outputs(self):
        """Save all outputs to disk and optionally push to Hugging Face."""
        output_dir = Path(self.config.pdf_output_dir)

        # 1. Save full extracted markdown (one file per page)
        pages_dir = output_dir / "pages"
        pages_dir.mkdir(exist_ok=True)
        for entry in self.results:
            page_file = pages_dir / f"page_{entry['page_number']:02d}.md"
            page_file.write_text(entry["raw_markdown"], encoding="utf-8")

        logger.info(f"Saved {len(self.results)} page markdown files to {pages_dir}")

        # 2. Save combined markdown (all pages in one file)
        combined = []
        for entry in self.results:
            combined.append(f"<!-- Page {entry['page_number']} -->\n")
            combined.append(entry["raw_markdown"])
            combined.append("\n\n---\n\n")

        combined_path = output_dir / "full_course.md"
        combined_path.write_text("\n".join(combined), encoding="utf-8")
        logger.info(f"Saved combined markdown: {combined_path}")

        # 3. Save structured JSON (for dataset ingestion)
        json_path = output_dir / "structured_data.json"
        json_path.write_text(
            json.dumps(self.results, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        logger.info(f"Saved structured JSON: {json_path}")

        # 4. Save a flattened chunked dataset
        all_chunks = []
        for entry in self.results:
            for chunk in entry["chunks"]:
                all_chunks.append({
                    "page_number": entry["page_number"],
                    "subject": entry["subject"],
                    "level": entry["level"],
                    "language": entry["language"],
                    "section_title": chunk["section_title"],
                    "content_type": chunk["content_type"],
                    "content": chunk["content"],
                    "math_formulas": chunk["math_formulas"],
                })

        chunks_path = output_dir / "chunks.json"
        chunks_path.write_text(
            json.dumps(all_chunks, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        logger.info(f"Saved {len(all_chunks)} chunks: {chunks_path}")

        # 5. Write processing summary
        summary = {
            "config": asdict(self.config),
            "stats": {
                "total_pages_processed": len(self.results),
                "total_chunks": len(all_chunks),
                "total_chars": sum(len(e["raw_markdown"]) for e in self.results),
                "total_math_formulas": sum(
                    len(e["math_formulas"]) for e in self.results
                ),
                "content_types": {},
            },
        }
        for chunk in all_chunks:
            ct = chunk["content_type"]
            summary["stats"]["content_types"][ct] = (
                summary["stats"]["content_types"].get(ct, 0) + 1
            )

        summary_path = output_dir / "summary.json"
        summary_path.write_text(
            json.dumps(summary, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        logger.info(f"Saved summary: {summary_path}")

        # 6. Optionally push to Hugging Face
        if self.config.push_to_hub:
            self._push_to_hub(all_chunks)

    def _push_to_hub(self, chunks: List[Dict[str, Any]]):
        """Push the structured dataset to Hugging Face Hub."""
        try:
            if self.config.hub_token:
                login(token=self.config.hub_token)
            else:
                token = os.getenv("HF_TOKEN")
                if token:
                    login(token=token)
                else:
                    logger.warning("No HF_TOKEN found, skipping push to Hub")
                    return

            # Convert to Hugging Face Dataset
            dataset = Dataset.from_list(chunks)
            dataset.push_to_hub(self.config.hub_dataset_name)
            logger.info(f"Pushed dataset to {self.config.hub_dataset_name}")

        except Exception as e:
            logger.error(f"Failed to push to Hub: {e}")


# ==============================================================================
# CELL 7: Run Pipeline
# ==============================================================================

if __name__ == "__main__":
    pipeline = M3allemPDFPipeline(config)
    results = pipeline.run()

    print(f"\n✅ Pipeline finished!")
    print(f"   Pages processed: {len(results)}")
    total_chunks = sum(len(r["chunks"]) for r in results)
    print(f"   Total chunks extracted: {total_chunks}")
    print(f"   Output directory: {config.pdf_output_dir}")
    print(f"\n📁 Key output files:")
    print(f"   - {config.pdf_output_dir}/pages/page_XX.md (per-page markdown)")
    print(f"   - {config.pdf_output_dir}/full_course.md (all pages combined)")
    print(f"   - {config.pdf_output_dir}/structured_data.json (full structured data)")
    print(f"   - {config.pdf_output_dir}/chunks.json (flattened chunked dataset)")
    print(f"   - {config.pdf_output_dir}/summary.json (processing summary)")
