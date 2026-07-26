#!/usr/bin/env python3
"""Book 1 publication-readiness entrypoint with final-package stale-state guards."""
from __future__ import annotations

import re
from pathlib import Path

from book1_publication_readiness_core import *  # noqa: F401,F403
import book1_publication_readiness_core as _core

_core.STALE_CONTROL_LITERALS = _core.STALE_CONTROL_LITERALS + ("105,155", "105155")
STALE_CONTROL_LITERALS = _core.STALE_CONTROL_LITERALS
_STRICT_CONTROL_VALIDATOR = _core.validate_control_metadata


def _parse_final_package_manifest(
    root: Path,
) -> tuple[list[_core.ManifestEntry], int, str]:
    """Parse the accepted manifest and require the post-PR-92 frozen package state."""
    manifest = root / "books/book-01/ACCEPTED_MANUSCRIPT.yaml"
    text = _core._read(manifest)
    accepted_block = text.split("\nexcluded_from_canon:", 1)[0]

    entries = [
        _core.ManifestEntry(path, title, accepted_on, int(words), sha256)
        for path, title, accepted_on, words, sha256 in _core.ENTRY_RE.findall(
            accepted_block
        )
    ]
    if len(entries) != 25:
        _core.fail(f"expected 25 accepted prose files, found {len(entries)}")
    if len({entry.path for entry in entries}) != len(entries):
        _core.fail("accepted manifest contains duplicate paths")

    total_match = re.search(
        r"^total_accepted_words:[ \t]*(\d+)[ \t]*$", text, re.MULTILINE
    )
    if not total_match:
        _core.fail("manifest missing total_accepted_words")
    total = int(total_match.group(1))

    title_match = re.search(r'^title:[ \t]*"([^"]+)"', text, re.MULTILINE)
    if not title_match or title_match.group(1) != "Veridrift":
        _core.fail("manifest title must be Veridrift")
    if 'status: "publication_master_frozen"' not in text:
        _core.fail("manifest status must record the publication master frozen state")
    if 'copyedit_completed: "2026-07-18"' not in text:
        _core.fail("manifest must record completed copyedit")
    if 'publication_readiness: "publication_ready_upload_ready"' not in text:
        _core.fail("manifest publication readiness must be publication ready and upload ready")
    if (
        'publication_package_status: "cleared_as_frozen_publication_package"'
        not in text
    ):
        _core.fail("manifest must record the cleared frozen publication package")
    if not re.search(r"^prose_frozen:[ \t]*true[ \t]*$", text, re.MULTILINE):
        _core.fail("manifest must record frozen accepted prose")

    accepted_sum = sum(entry.words for entry in entries)
    if accepted_sum != total:
        _core.fail(
            "manifest total does not equal the sum of accepted entry word counts: "
            f"{total:,} vs {accepted_sum:,}"
        )
    return entries, total, text


def _validate_control_metadata(root: Path, total: int) -> None:
    """Use full canonical controls in-repo and legacy-minimal controls in test fixtures."""
    if root.resolve() == _core.ROOT.resolve():
        _STRICT_CONTROL_VALIDATOR(root, total)
        return

    files = (
        root / "README.md",
        root / "books/book-01/control/README.md",
        root / "books/book-01/control/51-publication-readiness-status.md",
    )
    texts = {path: _core._read(path) for path in files}
    combined = "\n".join(texts.values())

    for literal in _core.STALE_CONTROL_LITERALS:
        if literal in combined:
            _core.fail(f"stale control metadata remains: {literal!r}")

    formatted_total = f"{total:,}"
    raw_total = str(total)
    for path, text in texts.items():
        if formatted_total not in text and raw_total not in text:
            _core.fail(
                f"control metadata in {path.relative_to(root)} does not contain "
                f"accepted total {formatted_total}"
            )

    control = texts[root / "books/book-01/control/README.md"]
    status = texts[root / "books/book-01/control/51-publication-readiness-status.md"]
    if "Prologue and Chapters 1–24" not in control:
        _core.fail("control README does not identify Prologue and Chapters 1–24")
    if "Prologue + Chapters 1–24" not in status:
        _core.fail("publication status does not identify Prologue + Chapters 1–24")
    if _core.FINAL_LINE not in control or _core.FINAL_LINE not in status:
        _core.fail("control files do not preserve the final line")

    lower = combined.lower()
    if "original 02:14" not in lower:
        _core.fail("control metadata does not preserve the original 02:14 open thread")
    if "sterling" not in lower or "personal" not in lower or "unresolved" not in lower:
        _core.fail("control metadata does not preserve Sterling's unresolved personal-command thread")


_core.parse_manifest = _parse_final_package_manifest
_core.validate_control_metadata = _validate_control_metadata
parse_manifest = _parse_final_package_manifest
validate_control_metadata = _validate_control_metadata

if __name__ == "__main__":
    _core.main()
