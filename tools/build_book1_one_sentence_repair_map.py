#!/usr/bin/env python3
"""Build the explicit reviewed repair map for Book 1 one-sentence paragraphs."""
from __future__ import annotations

import json
import re
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

OUTPUT = ROOT / "books/book-01/control/52-one-sentence-repair-map.json"

ROUTINE_BEAT_RE = re.compile(
    r"^(?:(?:Julie|Marcus|Elias|Sarah|Sharma|Mercer|Vance|Bell|Hackett|Qureshi|Grant|Alvarez|Ortiz|Vega)|"
    r"(?:He|She|They|The\s+[A-Za-z'-]+))\s+"
    r"(?:looked|watched|turned|nodded|stopped|paused|hesitated|waited|stood|sat|moved|crossed|checked|"
    r"glanced|continued|followed|returned|reached|pulled|opened|closed|read|listened|remained|shifted|"
    r"exhaled|studied|leaned|stepped|walked|rose|lowered|lifted|caught|held|released|said nothing|did not answer)\b",
    re.IGNORECASE,
)

EXACT_KEEP = {
    "Julie turned back to the dead compound.",
    "The contents remained locked, but the index showed the package owner.",
    "Marcus did not move.",
    "Sarah did not answer.",
    "The console chimed.",
    "The warning remained for less than a second, then vanished.",
    "The image broke apart.",
    "The display updated.",
    "The panel advanced.",
    "Onscreen, 01:37 became 01:36.",
    "The wheel stopped.",
    "She pressed EXECUTE.",
    "The clock showed 00:04.",
    "The display tried to reconcile them.",
    "Then another.",
    "Not artillery.",
    "Elias went still.",
    "The media display changed.",
    "The first line appeared.",
    "Grant sealed the finding.",
}

SPEAKER_AMBIGUITY_KEEP = {
    ("books/book-01/manuscript/chapters/chapter-04.md", 313),
    ("books/book-01/manuscript/chapters/chapter-04.md", 315),
    ("books/book-01/manuscript/chapters/chapter-05.md", 410),
    ("books/book-01/manuscript/chapters/chapter-10.md", 312),
    ("books/book-01/manuscript/chapters/chapter-11.md", 59),
    ("books/book-01/manuscript/chapters/chapter-12.md", 140),
    ("books/book-01/manuscript/chapters/chapter-20.md", 25),
}

EXPLICIT_KEEP = {
    ("books/book-01/manuscript/chapters/chapter-05.md", 205): "preserve second-clock reveal",
    ("books/book-01/manuscript/chapters/chapter-05.md", 640): "preserve peak-action rescue beat",
    ("books/book-01/manuscript/chapters/chapter-08.md", 311): "preserve executive-override decision beat",
    ("books/book-01/manuscript/chapters/chapter-12.md", 248): "preserve field-endpoint reveal before display",
    ("books/book-01/manuscript/chapters/chapter-12.md", 393): "preserve isolated chapter-closing line",
}

EXPLICIT_ACTION = {
    ("books/book-01/manuscript/chapters/chapter-04.md", 511): (
        "merge_next",
        "pair sealed and public planning-record contrast",
    ),
}


def compact(text: str) -> str:
    return " ".join(text.split())


def candidate_records() -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for path in accepted_paths():
        relative = path.relative_to(ROOT).as_posix()
        paragraphs = split_paragraphs(path.read_text(encoding="utf-8"))
        kinds = [kind(paragraph) for paragraph in paragraphs]
        for index, paragraph in enumerate(paragraphs):
            if kinds[index] != "narrative" or sentence_count(paragraph) != 1:
                continue
            words = word_count(paragraph)
            previous_kind = kinds[index - 1] if index > 0 else None
            next_kind = kinds[index + 1] if index + 1 < len(kinds) else None
            is_intentional = intentional(paragraph)
            is_scene_open = index == 0 or previous_kind == "meta"
            is_scene_close = index == len(paragraphs) - 1 or next_kind == "meta"
            is_dialogue_adjacent = previous_kind == "dialogue" or next_kind == "dialogue"
            is_display_adjacent = previous_kind == "display" or next_kind == "display"
            is_routine = bool(ROUTINE_BEAT_RE.search(paragraph.strip())) and words <= 15

            reasons: list[str] = []
            if not is_intentional and not (is_scene_open or is_scene_close):
                if words <= 4:
                    reasons.append("very_short_interior")
                if is_routine:
                    reasons.append("routine_action_reaction")
                if words <= 8 and not is_dialogue_adjacent and not is_display_adjacent:
                    reasons.append("short_isolated_narrative")
            if not reasons:
                continue

            records.append(
                {
                    "file": relative,
                    "paragraph_number": index + 1,
                    "candidate": compact(paragraph),
                    "previous_kind": previous_kind,
                    "next_kind": next_kind,
                    "reasons": reasons,
                }
            )
    return records


def decide(record: dict[str, object]) -> tuple[str, str]:
    key = (str(record["file"]), int(record["paragraph_number"]))
    candidate = str(record["candidate"])
    previous_kind = record["previous_kind"]
    next_kind = record["next_kind"]

    if key in EXPLICIT_ACTION:
        return EXPLICIT_ACTION[key]
    if key in SPEAKER_AMBIGUITY_KEEP:
        return "keep", "speaker attribution would become ambiguous"
    if key in EXPLICIT_KEEP:
        return "keep", EXPLICIT_KEEP[key]
    if any(mark in candidate for mark in ("“", "”", '"')):
        return "keep", "contains spoken dialogue and is not a narrative defect"
    if candidate in EXACT_KEEP:
        return "keep", "protected emphasis, countdown, or display handoff"
    if previous_kind == "display" and next_kind == "display":
        return "keep", "bridges two protected display blocks"
    if previous_kind == "dialogue" and next_kind == "display":
        return "keep", "preserve speaker-safe trigger into protected display"
    if previous_kind == "narrative":
        return "merge_previous", "continue the preceding narrative paragraph"
    if next_kind == "narrative":
        return "merge_next", "lead into the following narrative paragraph"
    if previous_kind == "dialogue" and next_kind == "dialogue":
        return "attach_next_dialogue", "attach routine action to the acting character's following speech"
    if previous_kind == "display" and next_kind == "dialogue":
        return "attach_next_dialogue", "attach reaction to the following spoken response"
    return "keep", "attribution or technical handoff remains ambiguous"


def main() -> None:
    records = candidate_records()
    if len(records) != 230:
        raise RuntimeError(f"expected 230 baseline candidates, found {len(records)}")

    entries: list[dict[str, object]] = []
    counts: dict[str, int] = {}
    for record in records:
        action, reason = decide(record)
        counts[action] = counts.get(action, 0) + 1
        entries.append(
            {
                "file": record["file"],
                "paragraph_number": record["paragraph_number"],
                "candidate": record["candidate"],
                "action": action,
                "reason": reason,
            }
        )

    expected = {
        "attach_next_dialogue": 166,
        "keep": 61,
        "merge_previous": 2,
        "merge_next": 1,
    }
    if counts != expected:
        raise RuntimeError(f"reviewed action counts changed: expected={expected} actual={counts}")

    payload = {
        "version": 1,
        "baseline_words": 105081,
        "baseline_candidates": 230,
        "target_candidates_max": 75,
        "action_counts": counts,
        "entries": entries,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"reviewed repair map: {len(entries)} entries -> {OUTPUT.relative_to(ROOT)}")
    print(counts)


if __name__ == "__main__":
    main()
