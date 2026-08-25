# 78. Act III Antagonist Presence and Compression — Correction Record and Publication-Master Freeze

**Authority:** author approval, 2026-08-25, of the four recommendations recorded in `77-act-iii-antagonist-and-compression-lock.md`.
**Supersedes:** `76-production-quality-pass.md` as the current publication-master freeze record.
**New accepted total:** 109,498 words across 25 files, manifest version 2.

---

## 1. Changes made

| # | Change | File | Effect |
|---|---|---|---|
| E-1 | Counsel-supervised Vance interview inserted after the LSS Drennan section | `chapter-20.md` | 2,363 → 3,301 (+938) |
| E-2 | Receiving-instrument negotiation compressed | `chapter-19.md` | 2,745 → 2,707 (−38) |
| E-3 | Kashmir scene B trimmed | `chapter-16.md` | 5,283 → 5,209 (−74) |
| E-4 | Sterling scene | — | declined, per `77-` §5 |

Total: 108,672 → **109,498** (+826).

## 2. E-1 — Vance in Chapter 20

`Apex Counsel Conference Room / Reston, Virginia / October 15 / 09:58 Eastern Daylight Time.`
Grant conducts the interview. Alvarez attends. Julie watches on the incident channel and does not intervene.

Every constraint in `77-` §4 is satisfied:

- Julie is not in the room and does not speak (§4.1).
- Vance answers `"On advice of counsel, I decline to answer"` to every question and concedes nothing (§4.2). His one unprompted line — `"You have the sources."` — is an assertion about the record, not about his conduct.
- Grant reads from a scope card limited to the three categories Chapter 16 already established through Sarah's preservation notice: the executive certificate registered to him, the material-loss force addendum, and the occupied-room suppression override. No fourth category is reached (§4.3).
- The 02:14 constructor and Sterling are not narrowed (§4.4).
- Grant states the procedural reason on the record — that a refusal must exist so he cannot later be characterised as never having been asked — and states explicitly that the refusal `"is not evidence of anything"` (§4.5).
- No new named characters (§4.6).
- Chapter 24 is untouched; the final line remains `The bubble stayed centered.` (§4.7).

His live authentication of the 07:52 reconstruction remains in Chapter 22, unspoiled.

**A chronology error was caught and fixed during drafting.** The scene was first placed at 11:14 Eastern, which falls after Chapter 21's 10:32 opening. R2 compares timestamps within a chapter, so it did not fire. The scene now sits at 09:58, between Chapter 20's 09:06 opening and Chapter 21's 10:32. This is the same class of defect as DC-01 and is recorded here because the rule set did not catch it — a reviewer did.

## 3. E-2 and E-3 — the compression figures in `77-` §3 were wrong

`77-` §3 specified 700–900 words out of Chapter 19's opening and roughly 300 out of Kashmir scene B. **Neither figure was supportable, and neither was met.** They were sized from a rhythm impression, not from a line-level measurement of what actually repeats. The measurements:

| Claim in `77-` §3 | Measurement | Delivered |
|---|---|---|
| Chapter 19 opening yields 700–900 words | The chapter is 2,745 words in total and its opening — the receiving-instrument negotiation, through the signed instrument — is **927**. A 700–900-word cut would have deleted the opening. | **38** |
| Kashmir scene B yields ~300 words | Scene B is 1,149 words. Its three movements — the glazed traverse, the fall and the casualty-rule decision, and Pal's argument to continue — each do distinct work. | **74** |

What was actually redundant, and was cut:

- **Chapter 19.** The eight-custodian roll-call, reduced to the four that carry the fragmentation point. Hartwell's demand for a named claimant, which restated Ortiz's `seven claimants` line. Grant's scope answer in the question ladder, which pre-stated the written clause four paragraphs later verbatim. The framing around the seven-package custody recitation; the manifest itself is kept intact. Four trailing nouns in the interpretation clause.
- **Kashmir scene B.** The field orientation check ran twice — once dramatized in dialogue, then summarized again immediately behind it. One question of four removed; patrol strength is established earlier in the same scene. Scene B's closing paragraph narrated the looking-before-entering discipline that scene C's opening nine minutes then dramatizes; it is cut to its first sentence.

