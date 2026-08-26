# 11. Book 2 Continuity Tooling and First Findings

**Date:** 2026-08-26
**Authority:** author direction, 2026-08-26, to correct the defects found and port Book 1's continuity tooling.
**Effect on canon:** Chapter 1 is untouched. Chapter 2 is corrected while still pending formal acceptance.

---

## 1. Why now

Book 2 had **no validation tooling of any kind**. Book 1 has ten validators and eight test suites; Book 2 had a hand-maintained YAML and nothing that could check it.

That mattered more than the file count suggests. **Book 2's premise is a chronology defect.** Chapter 1 turns on source clocks placing a downstream effect before the gate movement that supposedly caused it, across devices with different clock bases, synchronization states, and delay bounds. If the book's own arithmetic drifts anywhere across 109,800 planned words, the premise collapses. Book 1 shipped defect DC-01 — a derived date disagreeing with a stated one — with far less exposure, and a chronology error was caught by hand in Chapter 20 as recently as this month.

At 5,597 drafted words, installing the machinery costs almost nothing. At 105,000 it would be a retrofit.

## 2. Defects found

### D2-1 — the RCMP lead changed name and rank between chapters

| Source | Name |
|---|---|
| `manuscript/chapter-01.md` — **formally accepted canon** | Inspector **Amrita** Dhaliwal |
| `control/09-chapter-01-formal-acceptance.md` §Characters | Inspector **Amrita** Dhaliwal |
| `control/10-chapter-02-drafting-authorization.md` §5, §11 | Superintendent **Deepa** Dhaliwal |
| `manuscript/chapter-02.md` — draft, pending acceptance | Superintendent **Deepa** Dhaliwal |

Same character, same case, same Wednesday afternoon. Both chapters fall on 2027-06-23, so a promotion cannot explain the rank change.

**The defect originates in the control document, not the prose.** The Chapter 2 drafting authorization renamed and re-ranked her, and the draft followed its authorization faithfully. Nothing compared the authorization against the accepted chapter.

**Resolved** in favour of Chapter 1, which is accepted canon: `Inspector Amrita Dhaliwal`. Corrected in `chapter-02.md` (two occurrences) and in `10-chapter-02-drafting-authorization.md` (two occurrences). Chapter 1 was not edited.

### D2-2 — recorded word counts matched no method

`MANUSCRIPT_STATUS.yaml` recorded 2,712 and 2,870 words. Measured three defensible ways, the files give 2,706 / 2,859 (scene sums), 2,722 / 2,875 (prose after the migration provenance block), and 2,773 / 2,927 (whole file). The recorded figures match none of them; they came from pre-migration Drive tooling and became unverifiable at import.

**Resolved** by defining the method and building a counter — see §3 — then re-syncing. The hand-recorded `scene_words` arrays were **removed** rather than corrected: they cannot be reproduced from the prose without asserting a scene-splitting convention, and an unverifiable number in a control file is worse than no number.

Accepted 2,712 → **2,722**. Drafted 5,582 → **5,597**.

## 3. Tooling installed

| Tool | Purpose |
|---|---|
| `tools/book_profiles.py` | Everything that differs between books: source of truth, zones, artifact paths, time-anchor convention. |
| `tools/count_book2_words.py` | The locked counting method, `--expect` to gate CI, `--sync` to re-derive the recorded figures. |
| `tools/extract_book1_detail_index.py --book 2` | The detail index, over accepted **and drafted** prose. |
| `tools/check_book1_detail_rules.py --book 2` | Rules R1–R9 and the derived chronology. |
| `tools/test_book2_continuity.py` | 17 tests: negative controls plus Book 1 non-regression. |
| `.github/workflows/book2-continuity.yml` | Runs all of it on every push and pull request. |

**The tools keep their Book 1 names.** Roughly ten frozen Book 1 control records cite `extract_book1_detail_index.py` and `check_book1_detail_rules.py` by path. Renaming would orphan citations in documents that must not be rewritten, so the Book 1 name stays and `--book 2` selects the profile. This is recorded here because a reader will otherwise find it strange.

### Book 1 is unchanged, and that is asserted

The shared engine is the same code Book 1 depends on. Book 1's committed detail index and derived chronology are verified **byte-identical** by two tests in `test_book2_continuity.py`, which fired correctly during this work when a heading change moved Book 1's chronology by one line. Book 1's heading strings are now reproduced verbatim for that reason.

### Book 2's zones come from canon, not from invention

`outline/07-scene-architecture-and-chapter-mission-locks.md`: *"Canadian locations use PDT (UTC−7) during this period."* The profile declares PDT and UTC. **No American zone is defined**, because no control document establishes one yet; add it when one does.

### R2 needed a new anchor, or it was inert

Book 1 states narrative-present time in standalone scene headers. Book 2 states it inline — `At 15:34, Julie asked`. Run as-is, R2 checked **zero** timestamps: the single most valuable rule was silently doing nothing.

The Book 2 profile adds a **sentence-initial** inline anchor. Sentence-initial only, deliberately: a mid-sentence time is often a forward reference — *"the proposed session was set for 09:00 the following morning"* — and treating one as narrative present would invent a backward step that isn't there.

### R9 is new

R6 catches near-miss *spellings* of a recurring name. It could not catch D2-1, because `Amrita` and `Deepa` are not near-misses and each appears once. R9 flags a recurring surname that pairs with more than one given name or rank. It is a reporting rule — promotions happen and relatives share surnames.

Calibration mattered. The first version produced **41 findings on Book 1**, nearly all sentence-initial words read as given names (`And Apex`, `Can Chen`). A rule that cries wolf gets ignored. Three filters brought it to **3**:

1. place and organization nouns, and number words, are not surnames (`Fairfax County`, `Payload Eighty-Eight`);
2. a longer form containing a shorter one is one rank, not two (`Special Agent` is not a second rank for `Agent`);
3. a candidate given name is rejected only when it is **both** sentence-initial **and** attested in lowercase elsewhere in the book — two signals, so a real given name that opens a sentence still counts. This is what keeps `Deepa Dhaliwal sat at the daughter's left.` catchable while discarding `Direct Mercer to recover the media.`

Book 1's three surviving findings are correct: `Reed` pairs with Major and Colonel, a real promotion across the six-year gap, and `Park` collides with a place name. Both are asserted by test, in both directions.

## 4. Current Book 2 state

```
PASS: no hard-rule findings; 2 item(s) flagged for review
```

Both review items are R2 backward steps in Chapter 2, and both are the **deliberate concurrent intercut**: the captivity scene (15:12–15:47) straddles the two interview scenes (15:00–15:34, 15:35–16:17). R2 surfaces them for adjudication rather than failing, which is the correct behaviour — an accidental reversal would be indistinguishable from these without a human looking.

Recorded here so a later reader does not mistake a known intercut for an open defect.

## 5. Not done

- **Chapter 2 formal acceptance.** Still the next workstream. This record corrects a defect found in the draft; it does not accept the chapter.
- **The prologue** remains undrafted, and conflict BC-02 (two competing designs) is unresolved.
- **Book 2 still has no title.**
- **BC-04.** `05 - Book 2 Act Architecture` is cited as governing authority by six documents and does not exist. Note that `09-chapter-01-formal-acceptance.md` lists it under "Documents verified" — that acceptance record attests to having reviewed a document that has never existed in this repository. Recorded, not resolved.
