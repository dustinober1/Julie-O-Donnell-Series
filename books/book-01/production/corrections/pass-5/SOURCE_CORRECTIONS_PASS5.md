# VERIDRIFT — Pass 5 Source and Styling Map

Pass 5 changes formatting and card order only, except for the exact removal of the Prologue `Location:` label. Plot, chronology, dialogue, evidence, technology, and chapter endings remain unchanged.

## Locked styles

### Scene Card

Use for location, date, time, and dual-time-zone cards.

- Narrative serif font family
- Small caps
- Centered
- No first-line indent
- Controlled spacing
- Keep with following paragraph
- Automatic hyphenation suppressed

### System Display

Use for terminal output, interface labels, certificates, timers, status messages, identifiers, and other literal machine records.

- Monospaced font
- Left aligned with controlled side indents
- No first-line indent
- Intentional line breaks preserved
- Automatic hyphenation suppressed
- Safe word wrapping enabled

## Exact ledger actions

- **P06 — Prologue:** delete `Location: ` and apply Scene Card to `Forward Operating Base, Near the Pakistan Border`.
- **P07 — Chapter 5:** apply Scene Card to the standalone `Reston, Virginia` transition.
- **P08 — Chapter 14:** order and style the card as:
  1. `Commercial Garage West of Hartwell`
  2. `07:46:00 EDT / 17:16:00 IST`
- **P09 — Full master:** replace all uses of the old production `SceneMetadata` and `DisplayText` paragraph styles with Scene Card or System Display as appropriate. Normalize every scene-card group to location before date/time.

## Reclassified standalone records

The following were not scene cards and are now treated accordingly:

- `04:54:47` — System Display
- `04:58:11` — System Display
- `05:55:08 EASTERN DAYLIGHT TIME.` — System Display
- `07:08 EDT.` — Body No Indent, because it is a handwritten paper-log entry rather than a machine display

## Later-card order corrections

The following chapter-opening or transition pairs now place location before date/time:

- Chapter 15: Commercial Garage West of Hartwell / October 13, 07:49 EDT
- Chapter 16: Secure MPD Evidence Intake / October 13, 08:18 EDT
- Chapter 17: Secure MPD Evidence Intake / October 14, 09:17 EDT
- Chapter 18: Forward Post Arjun / October 14, 18:42 IST / 09:12 EDT
- Chapter 19: Secure MPD Evidence Intake / October 14, 10:01 EDT / 19:31 IST
- Chapter 20: Secure MPD Evidence Intake / October 15, 09:06 EDT
- Chapter 21: Secure MPD Evidence Intake / October 15, 10:32 EDT
- Chapter 22: Secure MPD Evidence Intake / October 15, 12:18 EDT
- Chapter 23: Secure MPD Evidence Intake / October 15, 13:12 EDT
- Chapter 24: Secure MPD Evidence Intake / October 16, 09:04 EDT
