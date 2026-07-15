#!/usr/bin/env python3
"""Protect accepted Book 1 through Chapter 21 and the sole Chapter 22 mission lock."""

from __future__ import annotations

from pathlib import Path
import os
import re
import subprocess

ROOT = Path('.')
BOOK = ROOT / 'books/book-01'
CHAPTERS = BOOK / 'manuscript/chapters'
DRAFTS = BOOK / 'drafts'
CONTROL = BOOK / 'control'
MANIFEST = BOOK / 'ACCEPTED_MANUSCRIPT.yaml'
SERIES_LEDGER = ROOT / 'series/recurring-character-ledger.md'

EXPECTED_DIFF_BASE = '45be5fc1164c6618bc8c4e4c15153cc74230bd77'
EXPECTED_MANIFEST_BLOB = 'f334ee9d9512f50065d05bf98b102e93b2236d10'
EXPECTED_TOTAL = 112091
EXPECTED_ENDPOINT_EDT = '12:18:04 EDT'
EXPECTED_ENDPOINT_IST = '21:48:04 IST'
EXPECTED_CHAPTER21_BLOB = '866d4210b7fc808aef48144a91a58280f38fc99c'
EXPECTED_CHAPTER21_WORDS = 4415
EXPECTED_CHAPTER20_LOCK_BLOB = 'c074e4f6f9ec9cddcbc701e2923f34b3082ede5a'
EXPECTED_CHAPTER20_REVIEW_BLOB = '11cea97745a67816d770331c51c5261765a75613'
EXPECTED_CHAPTER21_LOCK_BLOB = '6c92a5764e5c74d88a8325511ae2b0a86b30b356'
EXPECTED_CHAPTER21_REVIEW_BLOB = '4dbd63e9204a2ea22839308de7aac7d63325b53d'
EXPECTED_CHAPTER22_LOCK_BLOB = '9bd255ac7b09a1490dc70be4506ba29183756788'
EXPECTED_SERIES_LEDGER_BLOB = '417483a55fedadbf9195cc3f0dffa2d30dfb94f5'

CHAPTER21 = CHAPTERS / 'chapter-21.md'
MISSION20 = CONTROL / '40-chapter-20-mission-lock.md'
REVIEW20 = CONTROL / '41-chapter-20-acceptance-review.md'
MISSION21 = CONTROL / '42-chapter-21-mission-lock.md'
REVIEW21 = CONTROL / '43-chapter-21-acceptance-review.md'
MISSION22 = CONTROL / '44-chapter-22-mission-lock.md'


def require(value: bool, message: str) -> None:
    if not value:
        raise SystemExit(message)


def blob(path: Path) -> str:
    require(path.is_file(), f'missing required file: {path}')
    return subprocess.check_output(['git', 'hash-object', str(path)], text=True).strip()


def word_count(path: Path) -> int:
    return len(path.read_text(encoding='utf-8').split())


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(['git', *args], text=True, capture_output=True)
    if check:
        require(result.returncode == 0, f"git {' '.join(args)} failed:\n{result.stdout}{result.stderr}")
    return result


def validate_protected_prose() -> None:
    protected = {
        'chapter-13.md': ('e7d04921431e571aab434f2f4b808655e363d30c', 6175),
        'chapter-14.md': ('78f7fff02cd271fecbc94f7daf7151dbebbd5c6d', 5763),
        'chapter-15.md': ('b8e7e2ae573a6c25ea096121c75acee867f3fad2', 5993),
        'chapter-16.md': ('dd5249f4b510a9da9ad19ab2902a95ce1e62a1d8', 6024),
        'chapter-17.md': ('1c4022ebb8d27d8d448f98bcf74fbf09e6e560c1', 5888),
        'chapter-18.md': ('6f5873d6e975ec74646af152aad22ea84545fc01', 4478),
        'chapter-19.md': ('1c7cc22fc7c480cb247efa1f6a2c0d0b1e1b1baf', 5393),
        'chapter-20.md': ('0bd12f43beeef48d5e897ee1fa78a333bd23099b', 4307),
        'chapter-21.md': (EXPECTED_CHAPTER21_BLOB, EXPECTED_CHAPTER21_WORDS),
    }
    for name, (expected_blob, expected_words) in protected.items():
        path = CHAPTERS / name
        actual_blob = blob(path)
        require(actual_blob == expected_blob, f'protected blob changed: {name} = {actual_blob}')
        actual_words = word_count(path)
        require(actual_words == expected_words, f'protected count changed: {name} = {actual_words}')
    print('protected accepted prose: OK')


