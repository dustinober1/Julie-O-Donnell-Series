#!/usr/bin/env python3
"""Generate repeatable developmental metrics for the accepted Book 1 manuscript."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "books/book-01/ACCEPTED_MANUSCRIPT.yaml"
OUTPUT = ROOT / "artifacts/book1-developmental-analysis.md"


def accepted_paths() -> list[Path]:
    text = MANIFEST.read_text(encoding="utf-8")
    block = text.split("\nexcluded_from_canon:", 1)[0]
    paths = [
        ROOT / value
        for value in re.findall(
            r'^\s+(?:-\s+)?path:\s+"([^"]+)"\s*$',
            block,
            re.MULTILINE,
        )
    ]
    if len(paths) != 25:
        raise RuntimeError(f"expected 25 accepted prose files, found {len(paths)}")
    return paths


def paragraph_metrics(text: str) -> tuple[int, int, int]:
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", text) if part.strip()]
    prose = [part for part in paragraphs if not part.startswith("#")]
    one_sentence = 0
    very_short = 0
    for paragraph in prose:
        words = paragraph.split()
        if len(words) <= 7:
            very_short += 1
        sentence_marks = len(re.findall(r"[.!?](?:[”\"])?(?:\s|$)", paragraph))
        if sentence_marks <= 1:
            one_sentence += 1
    return len(prose), one_sentence, very_short


def main() -> None:
    paths = accepted_paths()
    rows: list[tuple[str, int, int, int, int, int, int]] = []
    total_words = 0
    total_paragraphs = 0
    total_one_sentence = 0
    total_very_short = 0
    total_not_fragments = 0
    total_proof_patterns = 0

    for path in paths:
        text = path.read_text(encoding="utf-8")
        words = len(text.split())
        paragraphs, one_sentence, very_short = paragraph_metrics(text)
        not_fragments = len(re.findall(r"(?m)^(?:Not|No)\s+[^\n.!?]{1,45}[.!?]?$", text))
        proof_patterns = len(
            re.findall(
                r"\b(?:That|It|This) (?:did not|does not|didn’t|doesn’t) prove\b|\bIt proved\b|\bThat proved\b",
                text,
                re.IGNORECASE,
            )
        )
        rows.append(
            (
                path.name,
                words,
                paragraphs,
                one_sentence,
                very_short,
                not_fragments,
                proof_patterns,
            )
        )
        total_words += words
        total_paragraphs += paragraphs
        total_one_sentence += one_sentence
        total_very_short += very_short
        total_not_fragments += not_fragments
        total_proof_patterns += proof_patterns

    lines = [
        "# Book 1 Developmental Analysis",
        "",
        "Generated from the accepted-manuscript inventory on the current branch.",
        "",
        f"- Accepted words: **{total_words:,}**",
        f"- Prose paragraphs: **{total_paragraphs:,}**",
        f"- One-sentence paragraphs: **{total_one_sentence:,}**",
        f"- Paragraphs of seven words or fewer: **{total_very_short:,}**",
        f"- Isolated `Not`/`No` fragments: **{total_not_fragments:,}**",
        f"- Explicit proof/limitation constructions: **{total_proof_patterns:,}**",
        "",
        "| File | Words | Prose paras | One-sentence | ≤7 words | Not/No fragments | Proof patterns |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in rows:
        lines.append(
            f"| {row[0]} | {row[1]:,} | {row[2]:,} | {row[3]:,} | {row[4]:,} | {row[5]:,} | {row[6]:,} |"
        )

    lines.extend(
        [
            "",
            "## Revision target",
            "",
            "- Final accepted words: **105,000–110,000**",
            "- Preserve short-paragraph intensity for countdowns, reversals, and emotional decisions.",
            "- Reduce repetitive short-paragraph and proof-ceiling density most aggressively in Chapters 13–23.",
            "",
        ]
    )
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print(OUTPUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
