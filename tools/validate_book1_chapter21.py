#!/usr/bin/env python3
"""Validate accepted Book 1 through Chapter 21 and protect the next unopened gate."""

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

EXPECTED_MANIFEST_BLOB = 'f334ee9d9512f50065d05bf98b102e93b2236d10'
EXPECTED_TOTAL = 112091
EXPECTED_CHAPTER21_BLOB = '866d4210b7fc808aef48144a91a58280f38fc99c'
EXPECTED_CHAPTER21_WORDS = 4415
EXPECTED_CHAPTER21_LOCK_BLOB = '6c92a5764e5c74d88a8325511ae2b0a86b30b356'
EXPECTED_CHAPTER20_LOCK_BLOB = 'c074e4f6f9ec9cddcbc701e2923f34b3082ede5a'
CHAPTER21 = CHAPTERS / 'chapter-21.md'
REVIEW21 = CONTROL / '43-chapter-21-acceptance-review.md'


def require(value: bool, message: str) -> None:
    if not value:
        raise SystemExit(message)


def blob(path: Path) -> str:
    return subprocess.check_output(['git', 'hash-object', str(path)], text=True).strip()


def word_count(path: Path) -> int:
    return len(path.read_text(encoding='utf-8').split())


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
        require(path.is_file(), f'missing protected chapter: {name}')
        actual_blob = blob(path)
        require(actual_blob == expected_blob, f'protected blob changed: {name} = {actual_blob}')
        actual_words = word_count(path)
        require(actual_words == expected_words, f'protected count changed: {name} = {actual_words}')
    print('protected accepted prose: OK')


def validate_manifest_and_reviews() -> None:
    require(MANIFEST.is_file(), 'accepted manifest missing')
    actual_manifest_blob = blob(MANIFEST)
    require(actual_manifest_blob == EXPECTED_MANIFEST_BLOB, f'accepted manifest changed: {actual_manifest_blob}')
    manifest = MANIFEST.read_text(encoding='utf-8')
    require(f'accepted_words: {EXPECTED_TOTAL}' in manifest, 'accepted total changed')
    require('accepted_endpoint:\n  chapter: 21' in manifest, 'accepted endpoint is not Chapter 21')
    require('eastern: "12:18:04 EDT"' in manifest, 'accepted EDT endpoint changed')
    require('india: "21:48:04 IST"' in manifest, 'accepted IST endpoint changed')
    listed = [int(n) for n in re.findall(r'chapter-(\d+)\.md', manifest)]
    require(listed.count(21) == 1 and max(listed) == 21, f'Chapter 21 manifest entry invalid: {listed}')

    mission20 = CONTROL / '40-chapter-20-mission-lock.md'
    review20 = CONTROL / '41-chapter-20-acceptance-review.md'
    require(blob(mission20) == EXPECTED_CHAPTER20_LOCK_BLOB, 'Chapter 20 mission lock changed')
    require(review20.is_file() and '# ACCEPT' in review20.read_text(encoding='utf-8'), 'Chapter 20 ACCEPT review missing')

    mission21 = CONTROL / '42-chapter-21-mission-lock.md'
    require(blob(mission21) == EXPECTED_CHAPTER21_LOCK_BLOB, 'Chapter 21 mission lock changed')
    require(sorted(CONTROL.glob('*chapter-21-mission-lock*.md')) == [mission21], 'Chapter 21 mission lock duplicated')
    require(REVIEW21.is_file(), 'Chapter 21 acceptance review missing')
    review = REVIEW21.read_text(encoding='utf-8')
    for sentinel in [
        '# ACCEPT',
        '## Promotion authorization',
        f'Final reviewed prose blob:** `{EXPECTED_CHAPTER21_BLOB}`',
        f'Exact final word count:** **{EXPECTED_CHAPTER21_WORDS:,}**',
        f'Accepted-manuscript total after promotion:** **{EXPECTED_TOTAL:,}**',
        'No review-authorized prose repair was necessary.',
    ]:
        require(sentinel in review, f'Chapter 21 review missing: {sentinel}')
    print('manifest, mission locks, and reviews: OK')


def validate_chapter21_content_and_placement() -> None:
    require(CHAPTER21.is_file(), 'accepted Chapter 21 missing')
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


