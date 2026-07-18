# Julie O'Donnell Series

Canonical repository for the contemporary geopolitical techno-thriller series centered on Julie O'Donnell.

## Current release candidate

**Book 1: _Veridrift_**

- Prologue plus 24 chapters.
- Accepted revised manuscript: **105,081 words**.
- Developmental revision completed **July 18, 2026**.
- Publication-rhythm pass completed **July 18, 2026**, reducing routine isolated narrative beats while preserving dialogue, scene metadata, system displays, and story content.
- Targeted one-sentence-paragraph repair completed **July 18, 2026**, integrating reviewed routine reactions and technical transitions without changing accepted words.
- Final act unfolds across October 13–16 rather than a single implausibly compressed morning.
- Publication blockers, drafting metatext, duplicated thermostat transmission, date conflicts, heading inconsistencies, and system-display artifacts have been removed.
- The causal chain from Validation Package 88 through `SIGMA-NORMALIZE-4` and the live poisoned feed is explicit.
- Julie's overbroad K-17 provenance boundary and signed supplemental correction are canon.
- Original 02:14 constructor and Senator Sterling's personal knowledge or command remain deliberately unresolved series threads.

## Publication state

The developmental revision is complete, but the novel is **not yet approved for publication**. The repository now contains the full publication-readiness control program: specialist packets and issues, continuity ledgers, findings intake, strict manifest validation, late-act diagnostics, a copyedit style sheet, and production-proof gates.

Required next stages:

1. Complete the **seven** external specialist reviews tracked in `books/book-01/control/52-specialist-review-register.md` and GitHub issues #70–#76.
2. Apply only approved critical and material corrections, then reconcile all continuity ledgers.
3. Complete the controlled late-act compression, character-voice pass, line/copyedit, and proofread.
4. Regenerate print and ebook production files from the accepted-manuscript inventory.
5. Mark the book ready only after the final validator and production-proof report pass.

## Source of truth

`books/book-01/ACCEPTED_MANUSCRIPT.yaml` is the canonical prose inventory. Only the listed prologue and chapter files are accepted manuscript sources.

Core paths:

- `books/book-01/manuscript/`
- `books/book-01/control/`
- `books/book-01/ACCEPTED_MANUSCRIPT.yaml`
- `series/`
- `tools/`

Generated or historical compiled files—including the obsolete twelve-chapter Word export—are not authoritative. `tools/compile_book1_from_manifest.py` creates validated review compilations from the accepted inventory and writes a build-provenance sidecar.
