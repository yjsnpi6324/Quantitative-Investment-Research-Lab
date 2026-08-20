# Market-State Classification — Experiment 001

## Objective

Build and validate a market-regime classifier for A-share research so downstream forecasting methods can condition their weights on the current regime.

## Research question

Does explicit market-state classification improve forecast stability and out-of-sample performance versus a regime-agnostic baseline?

## Candidate states

Initial hypothesis:

- Trend / risk-on
- Trend / risk-off
- Range / neutral
- Risk release
- Recovery / repair

These labels are hypotheses, not final truth. Definitions must be data-driven and frozen before evaluation.

## Baseline

A regime-agnostic forecasting baseline with fixed model weights and no state-conditioned routing.

## Candidate signals

- Broad-index trend and breadth
- Volatility / drawdown
- Volume and turnover structure
- Relative strength dispersion
- Sector leadership concentration
- Momentum / reversal characteristics
- Market liquidity proxies

## Validation design

1. Use point-in-time data only.
2. Avoid survivorship bias and future constituent information.
3. Define labels using information available at prediction time.
4. Use rolling / walk-forward evaluation.
5. Keep a strict out-of-sample holdout.
6. Test across multiple market phases.
7. Include transaction-cost sensitivity when downstream use implies trading.
8. Compare against the simplest reasonable baseline.

## Metrics

Primary:

- Directional accuracy
- Balanced accuracy by regime
- Forecast calibration

Secondary:

- Precision / recall by regime
- Stability across time windows
- Downside error concentration
- Incremental performance versus baseline

## Experiment status

**Planned**

No performance claim is made until the dataset, label definition, baseline, and evaluation protocol are frozen.

## Required artifacts

- Dataset specification
- Regime label specification
- Baseline result
- Candidate-model result
- Out-of-sample evaluation
- Failure-case analysis
- Evaluation record
- Method Registry update

## Linked system flow

`Project → Task → Experiment 001 → Evaluation → Notion → Method Registry → Next Task`

## Decision rule

Promote only if the classifier demonstrates robust out-of-sample incremental value across materially different market phases. Otherwise keep testing or retire the candidate.