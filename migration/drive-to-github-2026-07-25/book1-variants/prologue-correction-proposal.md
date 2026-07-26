# Proposed Correction — Prologue Narrative Time Format

**Status:** requires explicit author approval; not applied  
**Affected accepted file:** `books/book-01/manuscript/prologue.md`  
**Accepted manifest SHA-256:** `9f1285a83b3379b8f34ced719ad7b2d9d79b645a8eb5587aa38822710683506e`  
**Publication baseline:** `9708fdd86e9292a75b7683152c7746567f015cc6`

## Three source states

| Source | Exact wording | Source identity |
|---|---|---|
| Frozen accepted Markdown | `At 0214, the geolocation track...` | accepted manifest path at PR #92 baseline |
| Post-freeze Drive Doc | `At 0214 hours, the geolocation track...` | Drive ID `1upUvx5RV-ToSFLLc5k_mQQZhjerethTDWi5PiXPEoAg`; modified `2026-07-21T02:39:35.504Z` |
| Approved production correction | `At 02:14, the geolocation track...` | T07 in `books/book-01/production/corrections/pass-4/SOURCE_CORRECTIONS_PASS4.md`; verified by Pass 4 change log and verification report |

## Evidence

The Pass 4 correction map states: change the Prologue narrative phrase `At 0214` to `At 02:14` and do not alter literal identifiers containing `0214`.

The Pass 4 verification report records:

- narrative `At 0214` count: 0;
- narrative `At 02:14` count: 1;
- the tracked and clean production masters rendered and passed visual QA.

The final package was later cleared in PR #92, but the accepted Markdown manifest still contains `At 0214`. This is a source/package synchronization conflict, not evidence that the later Drive wording is authoritative.

## Proposed correction for a separate PR

Replace only:

`At 0214, the geolocation track placed the handset behind the western ridge...`

with:

`At 02:14, the geolocation track placed the handset behind the western ridge...`

Do not add `hours`. Do not add the Drive scene break. Do not alter compressed identifiers containing `0214`.

## Required approval and validation

A correction PR must:

1. record explicit author approval;
2. change only the accepted Prologue line;
3. recompute the Prologue word count and SHA-256;
4. update `books/book-01/ACCEPTED_MANUSCRIPT.yaml`;
5. regenerate and revalidate all derived publication outputs;
6. verify the final line and all 25 accepted paths remain intact;
7. create a new correction and publication-freeze record.

Until that process occurs, the frozen accepted Markdown remains authoritative.
