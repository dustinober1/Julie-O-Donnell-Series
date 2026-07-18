#!/usr/bin/env python3
"""Repair Book 1 paragraph rhythm without changing story content.

The pass is intentionally conservative:
- all dialogue paragraphs remain byte-for-byte unchanged;
- headings, scene metadata, system displays, lists, and separators remain unchanged;
- only consecutive narrative paragraphs are combined;
- selected scene-opening, scene-ending, countdown, and motif beats stay isolated;
- lexical word order and the repository word-count method remain unchanged.
"""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "books/book-01"
MANIFEST = BOOK / "ACCEPTED_MANUSCRIPT.yaml"
REPORT = ROOT / "artifacts/book1-publication-rhythm-pass.md"
CONTROL = BOOK / "control/51-publication-rhythm-pass.md"
DATE = "2026-07-18"

PATH_RE = re.compile(r'^\s+(?:-\s+)?path:\s*"([^"]+)"\s*$')
TIME_RE = re.compile(
    r"^(?:\d{1,2}:\d{2}(?::\d{2})?\s+)?(?:Eastern|Indian|Pacific|Central|Mountain) "
    r"(?:Daylight|Standard) Time$"
)
DATE_RE = re.compile(
    r"^(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:,\s+\d{4})?$"
)
SENTENCE_END_RE = re.compile(r"[.!?](?:[”\"])?$")
SENTENCE_MARK_RE = re.compile(r"[.!?](?:[”\"])?(?:\s|$)")
WORD_RE = re.compile(r"[A-Za-z0-9]+(?:[’'][A-Za-z0-9]+)*")

INTENTIONAL_EMPHASIS = {
    "the fence had failed for an honest reason.",
    "centered.",
    "that was the problem.",
    "four seconds.",
    "that was the first lie.",
    "that was the second lie.",
    "too perfect.",
    "people.",
    "done.",
    "no one celebrated.",
    "the bubble stayed centered.",
}


@dataclass(frozen=True)
class Config:
    target_min: int
    target_max: int
    max_parts: int


@dataclass
class Metrics:
    narrative_paragraphs: int = 0
    narrative_one_sentence: int = 0
    narrative_le_2: int = 0
    narrative_le_7: int = 0
    short_narrative_sentences: int = 0
    isolated_not_no: int = 0
    dialogue_paragraphs: int = 0

    def add(self, other: "Metrics") -> None:
        for field in self.__dataclass_fields__:
            setattr(self, field, getattr(self, field) + getattr(other, field))


def accepted_paths() -> list[Path]:
    text = MANIFEST.read_text(encoding="utf-8")
    block = text.split("\nexcluded_from_canon:", 1)[0]
    paths = [ROOT / match.group(1) for line in block.splitlines() if (match := PATH_RE.match(line))]
    if len(paths) != 25:
        raise RuntimeError(f"expected 25 accepted prose files, found {len(paths)}")
    return paths


def split_paragraphs(text: str) -> list[str]:
    return [part.strip() for part in re.split(r"\n\s*\n", text.strip()) if part.strip()]


def word_count(text: str) -> int:
    return len(text.split())


def lexical_signature(text: str) -> tuple[str, ...]:
    return tuple(word.lower() for word in WORD_RE.findall(text))


def uppercase_ratio(text: str) -> float:
    letters = [char for char in text if char.isalpha()]
    if not letters:
        return 0.0
    return sum(char.isupper() for char in letters) / len(letters)


def kind(paragraph: str) -> str:
    stripped = paragraph.strip()
    if stripped.startswith("#") or stripped == "---":
        return "meta"
    if stripped.startswith(("“", '"', "‘")):
        return "dialogue"
    if stripped.startswith(("- ", "* ", "• ")):
        return "meta"
    if "\n" in stripped:
        return "display"
    words = stripped.split()
    if TIME_RE.fullmatch(stripped) or DATE_RE.fullmatch(stripped):
        return "meta"
    if len(words) <= 14 and not SENTENCE_END_RE.search(stripped):
        return "meta"
    if uppercase_ratio(stripped) >= 0.78 and len(words) <= 90:
        return "display"
    return "narrative"


