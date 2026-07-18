# Book 1 Production Proof Report

**Book:** *Veridrift*  
**Current status:** NOT STARTED — blocked by specialist corrections, continuity validation, and final copyedit.

## Source rule

Every production file must be generated from the 25 prose files listed in `../ACCEPTED_MANUSCRIPT.yaml`. A production correction is not complete until it is applied to the canonical source and all outputs are regenerated.

## Required outputs

| Output | Path / identifier | Generated commit | Proofed | Status |
|---|---|---|---|---|
| Canonical Markdown compilation | — | — | — | Blocked |
| Review Word document | — | — | — | Blocked |
| EPUB | — | — | — | Blocked |
| Print PDF | — | — | — | Blocked |
| Production checksum manifest | — | — | — | Blocked |

## Pre-production gate

- [ ] All seven specialist reviews have named, dated dispositions.
- [ ] All accepted critical and material corrections are applied.
- [ ] Continuity ledgers are reconciled.
- [ ] Late-act compression is complete.
- [ ] Character voice/cast pass is complete.
- [ ] Line/copyedit is complete.
- [ ] `tools/test_validate_book1_publication_readiness.py` passes.
- [ ] `tools/validate_book1_publication_readiness.py` passes against the final manifest.
- [ ] Accepted word counts and hashes are regenerated.
- [ ] Final line remains `The bubble stayed centered.`

## Text proof checklist

- [ ] Prologue and 24 chapter headings match the manifest.
- [ ] No Chapter 25 exists.
- [ ] Scene headings are complete and not stranded from the following prose.
- [ ] No drafting metatext or chapter references remain inside narrative prose.
- [ ] All dialogue punctuation and paragraphing are correct.
- [ ] No dropped words, duplicated words, or accidental repeated paragraphs.
- [ ] Names, ranks, agencies, locations, identifiers, and evidence counts match the style sheet.
- [ ] EDT/IST labels and conversions match the master timeline.
- [ ] Every system display renders as plain display text rather than code formatting.
- [ ] The final farm section contains no exact timestamp.

## Print PDF proof checklist

- [ ] Correct trim size, margins, gutter, headers, and folios.
- [ ] No accidental blank recto/verso pages.
- [ ] Chapter titles begin consistently.
- [ ] Scene-heading lines do not split awkwardly.
- [ ] System-display blocks do not orphan single lines.
- [ ] No widows/orphans that materially damage reading rhythm.
- [ ] Em dashes, apostrophes, smart quotes, and special characters embed correctly.
- [ ] No clipped text, substituted font, or missing glyph.
- [ ] Final line appears once and is not followed by teaser prose.

## EPUB proof checklist

Test on a Kindle-sized display, phone, tablet, dark mode, large font, and small font.

- [ ] Table of contents contains prologue and Chapters 1–24 only.
- [ ] Chapter navigation opens at the correct heading.
- [ ] Scene breaks remain visible at all font sizes.
- [ ] System displays wrap without becoming unreadable.
- [ ] No forced line breaks create isolated single words.
- [ ] Italics and emphasis survive conversion.
- [ ] No hidden page headers, print folios, or PDF artifacts appear.
- [ ] Final line remains intact.

## Word document proof checklist

- [ ] Navigation pane recognizes prologue and all chapter headings.
- [ ] Styles are used consistently rather than manual formatting.
- [ ] Track Changes and comments are removed from the clean export.
- [ ] Document properties contain the correct title and author identity selected for publication.
- [ ] No stale twelve-chapter content is present.
- [ ] Word count is reconciled to the production method and canonical Markdown count.

## Checksum and provenance

The production checksum manifest must record:

- accepted-manifest commit;
- each canonical source path and SHA-256;
- generated output filename, byte size, and SHA-256;
- generation date and tool/version;
- proofreader and proof date;
- any production correction commits applied after first generation.

## Proof findings

| ID | Output | Location | Severity | Finding | Source correction | Regenerated | Verified |
|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — |

## Final approval

- [ ] Text proof approved.
- [ ] Print PDF approved.
- [ ] EPUB approved.
- [ ] Word review file approved.
- [ ] Checksum manifest approved.
- [ ] Public metadata does not promise that Book 1 proves the original constructor or Sterling's personal command.
- [ ] Repository status changed to `ready_for_publication` only after all approvals above.

**Final production verdict:** BLOCKED
