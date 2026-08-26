#!/usr/bin/env python3
"""Count Book 2 Markdown words using a defined, checkable method.

Book 2 had no counter. Four different numbers could be produced for the same
file depending on what you counted, and ``MANUSCRIPT_STATUS.yaml`` matched none
of them -- its figures came from the pre-migration Drive tooling and had no way
to be verified after import.

**The locked method.** Strip the migration provenance comment, then
``len(text.split())`` on the remainder. The provenance block is import metadata,
not prose; Book 1's files carry no such block, so the two books' counts stay
comparable. The ``# Chapter N`` heading is counted, matching Book 1.

Run with ``--expect N`` to gate CI, or ``--sync`` to rewrite the per-unit and
total figures in ``MANUSCRIPT_STATUS.yaml``.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
STATUS = REPO_ROOT / "books/book-02/MANUSCRIPT_STATUS.yaml"

PROVENANCE = re.compile(r"\A<!--.*?-->\s*", re.DOTALL)
UNIT_BLOCK = re.compile(
    r'^  - unit: "([^"]+)"\n'
    r'    title: "[^"]+"\n'
    r"    path: (null|\"[^\"]+\")\n"
    r'    status: "([^"]+)"',
    re.MULTILINE,
)


def prose_of(path: Path) -> str:
    """The countable prose: everything after the migration provenance block."""
    return PROVENANCE.sub("", path.read_text(encoding="utf-8"))


def count(path: Path) -> int:
    return len(prose_of(path).split())


def units() -> list[tuple[str, Path | None, str]]:
    text = STATUS.read_text(encoding="utf-8")
    out = []
    for unit, raw_path, status in UNIT_BLOCK.findall(text):
        path = None if raw_path == "null" else REPO_ROOT / raw_path.strip('"')
        out.append((unit, path, status))
    if not out:
        raise SystemExit(f"no narrative units found in {STATUS}")
    return out


def sync() -> int:
    """Rewrite the recorded per-unit words and totals from the prose."""
    text = STATUS.read_text(encoding="utf-8")
    accepted = drafted = 0
    changes: list[str] = []

    for unit, path, status in units():
        if path is None:
            continue
        actual = count(path)
        drafted += actual
        if status == "formally_accepted_canon":
            accepted += actual
        block = re.search(
            r'(  - unit: "%s".*?)(?=\n  - unit: |\n[a-z_]+:)' % re.escape(unit),
            text, re.DOTALL,
        )
        if not block:
            raise SystemExit(f"could not locate the block for {unit}")
        body = block.group(1)
        m = re.search(r"^    words: (\d+)$", body, re.MULTILINE)
        if m and int(m.group(1)) != actual:
            changes.append(f"{unit} words {m.group(1)} -> {actual}")
            text = text.replace(body, re.sub(
                r"^    words: \d+$", f"    words: {actual}", body, flags=re.MULTILINE))
        # scene_words were recorded by hand and cannot be reproduced from the
        # prose without asserting a scene-splitting convention, so they are
        # removed rather than left standing as unverifiable numbers.
        body2 = re.search(
            r'(  - unit: "%s".*?)(?=\n  - unit: |\n[a-z_]+:)' % re.escape(unit),
            text, re.DOTALL).group(1)
        if "    scene_words:" in body2:
            changes.append(f"{unit} scene_words removed (unverifiable)")
            text = text.replace(body2, re.sub(
                r"^    scene_words: \[[^\]]*\]\n", "", body2, flags=re.MULTILINE))

    for field, value in (("accepted_words", accepted), ("drafted_words", drafted)):
        m = re.search(rf"^{field}: (\d+)$", text, re.MULTILINE)
        if m and int(m.group(1)) != value:
            changes.append(f"{field} {m.group(1)} -> {value}")
            text = re.sub(rf"^{field}: \d+$", f"{field}: {value}", text, flags=re.MULTILINE)

    STATUS.write_text(text, encoding="utf-8")
    for line in changes:
        print(f"  {line}")
    return len(changes)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--expect", type=int, help="fail unless drafted words equal this")
    parser.add_argument("--sync", action="store_true", help="rewrite MANUSCRIPT_STATUS.yaml")
    args = parser.parse_args()

    if args.sync:
        changed = sync()
        print(f"Synced {STATUS.relative_to(REPO_ROOT)}: {changed} change(s)")
        return 0

    accepted = drafted = 0
    for unit, path, status in units():
        if path is None:
            print(f"{'':>8}  {unit} (undrafted)")
            continue
        words = count(path)
        drafted += words
        if status == "formally_accepted_canon":
            accepted += words
        print(f"{words:8,}  {path.relative_to(REPO_ROOT)}  [{status}]")
    print(f"{accepted:8,}  ACCEPTED")
    print(f"{drafted:8,}  DRAFTED")

    if args.expect is not None and drafted != args.expect:
        print(f"FAIL: expected {args.expect:,} drafted words, found {drafted:,}",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
