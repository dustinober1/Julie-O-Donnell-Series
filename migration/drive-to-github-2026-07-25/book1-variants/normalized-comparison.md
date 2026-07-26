# Normalized Comparison — Drive-Native Prologue and Chapter 1

**Comparison baseline:** accepted Book 1 Markdown at `9708fdd86e9292a75b7683152c7746567f015cc6`  
**Disposition rule:** no post-freeze Drive difference changes accepted prose automatically.

## Method

The Drive Docs were exported as Markdown. Comparison normalization removed Google-export escape characters, normalized line endings and nonbreaking spaces, and treated display-line wrapping as formatting. Curly quotation marks, em dashes, words, punctuation, paragraph order, and scene-break markers remained significant.

## Prologue

### Formatting-only differences

- Several display fields are separate lines in Drive but collapsed into prose paragraphs in the publication-master Markdown.
- Drive contains two nonbreaking-space artifacts after `No.` in dialogue.
- Google-export line wrapping differs.

### Substantive or structural differences

| Location | Accepted GitHub Markdown | Drive-native Doc | Classification | Disposition |
|---|---|---|---|---|
| relay-history sentence | `At 0214,` | `At 0214 hours,` | substantive wording divergence | neither applied automatically |
| after `That was the first lie.` | no scene break | `---` | structural Drive divergence | Drive separator remains non-authoritative |

A third source exists: the approved Pass 4 production correction changes the same narrative phrase to `At 02:14,`. That correction was verified in the production master but is absent from the frozen accepted Markdown. See `prologue-correction-proposal.md`.

## Chapter 1

After display and whitespace normalization, the lexical prose matches the accepted GitHub Chapter 1.

One structural difference remains:

- Drive inserts `---` before `Julie carried the shotgun into the house. At 10:43...`.
- The accepted GitHub Chapter 1 has no scene break there.

**Classification:** accidental or isolated Drive structural divergence.  
**Disposition:** GitHub remains authoritative; no accepted prose change proposed.

## Authority result

- Accepted Book 1 Markdown remains unchanged.
- Both Drive variants are preserved as migration evidence.
- The Prologue punctuation/time-format conflict is isolated for explicit correction review.
- Chapter 1 requires no correction proposal.