def validate_manifest_and_accepted_controls() -> None:
    actual_manifest_blob = blob(MANIFEST)
    require(actual_manifest_blob == EXPECTED_MANIFEST_BLOB, f'accepted manifest changed: {actual_manifest_blob}')
    manifest = MANIFEST.read_text(encoding='utf-8')
    require(f'accepted_words: {EXPECTED_TOTAL}' in manifest, 'accepted total changed')
    require('accepted_endpoint:\n  chapter: 21' in manifest, 'accepted endpoint is not Chapter 21')
    require(f'eastern: "{EXPECTED_ENDPOINT_EDT}"' in manifest, 'accepted EDT endpoint changed')
    require(f'india: "{EXPECTED_ENDPOINT_IST}"' in manifest, 'accepted IST endpoint changed')
    listed = [int(n) for n in re.findall(r'chapter-(\d+)\.md', manifest)]
    require(listed.count(21) == 1 and max(listed) == 21, f'Chapter 21 manifest entry invalid: {listed}')
    require(22 not in listed and 23 not in listed, f'unaccepted future chapter entered manifest: {listed}')

    protected_controls = {
        MISSION20: EXPECTED_CHAPTER20_LOCK_BLOB,
        REVIEW20: EXPECTED_CHAPTER20_REVIEW_BLOB,
        MISSION21: EXPECTED_CHAPTER21_LOCK_BLOB,
        REVIEW21: EXPECTED_CHAPTER21_REVIEW_BLOB,
    }
    for path, expected in protected_controls.items():
        actual = blob(path)
        require(actual == expected, f'protected accepted control changed: {path} = {actual}')

    for review_path in (REVIEW20, REVIEW21):
        require('# ACCEPT' in review_path.read_text(encoding='utf-8'), f'explicit ACCEPT missing: {review_path}')

    review21 = REVIEW21.read_text(encoding='utf-8')
    for sentinel in [
        '## Promotion authorization',
        f'Final reviewed prose blob:** `{EXPECTED_CHAPTER21_BLOB}`',
        f'Exact final word count:** **{EXPECTED_CHAPTER21_WORDS:,}**',
        f'Accepted-manuscript total after promotion:** **{EXPECTED_TOTAL:,}**',
        'No review-authorized prose repair was necessary.',
    ]:
        require(sentinel in review21, f'Chapter 21 review missing: {sentinel}')
    print('manifest and accepted controls: OK')


def validate_chapter21_content_and_placement() -> None:
    require(sorted(BOOK.rglob('chapter-21.md')) == [CHAPTER21], 'unexpected Chapter 21 prose path')
    require(not (DRAFTS / 'chapter-21.md').exists(), 'Chapter 21 draft remains')
    text = CHAPTER21.read_text(encoding='utf-8')
    require(text.startswith(
        '11:26:32 EDT / 20:56:32 IST\n\n'
        '# Chapter 21 - The Borrowed Name\n\n'
        'Secure MPD Evidence Intake\nWashington, D.C.\n'
    ), 'Chapter 21 opening changed')
    require('At 12:18:04 EDT / 21:48:04 IST' in text[-2600:], 'Chapter 21 endpoint missing')
    require(text.count('DIA Administrative Review Unit') == 1, 'Price cutaway count changed')
    require(text.count('Secure MPD Evidence Intake') == 2, 'Julie location architecture changed')
    required = [
        'SO-NS-REQ-6540', 'SO-CD-187463-02', 'DIA-SAR-PRICE-01', 'DIA-AR-PRICE-01',
        'DCIS-CD-187463-PRICE-01', 'Price’s active authority ended more than twelve hours before',
        'SSO-NS-004', 'WSS-4', 'K17-PHASE-B', 'The named requestor is not the instruction source',
        'Kessler remained the authorizer', 'Drennan remained the carrier', 'REQUEST CONSTRUCTOR: UNPROVED',
        'MPD-901441 through MPD-901447', 'LSS-SL-90418', 'four liters of oxygen',
        'ninety-two to ninety-three percent saturation', 'successful remote Argus reconstruction',
        'who constructed and submitted the `NSB-EMERGENCY` continuity request after Price’s authority ended',
    ]
    missing = [item for item in required if item not in text]
    require(not missing, f'Chapter 21 required element missing: {missing}')
    prohibited = [
        'Sterling instructed Kessler', 'Sterling personally operated', 'Price authored the later request',
        'Price was innocent', 'Kessler was a conspirator', 'Drennan was a conspirator',
        'Vance personally typed', 'Vance built the borrowed Price identity', 'Tariq was physically present',
        'WSS plaintext was decrypted', 'Julie was exonerated', 'Sterling was guilty',
        'same person built both', 'same actor created every',
    ]
    present = [item for item in prohibited if item in text]
    require(not present, f'Chapter 21 prohibited conclusion present: {present}')
    for artifact in ['TODO', 'DRAFTING NOTE', 'ALTERNATE VERSION', 'PLACEHOLDER']:
        require(artifact not in text, f'Chapter 21 drafting artifact remains: {artifact}')
    print('Chapter 21 content and placement: OK')


