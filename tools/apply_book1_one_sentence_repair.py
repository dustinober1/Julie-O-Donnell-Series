#!/usr/bin/env python3
"""Apply the reviewed Book 1 one-sentence paragraph repair map."""
from __future__ import annotations

import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path

from build_book1_one_sentence_repair_map import candidate_records
from reflow_book1_publication_rhythm import (
    ROOT,
    accepted_paths,
    kind,
    lexical_signature,
    metrics,
    split_paragraphs,
    update_manifest,
    update_opening_locks,
)

BOOK = ROOT / "books/book-01"
MAP = BOOK / "control/52-one-sentence-repair-map.json"
REPORT = ROOT / "artifacts/book1-one-sentence-repair.md"
CONTROL = BOOK / "control/53-one-sentence-repair.md"
DATE = "2026-07-18"
QUOTE_RE = re.compile(r"“[^”]*”", re.DOTALL)


def compact(text: str) -> str:
    return " ".join(text.split())


def quote_signature(text: str) -> tuple[str, ...]:
    return tuple(QUOTE_RE.findall(text))


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def insert_once(path: Path, marker: str, addition: str) -> None:
    text = path.read_text(encoding="utf-8")
    if addition.strip() in text:
        return
    if marker not in text:
        raise RuntimeError(f"control marker missing in {path.relative_to(ROOT)}")
    path.write_text(text.replace(marker, marker + addition, 1), encoding="utf-8")


def apply_file(path: Path, entries: list[dict[str, object]]) -> int:
    original = path.read_text(encoding="utf-8")
    original_words = len(original.split())
    original_lexical = lexical_signature(original)
    original_quotes = quote_signature(original)
    original_paragraphs = split_paragraphs(original)
    original_protected = [p for p in original_paragraphs if kind(p) in {"meta", "display"}]
    original_final = original_paragraphs[-1]

    paragraphs = list(original_paragraphs)
    changed = 0
    actionable = [entry for entry in entries if entry["action"] != "keep"]
    for entry in sorted(actionable, key=lambda item: int(item["paragraph_number"]), reverse=True):
        index = int(entry["paragraph_number"]) - 1
        if index < 0 or index >= len(paragraphs):
            raise RuntimeError(f"stale paragraph index in {path.name}: {entry}")
        candidate = compact(paragraphs[index])
        if candidate != entry["candidate"]:
            raise RuntimeError(
                f"stale candidate in {path.name} paragraph {entry['paragraph_number']}: "
                f"expected={entry['candidate']!r} actual={candidate!r}"
            )

        action = str(entry["action"])
        if action == "merge_previous":
            if index == 0 or kind(paragraphs[index - 1]) != "narrative":
                raise RuntimeError(f"unsafe merge_previous in {path.name}:{index + 1}")
            paragraphs[index - 1] = paragraphs[index - 1].rstrip() + " " + paragraphs[index].lstrip()
            del paragraphs[index]
        elif action == "merge_next":
            if index + 1 >= len(paragraphs) or kind(paragraphs[index + 1]) != "narrative":
                raise RuntimeError(f"unsafe merge_next in {path.name}:{index + 1}")
            paragraphs[index] = paragraphs[index].rstrip() + " " + paragraphs[index + 1].lstrip()
            del paragraphs[index + 1]
        elif action == "attach_next_dialogue":
            if index + 1 >= len(paragraphs) or kind(paragraphs[index + 1]) != "dialogue":
                raise RuntimeError(f"unsafe attach_next_dialogue in {path.name}:{index + 1}")
            paragraphs[index] = paragraphs[index].rstrip() + " " + paragraphs[index + 1].lstrip()
            del paragraphs[index + 1]
        else:
            raise RuntimeError(f"unknown repair action: {action}")
        changed += 1

    updated = "\n\n".join(paragraphs).rstrip() + "\n"
    if len(updated.split()) != original_words:
        raise RuntimeError(f"word count changed in {path.relative_to(ROOT)}")
    if lexical_signature(updated) != original_lexical:
        raise RuntimeError(f"lexical word order changed in {path.relative_to(ROOT)}")
    if quote_signature(updated) != original_quotes:
        raise RuntimeError(f"dialogue wording/order changed in {path.relative_to(ROOT)}")
    updated_paragraphs = split_paragraphs(updated)
    updated_protected = [p for p in updated_paragraphs if kind(p) in {"meta", "display"}]
    if updated_protected != original_protected:
        raise RuntimeError(f"scene metadata or system display changed in {path.relative_to(ROOT)}")
    if original.count("\n---\n") != updated.count("\n---\n"):
        raise RuntimeError(f"scene separator count changed in {path.relative_to(ROOT)}")
    if updated_paragraphs[-1] != original_final:
        raise RuntimeError(f"chapter ending changed in {path.relative_to(ROOT)}")

    if updated != original:
        path.write_text(updated, encoding="utf-8")
    return changed


def update_controls() -> None:
    insert_once(
        ROOT / "README.md",
        "- Publication-rhythm pass completed **July 18, 2026**, reducing routine isolated narrative beats while preserving dialogue, scene metadata, system displays, and story content.\n",
        "- Targeted one-sentence-paragraph repair completed **July 18, 2026**, integrating reviewed routine reactions and technical transitions without changing accepted words.\n",
    )
    insert_once(
        ROOT / "PROJECT_STATE.yaml",
        f'  publication_rhythm_pass_completed: "{DATE}"\n',
        f'  one_sentence_paragraph_repair_completed: "{DATE}"\n',
    )
    insert_once(
        BOOK / "manuscript/STATUS.md",
        "- Publication-rhythm pass completed: **July 18, 2026**.\n",
        "- Targeted one-sentence-paragraph repair completed: **July 18, 2026**.\n",
    )
    insert_once(
        BOOK / "control/00-overview.md",
        "- Publication-rhythm pass completed: **2026-07-18**.\n",
        "- Targeted one-sentence-paragraph repair completed: **2026-07-18**.\n",
    )


