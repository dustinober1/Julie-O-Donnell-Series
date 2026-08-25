# 76. Book 1 — Production-Quality Pass

**Authority:** author direction, 2026-08-25 — "don't stop until the prose is production quality."
**Supersedes:** `74-editorial-correction-record.md` as the current publication-master freeze. `74-` and `66-` are retained as historical freeze records.
**Prior accepted total:** 105,160 words
**New accepted total:** 108,672 words
**Accepted files:** 25 (unchanged) · **Manifest version:** 2 (unchanged)
**Final line:** unchanged — *The bubble stayed centered.*

---

## 1. A correction to the review that started this

`73-complete-editorial-review.md` finding **D-6** claimed that Chapters 3–5 were inconsistent for separating each scene-header element with a blank line, while Chapters 5–24 used a tight multi-line block, and recommended normalising toward the tight form.

**That finding was backwards, and it mattered.** The recommendation was acted on, verified against the real builder, found to make the book worse, and reversed inside this pass. The record below states what was actually true.

The production builder's `TIME_RE` requires a paragraph to **begin** with a clock time. `identify_scene_meta()` joins a paragraph's lines with spaces before testing. So:

| Header form | Joined test string | Result |
|---|---|---|
| Blank-separated | `15:49 Eastern Daylight Time` | matches → **Scene Metadata** (centred small-caps) |
| Tight multi-line | `Apex Campus Utility Easement Reston, Virginia 15:49 Eastern Daylight Time` | no match → falls through to **Display Text** = **monospace** |

The blank-separated form was the correct one. D-6 identified a real inconsistency and pointed at the wrong half of it.

## 2. The defect this exposed

Measured against the shipped commit `b968612` using the checked-in builder payload:

> **54 of the book's 64 scene headers rendered in monospace** in `Veridrift_Publication_Master_FINAL.docx`, `Veridrift_FINAL.epub` and `Veridrift_PRINT_INTERIOR_FINAL.pdf`.

Every scene header in Chapters 5 through 24 — sixty percent of the book — appeared in a typewriter face instead of centred small-caps. The ten correct ones were exactly the blank-separated blocks in Chapters 3–5.

**Why every existing control passed it.** `cross-format-text-validation.md` compares DOCX, EPUB and PDF against the source *character by character*. Monospace text contains the same characters as small-caps text. Nothing in the repository compared a paragraph's **style** to its **role**. `visual-inspection-report.md` was the only control positioned to catch it and did not.

## 3. Two builder defects behind it

`identify_scene_meta()` had two faults, both now fixed in the payload:

1. **No forward walk.** It absorbed short header lines *preceding* the time line but never following it. Act III places the date and time first and the location second, so Act III location lines could never join the header.
2. **Abbreviation-intolerant adjacency.** Any candidate ending in `.` was rejected as a sentence. `Washington, D.C.` is the location line of most Act III scenes.

The fix adds a forward walk and a helper, `_scene_meta_adjacent()`, that accepts a trailing period when it terminates an abbreviation (`\b(?:[A-Z]\.){2,}$`). The payload was re-encoded and all three loader checksums — `PAYLOAD_SHA256`, `SOURCE_SHA256`, `PATCHED_SOURCE_SHA256` — recomputed. The loader's separate PDF-validator patch is untouched and still applies cleanly.

**Result: 190 paragraphs styled Scene Metadata, 0 scene headers in monospace.** The only remaining Display Text block containing prose-like words is the screen field list in Chapter 1 (`Timestamp. / Signal amplitude. / …`), which is correctly monospace.

## 3b. A second production defect, found by building

Once the package could actually be built, inspecting the binaries surfaced a defect that had nothing to do with scene headers.

The recorded builder treats `_` as an emphasis delimiter. The accepted prose contains underscores in exactly one place — the identifier `PAK_RELAY_17A` and its derivative `PAK_RELAY_17A_SOURCE_CORRECTION`, ten occurrences — and never as emphasis. The book's only intentional italic is `*analyst delay*` in the prologue.

So the builder **consumed the underscores and italicised the interior**. The shipped DOCX reads `PAKRELAY17ASOURCECORRECTION` with SOURCE in italics. The EPUB carries `PAK<em>RELAY</em>17A`. Sixteen occurrences across the three formats, of the object identifier the entire plot turns on.

**Why cross-format validation could not see it, again.** `validate_pdf_chars` compares the output against `strip_inline_markdown(source)`. Both sides of the comparison run through the same stripper, so both drop the underscores and the streams match exactly. This is the same blind spot that hid the monospace defect, in a different guise: the validator compares the source *after* markdown interpretation to the output *after* markdown interpretation, so any misinterpretation is invisible by construction.

The loader now removes `_` from the inline tokeniser and the stripper. Verified in the built binaries: `PAK_RELAY_17A` appears intact ten times in DOCX, EPUB and PDF; the whole book contains exactly one italic run, `analyst delay`.

