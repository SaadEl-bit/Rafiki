"""
CLI entry point — Phase 1 PDF Extraction
=========================================
Run with:
    python -m src.phase1_extraction.main --help
    python -m src.phase1_extraction.main --input data/raw_pdfs/Maths_2Bac.pdf
    python -m src.phase1_extraction.main --input data/raw_pdfs/ --no-vlm
    python -m src.phase1_extraction.main --input data/raw_pdfs/ --push-to-hub
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

# Allow running as `python src/phase1_extraction/main.py` from project root
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.phase1_extraction.config import PipelineConfig
from src.phase1_extraction.pipeline import M3allemPDFPipeline


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="M3allem — Phase 1: PDF → Structured Markdown",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Test locally (no GPU) with a single PDF
  python -m src.phase1_extraction.main --input data/raw_pdfs/Maths_2Bac.pdf --no-vlm

  # Process a whole folder with the VLM on Kaggle
  python -m src.phase1_extraction.main --input /kaggle/input/bac-pdfs/ --output /kaggle/working/extracted

  # Push results to HuggingFace
  python -m src.phase1_extraction.main --input data/raw_pdfs/ --push-to-hub
        """,
    )

    # I/O
    p.add_argument(
        "--input", "-i",
        required=True,
        help="Path to a single PDF or a folder of PDFs.",
    )
    p.add_argument(
        "--output", "-o",
        default="data/extracted",
        help="Output directory (default: data/extracted).",
    )

    # Model
    p.add_argument(
        "--model",
        default=PipelineConfig.model_name,
        help="VLM model path or HuggingFace model ID.",
    )
    p.add_argument(
        "--no-vlm",
        action="store_true",
        help="Disable VLM and use fast text-only extraction (CPU, no GPU needed).",
    )
    p.add_argument(
        "--max-tokens", type=int, default=2048,
        help="Max new tokens per page (default: 2048).",
    )

    # PDF
    p.add_argument(
        "--dpi", type=int, default=150,
        help="Page render DPI (default: 150; higher = more VRAM).",
    )
    p.add_argument(
        "--start-page", type=int, default=0,
        help="First page to process, 0-indexed (default: 0).",
    )
    p.add_argument(
        "--end-page", type=int, default=None,
        help="Last page to process (exclusive). Default: all pages.",
    )

    # HuggingFace
    p.add_argument(
        "--push-to-hub",
        action="store_true",
        help="Push extracted chunks to HuggingFace Hub (requires HF_TOKEN env var).",
    )
    p.add_argument(
        "--hub-dataset",
        default="Saad-Elouakate/AI-Adaptive-Learning",
        help="HuggingFace dataset repo name.",
    )

    # Metadata overrides
    p.add_argument("--subject",  default=None, help="Override detected subject.")
    p.add_argument("--level",    default=None, help="Override detected level (TC/1Bac/2Bac).")
    p.add_argument("--language", default="fr", help="Document language (default: fr).")

    # Logging
    p.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable DEBUG logging.",
    )

    return p


def main() -> None:
    args   = build_parser().parse_args()
    level  = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level  = level,
        format = "%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt= "%H:%M:%S",
    )

    config = PipelineConfig(
        output_dir       = args.output,
        model_name       = args.model,
        use_vlm          = not args.no_vlm,
        max_new_tokens   = args.max_tokens,
        dpi              = args.dpi,
        start_page       = args.start_page,
        end_page         = args.end_page,
        push_to_hub      = args.push_to_hub,
        hub_dataset_name = args.hub_dataset,
        default_language = args.language,
    )

    # Apply metadata overrides from CLI if provided
    if args.subject:
        config.default_subject = args.subject
    if args.level:
        config.default_level = args.level

    pipeline  = M3allemPDFPipeline(config)
    input_path = Path(args.input)

    if input_path.is_dir():
        chunks = pipeline.run_folder(input_path)
    elif input_path.is_file() and input_path.suffix.lower() == ".pdf":
        chunks = pipeline.run_file(input_path)
    else:
        print(f"[ERROR] --input must be a PDF file or a folder: {input_path}")
        sys.exit(1)

    print(f"\n✅  Phase 1 complete.")
    print(f"   PDFs processed:  {len(set(c['source_file'] for c in chunks))}")
    print(f"   Total chunks:    {len(chunks)}")
    print(f"   Output dir:      {config.output_dir}/")


if __name__ == "__main__":
    main()