A repetition of rhetorical device was also found and **not** removed: Chapter 19 runs three question-and-answer ladders (Alvarez on scope, Sarah on her certificate, Julie on the proof ceilings). Ladders two and three are load-bearing — one is a certification under questioning, the other is the chapter's proof-ceiling beat. Ladder one was varied instead of cut, by breaking its metronome with an action beat and a qualified answer.

**The finding behind the two figures stands; the figures did not.** Chapter 19 and Chapter 16 are long because they carry structural material — the K-17 acknowledgment payoff and two full Kashmir sequences added under `75-`. That is length, not fat.

## 4. Act III shape after the change

| | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 |
|---|---|---|---|---|---|---|---|---|---|---|
| Words | 4,065 | 5,209 | 2,580 | 2,661 | 2,707 | 3,301 | 2,486 | 2,604 | 2,918 | 3,115 |

Vance's longest absence falls from five consecutive chapters (17–21, 12,835 words) to **three** (17–19, 7,948 words). Chapters 17–24 now run 2,486–3,301 against a mean of 2,796; the spread narrows.

## 5. Revalidation

| Control | Result |
|---|---|
| `verify_book1_revision.py` | PASS — 109,498 words |
| `validate_book1_publication_readiness.py` | PASS — 109,498 words |
| `validate_book1_paragraph_styles.py` | PASS — 193 scene-metadata paragraphs, 0 mis-styled |
| `check_book1_detail_rules.py` | PASS — no hard-rule findings; 6 review items, all pre-existing near-misses |
| Derived chronology | Regenerated. Every stated date equals its derived date, including the new `ch20:181 \| 09:58`. |
| `test_book1_detail_rules` | OK |
| `test_book1_production` | OK |
| `test_book1_publication_master_freeze` | OK |
| `test_compile_book1_from_manifest` | OK |
| `test_validate_book1_publication_readiness` | OK |
| `test_verify_book1_revision_report_state` | OK |

**Guards updated deliberately, not bypassed.** `EXPECTED_TOTAL`, `EXPECTED_CHAPTER_20_WORDS` and `EXPECTED_CHAPTER_20_SHA256` in `verify_book1_revision.py`, and `EXPECTED_TOTAL`, `EXPECTED_CH20_WORDS` and `EXPECTED_CH20_SHA` in the production loader, were moved only after the corresponding change was reviewed. `EXPECTED_CH20_END` and `EXPECTED_FINAL_LINE` were **not** touched: the Vance scene is an insertion, and Chapter 20's last sentence is unchanged.

One hardcoded literal in `test_book1_production.py` (`ch20.words == 2363`) was de-pinned to `mod.EXPECTED_CH20_WORDS`, matching the two assertions beside it.

## 6. Proofs rebuilt and verified in the binaries

Rebuilt from the 109,498-word master. Verified by reading the output files, not by inference:

| Check | DOCX | EPUB | Print PDF |
|---|---|---|---|
| Scene headers styled `Scene Metadata`, none in monospace | 193 / 0 | ✓ | ✓ |
| New Vance header renders as `Scene Metadata` | ✓ | ✓ | ✓ |
| `PAK_RELAY_17A` intact, no `PAKRELAY17A` corruption | 10 / 0 | 10 / 0 | absent |

Three paragraphs open with a clock time and are correctly monospace `Display Text`: two countdown readouts and one seal-opened log line. They are in-scene display content, not scene headers.

## 7. Known non-regression

`tools/validate_book1_chapter24.py` fails, and failed identically before this change. It is a drafting-era acceptance validator pinned to a 124,779-word state that has not existed since the developmental revision. It is not in CI and is not a current gate. It is left as-is; retiring or re-pinning it is a separate decision.

## 8. Freeze

The accepted Markdown prose is re-frozen at **109,498 words across 25 files**, manifest version 2, under the hashes in `../ACCEPTED_MANUSCRIPT.yaml`. The final line remains `The bubble stayed centered.`

Both deliberate series carryovers are intact and were not narrowed by the Vance scene:

- the human or upstream instruction behind the original 02:14 construction;
- Senator Sterling's personal knowledge, direction, intent, possession, operation, or command.

Any later accepted-prose change requires a new editorial exception record, explicit author approval, updated per-file word count and SHA-256, an updated total, complete revalidation, and a replacement publication-master freeze record.
