# Veridrift Interior Style Specification — Production Proof

## Authority and status

This is a proof specification, not a final locked publishing specification. Repository-locked values take precedence. The accepted prose remains byte-for-byte frozen.

## Page and margins

- Trim: 6 x 9 inches, used as a documented proof default because no locked trim was found.
- Mirrored margins: approximately 0.85 inch inner and 0.65 inch outer.
- Top and bottom margins: approximately 0.75 inch.
- Chapter openings: new pages; DOCX requests odd-page starts. The PDF does not force recto parity where automatic parity could create malformed pagination.

## Typography

- Body: DejaVu Serif, approximately 11 pt, approximately 14.5 pt leading.
- First-line indent: 0.25 inch.
- No first-line indent after a chapter heading, scene metadata, or scene break.
- Chapter headings: centered, restrained, and lowered on the opening page.
- Scene breaks: centered `* * *`.
- System displays: DejaVu Sans Mono, reduced size, indented from body measure.
- Widow/orphan controls are requested where supported.

## Running furniture

- Main-text page numbering begins with the Prologue.
- Chapter-opening pages suppress running heads and folios.
- Body pages use restrained title/chapter running heads and centered folios.
- Title, proof-notice, chapter-opening, and intentionally blank pages carry no running head.

## Front matter

Only the title and conspicuous production-proof notices are included. Author identity, copyright, publisher/imprint, edition, ISBNs, dedication, acknowledgments, logo, and cover are not invented.

## EPUB

- EPUB 3, reflowable, `en-US`.
- Prologue and Chapters 1–24 are separate navigable sections.
- No fixed page numbers, print running heads, JavaScript, remote resources, or forced body font family.
- No cover metadata is emitted without an approved final cover.
