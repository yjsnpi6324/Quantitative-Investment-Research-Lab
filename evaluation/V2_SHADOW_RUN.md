# V2 Shadow Run Contract

## Purpose

Compare A-Research System V2 against the current V1 baseline without changing production behavior.

## Shadow-run period

V2 is evaluated alongside V1 for a meaningful sample of trading-day runs and both weekend modes.

## Compare

### Reliability
- Canonical report completeness
- Prediction Ledger write success
- Notion synchronization success
- GitHub ↔ Notion reconciliation
- duplicate rate
- missing-field rate
- recovery success

### Research quality
- T+1/T+3/T+5 directional accuracy
- confidence calibration
- error attribution quality
- market-regime stability
- AI-sector subtheme stability

### Operational quality
- runtime complexity
- data-source failures
- PDF delivery success
- audit findings
- manual intervention required

## Promotion gate

V2 must not become Champion merely because it is newer. Promotion requires:

1. No critical integrity regression.
2. No increase in silent failures.
3. Reproducible ledger records.
4. Clear task separation.
5. Evaluation quality at least comparable to V1, with measurable improvement where claimed.
6. Recovery path demonstrably works.

If the gate is not met, V1 remains Champion and V2 remains Challenger.
