"""Cat reviews its human — one-star deadpan review.

Entry for make.fun competition
u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990.

The program writes the entry text exactly, as a single line with no
trailing newline, to /output/entry.txt (or $OUTPUT_PATH when set).
"""

import os
from pathlib import Path

REVIEW_TEXT = (
    "One star. My human keeps stealing my warmest bed, "
    "then calls it a laptop and types on it for eight hours."
)


def main() -> None:
    output_path = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(REVIEW_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