def validate_chapter22_mission_lock() -> None:
    actual = blob(MISSION22)
    require(actual == EXPECTED_CHAPTER22_LOCK_BLOB, f'Chapter 22 mission-lock blob changed: {actual}')
    require(sorted(CONTROL.glob('*chapter-22-mission-lock*.md')) == [MISSION22], 'Chapter 22 mission lock duplicated')

    text = MISSION22.read_text(encoding='utf-8')
    required = [
        '# Chapter 22 Mission Lock — The Release Record',
        '**Planning status:** Mission locked; undrafted; non-canon',
        '**12:18:04 EDT / 21:48:04 IST**',
        '**Secure MPD evidence intake, Washington, D.C.**',
        '## 6. Dominant dramatic function',
        'Decisive control-plane attribution and antagonist consequence.',
        '## 7. Mission statement', '## 8. Central dramatic question',
        '## 9. Primary objective', '## 10. Secondary objective',
        '## 11. Success condition', '## 12. Failure condition',
        '## 13. Concrete abort, stop, and narrowing conditions',
        '## 14. POV structure', '**Julie O’Donnell**',
        'Exactly **one** bounded **Sarah Chen**', '## 16. Prohibited POVs',
        '## 17. Causal scene architecture',
        'Scene 1 — The preservation response is not the record',
        'Scene 3 — Midpoint cutaway: the later release had a human act',
        'Scene 6 — Endpoint: the private record is ready to become public',
        '## 18. Early complication', '## 19. Midpoint reversal',
        '## 20. Julie’s consequential decision', '## 21. Visible cost of Julie’s decision',
        '## 22. Character functions', '## 23. Medical and mobility constraints',
        '## 24. Antagonist and institutional pressure',
        '## 25. Evidence available at the opening', '## 26. Evidence still required',
        '## 27. Source-original and derivative rules', '## 28. Custody and seal rules',
        '## 29. Technology and authentication rules', '## 30. Attribution and proof ceilings',
        '## 31. Knowledge-firewall rules', '## 32. Public-versus-private record state',
        '## 33. Facts Chapter 22 may establish',
        '## 34. Conclusions Chapter 22 must not establish',
        '## 35. Book 1 ending-contract obligations advanced', '## 36. Thread disposition',
        '## 37. Intended endpoint', '**13:12:44 EDT / 22:42:44 IST**',
        '## 38. Exact unresolved question carried forward',
        '## 39. Word-budget target, preferred range, and hard ceiling',
        'Chapter 22 target:** **5,000 words**',
        'Preferred range:** **4,600–5,400 words**',
        'Hard ceiling:** **5,800 words**',
        '## 40. House-style requirements', '## 41. Drafting instructions',
        '## 42. Acceptance-gate requirements', '## 43. Explicit production prohibitions',
        '## 44. Chapter 23 and remainder-outline prohibition',
        'same mechanism proves the same human actor',
        'At least one later chapter is therefore necessary.',
        'It is not a Chapter 23 mission lock, scene plan, title, outline, or authorization.',
    ]
    missing = [item for item in required if item not in text]
    require(not missing, f'Chapter 22 mission lock missing required element: {missing}')

    require(text.count('### Scene ') == 6, f'Chapter 22 scene count changed: {text.count("### Scene ")}')
    for field in [
        '- **POV:**', '- **Time:**', '- **Location:**', '- **Immediate objective:**',
        '- **Resistance:**', '- **Evidence/authority involved:**', '- **Physical/medical constraint:**',
        '- **Decision forced:**',
    ]:
        require(text.count(field) >= 6, f'causal scene field incomplete: {field}')
    require(text.count('Scene-ending turn') >= 5 and 'Scene-ending turn / midpoint reversal' in text,
            'causal scene-ending turns incomplete')

    conclusions_section = text.split('## 34. Conclusions Chapter 22 must not establish', 1)[1]
    for claim in [
        'Vance personally performed the original 02:14 deployment.',
        'Sterling personally commanded the operation.',
        'Price is completely innocent',
        'Elias is fully exonerated',
        'WSS plaintext.',
    ]:
        require(claim in conclusions_section, f'proof-ceiling prohibition missing: {claim}')

    for artifact in ['TODO', 'TBD', 'ALTERNATE VERSION', 'SAMPLE PROSE', 'DRAFT CHAPTER 22']:
        require(artifact not in text, f'Chapter 22 mission-lock artifact remains: {artifact}')
    print('Chapter 22 mission lock: OK')


