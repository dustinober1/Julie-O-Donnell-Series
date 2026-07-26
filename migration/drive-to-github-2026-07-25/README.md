# Google Drive to GitHub Migration — 2026-07-25

## Governing decision

GitHub is the sole active source of truth for the Julie O'Donnell Series: manuscript prose, accepted chapters, series bible, canon, character ledgers, timelines, decisions, mission locks, outlines, research controls, project state, and editorial or publication tracking.

Google Drive is retained only for archived snapshots, review copies generated from GitHub, large production binaries, and files shared with nontechnical collaborators. A later Drive timestamp does not establish authority.

## Scope and baseline

- Repository: `dustinober1/Julie-O-Donnell-Series`
- Default branch: `main`
- Live migration baseline: `9708fdd86e9292a75b7683152c7746567f015cc6`
- Drive root folder: `1PcxkAAZk2o_pT_R_Eokhd-rZOvUxDev7`
- Drive items inventoried: **72**
- Checksum-bearing Drive files: **60**
- Drive folders accounted for: **12**

Google-native documents are exported as Markdown for source checksums. Stored DOCX, JPEG, and M4B files are checksummed as raw bytes. Folder entries are non-checksum-bearing containers.

## Migration records

- `inventory.yaml` — exact Drive identities, timestamps, destinations, authority classifications, statuses, and source checksums.
- `conflict-log.md` — differences, authority decisions, and unresolved correction proposals.
- `verification-report.md` — completed validations and final source-of-truth transition evidence.

## Pull-request sequence

| Phase | Branch | Pull request | Status |
|---|---|---:|---|
| Book 1 publication status | `migration/reconcile-book1-status` | pending | in progress |
| Series bible and Book 1 variants | `migration/reconcile-series-bible` | pending | not started |
| Book 2 controls and architecture | `migration/import-book2-controls` | pending | not started |
| Accepted Book 2 Chapter 1 | `migration/import-book2-chapter-01` | pending | not started |
| Book 2 Chapter 2 draft | `migration/import-book2-chapter-02` | pending | not started |
| Final verification and authority transition | `migration/final-verification` | pending | not started |

Actual PR numbers replace `pending` after creation.

## Safety locks

- Book 1 accepted Markdown prose remains frozen unless an explicit correction record is approved.
- The post-freeze Drive-native Prologue and Chapter 1 are isolated for normalized comparison; they do not overwrite the publication master.
- Book 2 Chapter 1 is accepted only with its formal acceptance record.
- Book 2 Chapter 2 remains draft-only and is excluded from the accepted manifest.
- Large binaries remain external and are represented in Git by provenance, dimensions or format, approval state, and SHA-256.
- No Drive material is deleted.
