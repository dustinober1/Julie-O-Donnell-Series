# Book 1 One-Sentence Paragraph Repair Design

## Goal

Reduce the remaining mechanical one-sentence narrative rhythm in _Veridrift_ without changing story content, dialogue wording, chronology, evidence, technology, POV, character knowledge, reveals, or the ending.

## Accepted baseline

- Source of truth: `books/book-01/ACCEPTED_MANUSCRIPT.yaml`.
- Accepted prose: prologue plus Chapters 1–24.
- Accepted words: 105,081.
- Current narrative paragraphs: 2,198.
- Current one-sentence narrative paragraphs: 513.
- Strict review candidates: 230.
- Highest concentration: Chapters 4, 5, 1, 12, 13, 8, 14, and 10.

## Chosen approach

Use a context-aware paragraph-integration pass rather than another global reflow. Every strict candidate is evaluated with its previous and next paragraph. Routine action/reaction beats and technical transitions are attached to the most natural neighboring paragraph. Deliberate emphasis remains isolated.

## Protected material

The pass must preserve:

- all lexical words in their existing order;
- dialogue wording and speaker meaning;
- system-display blocks;
- scene headings, dates, times, locations, and separators;
- countdown beats and zero-crossing moments;
- major discoveries and reversals;
- protected motifs, including `Four seconds.`, `Too perfect.`, `People.`, and the final line;
- chapter endings and accepted chapter order.

## Repair rules

1. Merge routine reactions such as `Marcus paused.` or `Bell looked at her.` into the adjacent paragraph that owns the action.
2. Merge ordinary technical transitions such as `The console chimed.` or `The display updated.` unless the isolated beat marks a genuine reveal or countdown step.
3. Keep one-sentence paragraphs when isolation creates necessary suspense, establishes a scene boundary, or lands a consequential emotional or evidentiary turn.
4. Never merge across a scene separator or chapter boundary.
5. Never alter the wording of system output.
6. When dialogue surrounds a routine beat, attach the beat to the dialogue spoken by the acting character only when context makes the attribution unambiguous. Otherwise leave it isolated.

## Verification

The completed branch must prove:

- accepted word count remains 105,081;
- lexical word sequence remains unchanged in every accepted file;
- chapter headings, separators, system displays, and endings remain intact;
- accepted-file hashes and compiled manuscript are regenerated;
- publication-readiness checks and final revision verification pass;
- the strict candidate count falls materially, with a target below 75;
- no chapter exceeds a 30% one-sentence narrative rate except where justified by action structure.

## Repository output

- Updated accepted manuscript files.
- Updated manifest hashes and compiled manuscript.
- A permanent before/after audit report.
- A reusable context-aware repair tool with explicit protected-line rules.