## 4. Prose changes

| Review finding | Action |
|---|---|
| **D-4** 46 two-speaker paragraphs | **Resolved.** All 46 hand-reviewed; 37 were genuine speaker changes and were split (50 paragraph breaks). 9 were false positives where one character speaks twice and were left alone. |
| **D-5** two scene-break systems | **Resolved.** Chapter 2's Elias section is now bracketed by rules on entry and exit; Chapter 23's mid-paragraph jump to Forward Post Arjun is broken at the paragraph boundary. The system is now principled: a dateline marks a change of time or place, a rule marks a break where neither changes. No unmarked scene or POV transition remains. |
| **D-6** header form | **Reversed and resolved** — see §1–3. All 68 header blocks are now blank-separated. |
| **D-7** `11.2` vs `eleven-point-two` | **Closed, no change.** On re-reading, the prologue's numerals sit in a screen-reading register set by `Confidence: 94.1 percent.` in the same paragraph. The register shift is deliberate and correct under style-sheet rule 48. The review over-called this. |
| **D-8** three unrelated "forty-three seconds" | **Resolved.** Sarah's directive gap became ninety seconds (Ch 11 and its restatement in Ch 19); the continuity broker's interval became nineteen seconds (Ch 21). Forty-three seconds now belongs only to Julie's analytic-scope delay. |
| Dialogue idiom | **Reduced.** The pure question-deflection form ran 13 times, 4 of them in Chapter 1. Four were rewritten to say the actual objection. No chapter now carries more than two. |
| Marcus's Chapter 1 confession | **Trimmed.** His explicit admission is removed from Chapter 1 and now withheld — "a sentence short of the one she had spent six years waiting for" — so the Chapter 4 confession lands first. |

## 5. Act III thread redistribution

Executed under `75-act-iii-thread-redistribution-lock.md`. Kashmir previously appeared in Chapters 3, 4, 5 and 8, then vanished for 42,745 words before returning in Chapter 18.

Three scenes now dramatize what Chapter 18 formerly reported:

| Scene | Placement | Story time | Content |
|---|---|---|---|
| A | Ch 15 | Oct 13, 07:52 EDT / 17:22 IST | Sharma briefs Rao's patrol; Sethi's custodian limits; the three hard stops |
| B | Ch 16 | Oct 13, 17:11 EDT / 02:41 IST | The glazed traverse; Pal takes the harness and the anchor rock; Rao's casualty-rule decision |
| C | Ch 16 | Oct 13, 19:56 EDT / 05:26 IST | Nine minutes from Kestrel; the wicket; the cartridge release; the hard stop at the inner boundary |

Chapter 18 lost its retelling of all three and keeps the custody intake, the isolated read, Northern Command's pressure, Sharma's ravine backstory and the restoration plan.

**Chronology.** Scene C was first placed in Chapter 17 and the derived-chronology check caught it: an early-IST scene inside an Oct 14 EDT chapter registered as a backward step and pushed Chapters 18–19 to a derived October 15 against a stated October 14 — the same class of defect as DC-01. Scene C moved to Chapter 16, where 19:56 EDT sits correctly between 09:03 and 22:18. All scenes carry the Chapter 19 dual-clock form. **Every stated date now equals its derived date.**

The lock's seven constraints hold: no chronology change, no new proof, no new named characters, the hard stop preserved exactly, Pal's medical removal intact, the ending untouched, no POV expansion beyond Rao.

## 6. Word count

| | Words |
|---|---|
| Frozen master before this work | 105,157 |
| After `74-` corrections | 105,160 |
| **After this pass** | **108,672** |

Net +3,512 from the frozen master: roughly +4,400 of new Kashmir prose, −1,900 from the Chapter 18 compression, and small net gains from paragraph splits and the idiom rewrites. Inside the 105,000–110,000 target band.

## 7. Stale locks updated, and where they now live

Every deviation from the recorded builder payload is expressed as a commented patch in `tools/build_book1_production.py`, matching the three patches the loader already carried. **The payload itself is byte-identical to the recorded original.** An earlier iteration of this pass edited the compressed payload directly; that was reverted, because a change inside a base64 blob is invisible in review while a loader patch is plain text.

The loader now also derives two literals the recorded builder hardcoded — the accepted word count printed into build record 67, and one validation message that named the old total.

`tools/test_book1_production.py` pinned the historical PR #85 source commit and the old word total. The total now reads from `EXPECTED_TOTAL`; the commit assertion now checks that the manifest carries a well-formed commit rather than one specific historical value, because the build legitimately records whichever commit it ran from.

## 7b. Guard constants updated

`tools/verify_book1_revision.py` protects the prologue and Chapter 1 hashes and Chapter 20's word count, hash and final sentence. The prologue and Chapter 1 both changed in this pass (a speaker split in the prologue, the Marcus trim and header reflow in Chapter 1), and Chapter 20's hash changed from two speaker splits though its word count and final sentence did not.

