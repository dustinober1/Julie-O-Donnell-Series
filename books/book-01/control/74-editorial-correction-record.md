# 74. Editorial Correction Record — Book 1

**Authority:** author direction, 2026-08-25, in response to `73-complete-editorial-review.md`.
**Supersedes:** `66-publication-master-freeze.md` as the current freeze record. `66-` is retained as the historical record of the previous freeze.
**Prior accepted total:** 105,157 words
**New accepted total:** 105,160 words
**Manifest version:** 2 (unchanged)
**Accepted files:** 25 (unchanged)
**Final line:** unchanged — *The bubble stayed centered.*

---

## 1. Why this record exists

`73-complete-editorial-review.md` recorded the first full editorial read of the accepted prose. It found eight defects. Three were unambiguous factual or frame errors in the frozen master, and a fourth was a reading defect a reader meets directly on the page. The author authorized correction of those four.

The remaining four findings (D-4 dialogue paragraphing, D-6 dateline shape, D-7 numeral style, D-8 repeated interval) are style and consistency items that remain open author decisions. They are **not** corrected here.

## 2. Corrections applied

### C-1 — Chapter 24 — contradicted quantity (review finding D-1)

Chapter 12 establishes the Northbridge abort overrun three ways: the abort at `07:10:00`, the capture ending at `07:10:08.021 EDT`, and the sentence "The seal had cost eight seconds." Chapter 13 restates it — "You stayed eight seconds at Fenwick." Chapter 24 contradicted all three.

| | |
|---|---|
| **Was** | "…her entries, removals, deception, and **seven seconds** past the Northbridge abort would be charged." |
| **Now** | "…her entries, removals, deception, and **eight seconds** past the Northbridge abort would be charged." |

This is the book's most thematically load-bearing quantity — Julie's one deliberate violation of her own rule, cited in her final legal jeopardy.

### C-2 — Chapter 22 — out-of-frame narration (review finding D-2)

| | |
|---|---|
| **Was** | "…the same temptation the **manuscript's** institutions had repeatedly used against her and Elias." |
| **Now** | "…the same temptation the **institutions in this case** had repeatedly used against her and Elias." |

"Manuscript" had no in-world referent. Nothing in the story is a manuscript.

### C-3 — Chapter 23 — out-of-frame narration (review finding D-3)

| | |
|---|---|
| **Was** | "…without filling the **chapter** with inert cryptographic strings." |
| **Now** | "…without filling the **page** with inert cryptographic strings." |

"The chapter" was the book's chapter, not any in-world document. The nearby "the reader" in the same chapter means a reader of the public statement and was **left unchanged**, correctly.

### C-4 — Chapter 2 — unmarked mid-paragraph POV return (review finding D-5, partial)

Chapter 2 shifts POV from Julie to Elias two floors below with a locational bridge, runs 127 lines in Elias's POV, then returned to Julie **inside the same paragraph**:

> "Elias looked once at the production map. The false signals continued moving toward the border. No one shut them off. Julie ran the Package 88 index through three comparisons."

The paragraph is now split at the POV boundary and a `---` scene break inserted, matching the convention already used sixteen times across Chapters 16, 19, 20, 21, 22 and 24. Word count effect: +1 token, the break marker itself.

The wider half of D-5 — that the book runs two scene-break systems overall — remains open.

## 3. Word-count effect

| File | Was | Now | Δ |
|---|---|---|---|
| `chapter-02.md` | 5,150 | 5,151 | +1 |
| `chapter-22.md` | 2,602 | 2,604 | +2 |
| `chapter-23.md` | 2,918 | 2,918 | 0 |
| `chapter-24.md` | 3,115 | 3,115 | 0 |
| **Accepted total** | **105,157** | **105,160** | **+3** |

Within the 105,000–110,000 target band. Twenty-one of the twenty-five accepted files are byte-identical to the previous freeze.

## 4. Updated hashes

