# Prediction Recovery Baseline — 2026-08-26

This is the post-incident baseline after the large Notion deletion event.

## Confirmed recoverable records

The current durable Notion/GitHub evidence confirms the active prediction history beginning on 2026-08-20, with gaps documented below.

## Confirmed historical gaps

- `2026-08-20 × 基本盘预测` — original daily report not recoverable from currently accessible durable sources.
- `2026-08-21 × AI板块预测` — original daily report not recoverable from currently accessible durable sources.
- `2026-08-23` — non-trading day; no reliable standalone basic-market or AI-sector review was recovered. This is not counted as a missing trading-day prediction.

## Accounting treatment

The two unrecoverable historical predictions are classified as `MISSING_ORIGINAL_PREDICTION` and are excluded from hit-rate denominators. They must never be reconstructed from later market outcomes.

## Recovery policy

Future Notion deletion or corruption must be recoverable from the versioned GitHub Prediction Ledger. Every completed prediction run must produce a durable ledger record and then synchronize to Notion.

## Audit status

- GitHub evaluation framework: intact.
- Prediction Ledger schema: intact.
- Notion reconciliation contract: established.
- Historical unrecoverable samples: explicitly recorded.
- Further historical recovery: only from demonstrable original evidence.
