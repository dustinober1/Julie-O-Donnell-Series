# Book 2 Drive-to-GitHub Migration — 2026-08-04

Moves Book 2 out of Google Drive and into this repository, matching the governance already in force for Book 1 and the series controls.

**Authorization:** author instruction, 2026-08-04, to stop working out of the Google Drive folder.

**Result:** the repository is now the source of truth for Book 2. See `conflict-log.md` for the four conflicts found, including the fact that the Drive control documents explicitly forbade this.

## What moved

Julie O'Donnell Book 2 material only, from three Drive folders:

| Drive folder | Contents | Repository destination |
|---|---|---|
| `02_BOOK 2/01_Manuscript` | drafted chapters | `books/book-02/manuscript/` |
| `02_BOOK 2/00_CURRENT CONTROL & QA` | authority, canon, decisions, acceptance records | `books/book-02/control/` |
| `02_BOOK 2/02_Outline & Beats` | premise, architecture, mission locks | `books/book-02/outline/` |

Excluded: the folder documented in conflict BC-03, which holds a different series' control documents under Book 2 titles.

## Import method and its limits

Content was read through the Google Drive MCP `read_file_content` tool, which returns a text representation of each native Google Doc. **This is not a Drive-native Markdown export**, so the hashes recorded in `inventory.yaml` are computed over the committed repository files, not over a Drive export. They establish that the repository files have not changed since import; they cannot be compared against a Drive checksum.

Normalization applied to every file: line endings, Google export escape sequences (`\*`, `\[`, `\.`), paragraph spacing, and heading levels. Prose files additionally had curly typography restored to match Book 1 house style.

Every imported file carries a provenance header recording its Drive title, file ID, parent folder, modification time, and authority status.

## Prose fidelity verification

Both drafted chapters were verified against the word counts recorded independently in their Drive control documents, using the counting method those documents specify (`\b[\w]+(?:[’'\-][\w]+)*\b`, chapter heading and scene-break markers excluded):

| File | Counted after import | Recorded in Drive | Delta |
|---|---|---|---|
| `chapter-01.md` | 2,712 | 2,712 | 0 |
| `chapter-02.md` | 2,870 | 2,870 | 0 |

Scene distributions also match: 708/700/660/644 and 675/917/724/554.

## Import status

**Complete.** All fourteen Julie O'Donnell Book 2 documents found in the three enumerated Drive folders were imported:

| Destination | Words |
|---|---|
| `manuscript/chapter-01.md` | 2,712 (prose) |
| `manuscript/chapter-02.md` | 2,870 (prose) |
| `control/00-control-center.md` | amended on import, BC-01 |
| `control/01-book-1-to-book-2-canon-handoff.md` | |
| `control/02-development-blueprint.md` | |
| `control/03-decision-log-and-canon-ledger.md` | 83,951 |
| `control/04-premise-and-story-architecture-lock.md` | 68,839 |
| `control/08-chapter-01-drafting-authorization.md` | |
| `control/09-chapter-01-formal-acceptance.md` | |
| `control/10-chapter-02-drafting-authorization.md` | |
| `outline/00-premise-options-working.md` | superseded |
| `outline/01-prologue-situation-and-scene-lock.md` | superseded, BC-02 |
| `outline/06-chapter-architecture.md` | |
| `outline/07-scene-architecture-and-chapter-mission-locks.md` | 35,809 |

The three largest documents were imported through `tools/import_drive_doc.py`, which normalizes the Drive text export and writes the provenance header without routing the content through a conversation. Escape-residue checks came back clean on all three.

Coverage spot-checks: the decision log carries Decisions 001–149 and no Decision 150; the scene architecture covers the prologue through Chapter 37.

**One document could not be imported because it does not exist:** `05 - Book 2 Act Architecture`, cited as governing authority by six other documents. See `conflict-log.md` BC-04.

## Verification

`inventory.yaml` records every imported file with its Drive origin and a SHA-256 over the committed content.

To confirm nothing has drifted since import:

```bash
python3 - <<'PY'
import hashlib, pathlib, re
inv = pathlib.Path("migration/drive-to-github-2026-08-04/inventory.yaml").read_text()
bad = 0
for path, want in re.findall(r'path: "([^"]+)"\n\s+sha256: "([0-9a-f]{64})"', inv):
    got = hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()
    if got != want:
        print("MISMATCH", path); bad += 1
print("mismatches:", bad)
PY
```
