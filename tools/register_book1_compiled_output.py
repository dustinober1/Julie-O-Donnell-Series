#!/usr/bin/env python3
"""Register the revised compilation and synchronize canonical Book 1 controls."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from finalize_book1_revision_controls import main as finalize_controls

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "books/book-01"
MANIFEST = BOOK / "ACCEPTED_MANUSCRIPT.yaml"
COMPILED = BOOK / "compiled/current/Julie_O_Donnell_Book_1_REVISED.md"
DATE = "2026-07-18"
GENERATED_CONTROLS = (
    ROOT / "README.md",
    ROOT / "PROJECT_STATE.yaml",
    BOOK / "manuscript/STATUS.md",
    BOOK / "control/00-overview.md",
    BOOK / "control/16-chapter-by-chapter-status-record.md",
    BOOK / "control/24-thread-disposition-matrix.md",
    ROOT / "series/recurring-character-ledger.md",
)


def prose_paths() -> list[Path]:
    return [BOOK / "manuscript/prologue.md"] + [
        BOOK / f"manuscript/chapters/chapter-{number:02d}.md"
        for number in range(1, 25)
    ]


def word_count(path: Path) -> int:
    return len(path.read_text(encoding="utf-8").split())


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def title(path: Path) -> str:
    if path.name == "prologue.md":
        return "Six Years Ago"
    first_line = path.read_text(encoding="utf-8").splitlines()[0]
    prefix = f"# Chapter {int(path.stem.split('-')[-1])} — "
    if not first_line.startswith(prefix):
        raise RuntimeError(f"cannot derive title from {path.relative_to(ROOT)}")
    return first_line[len(prefix) :]


def quoted(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def write_manifest(paths: list[Path]) -> None:
    total = sum(word_count(path) for path in paths)
    lines = [
        "version: 2",
        "book: 1",
        'title: "Veridrift"',
        'status: "developmentally_revised"',
        f'generated_on: "{DATE}"',
        f'developmental_revision_completed: "{DATE}"',
        'publication_readiness: "specialist_review_and_copyedit_required"',
        "target_words_min: 105000",
        "target_words_max: 110000",
        f"total_accepted_words: {total}",
        "accepted_files:",
    ]
    for path in paths:
        relative = path.relative_to(ROOT).as_posix()
        lines.extend(
            [
                f"  - path: {quoted(relative)}",
                f"    title: {quoted(title(path))}",
                f"    accepted_on: {quoted(DATE)}",
                f"    words: {word_count(path)}",
                f"    sha256: {quoted(digest(path))}",
            ]
        )
    lines.extend(
        [
            "excluded_from_canon:",
            '  - path: "books/book-01/drafts/"',
            '    reason: "Unaccepted prose and historical drafting material."',
            '  - path: "archive/"',
            '    reason: "Historical provenance only."',
            '  - path: "docs/superpowers/"',
            '    reason: "Design and implementation records, not story canon."',
            f"  - path: {quoted(COMPILED.relative_to(ROOT).as_posix())}",
            '    reason: "Generated compilation for review; canonical prose remains the accepted file inventory."',
            "",
        ]
    )
    MANIFEST.write_text("\n".join(lines), encoding="utf-8")


def normalize_generated_controls() -> None:
    for path in GENERATED_CONTROLS:
        text = path.read_text(encoding="utf-8")
        normalized = "\n".join(line.rstrip() for line in text.splitlines()) + "\n"
        path.write_text(normalized, encoding="utf-8")


def main() -> None:
    paths = prose_paths()
    if not COMPILED.is_file():
        raise RuntimeError(f"compiled manuscript missing: {COMPILED.relative_to(ROOT)}")
    write_manifest(paths)
    finalize_controls()
    normalize_generated_controls()
    print(f"registered and synchronized {COMPILED.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
