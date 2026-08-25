#!/usr/bin/env python3
"""Load the deterministic Book 1 production builder from checked-in payload parts."""
from __future__ import annotations

import base64
import hashlib
import zlib
from pathlib import Path

PAYLOAD_SHA256 = "4fcb8764f380866501fed8fb653d746a25b7bc96622031c09ecbb1ff2edebd8d"
SOURCE_SHA256 = "3f9f3adaf0c3b3bd4a68e2200589ba54f1cb5c32d5f02b5eb32646725654e0ae"
PATCHED_SOURCE_SHA256 = "6955c940a369e45fe7ea6e4481f46309722d03e759d70ba205c489f946193b62"
base = Path(__file__).resolve().parent
names = [
    "build_book1_production.payload.part01a",
    "build_book1_production.payload.part01b",
    "build_book1_production.payload.part01c",
    "build_book1_production.payload.part01d",
    "build_book1_production.payload.part01e",
    "build_book1_production.payload.part01f",
    "build_book1_production.payload.part02",
    "build_book1_production.payload.part03",
    "build_book1_production.payload.part04",
    "build_book1_production.payload.part05",
]
parts = [base / name for name in names]
missing = [p.name for p in parts if not p.is_file()]
if missing:
    raise SystemExit(f"Production builder payload inventory is incomplete: {missing}")
payload = "".join(p.read_text(encoding="ascii") for p in parts)
if hashlib.sha256(payload.encode("ascii")).hexdigest() != PAYLOAD_SHA256:
    raise SystemExit("Production builder payload checksum mismatch")
source = zlib.decompress(base64.b64decode(payload))
if hashlib.sha256(source).hexdigest() != SOURCE_SHA256:
    raise SystemExit("Production builder source checksum mismatch")
old = b'''def extract_pdf_text(path: Path) -> str:\n    reader = PdfReader(str(path))\n    return "\\n".join((page.extract_text() or "") for page in reader.pages)\n\n\ndef validate_pdf_chars(ctx: BuildContext, pdf_text: str) -> tuple[bool, str, str]:\n    lines = [line.strip() for line in pdf_text.splitlines() if line.strip()]\n    headings = {e.heading for e in ctx.entries}\n    headings_upper = {e.heading.upper() for e in ctx.entries}\n    filtered: list[str] = []\n    in_body = False\n    for line in lines:\n        if line == ctx.entries[0].heading:\n            in_body = True\n            continue\n        if not in_body:\n            continue\n        if line in headings or line in headings_upper or line == "VERIDRIFT" or line == "* * *" or re.fullmatch(r"\\d+", line):\n            continue\n        filtered.append(line)\n    got = normalized_chars("".join(filtered))\n    expected = normalized_chars("".join(strip_inline_markdown(p) for e in ctx.entries for p in e.paragraphs if " ".join(p.split()).strip() not in {"---", "* * *", "***"}))\n    return got == expected, sha256_bytes(expected.encode()), sha256_bytes(got.encode())\n'''
new = b'''def extract_pdf_text(path: Path) -> str:\n    reader = PdfReader(str(path))\n    return "\\n\\f\\n".join((page.extract_text() or "") for page in reader.pages)\n\n\ndef validate_pdf_chars(ctx: BuildContext, pdf_text: str) -> tuple[bool, str, str]:\n    headings = {normalized_chars(e.heading): e.heading for e in ctx.entries}\n    headings_upper = {normalized_chars(e.heading.upper()): e.heading for e in ctx.entries}\n    first_heading = normalized_chars(ctx.entries[0].heading)\n    filtered: list[str] = []\n    in_body = False\n    for page_text in pdf_text.split("\\f"):\n        lines = [line.strip() for line in page_text.splitlines() if line.strip()]\n        if lines and re.fullmatch(r"\\d+", lines[0]):\n            lines.pop(0)\n        for count in range(1, min(4, len(lines)) + 1):\n            candidate = normalized_chars("".join(lines[:count]))\n            if candidate in headings or candidate in headings_upper:\n                if candidate == first_heading:\n                    in_body = True\n                lines = lines[count:]\n                break\n        if lines and lines[0] == "VERIDRIFT":\n            lines.pop(0)\n        if not in_body:\n            continue\n        filtered.extend(line for line in lines if line != "* * *")\n    got = normalized_chars("".join(filtered))\n    expected = normalized_chars("".join(strip_inline_markdown(p) for e in ctx.entries for p in e.paragraphs if " ".join(p.split()).strip() not in {"---", "* * *", "***"}))\n    return got == expected, sha256_bytes(expected.encode()), sha256_bytes(got.encode())\n'''
if source.count(old) != 1:
    raise SystemExit("Production builder PDF validator patch target mismatch")
