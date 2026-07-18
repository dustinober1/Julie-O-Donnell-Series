#!/usr/bin/env python3
"""Add a final bounded consequence passage to clear the 105k publication target."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "books/book-01/manuscript/chapters/chapter-08.md"
MARKER = "INITIAL RELEASE SUSPENSION ACHIEVED USING OVERBROAD DEPENDENCY BOUNDARY."
ANCHOR = """Julie compared the source time with the enclave clock. “Almost four minutes. Forty-three seconds of that belongs to my first boundary.”

“And distance?”"""
REPLACEMENT = """Julie compared the source time with the enclave clock. “Almost four minutes. Forty-three seconds of that belongs to my first boundary.”

Elias looked at her instead of the route. “The recovery record already shows why you chose the lineage scope.”

“It also shows what the scope deferred.”

“We can describe the delay as a property of the poisoned dependency structure.”

“It was. I still selected it.”

Julie opened the supplemental warning field. The enclave offered to attach the K-17 result as an ordinary post-reconciliation discovery. That wording would preserve the source and hide the fact that her first decision had kept it unavailable for forty-three seconds.

She replaced it.

INITIAL RELEASE SUSPENSION ACHIEVED USING OVERBROAD DEPENDENCY BOUNDARY.
FOURTEEN CORRECTION-DEPENDENT OBSERVATION REFERENCES DEFERRED.
SUPPLEMENTAL REVIEW RESTORED LOW-LEVEL MOVEMENT TOWARD K-17.
ADDITIONAL DELAY ATTRIBUTABLE TO ANALYTIC SCOPE: 43 SECONDS.
FIELD PRESENCE, IDENTITY, AND OBJECTIVE: UNCONFIRMED.

The console required separate signatures for the factual source recovery and the analytic limitation. Elias authenticated only that the fourteen event references came from the correction-dependent table, that their primary blocks remained unchanged, and that the supplemental process had restored them in source order. Julie authenticated the boundary choice and delay. Marcus added no command conclusion.

The warning would not present Julie as the analyst who had found every distinction in time. It would present the sequence in which she had stopped the larger lie, missed a smaller truth inside its machinery, and corrected the miss before anyone could make her first result final.

“Send the supplemental result to the preserved incident route,” she said. “Do not merge it into the original recovery record.”

Elias selected a linked addendum. “The first record remains complete. The correction travels beside it.”

That was the only version Julie could defend: not a perfect decision repaired in memory, but two authenticated acts whose order survived.

“And distance?”"""


def main() -> None:
    text = PATH.read_text(encoding="utf-8")
    if MARKER in text:
        return
    if ANCHOR not in text:
        raise RuntimeError("Chapter 8 floor anchor missing")
    PATH.write_text(text.replace(ANCHOR, REPLACEMENT, 1), encoding="utf-8")
    print(PATH.relative_to(ROOT))


if __name__ == "__main__":
    main()
