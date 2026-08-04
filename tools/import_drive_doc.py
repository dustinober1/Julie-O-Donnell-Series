#!/usr/bin/env python3
"""Normalize a Google Drive MCP text export into a repository Markdown file.

Used by the Book 2 Drive-to-GitHub migration. The MCP read_file_content tool
returns ``{"fileContent": "..."}``; for large documents that payload is written
to a file on disk rather than returned inline. This tool turns either form into
a committed Markdown file carrying a provenance header.

Normalization is deliberately conservative. It undoes Google-export escaping and
paragraph padding and nothing else: no rewrapping, no heading inference beyond
what the export already marks, and no prose changes. Anything it cannot do
safely is left alone for a human to look at.

Usage:
    python3 tools/import_drive_doc.py \\
        --payload /path/to/mcp-result.txt \\
        --output books/book-02/control/03-decision-log.md \\
        --title "03 - Book 2 Decision Log & Canon Ledger" \\
        --file-id 19UxBut... --parent "02_BOOK 2/00_CURRENT CONTROL & QA" \\
        --modified 2026-07-26T01:03:24.215Z \\
        --authority "active Book 2 canon ledger"
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Google's Markdown export escapes characters that are Markdown-significant.
ESCAPES = {
    r"\*": "*", r"\_": "_", r"\[": "[", r"\]": "]", r"\(": "(", r"\)": ")",
    r"\#": "#", r"\+": "+", r"\-": "-", r"\.": ".", r"\!": "!", r"\`": "`",
    r"\>": ">", r"\|": "|", r"\~": "~", r"\\": "\\",
}


def normalize(text: str) -> str:
    # The export pads every paragraph with a trailing two-space line and blank
    # lines. Strip the padding without collapsing intentional blank lines.
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"\n[ \t]+\n", "\n\n", text)

    for escaped, plain in ESCAPES.items():
        text = text.replace(escaped, plain)

    lines = [line.rstrip() for line in text.split("\n")]

    # Numbered list items export as "1\." which the escape pass turns into "1."
    # already; nothing further is needed. Collapse runs of 3+ blank lines to 2.
    out: list[str] = []
    blanks = 0
    for line in lines:
        if line:
            blanks = 0
            out.append(line)
        else:
            blanks += 1
            if blanks <= 1:
                out.append(line)
    return "\n".join(out).strip() + "\n"


def load_payload(path: Path) -> str:
    raw = path.read_text(encoding="utf-8")
    try:
        return json.loads(raw)["fileContent"]
    except (json.JSONDecodeError, KeyError, TypeError):
        # Allow a plain-text payload too.
        return raw


def header(args: argparse.Namespace) -> str:
    lines = [
        "<!--",
        "Migration provenance",
        f"Drive title: {args.title}",
        f"Drive file ID: {args.file_id}",
        f"Drive parent: {args.parent}",
        f"Drive modified: {args.modified}",
        f"Imported: {args.imported}",
        "Import method: Google Drive MCP read_file_content text representation",
        f"Authority: {args.authority}",
        "Normalization: line endings, Google-export escape sequences, and paragraph spacing only",
    ]
    if args.note:
        lines.append(f"Note: {args.note}")
    lines.append("-->")
    return "\n".join(lines) + "\n\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--payload", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--file-id", required=True)
    parser.add_argument("--parent", required=True)
    parser.add_argument("--modified", required=True)
    parser.add_argument("--authority", required=True)
    parser.add_argument("--imported", default="2026-08-04")
    parser.add_argument("--note", default="")
    args = parser.parse_args()

    body = normalize(load_payload(args.payload))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(header(args) + body, encoding="utf-8")

    words = len(body.split())
    print(f"Wrote {args.output} — {words:,} words, {len(body):,} characters")


if __name__ == "__main__":
    main()