def sentence_count(paragraph: str) -> int:
    count = len(SENTENCE_MARK_RE.findall(paragraph))
    return count or 1


def metrics(text: str) -> Metrics:
    result = Metrics()
    for paragraph in split_paragraphs(text):
        paragraph_kind = kind(paragraph)
        if paragraph_kind == "dialogue":
            result.dialogue_paragraphs += 1
            continue
        if paragraph_kind != "narrative":
            continue
        result.narrative_paragraphs += 1
        words = paragraph.split()
        if sentence_count(paragraph) == 1:
            result.narrative_one_sentence += 1
        if len(words) <= 2:
            result.narrative_le_2 += 1
        if len(words) <= 7:
            result.narrative_le_7 += 1
        if len(words) <= 7 and re.match(r"^(?:Not|No)\b", paragraph):
            result.isolated_not_no += 1
        for sentence in re.split(r"(?<=[.!?])(?:[”\"])?\s+", paragraph):
            if sentence and len(sentence.split()) <= 2:
                result.short_narrative_sentences += 1
    return result


def config_for(path: Path) -> Config:
    name = path.name
    if name == "prologue.md":
        return Config(34, 105, 4)
    number_match = re.search(r"(\d{2})", name)
    number = int(number_match.group(1)) if number_match else 0
    if number in {1, 2}:
        return Config(40, 110, 5)
    if number in {3, 4, 5}:
        return Config(46, 112, 6)
    if number in {6, 7, 8, 9}:
        return Config(28, 90, 3)
    if number in {10, 11}:
        return Config(36, 105, 4)
    if number in {12, 13, 14}:
        return Config(42, 110, 5)
    return Config(34, 105, 4)


def intentional(paragraph: str) -> bool:
    normalized = " ".join(paragraph.lower().split())
    return normalized in INTENTIONAL_EMPHASIS


def reflow_run(
    run: list[str],
    config: Config,
    *,
    scene_open: bool,
    scene_close: bool,
    file_end: bool,
) -> list[str]:
    output: list[tuple[str, bool]] = []
    current: list[str] = []
    current_words = 0

    def flush() -> None:
        nonlocal current, current_words
        if current:
            output.append((" ".join(current), False))
            current = []
            current_words = 0

    for index, paragraph in enumerate(run):
        words = word_count(paragraph)
        keep = intentional(paragraph)
        if index == 0 and scene_open and words <= 10:
            keep = True
        if index == len(run) - 1 and scene_close and words <= 12:
            keep = True
        if index == len(run) - 1 and file_end:
            keep = True

        if keep:
            flush()
            output.append((paragraph, True))
            continue

        if current and (
            current_words + words > config.target_max
            or len(current) >= config.max_parts
        ):
            flush()

        current.append(paragraph)
        current_words += words
        if current_words >= config.target_min:
            flush()

    flush()

    if len(output) >= 2:
        last_text, last_kept = output[-1]
        previous_text, previous_kept = output[-2]
        if (
            not last_kept
            and not previous_kept
            and word_count(last_text) < config.target_min
            and word_count(previous_text) + word_count(last_text) <= config.target_max
        ):
            output[-2] = (previous_text + " " + last_text, False)
            output.pop()

    return [text for text, _ in output]


def exact_cadence_cleanup(text: str) -> str:
    # Punctuation-only cleanup of a conspicuous fragment pair; lexical order and word count stay fixed.
    text = text.replace(
        "In the holding room, he looked smaller. Not weaker. More precise.",
        "In the holding room, he looked smaller: not weaker, more precise.",
    )
    return text


