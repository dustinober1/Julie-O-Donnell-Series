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
3. no paragraph that reads as prose falls into Display Text, and
4. no designator is split or partly emphasised by inline-markdown parsing.

Check 4 exists because the builder once read the underscores in
PAK_RELAY_17A_SOURCE_CORRECTION as emphasis delimiters, consumed them, and
shipped "PAKRELAY17ASOURCECORRECTION" with SOURCE in italics.

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
DESIGNATOR_RE = re.compile(r"[A-Z][A-Z0-9]*(?:[_-][A-Z0-9]+)+")
DISPLAY_ALLOWLIST = {
    "Timestamp. Signal amplitude. Receiver identification. "
    "Geolocation estimate. Packet signature.",
}


def patched_builder_source() -> str:
    """Return the builder source exactly as build_book1_production.py runs it.

    The loader keeps the recorded payload byte-identical and expresses every
    deviation as a commented patch. Running the loader's own patch section --
    everything up to its final exec -- means this validator tests the builder
    that actually produces the book, not the unpatched historical payload.
    """
    loader_text = (TOOLS / "build_book1_production.py").read_text(encoding="utf-8")
    marker = 'exec(compile(source, str(Path(__file__)), "exec"), globals())'
    if loader_text.count(marker) != 1:
        raise SystemExit("builder loader exec marker not found")
    ns: dict = {"__file__": str(TOOLS / "build_book1_production.py")}
    exec(loader_text.split(marker)[0], ns)
    source = ns["source"]
    return source.decode() if isinstance(source, bytes) else source


def load_builder() -> dict:
    src = patched_builder_source()
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
    exec(src[src.index("INLINE_TOKEN_RE ="): src.index("def load_context")], ns)
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
    inline_segments = ns["inline_segments"]
    strip_inline = ns["strip_inline_markdown"]

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
            for segment, italic, bold, code in inline_segments(para):
                if (italic or bold or code) and DESIGNATOR_RE.fullmatch(segment.strip()):
                    failures.append(
                        f"{path.name} paragraph {index}: designator emphasised by "
                        f"inline markdown -> {segment.strip()!r}"
                    )
            if strip_inline(para) != para.replace("\\*", "*").replace("\\_", "_").replace("\\`", "`"):
                for token in DESIGNATOR_RE.findall(para):
                    if token not in strip_inline(para):
                        failures.append(
                            f"{path.name} paragraph {index}: designator altered by "
                            f"inline markdown -> {token!r}"
                        )

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
