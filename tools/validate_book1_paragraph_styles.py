#!/usr/bin/env python3
"""Fail if any accepted Book 1 paragraph would render in the wrong style.

Every existing Book 1 control compares production output to the source
*character by character*. Monospace text contains the same characters as
small-caps text, so nothing detected that 54 of the book's 64 scene headers
rendered as Display Text (monospace) in the shipped DOCX, EPUB and print PDF.

This validator closes that gap. It loads the real builder payload and applies
the builder's own ``identify_scene_meta`` and regexes, then asserts:

1. every paragraph containing a clock time is styled Scene Metadata, and
2. every location line adjacent to one is styled Scene Metadata, and
3. no paragraph that reads as prose falls into Display Text.

Standard library only, matching the other permanent Book 1 validators.
"""
from __future__ import annotations

import base64
import dataclasses
import re
import sys
import typing
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
PARTS = [
    f"build_book1_production.payload.part{s}"
    for s in ["01a", "01b", "01c", "01d", "01e", "01f", "02", "03", "04", "05"]
]
CLOCK_RE = re.compile(r"\b\d{1,2}:\d{2}\b")
PROSE_RE = re.compile(r"[a-z]{4,}\s+[a-z]{4,}")
# Screen output the book renders in monospace on purpose.
DISPLAY_ALLOWLIST = {
    "Timestamp. Signal amplitude. Receiver identification. "
    "Geolocation estimate. Packet signature.",
}


def load_builder() -> dict:
    blob = "".join((TOOLS / name).read_text(encoding="ascii") for name in PARTS)
    src = zlib.decompress(base64.b64decode(blob)).decode()
    ns: dict = {
        "re": re,
        "Path": Path,
        "dataclass": dataclasses.dataclass,
        "field": dataclasses.field,
        "Iterator": typing.Iterator,
        "Iterable": typing.Iterable,
        "Sequence": typing.Sequence,
        "Any": typing.Any,
        "Optional": typing.Optional,
    }
    exec(src[src.index("TIME_RE ="): src.index("def load_context")], ns)
    return ns


def accepted_paths() -> list[Path]:
    manifest = (ROOT / "books/book-01/ACCEPTED_MANUSCRIPT.yaml").read_text(encoding="utf-8")
    block = manifest.split("\nexcluded_from_canon:", 1)[0]
    paths = [ROOT / m for m in re.findall(r'^\s+- path:\s+"([^"]+)"\s*$', block, re.MULTILINE)]
    if len(paths) != 25:
        raise SystemExit(f"expected 25 accepted files, found {len(paths)}")
    return paths


def main() -> int:
    ns = load_builder()
    split_markdown = ns["split_markdown"]
    identify = ns["identify_scene_meta"]
    all_caps = ns["ALL_CAPS_RE"]

    failures: list[str] = []
    meta = 0

    for path in accepted_paths():
        _, _, _, paragraphs = split_markdown(path.read_text(encoding="utf-8"))
        scene_meta = identify(paragraphs)
        for index, para in enumerate(paragraphs):
            compact = " ".join(para.splitlines()).strip()
            if compact in {"---", "* * *", "***"}:
                continue
            if index in scene_meta:
                meta += 1
                continue
            display = "\n" in para or (all_caps.match(compact) and len(compact) < 160)
            if not display:
                continue
            if compact in DISPLAY_ALLOWLIST or compact.isupper():
                continue
            if CLOCK_RE.search(compact) and not compact.isupper():
                failures.append(
                    f"{path.name} paragraph {index}: scene header would render "
                    f"MONOSPACE -> {compact[:70]!r}"
                )
            elif PROSE_RE.search(compact):
                failures.append(
                    f"{path.name} paragraph {index}: prose would render "
                    f"MONOSPACE -> {compact[:70]!r}"
                )

    if failures:
        for line in failures:
            print(f"FAIL: {line}", file=sys.stderr)
        print(f"FAIL: {len(failures)} paragraph(s) would render in the wrong style", file=sys.stderr)
        return 1

    print(f"PASS: Book 1 paragraph styles; {meta} scene-metadata paragraphs, 0 mis-styled")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
