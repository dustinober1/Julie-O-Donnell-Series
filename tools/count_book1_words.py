#!/usr/bin/env python3
"""Count accepted Book 1 Markdown words using the repository's locked method.

Method: ``len(Path(path).read_text(encoding="utf-8").split())`` for every
``accepted_files`` entry in ``books/book-01/ACCEPTED_MANUSCRIPT.yaml``.
The script uses only the Python standard library and does not change files.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
MANIFEST = REPO_ROOT / "books/book-01/ACCEPTED_MANUSCRIPT.yaml"
PATH_RE = re.compile(r'^\s{4}path:\s*["\']?([^"\']+?)["\']?\s*$')


def accepted_paths(manifest: Path = MANIFEST) -> list[Path]:
    """Return accepted prose paths in manifest order without a YAML dependency."""
    in_accepted = False
    paths: list[Path] = []
    for line in manifest.read_text(encoding="utf-8").splitlines():
        if line == "accepted_files:":
            in_accepted = True
            continue
        if in_accepted and line and not line.startswith(" "):
            break
        if in_accepted:
            match = PATH_RE.match(line)
            if match:
                paths.append(REPO_ROOT / match.group(1))
    if not paths:
        raise ValueError(f"No accepted prose paths found in {manifest}")
    return paths


def count_words(path: Path) -> int:
    return len(path.read_text(encoding="utf-8").split())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--expect",
        type=int,
        help="Exit nonzero unless the accepted total equals this value.",
    )
    args = parser.parse_args()

    total = 0
    for path in accepted_paths():
        if not path.is_file():
            print(f"missing: {path.relative_to(REPO_ROOT)}", file=sys.stderr)
            return 2
        words = count_words(path)
        total += words
        print(f"{words:>6}  {path.relative_to(REPO_ROOT)}")

    print(f"{total:>6}  TOTAL")
    if args.expect is not None and total != args.expect:
        print(f"expected {args.expect}, found {total}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
