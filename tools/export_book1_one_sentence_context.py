#!/usr/bin/env python3
"""Export full context for every strict one-sentence paragraph candidate."""
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

OUTPUT = ROOT / "artifacts/book1-one-sentence-context.json"

ROUTINE_BEAT_RE = re.compile(
    r"^(?:(?:Julie|Marcus|Elias|Sarah|Sharma|Mercer|Vance|Bell|Hackett|Qureshi|Grant|Alvarez|Ortiz|Vega)|"
    r"(?:He|She|They|The\s+[A-Za-z'-]+))\s+"
    r"(?:looked|watched|turned|nodded|stopped|paused|hesitated|waited|stood|sat|moved|crossed|checked|"
    r"glanced|continued|followed|returned|reached|pulled|opened|closed|read|listened|remained|shifted|"
    r"exhaled|studied|leaned|stepped|walked|rose|lowered|lifted|caught|held|released|said nothing|did not answer)\b",
    re.IGNORECASE,
)


def compact(text: str | None) -> str | None:
    if text is None:
        return None
    return " ".join(text.split())


def main() -> None:
    records: list[dict[str, object]] = []
    for path in accepted_paths():
        text = path.read_text(encoding="utf-8")
        paragraphs = split_paragraphs(text)
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
            is_scene_boundary = is_scene_open or is_scene_close
            is_dialogue_adjacent = previous_kind == "dialogue" or next_kind == "dialogue"
            is_display_adjacent = previous_kind == "display" or next_kind == "display"
            is_routine = bool(ROUTINE_BEAT_RE.search(paragraph.strip())) and words <= 15

            reasons: list[str] = []
            if not is_intentional and not is_scene_boundary:
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
                    "file": path.relative_to(ROOT).as_posix(),
                    "paragraph_number": index + 1,
                    "index": index,
                    "words": words,
                    "reasons": reasons,
                    "candidate": compact(paragraph),
                    "previous_kind": previous_kind,
                    "previous": compact(paragraphs[index - 1]) if index > 0 else None,
                    "next_kind": next_kind,
                    "next": compact(paragraphs[index + 1]) if index + 1 < len(paragraphs) else None,
                    "scene_open": is_scene_open,
                    "scene_close": is_scene_close,
                    "dialogue_adjacent": is_dialogue_adjacent,
                    "display_adjacent": is_display_adjacent,
                }
            )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(records, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"exported {len(records)} candidates -> {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
