# Workflow Guide

## Production Hold

Production is on hold until the scaffold is reviewed.

## Standard Chapter Workflow

```text
/julie-repo-verify
/julie-chapter-context <book> <chapter>
/julie-plan-chapter <book> <chapter>
/julie-draft-chapter <book> <chapter>
/julie-revise-chapter <book> <chapter>
/julie-continuity-pass <book> <chapter>
/julie-ai-tell-sweep <book> <chapter>
/julie-canon-update <book> <chapter>
/julie-next-chapter-prompt <book> <next-chapter>
```

## Canon Rule

Chapter commands may discover canon. Only canon-maintenance commands may promote canon.

## First Recommended Production Sequence

After review:

```text
/julie-series-status
/julie-chapter-context 1 prologue
/julie-plan-chapter 1 prologue
```
