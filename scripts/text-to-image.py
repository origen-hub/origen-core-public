#!/usr/bin/env python3
"""
Convert all ASCII diagram text files into PNG images.

Source:   docs/public/diagrams/*.txt
Output:   docs/public/images/<basename>.png

Usage:
    python scripts/text-to-image.py
"""

import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "docs" / "public" / "diagrams"
OUT_DIR = PROJECT_ROOT / "docs" / "public" / "images"

OUT_DIR.mkdir(parents=True, exist_ok=True)

FONT_CANDIDATES = [
    # Awdaita
    "resources/fonts/AdwaitaMono-Regular.ttf"
]


def load_font(size=14):
    for path in FONT_CANDIDATES:
        try:
            return ImageFont.truetype(path, size=size)
        except OSError:
            continue

    raise RuntimeError(
        "No suitable monospaced font found.\n"
        "Install one of:\n"
        "  • NotoSansMono\n"
        "  • DejaVuSansMono\n"
        "Or update FONT_CANDIDATES in scripts/text-to-image.py"
    )


FONT = load_font()
PADDING = 30


def render_text_to_image(text: str, out_path: Path):
    lines = text.splitlines() or [""]

    # measure size
    tmp = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    max_w = max(tmp.textlength(line, font=FONT) for line in lines)
    line_h = FONT.getbbox("Hg")[3] + 4
    h = line_h * len(lines)

    img = Image.new("RGB",
                    (int(max_w + PADDING * 2), int(h + PADDING * 2)),
                    "white")
    draw = ImageDraw.Draw(img)

    y = PADDING
    for line in lines:
        draw.text((PADDING, y), line, font=FONT, fill="black")
        y += line_h

    img.save(out_path, "PNG")


def main():
    files = sorted(SRC_DIR.glob("*.txt"))
    if not files:
        print(f"[text-to-image] No .txt files in {SRC_DIR}")
        return

    for f in files:
        out = OUT_DIR / (f.stem + ".png")
        text = f.read_text(encoding="utf-8", errors="replace")
        render_text_to_image(text, out)
        print(f"[text-to-image] generated {out.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
