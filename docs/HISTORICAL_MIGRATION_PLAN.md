# Historical Data Migration Plan

## Rules

- Only migrate records with original prediction evidence.
- Never reconstruct missing forecasts from market outcomes.
- Keep original prediction immutable.
- Append actual outcome and error attribution later.

## Priority

1. Existing Champion evaluations
2. T+1/T+3/T+5 completed predictions
3. Challenger experiments
4. Deprecated models

## Required fields

- Prediction ID
- Evaluation ID
- Model ID
- Production ID
- Horizon
- Prediction
- Actual
- Result
- Error Cause
- Score
