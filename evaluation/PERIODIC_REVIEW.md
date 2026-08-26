# Periodic Prediction Accuracy Review

The evaluation system must review prediction performance at four horizons: **monthly, quarterly, semiannual, and rolling windows**.

## Review cadence

- **Monthly:** close the calendar month after all eligible T+1/T+3/T+5 outcomes are available. Compare Basic Market vs AI Sector separately and together.
- **Quarterly:** aggregate the three completed calendar months; identify regime-specific strengths/failures, calibration drift, source degradation, and model/rule changes.
- **Semiannual:** aggregate six completed months; perform a deeper stability and robustness review and assess whether Champion models still deserve production status.
- **Rolling:** maintain 20-trading-day, 60-trading-day, and 120-trading-day rolling metrics so deterioration is detected before a formal period closes.

## Required metrics

For each period and each task, report separately for T+1/T+3/T+5 trading days:

1. Direction hit rate.
2. Conditional hit rate by market regime.
3. Hit rate by confidence bucket.
4. Brier score and calibration error when probabilistic forecasts are available.
5. MAE/RMSE for numerical forecasts where applicable.
6. Sample size, eligible predictions, missing outcomes, and exclusion reasons.
7. Error-type distribution and top recurring failure modes.
8. Model/rule/data version performance.
9. Comparison with the prior period and rolling baseline.
10. Statistical uncertainty / confidence interval where sample size permits.

## Governance rules

- Never treat a small sample as evidence of model improvement.
- A period review diagnoses; it does not directly rewrite the model.
- Any Champion promotion, downgrade, or retirement must follow Challenger → Walk-Forward → OOS → robustness validation.
- Monthly reviews are operational; quarterly reviews are structural; semiannual reviews are strategic.
- If monthly deterioration is detected, open a self-audit event immediately rather than waiting for the quarterly review.

## Deliverables

Each completed review should produce:

- a versioned evaluation snapshot in GitHub;
- a Notion review record / summary;
- a list of open audit findings and recommended actions;
- explicit model/rule/data versions used;
- a decision: **maintain / investigate / downgrade / retire / promote challenger**.

The review system must remain reproducible from the Prediction Ledger and evaluation records.