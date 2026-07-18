#!/usr/bin/env python3
"""Generate repeatable late-act compression and prose-pattern diagnostics."""
from __future__ import annotations

import collections
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "books/book-01/ACCEPTED_MANUSCRIPT.yaml"
OUTPUT = ROOT / "artifacts/book1-publication-style-audit.md"

ENTRY_RE = re.compile(r'^[ \t]*-[ \t]+path:[ \t]*"([^"]+)"[ \t]*$', re.MULTILINE)
SENTENCE_RE = re.compile(r"(?<=[.!?])(?:[”\"])?\s+")

PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("does-not-prove", re.compile(r"\b(?:does|did) not prove\b", re.IGNORECASE)),
    ("not-established", re.compile(r"\bnot established\b", re.IGNORECASE)),
    ("registered-authority", re.compile(r"\bregistered authority\b", re.IGNORECASE)),
    ("physical-possession", re.compile(r"\bphysical possession\b", re.IGNORECASE)),
    ("physical-custody", re.compile(r"\bphysical custody\b", re.IGNORECASE)),
    ("named-receiver", re.compile(r"\bnamed (?:federal )?(?:receiver|receiving authority|custodian)\b", re.IGNORECASE)),
    ("preservation-not-production", re.compile(r"\bpreservation is not production\b", re.IGNORECASE)),
    ("source-limited", re.compile(r"\bsource-limited\b", re.IGNORECASE)),
    ("seven-packages", re.compile(r"\bseven packages\b", re.IGNORECASE)),
    ("136-47-311", re.compile(r"136|one hundred thirty-six|47|forty-seven|311|three hundred eleven", re.IGNORECASE)),
    ("visible-hands", re.compile(r"\bhands? (?:visible|where .* can see)\b", re.IGNORECASE)),
    ("fixed-camera", re.compile(r"\bfixed camera\b", re.IGNORECASE)),
    ("clock-proof", re.compile(r"\bclock (?:basis|source|offset)\b", re.IGNORECASE)),
)


def accepted_paths() -> list[Path]:
    text = MANIFEST.read_text(encoding="utf-8")
    block = text.split("\nexcluded_from_canon:", 1)[0]
    paths = [ROOT / value for value in ENTRY_RE.findall(block)]
    if len(paths) != 25:
        raise RuntimeError(f"expected 25 accepted prose files, found {len(paths)}")
    return paths


def paragraph_metrics(text: str) -> tuple[int, int, int]:
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", text) if part.strip()]
    prose = [part for part in paragraphs if not part.startswith("#")]
    one_sentence = 0
    short = 0
    for paragraph in prose:
        words = paragraph.split()
        if len(words) <= 7:
            short += 1
        sentence_marks = len(re.findall(r"[.!?](?:[”\"])?(?:\s|$)", paragraph))
        if sentence_marks <= 1:
            one_sentence += 1
    return len(prose), one_sentence, short


def normalized_sentences(text: str) -> list[str]:
    prose = re.sub(r"(?m)^#.*$", "", text)
    sentences = SENTENCE_RE.split(prose)
    normalized: list[str] = []
    for sentence in sentences:
        value = re.sub(r"\s+", " ", sentence).strip().lower()
        words = value.split()
        if 8 <= len(words) <= 40 and not value.isupper():
            normalized.append(value)
    return normalized


def main() -> None:
    paths = accepted_paths()
    late_paths = [
        path
        for path in paths
        if path.name.startswith("chapter-")
        and 15 <= int(path.stem.split("-")[-1]) <= 23
    ]

    rows: list[tuple[str, int, int, int, dict[str, int]]] = []
    sentence_counts: collections.Counter[str] = collections.Counter()
    totals: collections.Counter[str] = collections.Counter()

    for path in late_paths:
        text = path.read_text(encoding="utf-8")
        paragraphs, one_sentence, short = paragraph_metrics(text)
        counts = {name: len(pattern.findall(text)) for name, pattern in PATTERNS}
        totals.update(counts)
        sentence_counts.update(normalized_sentences(text))
        rows.append((path.name, paragraphs, one_sentence, short, counts))

    repeated = [
        (sentence, count)
        for sentence, count in sentence_counts.most_common()
        if count >= 2
    ][:30]

    lines = [
        "# Book 1 Publication-Style Audit",
        "",
        "Generated from accepted Chapters 15–23. This is a diagnostic, not an instruction to delete every flagged construction.",
        "",
        "## Late-act paragraph density",
        "",
        "| File | Prose paragraphs | One-sentence | ≤7 words | Proof/authority pattern total |",
        "|---|---:|---:|---:|---:|",
    ]
    for filename, paragraphs, one_sentence, short, counts in rows:
        lines.append(
            f"| {filename} | {paragraphs:,} | {one_sentence:,} | {short:,} | {sum(counts.values()):,} |"
        )

    lines.extend(
        [
            "",
            "## Pattern totals",
            "",
            "| Pattern | Count | Editorial use |",
            "|---|---:|---|",
        ]
    )
    editorial_use = {
        "does-not-prove": "Keep first dramatic demonstrations; compress reminders after the proof ceiling is established.",
        "not-established": "Necessary in findings; vary prose outside formal findings.",
        "registered-authority": "Preserve distinction, reduce repeated full explanation.",
        "physical-possession": "Preserve distinction, especially for Vance, Tariq, and Sterling.",
        "physical-custody": "Retain at transfers; compress stable-state repetition.",
        "named-receiver": "Retain at first MPD/DCIS conflict; shorten later recitals.",
        "preservation-not-production": "Retain as a governing legal principle; avoid multiple identical explanations.",
        "source-limited": "Prefer exact source descriptions over repeated label when possible.",
        "seven-packages": "Full list once at scene handoff and once at common intake; use `the seven packages` afterward.",
        "136-47-311": "Full counts at capture, verification, and formal inventory; avoid routine repetition after stable custody.",
        "visible-hands": "Establish scene geometry once per new authority; trim repeated body-position reminders.",
        "fixed-camera": "Establish recording architecture once per location unless camera state changes.",
        "clock-proof": "Retain when source clocks differ; compress routine restatement.",
    }
    for name, _pattern in PATTERNS:
        lines.append(f"| {name} | {totals[name]:,} | {editorial_use[name]} |")

    lines.extend(["", "## Repeated normalized sentences", ""])
    if repeated:
        for sentence, count in repeated:
            lines.append(f"- **{count}×** {sentence}")
    else:
        lines.append("- No repeated normalized sentence of 8–40 words appeared more than once.")

    lines.extend(
        [
            "",
            "## Editing gate",
            "",
            "- Do not compress technical or legal passages until the corresponding specialist review is complete.",
            "- Preserve the first full dramatic demonstration of every proof ceiling.",
            "- Preserve MPD handoff, board examination, K-17 local record, Hartwell production, LSS custody exception, Price comparison, construction/release split, Vance release, and aborted public overclaim.",
            "- Regenerate the accepted manifest after any prose edit.",
            "",
        ]
    )
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print(OUTPUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