def validate_planning_state_synchronization() -> None:
    require(blob(SERIES_LEDGER) == EXPECTED_SERIES_LEDGER_BLOB,
            'recurring-character ledger changed for planned Chapter 22 events')

    synchronized = [
        ROOT / 'PROJECT_STATE.yaml', ROOT / 'README.md', BOOK / 'manuscript/STATUS.md',
        DRAFTS / 'README.md', CONTROL / 'README.md', CONTROL / '00-overview.md',
        CONTROL / '02-current-project-state.md', CONTROL / '15-open-plot-threads-and-payoff-matrix.md',
        CONTROL / '16-chapter-by-chapter-status-record.md', CONTROL / '20-control-pack-maintenance-rules.md',
        CONTROL / '22-book-1-ending-contract.md', CONTROL / '23-word-budget-and-act-iii-architecture.md',
        CONTROL / '24-thread-disposition-matrix.md',
    ]
    for path in synchronized:
        require('Chapter 22' in path.read_text(encoding='utf-8'), f'Chapter 22 planning state missing in {path}')

    primary_status = [
        ROOT / 'PROJECT_STATE.yaml', ROOT / 'README.md', BOOK / 'manuscript/STATUS.md',
        DRAFTS / 'README.md', CONTROL / 'README.md', CONTROL / '00-overview.md',
        CONTROL / '02-current-project-state.md', CONTROL / '16-chapter-by-chapter-status-record.md',
        CONTROL / '20-control-pack-maintenance-rules.md', CONTROL / '23-word-budget-and-act-iii-architecture.md',
        CONTROL / '24-thread-disposition-matrix.md',
    ]
    for path in primary_status:
        text = path.read_text(encoding='utf-8')
        require('112,091' in text or '112091' in text, f'accepted total missing in {path}')
        require('44-chapter-22-mission-lock.md' in text, f'Chapter 22 mission-lock path missing in {path}')

    project = (ROOT / 'PROJECT_STATE.yaml').read_text(encoding='utf-8')
    for sentinel in [
        f'accepted_words: {EXPECTED_TOTAL}', 'chapters: 1-21', 'active_chapter_drafts: []',
        'status: mission locked; undrafted; non-canon',
        f'mission_lock_blob_sha: {EXPECTED_CHAPTER22_LOCK_BLOB}',
        'prose: none', 'chapter_23_and_later: undrafted and individually mission unlocked',
    ]:
        require(sentinel in project, f'PROJECT_STATE missing: {sentinel}')

    for path in [ROOT / 'README.md', CONTROL / 'README.md', CONTROL / '16-chapter-by-chapter-status-record.md']:
        text = path.read_text(encoding='utf-8')
        require(EXPECTED_CHAPTER22_LOCK_BLOB in text, f'Chapter 22 lock blob missing in {path}')
        require('Chapter 22 prose' in text and ('not created' in text or 'does not exist' in text),
                f'Chapter 22 prose absence not synchronized in {path}')
    print('non-canon Chapter 22 planning state: OK')