```
chapter-02.md  91de1ea738153020ebed1b764183cb2d8708e666b64974853305802f7be134df
chapter-22.md  29c31126dc9cb9243aaf7f3e032bc8e94236e164736bcbb6da3d511c81f0f48b
chapter-23.md  8aa73b398737054b3fff2325c9f28448773919318dc88dc6978cf27830967bc4
chapter-24.md  a8e88adb04c527003115b06e31e7ec86168953baca8a16f8e14d6679ab6aa4b1
```

The prologue and Chapter 1 hashes protected by `tools/verify_book1_revision.py` are unchanged. Chapter 20's protected word count, hash and final sentence are unchanged.

## 5. Revalidation

| Check | Result |
|---|---|
| `tools/count_book1_words.py --expect 105160` | PASS |
| `tools/validate_book1_publication_readiness.py` | PASS — accepted words 105,160 |
| `tools/check_book1_detail_rules.py` | PASS — no hard-rule findings; 5 review items, all previously adjudicated |
| `tools/test_book1_detail_rules.py` | OK (14 tests) |
| `tools/test_book1_publication_master_freeze.py` | OK |
| `tools/test_compile_book1_from_manifest.py` | OK |
| `tools/test_validate_book1_publication_readiness.py` | OK |
| `tools/test_verify_book1_revision_report_state.py` | OK |
| `tools/test_book1_production.py` | SKIPPED — `docx` not installed in this source-only workflow |

`tools/verify_book1_revision.py` carried `EXPECTED_TOTAL = 105_157`. That constant is superseded and now reads `105_160`. No other constant in that script changed: the protected prologue and Chapter 1 hashes, the Chapter 20 expectations, and the forbidden-content list are untouched.

## 6. Publication-master freeze

The accepted Markdown prose is re-frozen at **105,160 words across 25 files**, manifest version 2, under the hashes in §4 and the manifest itself.

## 7. Production package state — ACTION REQUIRED

**The frozen publication package recorded in `../production/final/` no longer matches the accepted prose.**

`Veridrift_Publication_Master_FINAL.docx`, `Veridrift_FINAL.epub`, `Veridrift_PRINT_INTERIOR_FINAL.pdf` and `Veridrift_Final_Publication_Package.zip` were all built from the 105,157-word master. Four of their source files have changed. The recorded SHA-256 values in `../production/final/CHECKSUMS.sha256` remain valid **for those binaries** but the binaries are now derived from superseded prose.

Book 1 is therefore **not upload-ready** until the package is rebuilt. This is a build action, not a manuscript defect: the prose is correct and frozen; the derived outputs are stale.

Required before any retailer upload:

1. Rebuild with `tools/build_book1_production.py` in an environment with the production dependencies installed (`requirements-production.txt` — `docx` is absent here, so the rebuild could not run in this workflow).
2. Re-run `tools/test_book1_production.py`, which currently skips.
3. Regenerate `../production/final/CHECKSUMS.sha256` and the package manifest.
4. Perform the retailer-specific preview already required by `PROJECT_STATE.yaml`.
5. Record the rebuild in a new production-package build record.

## 8. Corrections to control records

`73-complete-editorial-review.md` finding D-4 identified two control records that overstate their own scope lock. Both are corrected in this pass, because the claim is about a completed pass rather than about the prose:

- `51-publication-rhythm-pass.md` stated "Dialogue and non-narrative technical formatting remain unchanged."
- `53-one-sentence-repair.md` stated "Dialogue wording, system displays, scene metadata, chronology, evidence, technology, POV, reveals, and ending remain unchanged."

The *wording* claim is accurate. The *formatting* claim is not: `52-one-sentence-repair-map.json` records `action_counts: {"attach_next_dialogue": 166}`, and those 166 operations changed dialogue paragraph boundaries. Both records now state what the pass actually did and cross-reference the 46 resulting two-speaker paragraphs.

No prose changed as a result of §8. The underlying paragraphing (D-4) remains an open author decision.

## 9. What this record does not decide

- D-4, D-6, D-7 and D-8 remain open.
- The Act III structural recommendation in `73-` §3 and the redistribution plan in `75-act-iii-thread-redistribution-lock.md` are unaffected by this correction and remain unexecuted.
- Retail release status remains not established by repository evidence.