source = source.replace(old, new)
if hashlib.sha256(source).hexdigest() != PATCHED_SOURCE_SHA256:
    raise SystemExit("Patched production builder source checksum mismatch")

# PR #92 advanced the accepted-manifest readiness state after this immutable
# builder payload was recorded. Preserve payload and PDF-patch integrity, then
# update only the validation comparison.
legacy_readiness_check = (
    b'if manifest.get("publication_readiness") != '
    b'"proofread_and_production_required":'
)
current_readiness_check = (
    b'if manifest.get("publication_readiness") != '
    b'"publication_ready_upload_ready":'
)
if source.count(legacy_readiness_check) != 1:
    raise SystemExit("Production builder readiness-check patch target mismatch")
source = source.replace(legacy_readiness_check, current_readiness_check)

# A reproducibility run may regenerate historical proof records, but it must not
# reopen a final approval record that PR #92 has already cleared. Legacy branches
# still receive the historical pending-approval template.
legacy_approval_write = (
    b'(ctx.root / CONTROL_DIR_REL / "69-production-proof-approval.md")'
    b'.write_text(approval, encoding="utf-8")'
)
current_approval_write = b'''approval_path = ctx.root / CONTROL_DIR_REL / "69-production-proof-approval.md"\n    approval_is_final = (\n        approval_path.is_file()\n        and "cleared_as_frozen_publication_package"\n        in approval_path.read_text(encoding="utf-8")\n    )\n    if not approval_is_final:\n        approval_path.write_text(approval, encoding="utf-8")'''
if source.count(legacy_approval_write) != 1:
    raise SystemExit("Production builder approval-record patch target mismatch")
source = source.replace(legacy_approval_write, current_approval_write)

# The recorded builder marks a scene header only when a paragraph BEGINS with a
# clock time, then absorbs neighbouring header lines by walking backward and
# never forward. Two consequences shipped in the frozen package: Act III places
# the location lines AFTER the date and time, so they never joined the header,
# and the adjacency test rejected any line ending in ".", which is
# "Washington, D.C.". Unreached header lines fall through to the Display Text
# branch and render in MONOSPACE; 54 of the book's 64 scene headers were
# affected. Character-level cross-format validation cannot detect it, because
# monospace text carries the same characters as small-caps text.
# See books/book-01/control/76-production-quality-pass.md.
legacy_scene_meta = b'def identify_scene_meta(paragraphs: tuple[str, ...]) -> frozenset[int]:\n    marked: set[int] = set()\n    for i, para in enumerate(paragraphs):\n        one_line = " ".join(para.splitlines()).strip()\n        if TIME_RE.match(one_line):\n            marked.add(i)\n            j = i - 1\n            while j >= 0 and i - j <= 3:\n                candidate = " ".join(paragraphs[j].splitlines()).strip()\n                if not candidate or len(candidate) > 90 or candidate.startswith(("\xe2\x80\x9c", \'"\')):\n                    break\n                if candidate.endswith((".", "?", "!", ":", ";")):\n                    break\n                if candidate in {"* * *", "---"}:\n                    break\n                marked.add(j)\n                j -= 1\n    return frozenset(marked)'
current_scene_meta = b'ABBREV_TAIL_RE = re.compile(r"\\b(?:[A-Z]\\.){2,}$")\n\n\ndef _scene_meta_adjacent(candidate: str) -> bool:\n    """True when a line can join the scene header beside a time line."""\n    if not candidate or len(candidate) > 90 or candidate.startswith(("\xe2\x80\x9c", \'"\')):\n        return False\n    if candidate in {"* * *", "---"}:\n        return False\n    if candidate.endswith(("?", "!", ":", ";")):\n        return False\n    # A trailing period ends a sentence, except in an abbreviation such as\n    # "Washington, D.C.", which is a location line rather than prose.\n    if candidate.endswith(".") and not ABBREV_TAIL_RE.search(candidate):\n        return False\n    return True\n\n\ndef identify_scene_meta(paragraphs: tuple[str, ...]) -> frozenset[int]:\n    marked: set[int] = set()\n    for i, para in enumerate(paragraphs):\n        one_line = " ".join(para.splitlines()).strip()\n        if TIME_RE.match(one_line):\n            marked.add(i)\n            j = i - 1\n            while j >= 0 and i - j <= 3:\n                candidate = " ".join(paragraphs[j].splitlines()).strip()\n                if not _scene_meta_adjacent(candidate) or TIME_RE.match(candidate):\n                    break\n                marked.add(j)\n                j -= 1\n            k = i + 1\n            while k < len(paragraphs) and k - i <= 3:\n                candidate = " ".join(paragraphs[k].splitlines()).strip()\n                if not _scene_meta_adjacent(candidate) or TIME_RE.match(candidate):\n                    break\n                marked.add(k)\n                k += 1\n    return frozenset(marked)'
if source.count(legacy_scene_meta) != 1:
    raise SystemExit("Production builder scene-metadata patch target mismatch")
