#!/usr/bin/env python3
"""Load the deterministic Book 1 production builder from checked-in payload parts."""
from __future__ import annotations

import base64
import hashlib
import zlib
from pathlib import Path

PAYLOAD_SHA256 = "4fcb8764f380866501fed8fb653d746a25b7bc96622031c09ecbb1ff2edebd8d"
SOURCE_SHA256 = "3f9f3adaf0c3b3bd4a68e2200589ba54f1cb5c32d5f02b5eb32646725654e0ae"
base = Path(__file__).resolve().parent
parts = sorted(base.glob("build_book1_production.payload.part*"))
if [p.name for p in parts] != [f"build_book1_production.payload.part{i:02d}" for i in range(1, 6)]:
    raise SystemExit(f"Production builder payload inventory is incomplete: {[p.name for p in parts]}")
payload = "".join(p.read_text(encoding="ascii") for p in parts)
if hashlib.sha256(payload.encode("ascii")).hexdigest() != PAYLOAD_SHA256:
    raise SystemExit("Production builder payload checksum mismatch")
source = zlib.decompress(base64.b64decode(payload))
if hashlib.sha256(source).hexdigest() != SOURCE_SHA256:
    raise SystemExit("Production builder source checksum mismatch")
exec(compile(source, str(Path(__file__)), "exec"), globals())
