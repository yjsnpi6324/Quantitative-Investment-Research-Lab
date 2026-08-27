# Auto Governance Runbook

## 1. Daily prediction gate
1. Resolve Task -> Production ID -> Champion.
2. Build Data Snapshot ID.
3. Run Data Quality Gate: PASS/WARNING/BLOCK.
4. BLOCK prevents production prediction; emit an incident instead of fabricating output.
5. Generate prediction and lock immutable ledger with SHA-256 hash.

## 2. Due evaluation
1. Identify T+1/T+3/T+5 trading-day due predictions.
2. Fetch actual outcomes through adapters.
3. Preserve locked prediction.
4. Append Evaluation only.
5. Score HIT=1.0, PARTIAL=0.5, MISS=0.0.
6. Recompute rolling metrics and Champion Health.

## 3. Audit invariants
- Hash mismatch invalidates the record for scoring until investigated.
- Missing original predictions never enter the denominator.
- Actuals cannot overwrite prediction payloads.
- Every evaluation references Production ID, model version and Data Snapshot ID.

## 4. Adapter boundary
External adapters for Notion, market data and GitHub are intentionally separate from scoring logic so governance rules remain testable and deterministic.
