#!/usr/bin/env python3
"""Mark superseded Book 1 review reports as historical without deleting their audit value."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = (
    "books/book-01/control/12-cross-check-final-manuscript-vs-original-book-1-request.md",
    "books/book-01/control/13-book-1-continuity-and-retcon-watchlist.md",
    "books/book-01/control/18-book-1-continuity-and-retcon-watchlist.md",
    "books/book-01/control/21-book-1-continuity-and-retcon-watchlist.md",
    "books/book-01/control/25-book-1-continuity-retcon-watchlist.md",
    "books/book-01/control/26-book-1-final-publication-readiness-review.md",
    "books/book-01/control/28-book-1-continuity-and-retcon-watchlist.md",
    "books/book-01/control/29-book-1-final-continuity-pass.md",
    "books/book-01/control/30-book-1-prose-flow-pass.md",
    "books/book-01/control/31-book-1-final-publication-readiness-review.md",
)

BANNER = """> [!IMPORTANT]
> **HISTORICAL PRE-REVISION REPORT — SUPERSEDED JULY 18, 2026**
>
> This file documents an earlier manuscript state and is retained only for audit history. It must not be used to determine the current word count, continuity state, publication readiness, or controlling prose. The current source of truth is `books/book-01/ACCEPTED_MANUSCRIPT.yaml`; current status is summarized in `books/book-01/control/51-developmental-revision-summary.md` and verified in `artifacts/book1-final-verification.md`.

---

"""


def main() -> None:
    changed = 0
    for relative in FILES:
        path = ROOT / relative
        if not path.is_file():
            raise RuntimeError(f"missing historical control file: {relative}")
        text = path.read_text(encoding="utf-8")
        if "HISTORICAL PRE-REVISION REPORT" in text:
            continue
        path.write_text(BANNER + text, encoding="utf-8")
        print(relative)
        changed += 1
    print(f"marked {changed} pre-revision control reports historical")


if __name__ == "__main__":
    main()
