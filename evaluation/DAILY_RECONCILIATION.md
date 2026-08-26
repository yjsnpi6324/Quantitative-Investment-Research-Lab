# Daily Prediction Reconciliation

Before closing each prediction task run, perform this checklist:

- [ ] Canonical Report generated.
- [ ] Basic Market / AI Sector task identity is explicit.
- [ ] Date and trading-day status are explicit.
- [ ] T+1/T+3/T+5 trading-day forecasts are present or explicitly unavailable.
- [ ] Original prediction is written to the GitHub Prediction Ledger.
- [ ] Notion record is created with the same date/task/type/model version.
- [ ] Notion ↔ GitHub reconciliation status is `MATCHED`.
- [ ] If a mismatch exists, create an audit finding; do not overwrite silently.
- [ ] When an outcome matures, append actual result and validation rather than editing the original forecast.
- [ ] Missing original predictions are labeled `MISSING_ORIGINAL_PREDICTION` and excluded from accuracy denominators.
- [ ] PDF is a mirror of the Canonical Report; PDF failure does not erase or invalidate the durable prediction record.

## Close condition

A task run is considered durably closed only when the original prediction exists in GitHub and the Notion record has either been reconciled as `MATCHED` or has a documented recovery/audit status.
