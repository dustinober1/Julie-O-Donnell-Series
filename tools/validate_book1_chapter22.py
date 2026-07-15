#!/usr/bin/env python3
"""Protect accepted Book 1 through Chapter 21 and the sole non-canon Chapter 22 draft."""

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

EXPECTED_DIFF_BASE = '6669d120a88ce9d6940fa9e75fc2a369bb277aa5'
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
EXPECTED_CHAPTER22_DRAFT_BLOB = '034ab496794594427d8409d03e7c6659d41b6a91'
EXPECTED_CHAPTER22_DRAFT_WORDS = 4641
EXPECTED_SERIES_LEDGER_BLOB = '417483a55fedadbf9195cc3f0dffa2d30dfb94f5'

CHAPTER21 = CHAPTERS / 'chapter-21.md'
DRAFT22 = DRAFTS / 'chapter-22.md'
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
        MISSION22: EXPECTED_CHAPTER22_LOCK_BLOB,
    }
    for path, expected in protected_controls.items():
        actual = blob(path)
        require(actual == expected, f'protected control changed: {path} = {actual}')

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
        'Decisive control-plane attribution and antagonist consequence.',
        'Exactly **one** bounded **Sarah Chen**',
        'Scene 1 — The preservation response is not the record',
        'Scene 3 — Midpoint cutaway: the later release had a human act',
        'Scene 6 — Endpoint: the private record is ready to become public',
        '**13:12:44 EDT / 22:42:44 IST**',
        'Chapter 22 target:** **5,000 words**',
        'Preferred range:** **4,600–5,400 words**',
        'Hard ceiling:** **5,800 words**',
        'same mechanism proves the same human actor',
        'At least one later chapter is therefore necessary.',
        'It is not a Chapter 23 mission lock, scene plan, title, outline, or authorization.',
    ]
    missing = [item for item in required if item not in text]
    require(not missing, f'Chapter 22 mission lock missing required element: {missing}')
    require(text.count('### Scene ') == 6, f'Chapter 22 mission-lock scene count changed: {text.count("### Scene ")}')
    print('Chapter 22 mission lock: OK')