def reflow(path: Path, text: str) -> str:
    paragraphs = split_paragraphs(text)
    kinds = [kind(paragraph) for paragraph in paragraphs]
    output: list[str] = []
    index = 0
    config = config_for(path)

    while index < len(paragraphs):
        if kinds[index] != "narrative":
            output.append(paragraphs[index])
            index += 1
            continue

        start = index
        while index < len(paragraphs) and kinds[index] == "narrative":
            index += 1
        run = paragraphs[start:index]
        previous_kind = kinds[start - 1] if start > 0 else None
        next_kind = kinds[index] if index < len(paragraphs) else None
        output.extend(
            reflow_run(
                run,
                config,
                scene_open=previous_kind == "meta",
                scene_close=next_kind == "meta",
                file_end=index == len(paragraphs),
            )
        )

    updated = exact_cadence_cleanup("\n\n".join(output).rstrip() + "\n")
    return updated


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def update_manifest(paths: list[Path], total: int) -> None:
    text = MANIFEST.read_text(encoding="utf-8")
    text = re.sub(
        r"^total_accepted_words:\s*\d+\s*$",
        f"total_accepted_words: {total}",
        text,
        count=1,
        flags=re.MULTILINE,
    )
    if "publication_rhythm_pass_completed:" not in text:
        marker = f'developmental_revision_completed: "{DATE}"\n'
        text = text.replace(marker, marker + f'publication_rhythm_pass_completed: "{DATE}"\n', 1)

    for path in paths:
        relative = path.relative_to(ROOT).as_posix()
        words = len(path.read_text(encoding="utf-8").split())
        sha = digest(path)
        pattern = re.compile(
            rf'(\n\s+- path:\s+"{re.escape(relative)}".*?\n\s+words:)\s*\d+(\n\s+sha256:)\s*"[a-f0-9]+"',
            re.DOTALL,
        )
        text, count = pattern.subn(rf'\g<1> {words}\g<2> "{sha}"', text, count=1)
        if count != 1:
            raise RuntimeError(f"manifest entry not updated: {relative}")
    MANIFEST.write_text(text, encoding="utf-8")


def update_opening_locks() -> None:
    path = ROOT / "tools/verify_book1_revision.py"
    text = path.read_text(encoding="utf-8")
    for relative in (
        "books/book-01/manuscript/prologue.md",
        "books/book-01/manuscript/chapters/chapter-01.md",
    ):
        sha = digest(ROOT / relative)
        text, count = re.subn(
            rf'("{re.escape(relative)}":\s*)"[a-f0-9]+"',
            rf'\g<1>"{sha}"',
            text,
            count=1,
        )
        if count != 1:
            raise RuntimeError(f"protected opening lock not updated: {relative}")
    text = text.replace(
        "Protected accepted prologue and Chapter 1 hashes match the repository lock.",
        "Protected prologue and Chapter 1 hashes match the post-rhythm repository lock.",
    )
    path.write_text(text, encoding="utf-8")


def insert_once(path: Path, marker: str, addition: str) -> None:
    text = path.read_text(encoding="utf-8")
    if addition.strip() in text:
        return
    if marker not in text:
        raise RuntimeError(f"control marker missing in {path.relative_to(ROOT)}")
    path.write_text(text.replace(marker, marker + addition, 1), encoding="utf-8")


def update_controls() -> None:
    insert_once(
        ROOT / "README.md",
        "- Developmental revision completed **July 18, 2026**.\n",
        "- Publication-rhythm pass completed **July 18, 2026**, reducing routine isolated narrative beats while preserving dialogue, scene metadata, system displays, and story content.\n",
    )
    insert_once(
        ROOT / "PROJECT_STATE.yaml",
        f'  revision_completed: "{DATE}"\n',
        f'  publication_rhythm_pass_completed: "{DATE}"\n',
    )
    insert_once(
        BOOK / "manuscript/STATUS.md",
        "- Developmental revision completed: **July 18, 2026**.\n",
        "- Publication-rhythm pass completed: **July 18, 2026**.\n",
    )
    insert_once(
        BOOK / "control/00-overview.md",
        "- Developmental revision completed: **2026-07-18**.\n",
        "- Publication-rhythm pass completed: **2026-07-18**.\n",
    )


