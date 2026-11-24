"""One-star review from a cat that has never once been let through
a door at the right moment.

Entry for the make.fun competition
u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990.

Running this program writes the review to /output/entry.txt
(or $OUTPUT_PATH when set): exactly one line, no trailing newline.
"""

import os
from pathlib import Path

CAT_REVIEW = (
    "One star. She opens the door, watches me stare at it, "
    "then closes it again. Four years in this house and I still "
    "have no idea what is on the other side."
)


def write_review() -> Path:
    out = Path(os.getenv("OUTPUT_PATH") or "/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(CAT_REVIEW, encoding="utf-8")
    return out


def main() -> None:
    write_review()


if __name__ == "__main__":
    main()
