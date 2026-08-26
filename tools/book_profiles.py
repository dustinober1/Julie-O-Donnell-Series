#!/usr/bin/env python3
"""Per-book settings for the detail-continuity tooling.

The extractor and the rule engine were written for Book 1 and hardcoded its
two time zones, its manifest format, and its artifact paths. Book 2's premise
is a timestamp-normalization failure across heterogeneous clock bases, so the
same machinery matters there more, not less -- and it is far cheaper to install
at 5,600 words than at 105,000.

This module holds everything that differs between books. Book 1's profile
reproduces the previous hardcoded constants exactly, so its extracted index and
its derived chronology stay byte-identical.

A note on the tool names. ``extract_book1_detail_index.py`` and
``check_book1_detail_rules.py`` keep their Book 1 names even though they now
serve both books, because roughly ten frozen Book 1 control records cite them by
path. Renaming would orphan those citations in documents that must not be
rewritten. Run Book 2 with ``--book 2``.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


@dataclass(frozen=True)
class Zone:
    """One named clock basis and its offset from the book's base zone."""

    canon: str
    aliases: tuple[str, ...]
    offset_seconds: int


@dataclass(frozen=True)
class BookProfile:
    key: str
    number: int
    source_of_truth: Path
    source_kind: str          # "accepted-manifest" | "narrative-units"
    expected_units: int | None
    index_path: Path
    chronology_path: Path
    zones: tuple[Zone, ...]
    base_zone: str
    zone_pair: tuple[str, str] | None   # the pair R1 checks, if any
    prose_root: Path
    # Book 1 states narrative-present time in standalone scene headers. Book 2
    # states it inline, sentence-initially ("At 15:34, Julie asked"). Anchoring
    # R2 on the sentence-initial form only is deliberate: a mid-sentence time is
    # often a forward reference ("set for 09:00 the following morning"), and
    # treating one as narrative present would invent a backward step.
    inline_time_anchor: str | None = None
    _canon: dict = field(default_factory=dict, repr=False, compare=False)

    # -- zone helpers -----------------------------------------------------

    def zone_canon(self) -> dict[str, str]:
        """Lowercased alias -> canonical zone name."""
        table: dict[str, str] = {}
        for zone in self.zones:
            for alias in zone.aliases:
                table[alias.lower()] = zone.canon
        return table

    def zone_alternation(self) -> str:
        """Regex alternation over every alias, longest first.

        Longest-first matters: "Eastern" would otherwise shadow "Eastern
        Daylight Time" and the zone would be misread as the bare form.
        """
        aliases = sorted(
            {alias for zone in self.zones for alias in zone.aliases},
            key=len,
            reverse=True,
        )
        return "|".join(re.escape(alias) for alias in aliases)

    def offset_between(self, first: str, second: str) -> int:
        """Seconds to add to `first` to reach `second`."""
        by_name = {zone.canon: zone for zone in self.zones}
        return by_name[second].offset_seconds - by_name[first].offset_seconds

    def offset_label(self) -> str:
        if not self.zone_pair:
            return ""
        seconds = self.offset_between(*self.zone_pair)
        sign = "+" if seconds >= 0 else "-"
        hours, rem = divmod(abs(seconds), 3600)
        return f"{sign}{hours:02d}:{rem // 60:02d}"


BOOK_1 = BookProfile(
    key="book-01",
    number=1,
    source_of_truth=REPO_ROOT / "books/book-01/ACCEPTED_MANUSCRIPT.yaml",
    source_kind="accepted-manifest",
    expected_units=25,
    index_path=REPO_ROOT / "artifacts/book1-detail-index.json",
    chronology_path=REPO_ROOT / "artifacts/book1-derived-chronology.md",
    prose_root=REPO_ROOT / "books/book-01/manuscript",
    base_zone="EDT",
    zone_pair=("EDT", "IST"),
    zones=(
        Zone("EDT", ("EDT", "Eastern", "Eastern Daylight Time"), 0),
        Zone("IST", ("IST", "Indian", "Indian Standard Time"), int(9.5 * 3600)),
    ),
)

# Book 2's zones come from outline/07-scene-architecture-and-chapter-mission-locks.md:
# "Canadian locations use PDT (UTC-7) during this period." Only PDT and UTC are
# canon today. No American zone is pinned yet, so none is invented here; add one
# when a control document establishes it.
BOOK_2 = BookProfile(
    key="book-02",
    number=2,
    source_of_truth=REPO_ROOT / "books/book-02/MANUSCRIPT_STATUS.yaml",
    source_kind="narrative-units",
    expected_units=None,          # Book 2 is mid-drafting; the count grows.
    index_path=REPO_ROOT / "artifacts/book2-detail-index.json",
    chronology_path=REPO_ROOT / "artifacts/book2-derived-chronology.md",
    prose_root=REPO_ROOT / "books/book-02/manuscript",
    inline_time_anchor=r"^At (\d{1,2}):([0-5]\d)(?::([0-5]\d)(\.\d+)?)?(?:\s+(ZONES))?\b",
    base_zone="PDT",
    zone_pair=("PDT", "UTC"),
    zones=(
        Zone("PDT", ("PDT", "Pacific", "Pacific Daylight Time"), 0),
        Zone("UTC", ("UTC", "Zulu", "Coordinated Universal Time"), 7 * 3600),
    ),
)

PROFILES = {1: BOOK_1, 2: BOOK_2}


def profile(number: int | str) -> BookProfile:
    try:
        return PROFILES[int(number)]
    except (KeyError, ValueError):
        known = ", ".join(str(k) for k in sorted(PROFILES))
        raise SystemExit(f"unknown book {number!r}; known books: {known}")


def add_book_argument(parser) -> None:
    parser.add_argument(
        "--book",
        default=1,
        type=int,
        choices=sorted(PROFILES),
        help="which book to operate on (default: 1)",
    )
