#!/usr/bin/env python3
"""Compile the accepted Book 1 prose inventory after strict validation."""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

from validate_book1_publication_readiness import (
    ROOT,
    TARGET_MAX,
    TARGET_MIN,
    parse_manifest,
    validate_repository,
)

DEFAULT_OUTPUT = ROOT / "books/book-01/compiled/current/Veridrift_ACCEPTED.md"


def compile_book(
    root: Path,
    output: Path,
    *,
    target_min: int = TARGET_MIN,
    target_max: int = TARGET_MAX,
) -> tuple[int, str]:
    """Validate and concatenate accepted prose; return word count and output SHA-256."""
    root = root.resolve()
    output = output.resolve()
    total = validate_repository(root, target_min=target_min, target_max=target_max)
    entries, _manifest_total, _manifest_text = parse_manifest(root)

    sections = [
        (root / entry.path).read_text(encoding="utf-8").rstrip()
        for entry in entries
    ]
    compiled = "\n\n".join(sections) + "\n"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(compiled, encoding="utf-8")

    output_sha = hashlib.sha256(compiled.encode("utf-8")).hexdigest()
    manifest_path = root / "books/book-01/ACCEPTED_MANUSCRIPT.yaml"
    build = {
        "book": "Veridrift",
        "source_manifest": str(manifest_path.relative_to(root)),
        "source_manifest_sha256": hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
        "accepted_files": [entry.path for entry in entries],
        "accepted_words": total,
        "output": str(output.relative_to(root)) if output.is_relative_to(root) else str(output),
        "output_bytes": len(compiled.encode("utf-8")),
        "output_sha256": output_sha,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "authority": "Generated review compilation only; canonical prose remains the accepted manifest inventory.",
    }
    sidecar = output.with_suffix(output.suffix + ".build.json")
    sidecar.write_text(json.dumps(build, indent=2) + "\n", encoding="utf-8")
    return total, output_sha


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Markdown compilation path",
    )
    args = parser.parse_args()

    total, output_sha = compile_book(ROOT, args.output)
    print(
        f"PASS: compiled {total:,} accepted words to "
        f"{args.output.resolve()} sha256={output_sha}"
    )


if __name__ == "__main__":
    main()