**The guard fired correctly** on the first prologue edit and was updated deliberately, not bypassed. `EXPECTED_TOTAL` is now 108,672.

`tools/test_book1_detail_rules.py` pinned two chronology scenes by line number. Reflow moved them. The test now anchors on scene-header text instead, so it keeps testing the DC-01 reading rather than a line offset.

## 8. Verification

| Check | Result |
|---|---|
| `validate_book1_publication_readiness.py` | PASS — 108,672 words |
| `verify_book1_revision.py` | PASS — 108,672 words |
| `check_book1_detail_rules.py` | PASS — no hard-rule findings; 6 review items |
| `test_book1_detail_rules.py` | OK (14 tests) |
| `test_book1_publication_master_freeze.py` | OK |
| `test_compile_book1_from_manifest.py` | OK |
| `test_validate_book1_publication_readiness.py` | OK |
| `test_verify_book1_revision_report_state.py` | OK |
| `test_book1_production.py` | SKIPPED — `docx` absent in this source-only workflow |
| Paragraph-style audit | 190 Scene Metadata, **0** monospace headers |
| Derived chronology vs stated dates | every stated date equals its derived date |

The six R6/R2 review items are the previously adjudicated near-miss pairs (`Ford`/`Fort`, `India`/`Indian`, `Pakistan`/`Pakistani`, `Service`/`Services`, the Chapter 8 zone interleave) plus one new benign pair, `Naib`/`Naik` — the ranks Naib Subedar and Lance Naik, both correct.

## 9. Publication-master freeze

The accepted Markdown prose is re-frozen at **108,672 words across 25 files**, manifest version 2, under the hashes in `../ACCEPTED_MANUSCRIPT.yaml`.

## 10. Production proofs — rebuilt and verified

The production dependencies were installed into a clean virtualenv from `requirements-production.txt` and the package was rebuilt. **Both defects are confirmed fixed in real binaries, not inferred from the builder's logic.**

| | DOCX | EPUB | Print PDF |
|---|---|---|---|
| Scene-header paragraphs correctly styled | 190 | 190 | — |
| Scene headers in monospace | **0** | **0** | — |
| `PAK_RELAY_17A` intact | 10 | 10 | 10 |
| Mangled `PAKRELAY17A` | **0** | **0** | **0** |
| Italic runs in the whole book | `analyst delay` only | 1 `<em>` | — |
| Pages / final line | — | — | 467 · *The bubble stayed centered.* |

The DOCX `Scene Metadata` style resolves to DejaVu Serif, small-caps, centred; `Display Text` remains DejaVu Sans Mono, left-aligned. The EPUB stylesheet gives `p.scene-meta` centred small-caps and `p.display` monospace. The 364 remaining Display Text paragraphs are the book's screen output, which is correctly monospace.

All of the builder's own validations pass: DOCX OOXML parts and independent extraction, EPUB mimetype/TOC/XHTML extraction, print-PDF trim, embedded fonts and normalised extraction, and cross-format text comparison. `tools/test_book1_production.py` now **passes** (7 tests) with the dependencies present, and still skips cleanly without them.

**Still required before retailer upload:**

1. Author review of the visual contact sheets. The build marks visual inspection `PENDING AUTHOR REVIEW` by design; automated generation does not substitute for looking at the pages.
2. Promotion of the verified proofs in `../production/proofs/` into `../production/final/`, with `CHECKSUMS.sha256` and the package manifest regenerated. This pass rebuilt the **proofs**; the final package directory still carries the superseded records.
3. The retailer-specific preview.

## 11. Permanent guard added

The style defect survived every existing control because nothing compared a paragraph's rendered style to its role.

`tools/validate_book1_paragraph_styles.py` now closes that gap. It loads the real builder payload, applies the builder's own `identify_scene_meta()` and regexes, and fails when a paragraph carrying a clock time is not styled Scene Metadata, or when prose would fall into Display Text. Standard library only, matching the other permanent Book 1 validators.

It is wired into `.github/workflows/book1-detail-continuity.yml`, whose header now records why it exists.

Verified both ways: it passes on the repaired book (190 scene-metadata paragraphs, 0 mis-styled), and re-tightening a single Chapter 6 header in a scratch copy makes it fail with the exact defect named. It would have caught the shipped defect, and it would have caught the D-6 reversal on the first run.

## 12. Still open

- The book-wide question of whether Act III's date-first header order should be harmonised with Act II's location-first order. Both are now internally consistent and render correctly; this is taste, not defect.
- Everything in `73-` §4 that is developmental rather than mechanical: Vance's Act III embodiment and the Chapters 19–21 compression remain unexecuted.
- Retail release status remains not established by repository evidence.
