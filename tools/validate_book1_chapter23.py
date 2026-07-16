#!/usr/bin/env python3
"""Protect accepted Book 1 through Chapter 23 while Chapter 24 remains a draft."""
from validate_book1_chapter24_draft import CH23_REVIEW, blob, fail, read, validate_common, word_count

EXPECTED = {
    "books/book-01/manuscript/chapters/chapter-13.md": (6175, "e7d04921431e571aab434f2f4b808655e363d30c"),
    "books/book-01/manuscript/chapters/chapter-14.md": (5763, "78f7fff02cd271fecbc94f7daf7151dbebbd5c6d"),
    "books/book-01/manuscript/chapters/chapter-15.md": (5993, "b8e7e2ae573a6c25ea096121c75acee867f3fad2"),
    "books/book-01/manuscript/chapters/chapter-16.md": (6024, "dd5249f4b510a9da9ad19ab2902a95ce1e62a1d8"),
    "books/book-01/manuscript/chapters/chapter-17.md": (5888, "1c4022ebb8d27d8d448f98bcf74fbf09e6e560c1"),
    "books/book-01/manuscript/chapters/chapter-18.md": (4478, "6f5873d6e975ec74646af152aad22ea84545fc01"),
    "books/book-01/manuscript/chapters/chapter-19.md": (5393, "1c7cc22fc7c480cb247efa1f6a2c0d0b1e1b1baf"),
    "books/book-01/manuscript/chapters/chapter-20.md": (4307, "0bd12f43beeef48d5e897ee1fa78a333bd23099b"),
    "books/book-01/manuscript/chapters/chapter-21.md": (4415, "866d4210b7fc808aef48144a91a58280f38fc99c"),
    "books/book-01/manuscript/chapters/chapter-22.md": (4716, "034ab496794594427d8409d03e7c6659d41b6a91"),
    "books/book-01/manuscript/chapters/chapter-23.md": (4610, "1f511d36404450f201b34a075f441d350eb7cc52"),
}

validate_common()
for path, (words, expected_blob) in EXPECTED.items():
    if word_count(path) != words or blob(path) != expected_blob:
        fail(f"accepted chapter mismatch: {path}")
if sum(words for words, _ in EXPECTED.values()) != 57762:
    fail("accepted Act III subtotal mismatch")
review = read(CH23_REVIEW)
for phrase in ("## 25. Explicit verdict\n\n**ACCEPT**", "## 20. Review-authorized prose repair\n\n**None.**", "**4,610**", "121,417"):
    if phrase not in review:
        fail(f"Chapter 23 review missing {phrase}")
print("PASS: accepted Book 1 through Chapter 23 remains byte-protected during Chapter 24 drafting")
