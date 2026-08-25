# 79. Chapter 24 Validator Retirement and Ending-Invariant Guard

**Date:** 2026-08-25
**Trigger:** `78-act-iii-correction-record.md` §7 recorded `tools/validate_book1_chapter24.py` as failing, and as having failed identically before that change.
**Action:** retired and replaced.

---

## 1. Why it failed

The validator mixed two incompatible jobs in one file.

**A one-shot scope gate.** It pinned a base commit (`d8adea1…`), an exact changed-file set, and git blob hashes for twelve Act III chapters plus six control documents. That gate had one correct moment — the Chapter 24 acceptance PR — and could never pass again afterwards, by construction.

**A set of content invariants.** Chapter 24's opening, its ending, twenty-four required elements, and fourteen prohibited conclusions.

The first job broke the moment the developmental revision landed, and it took the second down with it. Because the file exits on the first failure, and the blob comparison ran first, **the content checks had not executed in months.** The ending guard was dark.

## 2. What was actually stale

Measured against the current manuscript before retirement:

| Pinned value | Pinned to | Actual |
|---|---|---|
| Book total | 124,779 | 109,498 |
| Act III subtotal | 61,124 | — structure changed |
| Chapter 24 words | 3,362 | 3,115 |
| Chapter 24 movements | `[800, 739, 673, 1147]` | `[765, 594, 513, 436, 803]` |
| Chapter 24 opening | `15:04:44 EDT / 00:34:44 IST` before the heading | heading first, then `October 16` |
| Required elements | 24 | **19 no longer exist** |

Chapter 24 was rewritten during the developmental revision: five movements, not four, and a different header order. Re-pinning those numbers to today's text would have rebuilt the same trap.

**One part was still true and still valuable.** All fourteen prohibited conclusions were absent, and five of the required elements survived. A negative invariant — *this must never be asserted* — does not rot when prose is revised. That is the part worth keeping.

## 3. The replacement

`tools/validate_book1_ending_invariants.py`. Nothing in it is pinned to a word count, a blob, or a commit.

| Check | Scope | Note |
|---|---|---|
| Prohibited conclusions | **whole accepted manuscript** | was Chapter 24 only |
| Final line exact | Chapter 24 | `The bubble stayed centered.` |
| Chapter 24 structural identity | Chapter 24 | anchored on heading text and location, not bytes |
| Required elements | Chapter 24 | 5, down from 24 — only those that survived revision |
| Series threads left open | Chapter 24 | new; the positive counterpart to the prohibited list |
| No Chapter 25 artifact | repository | retained |
| Accepted file count | manuscript | 25 |

The prohibited list grew from 14 entries to 31, covering both deliberate carryovers: Sterling's personal knowledge, direction, possession or command, and the human or upstream instruction behind the original 02:14 construction.

**Every entry is a literal, never a pattern.** The prose repeatedly *denies* these propositions — `It does not prove Senator Sterling held it`, `They did not have Sterling's command` — so a regex on `Sterling (held|commanded)` would fire on exactly the sentences that enforce the ceiling. Four candidate additions were rejected for this reason after checking their context:

- `Vance ordered` — appears in Chapter 22 inside a declaration being struck: *"Did you hear him say that?" "No." "Then it stays struck."*
- `Sterling personally` — appears only in limiting constructions and as an open question.
- `Julie was cleared` — Chapter 16, medical clearance for continued custody.
- `case closed` — the aluminum case, and a description of a job.

Each surviving entry was verified absent from the manuscript when added, and a test asserts that permanently, so no future addition can turn the validator permanently red.

## 4. Negative controls

`tools/test_book1_ending_invariants.py`, ten tests. Eight inject a defect, assert the validator fires, restore the file, and re-assert clean:

- the final line changed;
- a prohibited conclusion in Chapter 24;
- a prohibited conclusion **in Chapter 1** — the retired validator would have passed this;
- a series thread closed;
- a required element removed;
- drafting residue (`TODO`);
- the chapter title changed.

Two are structural: every prohibited phrase is absent from the manuscript, and the validator's own source contains no pinned hash or word count — the failure mode that killed its predecessor, asserted against.

## 5. CI

Both are now in `book1-manuscript-validation.yml`, which the retired validator never was. A following step confirms the negative controls restored the manuscript, so a mid-test failure cannot leave mutated prose behind.

## 6. Effect

The ending guard is running again for the first time since the developmental revision, it covers the whole book rather than one chapter, it is in CI, and it is built so that ordinary revision does not break it.

No prose changed. The accepted total remains **109,498 words across 25 files**; `78-act-iii-correction-record.md` remains the current publication-master freeze record.
