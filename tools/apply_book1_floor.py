#!/usr/bin/env python3
"""Add the final reviewer-requested Sharma depth and clear the Book 1 word floor."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "books/book-01/manuscript/chapters/chapter-18.md"
MARKER = "Her caution had a name before it became doctrine."
ANCHOR = """The medical officer ended the visit.

K-17 had not been taken."""
ADDITION = """The medical officer ended the visit.

Sharma remained outside the aid room after the door closed. In her first winter on the ridge, she had signed a patrol summary that called a missing soldier presumed swept into a ravine. The weather supported it; the search dogs did not. Three days later he was found alive in an abandoned shepherd shelter two kilometers east, frostbitten and furious that headquarters had converted a likely route into his death. His mother had received the provisional notice before the search team reached him.

Sharma had never forgotten the woman’s question at the hospital: Who decided likely meant finished?

Her caution had a name before it became doctrine.

Since then, every clean map carried the sound of that question. It had cost Sharma promotions, invitations to planning cells, and the easy reputation of an officer who never slowed a decision. It had also kept her from sending Pal’s injury ahead of him as proof of a story he had not told.

She returned to operations only after the aid-room door latched behind her.

K-17 had not been taken."""
EXPECTED_ADDED_WORDS = 172


def main() -> None:
    text = PATH.read_text(encoding="utf-8")
    if MARKER in text:
        return
    if ANCHOR not in text:
        raise RuntimeError("Chapter 18 Sharma-depth anchor missing")
    added_words = len(ADDITION.split()) - len(ANCHOR.split())
    if added_words != EXPECTED_ADDED_WORDS:
        raise RuntimeError(
            f"reviewer floor passage adds {added_words} words, expected {EXPECTED_ADDED_WORDS}"
        )
    PATH.write_text(text.replace(ANCHOR, ADDITION, 1), encoding="utf-8")
    print(PATH.relative_to(ROOT))


if __name__ == "__main__":
    main()