def percentage(before: int, after: int) -> str:
    if not before:
        return "0.0%"
    return f"{(before - after) / before:.1%}"


def write_reports(
    paths: list[Path],
    before_by_file: dict[str, Metrics],
    after_by_file: dict[str, Metrics],
    changed_files: list[str],
    total_words: int,
) -> None:
    before = Metrics()
    after = Metrics()
    for value in before_by_file.values():
        before.add(value)
    for value in after_by_file.values():
        after.add(value)

    lines = [
        "# Book 1 Publication-Rhythm Pass",
        "",
        f"Completed **{DATE}** against the accepted-manuscript inventory.",
        "",
        "## Result",
        "",
        f"- Accepted words: **{total_words:,}** (unchanged).",
        f"- Accepted prose files reviewed: **{len(paths)}**.",
        f"- Accepted prose files reflowed: **{len(changed_files)}**.",
        f"- Narrative paragraphs: **{before.narrative_paragraphs:,} → {after.narrative_paragraphs:,}** ({percentage(before.narrative_paragraphs, after.narrative_paragraphs)} reduction).",
        f"- Isolated narrative paragraphs of two words or fewer: **{before.narrative_le_2:,} → {after.narrative_le_2:,}** ({percentage(before.narrative_le_2, after.narrative_le_2)} reduction).",
        f"- Isolated narrative paragraphs of seven words or fewer: **{before.narrative_le_7:,} → {after.narrative_le_7:,}** ({percentage(before.narrative_le_7, after.narrative_le_7)} reduction).",
        f"- One-sentence narrative paragraphs: **{before.narrative_one_sentence:,} → {after.narrative_one_sentence:,}** ({percentage(before.narrative_one_sentence, after.narrative_one_sentence)} reduction).",
        f"- Isolated narrative `Not`/`No` fragments: **{before.isolated_not_no:,} → {after.isolated_not_no:,}**.",
        f"- Dialogue paragraphs preserved: **{after.dialogue_paragraphs:,}**.",
        "",
        "## Content lock",
        "",
        "- Dialogue paragraphs are byte-for-byte unchanged.",
        "- Headings, locations, dates, times, separators, lists, and system-display blocks are unchanged.",
        "- Lexical word order is unchanged in every accepted prose file.",
        "- Plot, evidence, technology, chronology, POV, character knowledge, dialogue meaning, reveals, and chapter endings are unchanged.",
        "- The prologue and Chapter 1 now carry new post-rhythm hashes and remain protected by the repository verifier.",
        "",
        "## Per-file metrics",
        "",
        "| File | Narrative paras | After | ≤2 before | ≤2 after | ≤7 before | ≤7 after |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for path in paths:
        key = path.name
        b = before_by_file[key]
        a = after_by_file[key]
        lines.append(
            f"| {key} | {b.narrative_paragraphs:,} | {a.narrative_paragraphs:,} | {b.narrative_le_2:,} | {a.narrative_le_2:,} | {b.narrative_le_7:,} | {a.narrative_le_7:,} |"
        )
    lines.extend(["", "## Changed accepted files", ""])
    lines.extend(f"- `{name}`" for name in changed_files)
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    control_lines = [
        "# Publication-Rhythm Pass — Book 1",
        "",
        f"**Completed:** {DATE}",
        "",
        "## Authority",
        "",
        "This pass was authorized after the author identified excessive isolated short lines and one- or two-word narrative paragraphs in the accepted manuscript.",
        "",
        "## Scope lock",
        "",
        "The pass changes paragraph architecture only, plus one punctuation-only cadence repair. It does not revise plot, pacing, scene order, POV order, chronology, evidence, technology, dialogue wording or meaning, character decisions, character knowledge, worldbuilding, reveals, suspense structure, or chapter endings.",
        "",
        "## Acceptance result",
        "",
        f"- Accepted words remain **{total_words:,}**.",
        f"- Isolated narrative paragraphs of two words or fewer fell from **{before.narrative_le_2:,}** to **{after.narrative_le_2:,}**.",
        f"- Isolated narrative paragraphs of seven words or fewer fell from **{before.narrative_le_7:,}** to **{after.narrative_le_7:,}**.",
        f"- One-sentence narrative paragraphs fell from **{before.narrative_one_sentence:,}** to **{after.narrative_one_sentence:,}**.",
        "- Dialogue and non-narrative technical formatting remain unchanged.",
        "- Updated accepted-file hashes are recorded in `books/book-01/ACCEPTED_MANUSCRIPT.yaml`.",
        "- Full measurements are in `artifacts/book1-publication-rhythm-pass.md`.",
        "",
        "## Publication boundary",
        "",
        "External specialist review, approved technical corrections, continuity review, copyedit, and proofread remain required before publication.",
        "",
    ]
    CONTROL.write_text("\n".join(control_lines), encoding="utf-8")


def main() -> None:
    paths = accepted_paths()
    before_by_file: dict[str, Metrics] = {}
    after_by_file: dict[str, Metrics] = {}
    changed_files: list[str] = []

    for path in paths:
        original = path.read_text(encoding="utf-8")
        before_by_file[path.name] = metrics(original)
        original_non_narrative = [p for p in split_paragraphs(original) if kind(p) != "narrative"]
        original_words = len(original.split())
        original_signature = lexical_signature(original)

        updated = reflow(path, original)

        if lexical_signature(updated) != original_signature:
            raise RuntimeError(f"lexical content changed: {path.relative_to(ROOT)}")
        if len(updated.split()) != original_words:
            raise RuntimeError(f"repository word count changed: {path.relative_to(ROOT)}")
        updated_non_narrative = [p for p in split_paragraphs(updated) if kind(p) != "narrative"]
        if updated_non_narrative != original_non_narrative:
            raise RuntimeError(f"dialogue or non-narrative block changed: {path.relative_to(ROOT)}")
        if original.count("\n---\n") != updated.count("\n---\n"):
            raise RuntimeError(f"scene separator count changed: {path.relative_to(ROOT)}")

        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed_files.append(path.relative_to(ROOT).as_posix())
        after_by_file[path.name] = metrics(updated)

    before_total = Metrics()
    after_total = Metrics()
    for value in before_by_file.values():
        before_total.add(value)
    for value in after_by_file.values():
        after_total.add(value)

    if changed_files:
        if after_total.narrative_le_2 > int(before_total.narrative_le_2 * 0.70):
            raise RuntimeError("two-word narrative isolation did not fall by at least 30%")
        if after_total.narrative_le_7 > int(before_total.narrative_le_7 * 0.75):
            raise RuntimeError("short narrative isolation did not fall by at least 25%")
        if after_total.narrative_one_sentence > int(before_total.narrative_one_sentence * 0.80):
            raise RuntimeError("one-sentence narrative paragraphs did not fall by at least 20%")

    total_words = sum(len(path.read_text(encoding="utf-8").split()) for path in paths)
    update_manifest(paths, total_words)
    update_opening_locks()
    update_controls()
    write_reports(paths, before_by_file, after_by_file, changed_files, total_words)

    print(f"publication-rhythm pass complete: {len(changed_files)} accepted files changed")
    print(f"accepted words unchanged: {total_words:,}")
    print(f"narrative paragraphs: {before_total.narrative_paragraphs:,} -> {after_total.narrative_paragraphs:,}")
    print(f"narrative <=2 words: {before_total.narrative_le_2:,} -> {after_total.narrative_le_2:,}")
    print(f"narrative <=7 words: {before_total.narrative_le_7:,} -> {after_total.narrative_le_7:,}")


if __name__ == "__main__":
    main()
