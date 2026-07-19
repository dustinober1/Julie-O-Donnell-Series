# Julie O'Donnell Series

Canonical repository for the contemporary geopolitical techno-thriller series centered on Julie O'Donnell.

## Current release candidate

**Book 1: _Veridrift_**

- Prologue plus 24 chapters.
- Accepted copyedited manuscript: **105,155 words**.
- Developmental revision completed **July 18, 2026**.
- Publication-rhythm pass completed **July 18, 2026**, reducing routine isolated narrative beats while preserving dialogue, scene metadata, system displays, and story content.
- Targeted one-sentence-paragraph repair completed **July 18, 2026**, integrating reviewed routine reactions and technical transitions without changing accepted words.
- Public-source desk review completed **July 18, 2026**, with three narrow corrections to targeting authority, PKI identity proof, and MPD release procedure.
- Post-research continuity audit completed **July 18, 2026** with minor control and status repairs and no accepted prose changes.
- Full mechanical copyedit reviewed and merged in PR #82 on **July 18, 2026**.
- The seven specialist-review issues were closed at the author's direction after reported specialist satisfaction. The repository records these as author waivers of the formal documentation gate, not as named qualification-backed approvals.
- Final act unfolds across October 13–16 rather than a single implausibly compressed morning.
- Publication blockers, drafting metatext, duplicated thermostat transmission, date conflicts, heading inconsistencies, system-display artifacts, and copyedit defects identified in the accepted manuscript have been removed.
- The causal chain from Validation Package 88 through `SIGMA-NORMALIZE-4` and the live poisoned feed is explicit.
- Julie's overbroad K-17 provenance boundary and signed supplemental correction are canon.
- Original 02:14 constructor and Senator Sterling's personal knowledge or command remain deliberately unresolved series threads.

## Publication state

The manuscript is **copyedited and content frozen**, but it is **not yet approved for publication**. The next mandatory gate is a controlled final proofread followed by production-master validation and output proofing.

Required next stages:

1. Proofread the 105,155-word canonical inventory for objective errors only.
2. Regenerate manifest counts and hashes if accepted prose changes.
3. Run the validator, unit tests, compiler, final-line assertion, YAML checks, and diff hygiene.
4. Freeze a publication-master commit.
5. Generate and manually inspect Word, EPUB, and print-PDF outputs.
6. Mark the book ready only after the final production proofs match the canonical inventory.

The late-act compression, character-voice pass, and small Vance credibility addition are no longer automatic stages. They remain waived unless a concrete defect justifies reopening content.

See `books/book-01/control/63-post-copyedit-publication-state-reconciliation.md` for the controlling transition record.

## Source of truth

`books/book-01/ACCEPTED_MANUSCRIPT.yaml` is the canonical prose inventory. Only the listed prologue and chapter files are accepted manuscript sources.

Core paths:

- `books/book-01/manuscript/`
- `books/book-01/control/`
- `books/book-01/ACCEPTED_MANUSCRIPT.yaml`
- `series/`
- `tools/`

Generated or historical compiled files—including the obsolete twelve-chapter Word export—are not authoritative. `tools/compile_book1_from_manifest.py` creates validated review compilations from the accepted inventory and writes a build-provenance sidecar.