source = source.replace(legacy_scene_meta, current_scene_meta)

# Control records 74, 76 and 78 moved the accepted total and changed Chapter 20's
# bytes and word count: 78- inserted the counsel-supervised Vance interview after
# the LSS Drennan section. Chapter 20's final sentence is untouched and stays
# locked verbatim, which is what the ending guard is actually for.
for legacy_lock, current_lock in (
    (b"EXPECTED_TOTAL = 105_157", b"EXPECTED_TOTAL = 109_498"),
    (b"EXPECTED_CH20_WORDS = 2363", b"EXPECTED_CH20_WORDS = 3301"),
    (b'EXPECTED_CH20_SHA = "9a18f6c51e652a2ae3e640f105d5cba288103891703e74a450e9e70cb80c986e"',
     b'EXPECTED_CH20_SHA = "7f6022b5a55cb5109326643ef4cdec980049c48433a6950a3c224212646f1645"'),
):
    if source.count(legacy_lock) != 1:
        raise SystemExit(f"Production builder lock patch target mismatch: {legacy_lock!r}")
    source = source.replace(legacy_lock, current_lock)

# The recorded builder treats "_" as an emphasis delimiter. The accepted prose
# contains underscores in exactly one place -- the identifier PAK_RELAY_17A and its
# derivative PAK_RELAY_17A_SOURCE_CORRECTION, ten occurrences -- and never as
# emphasis; the book's only italic run is *analyst delay* in the prologue. The
# builder therefore consumed those underscores and italicised the interior,
# shipping "PAKRELAY17ASOURCECORRECTION" with SOURCE in italics across DOCX, EPUB
# and PDF. Character-level cross-format validation cannot see it: both sides of
# the comparison run through strip_inline_markdown, so both drop the underscores.
# Removing "_" from the tokeniser and the stripper preserves the identifier.
# See books/book-01/control/76-production-quality-pass.md.
for legacy_inline, current_inline in (
    (b'INLINE_TOKEN_RE = re.compile(r"(\\*\\*[^*]+\\*\\*|(?<!\\*)\\*[^*]+\\*(?!\\*)|_[^_]+_|`[^`]+`)")',
     b'INLINE_TOKEN_RE = re.compile(r"(\\*\\*[^*]+\\*\\*|(?<!\\*)\\*[^*]+\\*(?!\\*)|`[^`]+`)")'),
    (b'    text = re.sub(r"_([^_]+)_", r"\\1", text)\n', b""),
):
    if source.count(legacy_inline) != 1:
        raise SystemExit(f"Production builder inline-markdown patch target mismatch: {legacy_inline!r}")
    source = source.replace(legacy_inline, current_inline)

# Two literals in the recorded builder still name the PR #85 state: the build
# record template hardcodes the accepted word count, and one validation message
# names the old total. Both are now derived. The readiness strings in the same
# templates are left alone: they describe the gate a fresh proof build sits
# behind, not the manifest field, which the loader already patches above.
for legacy_text, current_text in (
    (b'- Accepted words: 105,157',
     b'- Accepted words: {EXPECTED_TOTAL:,}'),
    (b'- Chapter 20: 2,363 words;',
     b'- Chapter 20: {EXPECTED_CH20_WORDS:,} words;'),
    (b'errors.append("manifest total is not 105157")',
     b'errors.append(f"manifest total is not {EXPECTED_TOTAL}")'),
):
    if source.count(legacy_text) != 1:
        raise SystemExit(f"Production builder record-template patch target mismatch: {legacy_text!r}")
    source = source.replace(legacy_text, current_text)

exec(compile(source, str(Path(__file__)), "exec"), globals())