def validate_chapter22_draft() -> None:
    require(DRAFT22.is_file(), 'Chapter 22 draft missing')
    require(sorted(DRAFTS.glob('chapter-22.md')) == [DRAFT22], 'Chapter 22 draft duplicated')
    require(not (CHAPTERS / 'chapter-22.md').exists(), 'Chapter 22 manuscript prose exists')
    actual_blob = blob(DRAFT22)
    require(actual_blob == EXPECTED_CHAPTER22_DRAFT_BLOB, f'Chapter 22 draft blob changed: {actual_blob}')
    count = word_count(DRAFT22)
    require(count == EXPECTED_CHAPTER22_DRAFT_WORDS, f'Chapter 22 draft count changed: {count}')
    require(4600 <= count <= 5400, f'Chapter 22 draft outside preferred range: {count}')
    require(count <= 5800, f'Chapter 22 draft exceeds hard ceiling: {count}')

    text = DRAFT22.read_text(encoding='utf-8')
    require(text.startswith(
        '12:18:04 EDT / 21:48:04 IST\n\n'
        '# Chapter 22 - The Release Record\n\n'
        'Secure MPD Evidence Intake\nWashington, D.C.\n'
    ), 'Chapter 22 opening changed')

    scene_starts = [
        '12:18:04 EDT / 21:48:04 IST',
        '12:25:40 EDT / 21:55:40 IST',
        '12:36:18 EDT / 22:06:18 IST',
        '12:47:09 EDT / 22:17:09 IST',
        '12:57:30 EDT / 22:27:30 IST',
        '13:08:20 EDT / 22:38:20 IST',
    ]
    for marker in scene_starts:
        require(text.count(marker) == 1, f'Chapter 22 scene marker count invalid: {marker} = {text.count(marker)}')
    require(text.count('At 13:12:44 EDT / 22:42:44 IST') == 1, 'Chapter 22 endpoint count invalid')
    require('At 13:12:44 EDT / 22:42:44 IST' in text[-1800:], 'Chapter 22 endpoint not near end')
    require(text.count('Apex Building Three\nReston, Virginia\n12:36:18 EDT / 22:06:18 IST') == 1,
            'Chen cutaway architecture invalid')

    required = [
        'SO-CB-6540-01', 'SO-CD-187463-03',
        'APX-B3-IDM-0214', 'APX-CD-187463-02',
        'APX-B3-RR-0754', 'APX-CD-187463-03',
        'ARGUS-CD-187463-01', 'CHEN-DECL-187463-01', 'MERCER-DECL-187463-01',
        'ARGUS-K17-RC-0751', 'DCIS-OAR-187463-01', 'DCIS-BF-187463-02',
        'DCIS-PRP-187463-01',
        'LIVE PALM CONFIRMATION: ACCEPTED',
        'LOCAL SOURCE-STATE WRITES: 0',
        'PERSONAL FINDING LIMITED TO LATER REMOTE RELEASE.',
        'ORIGINAL 02:14 HUMAN OPERATOR: NOT ESTABLISHED.',
        'STERLING PERSONAL COMMAND: NOT ESTABLISHED.',
        'COMMON CONSTRUCTION FAMILY: ESTABLISHED',
        'COMMON HUMAN INVOKER: NOT ESTABLISHED',
        'FAILED LOCAL COMMIT AND SUCCESSFUL REMOTE RECONSTRUCTION: DISTINCT EVENTS',
        'MPD-901441` through `MPD-901447',
        'sealed, separate, offline, stationary',
        '`SSO-NS-004` remained closed and unused',
        'all seven MPD packages remained sealed and stationary',
        'WSS kept its encrypted message blocks',
        'The later reconstruction',
        'Same mechanism',
        'One operator event.',
    ]
    missing = [item for item in required if item not in text]
    require(not missing, f'Chapter 22 required element missing: {missing}')

    prohibited = [
        '# Chapter 23', 'Chapter 23 -', 'Sterling instructed Vance',
        'Sterling personally commanded the operation', 'Vance personally performed the original 02:14 deployment',
        'Vance personally constructed every borrowed identity', 'Price was innocent',
        'Elias was exonerated', 'WSS plaintext was decrypted', 'Tariq was physically at K-17',
        'opened SSO-NS-004', 'operated SSO-NS-004', 'opened MPD-901',
        'reconstructed the 47 incomplete files', 'invented the 311 excluded files',
    ]
    present = [item for item in prohibited if item in text]
    require(not present, f'Chapter 22 prohibited conclusion or action present: {present}')
    for artifact in ['TODO', 'TBD', 'DRAFTING NOTE', 'ALTERNATE VERSION', 'PLACEHOLDER', 'SAMPLE PROSE']:
        require(artifact not in text, f'Chapter 22 drafting artifact remains: {artifact}')
    print('Chapter 22 draft content, count, and placement: OK')


def validate_draft_state_synchronization() -> None:
    require(blob(SERIES_LEDGER) == EXPECTED_SERIES_LEDGER_BLOB,
            'recurring-character ledger changed for non-canon Chapter 22 events')

    synchronized = [
        ROOT / 'PROJECT_STATE.yaml', ROOT / 'README.md', BOOK / 'manuscript/STATUS.md',
        DRAFTS / 'README.md', CONTROL / 'README.md', CONTROL / '00-overview.md',
        CONTROL / '02-current-project-state.md', CONTROL / '16-chapter-by-chapter-status-record.md',
        CONTROL / '20-control-pack-maintenance-rules.md',
        CONTROL / '23-word-budget-and-act-iii-architecture.md',
        CONTROL / '24-thread-disposition-matrix.md',
    ]
    for path in synchronized:
        text = path.read_text(encoding='utf-8')
        draft_path_sentinel = 'books/book-01/drafts/chapter-22.md' if path == ROOT / 'PROJECT_STATE.yaml' else 'drafts/chapter-22.md'
        for sentinel in [
            'Chapter 22', '112,091', '44-chapter-22-mission-lock.md',
            draft_path_sentinel, EXPECTED_CHAPTER22_DRAFT_BLOB,
            f'{EXPECTED_CHAPTER22_DRAFT_WORDS:,}', 'non-canon',
        ]:
            require(sentinel in text, f'Chapter 22 draft state missing in {path}: {sentinel}')
        require('acceptance review' in text.lower(), f'acceptance-review state missing in {path}')
        require('Chapter 23' in text, f'Chapter 23 prohibition missing in {path}')

    project = (ROOT / 'PROJECT_STATE.yaml').read_text(encoding='utf-8')
    for sentinel in [
        f'accepted_words: {EXPECTED_TOTAL}', 'chapters: 1-21',
        'active_chapter_drafts:\n      - 22',
        'status: first draft complete; non-canon; formal acceptance review pending',
        f'draft_blob_sha: {EXPECTED_CHAPTER22_DRAFT_BLOB}',
        f'draft_words: {EXPECTED_CHAPTER22_DRAFT_WORDS}',
        'draft_path: books/book-01/drafts/chapter-22.md',
        'acceptance_review: none',
        'chapter_23_and_later: undrafted and individually mission unlocked',
    ]:
        require(sentinel in project, f'PROJECT_STATE missing: {sentinel}')
    print('non-canon Chapter 22 draft state: OK')


