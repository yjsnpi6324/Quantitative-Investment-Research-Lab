# Prediction Fact Contract

## Canonical identity

Every original forecast has a stable identity:

`date × task × record_type × model_version`

## Required task values

- `基本盘预测`
- `AI板块预测`

## Record types

- `交易日预测`
- `本周总结`
- `下周前瞻`
- `非交易日复盘`

Only `交易日预测` enters normal T+1/T+3/T+5 prediction accuracy denominators. Weekend review/outlook records are evaluated under their own review rules unless explicitly promoted to a formal forecast record.

## Immutability

Original forecast fields are immutable after publication. Actual outcomes, validation status, error attribution, and audit findings are append-only.

## Missing data

`MISSING_ORIGINAL_PREDICTION` means the original forecast cannot be demonstrated from a durable source. It is excluded from accuracy denominators and cannot be reconstructed from subsequent outcomes.

## Synchronization

GitHub Ledger is the durable canonical fact layer. Notion is a synchronized human-facing layer. Any disagreement creates an audit finding; neither side may silently overwrite the other.
