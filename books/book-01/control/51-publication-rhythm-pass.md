# Publication-Rhythm Pass — Book 1

**Completed:** 2026-07-18

## Authority

This pass was authorized after the author identified excessive isolated short lines and one- or two-word narrative paragraphs in the accepted manuscript.

## Scope lock

The pass changes paragraph architecture only, plus one punctuation-only cadence repair. It does not revise plot, pacing, scene order, POV order, chronology, evidence, technology, dialogue wording or meaning, character decisions, character knowledge, worldbuilding, reveals, suspense structure, or chapter endings.

## Acceptance result

- Accepted words remain **105,081**.
- Isolated narrative paragraphs of two words or fewer fell from **261** to **32**.
- Isolated narrative paragraphs of seven words or fewer fell from **2,117** to **406**.
- One-sentence narrative paragraphs fell from **2,963** to **513**.
- The repository-wide prose metric fell from **5,836 / 8,361** one-sentence paragraphs (**69.8%**) to **3,386 / 5,909** (**57.3%**), including dialogue and technical blocks.
- Dialogue *wording* and non-narrative technical content remain unchanged. Dialogue *paragraphing* did change: see the correction below.

## Correction, 2026-08-25

This record originally stated that "Dialogue and non-narrative technical formatting remain unchanged." That was inaccurate and is corrected here under `74-editorial-correction-record.md` §8.

Dialogue wording was never altered. Dialogue paragraph boundaries were: the follow-on repair recorded in `52-one-sentence-repair-map.json` applied `attach_next_dialogue` **166 times**, attaching a narrative beat to the speech that followed it. Where the beat and the speech belonged to the same character the result is sound. Where they did not, the merge chained across a speaker change, and the book now contains **46 paragraphs carrying dialogue from two different speakers** — identified in `73-complete-editorial-review.md` finding D-4.

No prose was changed by this correction. D-4 remains an open author decision.
- Updated accepted-file hashes are recorded in `books/book-01/ACCEPTED_MANUSCRIPT.yaml`.
- The developmental analyzer now rejects incomplete accepted-manuscript inventories instead of silently producing an empty report.
- Full measurements are in `artifacts/book1-publication-rhythm-pass.md` and `artifacts/book1-developmental-analysis.md`.

## Publication boundary

External specialist review, approved technical corrections, continuity review, copyedit, and proofread remain required before publication.
