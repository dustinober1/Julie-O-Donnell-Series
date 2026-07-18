#!/usr/bin/env python3
"""Audit one-sentence paragraphs in the accepted Book 1 manuscript.

The audit distinguishes dialogue from narrative and flags only paragraphs that
remain plausible rhythm problems after the publication-rhythm pass. It does not
modify manuscript prose.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from reflow_book1_publication_rhythm import (
    ROOT,
    accepted_paths,
    intentional,
    kind,
    sentence_count,
    split_paragraphs,
    word_count,
)

OUTPUT = ROOT / "artifacts/book1-one-sentence-paragraph-audit.md"

ROUTINE_BEAT_RE = re.compile(
    r"^(?:(?:Julie|Marcus|Elias|Sarah|Sharma|Mercer|Vance|Bell|Hackett|Qureshi|Grant|Alvarez|Ortiz|Vega)|"
    r"(?:He|She|They|The\s+[A-Za-z'-]+))\s+"
    r"(?:looked|watched|turned|nodded|stopped|paused|hesitated|waited|stood|sat|moved|crossed|checked|"
    r"glanced|continued|followed|returned|reached|pulled|opened|closed|read|listened|remained|shifted|"
    r"exhaled|studied|leaned|stepped|walked|rose|lowered|lifted|caught|held|released|said nothing|did not answer)\b",
    re.IGNORECASE,
)


@dataclass
class Candidate:
    paragraph_number: int
    words: int
    reason: str
    text: str


@dataclass
class FileAudit:
    name: str
    narrative_paragraphs: int = 0
    narrative_one_sentence: int = 0
    narrative_one_sentence_le7: int = 0
    dialogue_paragraphs: int = 0
    dialogue_one_sentence: int = 0
    intentional_emphasis: int = 0
    scene_boundary: int = 0
    dialogue_adjacent: int = 0
    display_adjacent: int = 0
    interior_one_sentence: int = 0
    routine_candidates: int = 0
    review_candidates: list[Candidate] = field(default_factory=list)
    clusters: list[list[int]] = field(default_factory=list)
    length_bands: dict[str, int] = field(
        default_factory=lambda: {"1-7": 0, "8-15": 0, "16-30": 0, "31+": 0}
    )


def length_band(words: int) -> str:
    if words <= 7:
        return "1-7"
    if words <= 15:
        return "8-15"
    if words <= 30:
        return "16-30"
    return "31+"


def audit_file(path: Path) -> FileAudit:
    text = path.read_text(encoding="utf-8")
    paragraphs = split_paragraphs(text)
    kinds = [kind(paragraph) for paragraph in paragraphs]
    audit = FileAudit(name=path.name)
    one_sentence_narrative_indices: set[int] = set()

    for index, paragraph in enumerate(paragraphs):
        paragraph_kind = kinds[index]
        if paragraph_kind == "dialogue":
            audit.dialogue_paragraphs += 1
            if sentence_count(paragraph) == 1:
                audit.dialogue_one_sentence += 1
            continue
        if paragraph_kind != "narrative":
            continue

        audit.narrative_paragraphs += 1
        if sentence_count(paragraph) != 1:
            continue

        one_sentence_narrative_indices.add(index)
        audit.narrative_one_sentence += 1
        words = word_count(paragraph)
        audit.length_bands[length_band(words)] += 1
        if words <= 7:
            audit.narrative_one_sentence_le7 += 1

        previous_kind = kinds[index - 1] if index > 0 else None
        next_kind = kinds[index + 1] if index + 1 < len(kinds) else None
        is_intentional = intentional(paragraph)
        is_scene_open = index == 0 or previous_kind == "meta"
        is_scene_close = index == len(paragraphs) - 1 or next_kind == "meta"
        is_scene_boundary = is_scene_open or is_scene_close
        is_dialogue_adjacent = previous_kind == "dialogue" or next_kind == "dialogue"
        is_display_adjacent = previous_kind == "display" or next_kind == "display"
        is_interior = not is_intentional and not is_scene_boundary
        is_routine = bool(ROUTINE_BEAT_RE.search(paragraph.strip())) and words <= 15

        if is_intentional:
            audit.intentional_emphasis += 1
        if is_scene_boundary:
            audit.scene_boundary += 1
        if is_dialogue_adjacent:
            audit.dialogue_adjacent += 1
        if is_display_adjacent:
            audit.display_adjacent += 1
        if is_interior:
            audit.interior_one_sentence += 1
        if is_routine:
            audit.routine_candidates += 1

        reasons: list[str] = []
        if not is_intentional and not is_scene_boundary:
            if words <= 4:
                reasons.append("very short interior beat")
            if is_routine:
                reasons.append("routine action/reaction beat")
            if words <= 8 and not is_dialogue_adjacent and not is_display_adjacent:
                reasons.append("short isolated narrative beat")

        if reasons:
            audit.review_candidates.append(
                Candidate(
                    paragraph_number=index + 1,
                    words=words,
                    reason="; ".join(dict.fromkeys(reasons)),
                    text=" ".join(paragraph.split()),
                )
            )

    current: list[int] = []
    for index in range(len(paragraphs)):
        if index in one_sentence_narrative_indices:
            current.append(index + 1)
            continue
        if len(current) >= 2:
            audit.clusters.append(current)
        current = []
    if len(current) >= 2:
        audit.clusters.append(current)

    return audit


def pct(numerator: int, denominator: int) -> str:
    return f"{numerator / denominator:.1%}" if denominator else "0.0%"


def main() -> None:
    paths = accepted_paths()
    audits = [audit_file(path) for path in paths]

    total_narrative = sum(item.narrative_paragraphs for item in audits)
    total_narrative_one = sum(item.narrative_one_sentence for item in audits)
    total_narrative_le7 = sum(item.narrative_one_sentence_le7 for item in audits)
    total_dialogue = sum(item.dialogue_paragraphs for item in audits)
    total_dialogue_one = sum(item.dialogue_one_sentence for item in audits)
    total_intentional = sum(item.intentional_emphasis for item in audits)
    total_scene_boundary = sum(item.scene_boundary for item in audits)
    total_dialogue_adjacent = sum(item.dialogue_adjacent for item in audits)
    total_display_adjacent = sum(item.display_adjacent for item in audits)
    total_interior = sum(item.interior_one_sentence for item in audits)
    total_routine = sum(item.routine_candidates for item in audits)
    total_candidates = sum(len(item.review_candidates) for item in audits)
    total_clusters = sum(len(item.clusters) for item in audits)
    total_words = sum(len(path.read_text(encoding="utf-8").split()) for path in paths)
    bands = {
        label: sum(item.length_bands[label] for item in audits)
        for label in ("1-7", "8-15", "16-30", "31+")
    }

    candidate_rate = total_candidates / total_narrative if total_narrative else 0.0
    if candidate_rate <= 0.03:
        verdict = "The remaining one-sentence narrative paragraphs are largely controlled; only a light targeted pass is warranted."
    elif candidate_rate <= 0.07:
        verdict = "The manuscript still has a noticeable but localized one-sentence-paragraph habit; a targeted pass is warranted."
    else:
        verdict = "The one-sentence-paragraph habit remains broad enough to justify another manuscript-wide rhythm pass."

    lines = [
        "# Book 1 One-Sentence Paragraph Audit",
        "",
        "Generated from the accepted-manuscript inventory on the current rhythm-repair branch.",
        "",
        "## Verdict",
        "",
        verdict,
        "",
        "## Manuscript totals",
        "",
        f"- Accepted words: **{total_words:,}**.",
        f"- Narrative paragraphs: **{total_narrative:,}**.",
        f"- One-sentence narrative paragraphs: **{total_narrative_one:,}** ({pct(total_narrative_one, total_narrative)} of narrative paragraphs).",
        f"- One-sentence narrative paragraphs of seven words or fewer: **{total_narrative_le7:,}**.",
        f"- Dialogue paragraphs: **{total_dialogue:,}**; one-sentence dialogue paragraphs: **{total_dialogue_one:,}** ({pct(total_dialogue_one, total_dialogue)}).",
        f"- Deliberately protected emphasis lines: **{total_intentional:,}**.",
        f"- Scene-opening or scene-closing one-sentence paragraphs: **{total_scene_boundary:,}**.",
        f"- Dialogue-adjacent one-sentence narrative beats: **{total_dialogue_adjacent:,}**.",
        f"- Display-adjacent one-sentence narrative beats: **{total_display_adjacent:,}**.",
        f"- Interior one-sentence narrative paragraphs: **{total_interior:,}**.",
        f"- Routine action/reaction beats under the audit heuristic: **{total_routine:,}**.",
        f"- Paragraphs requiring human review under the strict candidate rules: **{total_candidates:,}** ({pct(total_candidates, total_narrative)} of narrative paragraphs).",
        f"- Consecutive one-sentence narrative clusters: **{total_clusters:,}**.",
        "",
        "## Length distribution",
        "",
        "| Words in one-sentence narrative paragraph | Count | Share |",
        "| --- | ---: | ---: |",
    ]
    for label in ("1-7", "8-15", "16-30", "31+"):
        lines.append(f"| {label} | {bands[label]:,} | {pct(bands[label], total_narrative_one)} |")

    lines.extend(
        [
            "",
            "## Per-file concentration",
            "",
            "| File | Narrative paras | One-sentence | Rate | ≤7 words | Interior | Routine candidates | Review candidates | Clusters |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for item in audits:
        lines.append(
            f"| {item.name} | {item.narrative_paragraphs:,} | {item.narrative_one_sentence:,} | "
            f"{pct(item.narrative_one_sentence, item.narrative_paragraphs)} | {item.narrative_one_sentence_le7:,} | "
            f"{item.interior_one_sentence:,} | {item.routine_candidates:,} | {len(item.review_candidates):,} | {len(item.clusters):,} |"
        )

    ranked = sorted(
        audits,
        key=lambda item: (len(item.review_candidates), item.narrative_one_sentence),
        reverse=True,
    )
    lines.extend(["", "## Highest-priority chapters", ""])
    for item in ranked[:8]:
        lines.append(
            f"- **{item.name}** — {len(item.review_candidates)} review candidates; "
            f"{item.narrative_one_sentence} one-sentence narrative paragraphs; {len(item.clusters)} clusters."
        )

    lines.extend(["", "## Review candidates", ""])
    for item in audits:
        if not item.review_candidates:
            continue
        lines.append(f"### {item.name}")
        lines.append("")
        for candidate in item.review_candidates[:12]:
            excerpt = candidate.text
            if len(excerpt) > 180:
                excerpt = excerpt[:177].rstrip() + "..."
            lines.append(
                f"- Paragraph {candidate.paragraph_number}, {candidate.words} words — "
                f"{candidate.reason}: “{excerpt}”"
            )
        if len(item.review_candidates) > 12:
            lines.append(f"- …and {len(item.review_candidates) - 12} additional candidates in this file.")
        lines.append("")

    lines.extend(
        [
            "## Interpretation rules",
            "",
            "- Dialogue is reported separately because a one-sentence spoken response is normal and should not be treated as a prose defect.",
            "- Scene openings, scene endings, protected motifs, countdowns, and system-display handoffs may legitimately use isolated sentences.",
            "- A review candidate is not automatically wrong. It is a paragraph whose brevity, placement, or routine action verb makes it worth a human cadence decision.",
            "- No manuscript prose was changed by this audit.",
            "",
        ]
    )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print(OUTPUT.relative_to(ROOT))
    print(f"one-sentence narrative paragraphs: {total_narrative_one}/{total_narrative} ({pct(total_narrative_one, total_narrative)})")
    print(f"strict review candidates: {total_candidates}")
    print(f"clusters: {total_clusters}")


if __name__ == "__main__":
    main()
