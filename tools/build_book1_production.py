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
exec(compile(source, str(Path(__file__)), "exec"), globals())
