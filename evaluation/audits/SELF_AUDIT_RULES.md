# Self-Audit Rules v1

Run after each completed evaluation batch and during non-trading-day maintenance.

## Severity

- P0: integrity failure — locked prediction may have been altered, duplicated IDs, impossible timestamps, or invalid horizon. Stop downstream promotion.
- P1: material degradation — source failure, systematic calibration drift, regime failure, or large unexplained performance deterioration. Create diagnostic work item.
- P2: operational issue — missing delivery, stale metadata, incomplete evaluation, or recoverable data-quality issue.
- P3: observation — unusual but not yet actionable.

## Audit sequence

1. Validate prediction ledger schema and uniqueness.
2. Validate information cutoff precedes prediction creation and outcome timing.
3. Validate T+1/T+3/T+5 are trading-day horizons.
4. Validate confidence and model/rule/data versions.
5. Reconcile evaluation records against locked predictions.
6. Calculate rolling and cumulative performance by task and horizon.
7. Check calibration and high-confidence performance.
8. Check market-regime-conditioned failures.
9. Check source/data-quality anomalies.
10. Check delivery-chain status: canonical report, Notion, PDF and verification.
11. Emit an audit log with severity and evidence.
12. If material, open a diagnostic/Challenger path; never silently change the historical record.

## Anti-self-deception rules

- Do not delete bad predictions.
- Do not change a forecast after its information cutoff.
- Do not promote a method from in-sample or a single backtest.
- Do not infer improvement from a tiny sample.
- Always report sample size with metrics.
- Preserve conflicting source evidence.
- Treat missing data as missing, not as a neutral value.