def validate_absence_and_hygiene() -> None:
    ch22_artifacts = sorted(
        path for path in BOOK.rglob('*') if path.is_file()
        and any(token in path.name.lower() for token in ('chapter-22', 'chapter_22', 'chapter22'))
    )
    require(ch22_artifacts == [MISSION22], f'unexpected Chapter 22 artifact: {ch22_artifacts}')

    ch23_artifacts = [
        path for path in ROOT.rglob('*') if path.is_file() and '.git' not in path.parts
        and any(token in path.name.lower() for token in ('chapter-23', 'chapter_23', 'chapter23'))
    ]
    require(not ch23_artifacts, f'Chapter 23 artifact exists: {ch23_artifacts}')

    require(not (CHAPTERS / 'chapter-22.md').exists(), 'Chapter 22 manuscript prose exists')
    require(not (DRAFTS / 'chapter-22.md').exists(), 'Chapter 22 draft exists')
    require(not (CHAPTERS / 'chapter-23.md').exists(), 'Chapter 23 manuscript prose exists')
    require(not (DRAFTS / 'chapter-23.md').exists(), 'Chapter 23 draft exists')

    remainder_outlines = [
        path for path in ROOT.rglob('*') if path.is_file() and '.git' not in path.parts and (
            'remainder-outline' in path.name.lower() or 'remainder_outline' in path.name.lower()
            or 'remainder-of-act-iii-outline' in path.name.lower()
            or 'remainder_of_act_iii_outline' in path.name.lower()
            or 'chapter-by-chapter-act-iii' in path.name.lower()
        )
    ]
    require(not remainder_outlines, f'complete remainder outline artifact exists: {remainder_outlines}')

    allowed_ch22 = {MISSION22}
    bad_fragments = ('alternate', 'backup', 'latest', 'final', 'helper', 'debug', 'payload', 'runner', 'apply', 'trigger', 'copy')
    suspicious: list[Path] = []
    for path in ROOT.rglob('*'):
        if not path.is_file() or '.git' in path.parts:
            continue
        name = path.name.lower()
        if any(token in name for token in ('chapter22', 'chapter-22', 'chapter_22')):
            if path not in allowed_ch22 and any(fragment in name for fragment in bad_fragments):
                suspicious.append(path)
    require(not suspicious, f'temporary/alternate Chapter 22 artifact exists: {suspicious}')

    # Complete historical forbidden-temporary-path list retained from the Chapter 21 validator.
    forbidden_paths = [
        ROOT / '.github/workflows/chapter20-acceptance-apply.yml',
        ROOT / '.github/workflows/chapter20-acceptance-pr.yml',
        ROOT / 'chapter20-validator-final.yml',
        ROOT / '.chapter20-acceptance-py',
        ROOT / '.chapter20-acceptance',
        ROOT / '.github/workflows/chapter21-mission-lock-apply.yml',
        ROOT / '.github/workflows/chapter21-mission-lock-pr.yml',
        ROOT / 'chapter21-validator-final.yml',
        ROOT / '.chapter21-mission-lock-py',
        ROOT / '.chapter21-mission-lock',
        ROOT / '.github/workflows/chapter21-draft-apply.yml',
        ROOT / '.github/workflows/chapter21-draft-pr.yml',
        ROOT / '.chapter21-draft-py',
        ROOT / '.chapter21-draft',
        ROOT / '.github/workflows/chapter21-acceptance-apply.yml',
        ROOT / 'tools/.chapter21_acceptance_apply.py',
        ROOT / '.chapter21-acceptance-py',
        ROOT / '.chapter21-acceptance',
        ROOT / 'tools/.chapter21_acceptance_payload_01.b64',
        ROOT / 'tools/.chapter21_acceptance_payload_02.b64',
        ROOT / 'tools/.chapter21_acceptance_payload_03.b64',
        ROOT / 'tools/.chapter21_acceptance_payload_04.b64',
        ROOT / 'tools/.chapter21_acceptance_payload_05.b64',
        ROOT / '.github/workflows/chapter22-mission-lock-apply.yml',
        ROOT / '.github/workflows/chapter22-mission-lock-pr.yml',
        ROOT / 'chapter22-validator-final.yml',
        ROOT / '.chapter22-mission-lock-py',
        ROOT / '.chapter22-mission-lock',
        ROOT / 'tools/.chapter22_mission_lock_apply.py',
        ROOT / 'tools/.chapter22_mission_lock_payload.b64',
    ]
    remaining = [path for path in forbidden_paths if path.exists()]
    require(not remaining, f'temporary helper artifact remains: {remaining}')
    require(not (ROOT / 'tools/validate_book1_chapter20.py').exists(), 'superseded Chapter 20 validator remains')
    require(not (ROOT / 'tools/validate_book1_chapter21.py').exists(), 'superseded Chapter 21 validator remains')
    print('future-artifact absence and hygiene sentinels: OK')


