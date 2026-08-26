# Notion ↔ GitHub Prediction Ledger Integrity

## Purpose

GitHub is the durable, versioned backup of prediction facts. Notion is the human-facing project/state/review layer. A missing Notion record must never imply a missing prediction if the GitHub ledger contains the original fact.

## Daily integrity key

Each prediction is identified by:

`date × task × prediction_type × model_version`

Tasks:
- `基本盘预测`
- `AI板块预测`

Prediction types:
- `交易日预测`
- `非交易日复盘`

## Required reconciliation

For every completed task run, reconcile Notion and GitHub by:

1. Date
2. Task
3. Prediction type
4. Model/rule/data version
5. T+1/T+3/T+5 forecast presence
6. Validation status after outcomes become available

Expected states:

- `MATCHED` — present and consistent in both systems.
- `NOTION_MISSING` — GitHub contains the canonical prediction but Notion is missing it; restore from GitHub.
- `GITHUB_MISSING` — Notion contains a prediction with no durable GitHub ledger record; create the ledger record only when the Notion record is demonstrably original.
- `FIELD_MISMATCH` — both exist but key fields disagree; stop automatic overwrite and open an audit finding.
- `MISSING_ORIGINAL_PREDICTION` — the original prediction cannot be recovered from either durable source. Do not reconstruct from later outcomes.

## Immutable-history rule

Once an original prediction is recorded, never overwrite it to improve apparent accuracy. Append actual outcomes, validation, error attribution, and audit findings.

## Missing-sample rule

`MISSING_ORIGINAL_PREDICTION` is excluded from accuracy denominators. It is not a hit and not a miss. Non-trading days are excluded from normal prediction denominators unless a valid non-trading-day research record is explicitly being evaluated.

## Recovery order

When Notion loses a record:

`GitHub Prediction Ledger → Notion reconstruction → validation → audit log`

Historical chat is a secondary recovery source only. Never infer an original forecast from subsequent market outcomes.

## Failure handling

If reconciliation fails, the task must report the mismatch and preserve the existing canonical record. It must not silently create duplicates or claim successful synchronization.

## Periodic audit

Run reconciliation before monthly, quarterly, and semiannual accuracy reviews. Record the number of matched, restored, mismatched, and unrecoverable samples.