def validate_absence_and_hygiene() -> None:
    ch22_artifacts = sorted(
        path for path in BOOK.rglob('*') if path.is_file()
        and any(token in path.name.lower() for token in ('chapter-22', 'chapter_22', 'chapter22'))
    )
    require(ch22_artifacts == sorted([MISSION22, DRAFT22]), f'unexpected Chapter 22 artifact: {ch22_artifacts}')

    ch22_reviews = sorted(CONTROL.glob('*chapter-22-acceptance-review*.md'))
    require(not ch22_reviews, f'Chapter 22 acceptance review exists: {ch22_reviews}')

    ch23_artifacts = [
        path for path in ROOT.rglob('*') if path.is_file() and '.git' not in path.parts
        and any(token in path.name.lower() for token in ('chapter-23', 'chapter_23', 'chapter23'))
    ]
    require(not ch23_artifacts, f'Chapter 23 artifact exists: {ch23_artifacts}')

    require(not (CHAPTERS / 'chapter-22.md').exists(), 'Chapter 22 manuscript prose exists')
    require(DRAFT22.exists(), 'Chapter 22 draft missing')
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

    allowed_ch22 = {MISSION22, DRAFT22}
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
        ROOT / '.github/workflows/chapter22-draft-apply.yml',
        ROOT / '.github/workflows/chapter22-draft-pr.yml',
        ROOT / '.chapter22-draft-py',
        ROOT / '.chapter22-draft',
        ROOT / 'tools/.chapter22_draft_apply.py',
        ROOT / 'tools/.chapter22_draft_payload.b64',
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
        '.github/workflows/book1-manuscript-validation.yml',
        'PROJECT_STATE.yaml', 'README.md',
        'books/book-01/manuscript/STATUS.md', 'books/book-01/drafts/README.md',
        'books/book-01/drafts/chapter-22.md',
        'books/book-01/control/README.md', 'books/book-01/control/00-overview.md',
        'books/book-01/control/02-current-project-state.md',
        'books/book-01/control/16-chapter-by-chapter-status-record.md',
        'books/book-01/control/20-control-pack-maintenance-rules.md',
        'books/book-01/control/23-word-budget-and-act-iii-architecture.md',
        'books/book-01/control/24-thread-disposition-matrix.md',
        'tools/validate_book1_chapter22.py',
    }
    unexpected = sorted(changed_paths - allowed)
    require(not unexpected, f'changed file outside Chapter 22 draft scope: {unexpected}')
    required_changed = {
        'books/book-01/drafts/chapter-22.md',
        'PROJECT_STATE.yaml', 'README.md',
        'books/book-01/manuscript/STATUS.md', 'books/book-01/drafts/README.md',
        'books/book-01/control/README.md', 'books/book-01/control/00-overview.md',
        'books/book-01/control/02-current-project-state.md',
        'books/book-01/control/16-chapter-by-chapter-status-record.md',
        'books/book-01/control/20-control-pack-maintenance-rules.md',
        'books/book-01/control/23-word-budget-and-act-iii-architecture.md',
        'books/book-01/control/24-thread-disposition-matrix.md',
        'tools/validate_book1_chapter22.py',
    }
    missing = sorted(required_changed - changed_paths)
    require(not missing, f'required Chapter 22 draft file missing from diff: {missing}')
    require(not any(path.startswith('books/book-01/manuscript/chapters/') for path in changed_paths),
            'accepted manuscript prose changed')
    require('books/book-01/ACCEPTED_MANUSCRIPT.yaml' not in changed_paths, 'accepted manifest changed in diff')
    require('series/recurring-character-ledger.md' not in changed_paths,
            'recurring-character ledger changed for draft-only events')
    require('books/book-01/control/44-chapter-22-mission-lock.md' not in changed_paths,
            'Chapter 22 mission lock changed during draft session')
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
    validate_chapter22_draft()
    validate_draft_state_synchronization()
    validate_absence_and_hygiene()
    validate_changed_file_scope()
    validate_diff_hygiene()
    print('Book 1 accepted Chapter 21 state and non-canon Chapter 22 draft: VALID')


if __name__ == '__main__':
    main()
