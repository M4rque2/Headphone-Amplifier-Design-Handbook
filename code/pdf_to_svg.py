#!/usr/bin/env python3
"""Convert all PDFs in ./pdf to SVGs in ./svg with matching base names.

Default behavior:
- Input folder: ./pdf
- Output folder: ./svg
- Output file name: same as PDF, but with .svg extension

The script tries available converters in this order:
1) PyMuPDF (pure Python, recommended)
2) inkscape
3) pdftocairo

Notes:
- This script targets simple schematic PDFs (usually single-page).
- For multi-page PDFs, tools may export only the first page when keeping one output name.
- With PyMuPDF, output is auto-trimmed to content bounds (plus a small margin).
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:
    fitz = None


def run_cmd(cmd: list[str]) -> tuple[bool, str]:
    try:
        completed = subprocess.run(
            cmd,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        return True, completed.stdout.strip()
    except subprocess.CalledProcessError as exc:
        err = (exc.stderr or exc.stdout or "").strip()
        return False, err
    except FileNotFoundError as exc:
        return False, str(exc)


def compute_content_bbox(page: "fitz.Page") -> "fitz.Rect | None":
    """Estimate visible content bounds from vector paths and text/image blocks."""
    rects: list[fitz.Rect] = []

    for drawing in page.get_drawings():
        rect = drawing.get("rect")
        if rect is not None:
            rects.append(fitz.Rect(rect))

    text_dict = page.get_text("dict")
    for block in text_dict.get("blocks", []):
        bbox = block.get("bbox")
        if bbox is not None:
            rects.append(fitz.Rect(bbox))

    if not rects:
        return None

    union = fitz.Rect(rects[0])
    for rect in rects[1:]:
        union |= rect
    return union


def convert_with_pymupdf(
    src_pdf: Path, dst_svg: Path, trim_margin_pt: float = 12.0
) -> tuple[bool, str]:
    """Convert first page of PDF to SVG using PyMuPDF."""
    if fitz is None:
        return False, "PyMuPDF is not installed. Install with: pip install pymupdf"

    try:
        doc = fitz.open(str(src_pdf))
        if len(doc) == 0:
            return False, "PDF has no pages"

        page = doc[0]
        content_bbox = compute_content_bbox(page)
        if content_bbox is not None:
            # Add a safety margin to avoid clipping thin strokes at the edges.
            margin = max(0.0, float(trim_margin_pt))
            crop = fitz.Rect(
                content_bbox.x0 - margin,
                content_bbox.y0 - margin,
                content_bbox.x1 + margin,
                content_bbox.y1 + margin,
            )
            crop &= page.rect
            if crop.width > 0 and crop.height > 0:
                page.set_cropbox(crop)

        svg_text = page.get_svg_image()
        dst_svg.write_text(svg_text, encoding="utf-8")
        doc.close()
        return True, ""
    except Exception as exc:
        return False, str(exc)


def convert_with_inkscape(src_pdf: Path, dst_svg: Path) -> tuple[bool, str]:
    return run_cmd(
        [
            "inkscape",
            str(src_pdf),
            "--export-type=svg",
            f"--export-filename={dst_svg}",
        ]
    )


def convert_with_pdftocairo(src_pdf: Path, dst_svg: Path) -> tuple[bool, str]:
    # pdftocairo needs an output prefix (without extension) with -singlefile.
    out_prefix = dst_svg.with_suffix("")
    return run_cmd(
        ["pdftocairo", "-svg", "-singlefile", str(src_pdf), str(out_prefix)]
    )


def pick_converter() -> tuple[str, callable] | None:
    candidates = [
        ("pymupdf", convert_with_pymupdf),
        ("inkscape", convert_with_inkscape),
        ("pdftocairo", convert_with_pdftocairo),
    ]
    for name, func in candidates:
        if name == "pymupdf":
            if fitz is not None:
                return name, func
            continue
        if shutil.which(name):
            return name, func
    return None


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Convert PDFs to SVGs while keeping file base names."
    )
    parser.add_argument(
        "--input",
        default="./pdf",
        help="Input folder containing PDF files (default: ./pdf)",
    )
    parser.add_argument(
        "--output",
        default="./svg",
        help="Output folder for SVG files (default: ./svg)",
    )
    parser.add_argument(
        "--trim-margin",
        type=float,
        default=12.0,
        help="Trim margin in PDF points when using PyMuPDF (default: 12.0)",
    )
    args = parser.parse_args()

    in_dir = Path(args.input).resolve()
    out_dir = Path(args.output).resolve()

    if not in_dir.exists() or not in_dir.is_dir():
        print(f"Input folder not found: {in_dir}", file=sys.stderr)
        return 1

    pdf_files = sorted(in_dir.glob("*.pdf"))
    if not pdf_files:
        print(f"No PDF files found in: {in_dir}")
        return 0

    out_dir.mkdir(parents=True, exist_ok=True)

    converter = pick_converter()
    if converter is None:
        print(
            "No supported converter found. Install PyMuPDF (pip install pymupdf) or install inkscape/pdftocairo.",
            file=sys.stderr,
        )
        return 2

    converter_name, converter_func = converter
    print(f"Using converter: {converter_name}")

    ok_count = 0
    fail_count = 0

    for pdf in pdf_files:
        svg = out_dir / (pdf.stem + ".svg")
        if converter_name == "pymupdf":
            ok, msg = converter_func(pdf, svg, args.trim_margin)
        else:
            ok, msg = converter_func(pdf, svg)
        if ok and svg.exists():
            ok_count += 1
            print(f"[OK]   {pdf.name} -> {svg.name}")
        else:
            fail_count += 1
            print(f"[FAIL] {pdf.name}", file=sys.stderr)
            if msg:
                print(f"       {msg}", file=sys.stderr)

    print(f"Done. Success: {ok_count}, Failed: {fail_count}")
    return 0 if fail_count == 0 else 3


if __name__ == "__main__":
    raise SystemExit(main())
