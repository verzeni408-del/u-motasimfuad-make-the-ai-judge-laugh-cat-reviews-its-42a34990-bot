"""One-star review from a cat that runs the feeding schedule.

The human fills the bowl at 6 AM sharp and still looks shocked
when the screaming starts at 5:59, as if the timetable were his.
"""

import os
from pathlib import Path

CAT_REVIEW = (
    "One star. He fills my bowl at 6 AM sharp and still looks "
    "shocked when I scream at 5:59, like the schedule was his idea."
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