def validate_synchronized_controls() -> None:
    synchronized = [
        ROOT / 'PROJECT_STATE.yaml', ROOT / 'README.md', BOOK / 'manuscript/STATUS.md',
        DRAFTS / 'README.md', CONTROL / 'README.md', CONTROL / '00-overview.md',
        CONTROL / '02-current-project-state.md', CONTROL / '04-source-of-truth-canon-locks.md',
        CONTROL / '05-master-timeline.md', CONTROL / '06-character-state-ledger.md',
        CONTROL / '07-relationship-and-trust-matrix.md', CONTROL / '08-evidence-and-chain-of-custody-ledger.md',
        CONTROL / '09-knowledge-and-information-control-matrix.md', CONTROL / '10-technology-and-system-rules.md',
        CONTROL / '11-organizations-authorities-and-institutional-control.md', CONTROL / '12-location-and-security-architecture.md',
        CONTROL / '13-antagonist-objectives-and-conspiracy-model.md', CONTROL / '14-public-narrative-versus-actual-record.md',
        CONTROL / '15-open-plot-threads-and-payoff-matrix.md', CONTROL / '16-chapter-by-chapter-status-record.md',
        CONTROL / '18-act-iii-entry-state.md', CONTROL / '20-control-pack-maintenance-rules.md',
        CONTROL / '22-book-1-ending-contract.md', CONTROL / '23-word-budget-and-act-iii-architecture.md',
        CONTROL / '24-thread-disposition-matrix.md', SERIES_LEDGER,
    ]
    for path in synchronized:
        text = path.read_text(encoding='utf-8')
        require('Chapter 21' in text, f'Chapter 21 state missing in {path}')
    project = (ROOT / 'PROJECT_STATE.yaml').read_text(encoding='utf-8')
    require(f'accepted_words: {EXPECTED_TOTAL}' in project, 'PROJECT_STATE accepted words changed')
    require('chapters: 1-21' in project, 'PROJECT_STATE chapter range changed')
    require('active_chapter_drafts: []' in project, 'PROJECT_STATE active drafts not empty')
    ledger = SERIES_LEDGER.read_text(encoding='utf-8')
    for sentinel in ['Chapter 21 accepted recurring-character delta', 'Leland Price — RECURRING', 'first accepted on-page appearance']:
        require(sentinel in ledger, f'recurring ledger missing: {sentinel}')
    print('synchronized accepted state and recurring ledger: OK')


def validate_absence_and_hygiene() -> None:
    chapter22_artifacts = [
        path for path in BOOK.rglob('*') if path.is_file()
        and ('chapter-22' in path.name.lower() or 'chapter_22' in path.name.lower())
    ]
    require(not chapter22_artifacts, f'Chapter 22 artifact exists: {chapter22_artifacts}')

    remainder_outlines = [
        path for path in BOOK.rglob('*') if path.is_file() and (
            'remainder-outline' in path.name.lower() or 'remainder_outline' in path.name.lower()
            or 'remainder-of-act-iii-outline' in path.name.lower()
            or 'remainder_of_act_iii_outline' in path.name.lower()
            or 'chapter-by-chapter-act-iii' in path.name.lower()
        )
    ]
    require(not remainder_outlines, f'complete remainder outline artifact exists: {remainder_outlines}')

    allowed_ch21 = {CHAPTER21, CONTROL / '42-chapter-21-mission-lock.md', REVIEW21}
    bad_fragments = ('alternate', 'backup', 'latest', 'final', 'helper', 'debug', 'payload', 'runner', 'apply', 'trigger', 'copy')
    suspicious = []
    for path in ROOT.rglob('*'):
        if not path.is_file() or '.git' in path.parts:
            continue
        name = path.name.lower()
        if 'chapter21' in name or 'chapter-21' in name or 'chapter_21' in name:
            if path not in allowed_ch21 and any(fragment in name for fragment in bad_fragments):
                suspicious.append(path)
    require(not suspicious, f'temporary/alternate Chapter 21 artifact exists: {suspicious}')

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
    ]
    remaining = [path for path in forbidden_paths if path.exists()]
    require(not remaining, f'temporary helper artifact remains: {remaining}')
    require(not (ROOT / 'tools/validate_book1_chapter20.py').exists(), 'superseded Chapter 20 validator remains')
    print('absence and hygiene sentinels: OK')


def validate_diff_hygiene() -> None:
    base = os.environ.get('BOOK1_DIFF_BASE', '44c2375b248530f47ee84875aaaee82c747e0010')
    result = subprocess.run(['git', 'diff', '--check', base, '--'], text=True, capture_output=True)
    require(result.returncode == 0, f'git diff --check failed against {base}:\n{result.stdout}{result.stderr}')
    print(f'git diff --check against {base}: OK')


def main() -> None:
    validate_protected_prose()
    validate_manifest_and_reviews()
    validate_chapter21_content_and_placement()
    validate_synchronized_controls()
    validate_absence_and_hygiene()
    validate_diff_hygiene()
    print('Book 1 accepted Chapter 21 state: VALID')


if __name__ == '__main__':
    main()
