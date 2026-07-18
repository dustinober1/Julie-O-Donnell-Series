#!/usr/bin/env python3
"""Apply idempotent, reviewable editorial patches to the accepted Book 1 prose."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTER_DIR = ROOT / "books/book-01/manuscript/chapters"

META_REPLACEMENTS = {
    "The answer matched Chapter 11.": "The answer matched the earlier custody record.",
    "the scene card begun in Chapter 14": "the intake chronology begun at Hartwell",
    "the end of Chapter 21": "the close of the borrowed-identity comparison",
    "the Chapter 21 comparison": "the borrowed-identity comparison",
    "during Chapter 21": "during the borrowed-identity comparison",
    "the same restraint geometry in which Chapter 22 had ended": "the same restraint geometry preserved after the release comparison",
    "On July thirteenth": "On October thirteenth",
}


def replace_idempotent(text: str, old: str, new: str, label: str) -> str:
    if new in text:
        return text
    if old in text:
        return text.replace(old, new)
    raise RuntimeError(f"expected editorial anchor missing: {label}")


def normalize_manuscript(text: str) -> str:
    text = re.sub(r"(?m)^# Chapter (\d+) - ", r"# Chapter \1 — ", text)
    for old, new in META_REPLACEMENTS.items():
        text = text.replace(old, new)
    text = text.replace("`", "")
    text = re.sub(r"(?m)^ {1,3}(?=\S)", "", text)
    text = re.sub(r"(?m)[ \t]+$", "", text)
    return text


def revise_chapter_05(text: str) -> str:
    duplicate_pattern = re.compile(
        r"(15:41 Eastern Daylight Time\n\n)"
        r"Elias Thorne had built a message out of a thermostat.*?"
        r"The room’s steel door opened\.\n\n"
        r"Arthur Vance entered without knocking\.",
        re.DOTALL,
    )
    replacement = (
        "15:41 Eastern Daylight Time\n\n"
        "The maintenance message had already gone out through the thermostat: "
        "0088 / COMP-04 / CORE-01. The building bus had accepted it, the display had "
        "returned to sixty-seven degrees, and Elias Thorne now sat beneath the camera "
        "with the circuit board hidden behind his Apex badge, waiting to learn whether "
        "anyone had noticed before Vance did.\n\n"
        "Arthur Vance entered without knocking."
    )
    if replacement in text:
        pass
    elif duplicate_pattern.search(text):
        text = duplicate_pattern.sub(replacement, text, count=1)
    else:
        raise RuntimeError("Chapter 5 thermostat duplicate anchor missing")

    family_anchor = "The Argus source certification would transmit in forty-seven minutes."
    family_detail = (
        "His father expected him in Richmond by seven for a retirement dinner Elias had "
        "spent three weeks promising not to miss. The wrapped gift was still in his "
        "townhouse beside a card he had not finished."
    )
    family_insert = family_anchor + "\n\n" + family_detail
    text = replace_idempotent(text, family_anchor, family_insert, "Elias family stake")
    while family_detail + "\n\n" + family_detail in text:
        text = text.replace(family_detail + "\n\n" + family_detail, family_detail, 1)

    confession_old = """“Have you ever considered why systems like Argus exist?”

Elias almost laughed.

“I helped build it.”

“You helped build a component. I’m asking whether you understand the purpose.”

“To analyze threat data.”

“To reduce ambiguity.”

“Those aren’t the same thing.”

“They are to the people responsible for acting.”

Vance opened the folder and removed the confession Elias had refused to sign earlier. The blank signature line waited at the bottom.

“Commanders do not have the luxury of your distinctions,” Vance said. “They receive incomplete information under time pressure. They need a defensible course of action.”

“You gave them fictional data.”

“We gave the model a complete pattern.”

“You removed the synthetic labels.”

“We corrected a test-environment limitation.”

Elias stared at him.

Vance did not appear to realize he had admitted anything.

Or he knew Elias would never be allowed to repeat it.

“People will die,” Elias said.

“People die when governments miscalculate.”

“You are manufacturing the calculation.”

“I am ensuring the system reaches the correct strategic conclusion.”

“The correct conclusion according to whom?”

“According to people who understand consequences beyond a single software package.”"""
    confession_new = """“Have you ever considered why systems like Argus exist?”

Elias almost laughed. “I helped build it.”

“You helped build a component. Commanders receive incomplete information under time pressure. They need a defensible course of action.”

“You gave them fictional data.”

“The model received a source-correction object derived from validated threat patterns.”

“Without the synthetic labels.”

“The operational configuration is under review.”

“By the people who approved it.”

Vance opened the folder and removed the statement Elias had refused to sign. The blank signature line waited at the bottom.

“Your source-boundary objection does not establish that the strategic warning is false,” Vance said.

“It establishes that you made fiction admissible.”

“It establishes a dispute about provenance. Until an authorized review resolves it, I will not withdraw a warning that may be correct.”

“You are protecting the conclusion.”

“I am protecting the decision process from an engineer who believes authorship confers command authority.”"""
    text = replace_idempotent(text, confession_old, confession_new, "Vance first confession")

    motive_old = """“I know that Pakistan has exploited uncertainty along the Line of Control for decades. I know India has repeatedly asked for more reliable American intelligence integration. And I know a controlled demonstration of Argus’s value will save the program from people who would dismantle it because they are frightened by its capabilities.”

“Controlled?”

“Regional actors understand escalation.”

“Then why fabricate an attack?”

Vance picked up his coffee.

“Because institutions rarely correct themselves in response to hypothetical danger.”"""
    motive_new = """“I know Pakistan has exploited uncertainty along the Line of Control for decades. I know India asked for machine-readable warning integration after previous failures. And I know withdrawing a strategic assessment because its author disputes a source boundary would cripple the program during a possible real threat.”

“So you need the warning to be right.”

Vance picked up his coffee. “I need authorized people to decide whether it is wrong.”"""
    text = replace_idempotent(text, motive_old, motive_new, "Vance motive confession")
    return text


def revise_chapter_24(text: str) -> str:
    old = "At exactly 08:14:44 EDT / 17:44:44 IST, Julie lifted her left hand from the level."
    new = "Julie lifted her left hand from the level."
    return replace_idempotent(text, old, new, "final timestamp")


def main() -> None:
    paths = sorted(CHAPTER_DIR.glob("chapter-*.md"))
    if len(paths) != 24:
        raise RuntimeError(f"expected 24 chapter files, found {len(paths)}")

    changed: list[str] = []
    for path in paths:
        original = path.read_text(encoding="utf-8")
        revised = normalize_manuscript(original)
        if path.name == "chapter-05.md":
            revised = revise_chapter_05(revised)
        if path.name == "chapter-24.md":
            revised = revise_chapter_24(revised)
        if revised != original:
            path.write_text(revised, encoding="utf-8")
            changed.append(str(path.relative_to(ROOT)))

    print("Changed files:")
    for path in changed:
        print(f"- {path}")


if __name__ == "__main__":
    main()
