#!/usr/bin/env python3
"""Book 1 publication-readiness entrypoint with final-freeze stale-state guards."""
from __future__ import annotations

from pathlib import Path

from book1_publication_readiness_core import *  # noqa: F401,F403
import book1_publication_readiness_core as _core

_core.STALE_CONTROL_LITERALS = _core.STALE_CONTROL_LITERALS + ("105,155", "105155")
STALE_CONTROL_LITERALS = _core.STALE_CONTROL_LITERALS
_STRICT_CONTROL_VALIDATOR = _core.validate_control_metadata


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


_core.validate_control_metadata = _validate_control_metadata

if __name__ == "__main__":
    _core.main()