def write_reports(
    paths: list[Path],
    changed_actions: int,
    changed_files: list[str],
    before_candidates: int,
    after_candidates: int,
    before_one_sentence: int,
    after_one_sentence: int,
    before_narrative: int,
    after_narrative: int,
) -> None:
    report_lines = [
        "# Book 1 One-Sentence Paragraph Repair",
        "",
        f"Completed **{DATE}** against the accepted-manuscript inventory.",
        "",
        "## Result",
        "",
        "- Accepted words: **105,081** (unchanged).",
        f"- Reviewed strict candidates: **{before_candidates}**.",
        f"- Paragraph integrations applied: **{changed_actions}**.",
        f"- Strict review candidates remaining: **{after_candidates}**.",
        f"- Narrative paragraphs: **{before_narrative:,} → {after_narrative:,}**.",
        f"- One-sentence narrative paragraphs: **{before_one_sentence:,} → {after_one_sentence:,}**.",
        f"- Accepted prose files changed: **{len(changed_files)}**.",
        "",
        "## Content lock",
        "",
        "- Lexical word order is unchanged in every accepted file.",
        "- All quoted dialogue wording and order are unchanged.",
        "- Scene metadata, system displays, separators, and chapter endings are unchanged.",
        "- Plot, chronology, evidence, technology, POV, character knowledge, decisions, reveals, and ending are unchanged.",
        "- Deliberate countdown, discovery, display-handoff, and motif lines remain isolated through explicit keep decisions.",
        "",
        "## Changed accepted files",
        "",
    ]
    report_lines.extend(f"- `{name}`" for name in changed_files)
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(report_lines).rstrip() + "\n", encoding="utf-8")

    control_lines = [
        "# One-Sentence Paragraph Repair — Book 1",
        "",
        f"**Completed:** {DATE}",
        "",
        "## Scope",
        "",
        "The accepted manuscript received a context-reviewed paragraph-integration pass based on the 230 strict candidates recorded after the publication-rhythm pass. The repair changes paragraph boundaries only.",
        "",
        "## Locked result",
        "",
        "- Accepted words remain **105,081**.",
        f"- Paragraph integrations applied: **{changed_actions}**.",
        f"- Strict candidates remaining: **{after_candidates}**.",
        "- Dialogue wording, system displays, scene metadata, chronology, evidence, technology, POV, reveals, and ending remain unchanged.",
        "- Full decisions are recorded in `52-one-sentence-repair-map.json`.",
        "- Full measurements are recorded in `artifacts/book1-one-sentence-repair.md`.",
        "",
        "## Publication boundary",
        "",
        "External specialist review, approved technical corrections, copyedit, and proofread remain required before publication.",
        "",
    ]
    CONTROL.write_text("\n".join(control_lines), encoding="utf-8")


def main() -> None:
    payload = json.loads(MAP.read_text(encoding="utf-8"))
    if payload.get("baseline_words") != 105081 or payload.get("baseline_candidates") != 230:
        raise RuntimeError("repair map baseline does not match accepted manuscript")

    before_records = candidate_records()
    if len(before_records) != 230:
        raise RuntimeError(f"expected 230 candidates before repair, found {len(before_records)}")

    paths = accepted_paths()
    before_metrics = {path.name: metrics(path.read_text(encoding="utf-8")) for path in paths}
    entries_by_file: dict[str, list[dict[str, object]]] = defaultdict(list)
    for entry in payload["entries"]:
        entries_by_file[str(entry["file"])].append(entry)

    changed_actions = 0
    changed_files: list[str] = []
    for path in paths:
        relative = path.relative_to(ROOT).as_posix()
        before_hash = digest(path)
        changed_actions += apply_file(path, entries_by_file.get(relative, []))
        if digest(path) != before_hash:
            changed_files.append(relative)

    total_words = sum(len(path.read_text(encoding="utf-8").split()) for path in paths)
    if total_words != 105081:
        raise RuntimeError(f"accepted total changed: {total_words}")

    after_records = candidate_records()
    after_candidates = len(after_records)
    if after_candidates > int(payload["target_candidates_max"]):
        raise RuntimeError(f"strict candidate target missed: {after_candidates}")

    after_metrics = {path.name: metrics(path.read_text(encoding="utf-8")) for path in paths}
    before_narrative = sum(value.narrative_paragraphs for value in before_metrics.values())
    after_narrative = sum(value.narrative_paragraphs for value in after_metrics.values())
    before_one = sum(value.narrative_one_sentence for value in before_metrics.values())
    after_one = sum(value.narrative_one_sentence for value in after_metrics.values())

    update_manifest(paths, total_words)
    update_opening_locks()
    update_controls()
    write_reports(
        paths,
        changed_actions,
        changed_files,
        len(before_records),
        after_candidates,
        before_one,
        after_one,
        before_narrative,
        after_narrative,
    )

    print(f"one-sentence repair complete: {changed_actions} integrations across {len(changed_files)} files")
    print(f"strict candidates: {len(before_records)} -> {after_candidates}")
    print(f"accepted words unchanged: {total_words:,}")


if __name__ == "__main__":
    main()