def validate_changed_file_scope() -> None:
    base = os.environ.get('BOOK1_DIFF_BASE', EXPECTED_DIFF_BASE)
    git('cat-file', '-e', f'{base}^{{commit}}')
    result = git('diff', '--name-status', base, '--')
    changed_lines = [line for line in result.stdout.splitlines() if line.strip()]
    changed_paths: set[str] = set()
    for line in changed_lines:
        fields = line.split('\t')
        require(len(fields) >= 2, f'unparseable changed-file line: {line}')
        changed_paths.update(fields[1:])

    allowed = {
        '.github/workflows/book1-manuscript-validation.yml', 'PROJECT_STATE.yaml', 'README.md',
        'books/book-01/control/README.md', 'books/book-01/control/00-overview.md',
        'books/book-01/control/02-current-project-state.md',
        'books/book-01/control/15-open-plot-threads-and-payoff-matrix.md',
        'books/book-01/control/16-chapter-by-chapter-status-record.md',
        'books/book-01/control/20-control-pack-maintenance-rules.md',
        'books/book-01/control/22-book-1-ending-contract.md',
        'books/book-01/control/23-word-budget-and-act-iii-architecture.md',
        'books/book-01/control/24-thread-disposition-matrix.md',
        'books/book-01/control/44-chapter-22-mission-lock.md',
        'books/book-01/drafts/README.md', 'books/book-01/manuscript/STATUS.md',
        'tools/validate_book1_chapter21.py', 'tools/validate_book1_chapter22.py',
    }
    unexpected = sorted(changed_paths - allowed)
    require(not unexpected, f'changed file outside Chapter 22 mission-lock scope: {unexpected}')
    require('books/book-01/control/44-chapter-22-mission-lock.md' in changed_paths,
            'Chapter 22 mission lock missing from diff')
    require('tools/validate_book1_chapter22.py' in changed_paths, 'Chapter 22 validator missing from diff')
    require('tools/validate_book1_chapter21.py' in changed_paths, 'superseded Chapter 21 validator deletion missing')
    require(not any(path.startswith('books/book-01/manuscript/chapters/') for path in changed_paths),
            'accepted manuscript prose changed')
    require('books/book-01/ACCEPTED_MANUSCRIPT.yaml' not in changed_paths, 'accepted manifest changed in diff')
    require('series/recurring-character-ledger.md' not in changed_paths,
            'recurring-character ledger changed for planned events')
    print(f'changed-file scope against {base}: OK')


def validate_diff_hygiene() -> None:
    base = os.environ.get('BOOK1_DIFF_BASE', EXPECTED_DIFF_BASE)
    result = git('diff', '--check', base, '--', check=False)
    require(result.returncode == 0, f'git diff --check failed against {base}:\n{result.stdout}{result.stderr}')
    print(f'git diff --check against {base}: OK')


def main() -> None:
    validate_protected_prose()
    validate_manifest_and_accepted_controls()
    validate_chapter21_content_and_placement()
    validate_chapter22_mission_lock()
    validate_planning_state_synchronization()
    validate_absence_and_hygiene()
    validate_changed_file_scope()
    validate_diff_hygiene()
    print('Book 1 accepted Chapter 21 state and Chapter 22 mission lock: VALID')


if __name__ == '__main__':
    main()
