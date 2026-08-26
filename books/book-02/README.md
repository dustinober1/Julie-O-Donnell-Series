# Book 2

Second novel in the Julie O'Donnell series. Untitled. In early drafting.

**This repository is the source of truth for Book 2.** Book 2 was migrated out of Google Drive on 2026-08-04; see `migration/drive-to-github-2026-08-04/`. Drive now holds archived snapshots only and cannot establish or change Book 2 canon.

## State

Two of thirty-eight planned narrative units exist.

| Unit | Title | Status | Words |
|---|---|---|---|
| Prologue | The Warning That Cannot Have Happened | undrafted | 1,800–2,200 planned |
| Chapter 1 | A Written Boundary | **formally accepted canon** | 2,722 |
| Chapter 2 | The Missing Architect | draft complete, pending formal acceptance | 2,875 |

Planned: prologue plus Chapters 1–37 across five acts, approximately 109,800 words.

Continuity tooling and the first findings against it are recorded in `control/11-continuity-tooling-and-first-findings.md`. Run `python3 tools/count_book2_words.py` for the word counts and `python3 tools/check_book1_detail_rules.py --book 2` for the continuity rules; both run in CI.

Machine-readable state is in `MANUSCRIPT_STATUS.yaml`. A file existing here does not make it accepted canon; acceptance is recorded per unit.

## Layout

- `manuscript/` — chapter prose. Acceptance state is recorded in each file's provenance header and in `MANUSCRIPT_STATUS.yaml`.
- `control/` — authority, canon handoff, decisions, and per-chapter drafting and acceptance records.
- `outline/` — premise, chapter architecture, scene architecture, and mission locks.

Start at `control/00-control-center.md`. The controlling premise is `control/04-premise-and-story-architecture-lock.md`; locked canon is `control/03-decision-log-and-canon-ledger.md` (Decisions 001–149).

## The premise, in one line

A public-safety warning at a Canadian dam is withdrawn because its normalized chronology places an effect before its cause, and the scientist who designed the binational warning architecture has a transfer record with no corresponding acceptance on the other side.

## Rules carried from Book 1

These come from `control/01-book-1-to-book-2-canon-handoff.md` and `series/recurring-character-ledger.md`, and they constrain every chapter:

- Julie has no clearance, standing credential, police power, or authority over her own unresolved case.
- Her Book 1 legal exposure — unauthorized access, classified-material removal, scope overrun — remains unresolved.
- Her right wrist remains immobilized.
- Every case begins with a written mandate naming authority, question, jurisdiction, classification boundary, and scope-change responsibility.
- Source originals stay with lawful custodians. Proof limits travel with findings.
- Returning characters retain counsel, consent, and an enforceable right to stop. Elias may not be contacted except through counsel.
- Argus is not sentient. The danger is human.

## Open items

- Book 2 has no title.
- The prologue is undrafted, and two conflicting prologue designs existed in Drive. The chapter architecture controls; the superseded Duffield data-center design is retained in `outline/01-prologue-situation-and-scene-lock.md` and marked. See conflict BC-02.
- `05 - Book 2 Act Architecture` is cited as governing authority by six documents but does not exist in Drive. Act-level content is covered by `outline/06-chapter-architecture.md` §4. See conflict BC-04.
