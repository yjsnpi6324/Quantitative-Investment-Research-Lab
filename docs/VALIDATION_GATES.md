# Quantitative Validation Gates

A model or factor should pass the following gates before it is considered for Champion promotion.

## Gate 1 — Research integrity

- [ ] Research objective is explicit
- [ ] Data sources and sample period are documented
- [ ] Point-in-Time availability is understood
- [ ] Look-ahead / future-function risk is checked
- [ ] Survivorship bias is assessed
- [ ] Leakage paths are checked

## Gate 2 — Realism

- [ ] Transaction costs are modelled or explicitly justified
- [ ] Slippage assumptions are documented
- [ ] Liquidity constraints are considered
- [ ] Turnover is measured
- [ ] Position / execution constraints are documented

## Gate 3 — Statistical validation

- [ ] Baseline / benchmark is defined
- [ ] In-sample and out-of-sample periods are separated
- [ ] Walk-Forward or equivalent temporal validation is used where applicable
- [ ] Multiple-testing / selection bias is considered
- [ ] Parameter sensitivity is tested

## Gate 4 — Robustness

- [ ] Results survive reasonable parameter perturbations
- [ ] Results are not dependent on one narrow market regime
- [ ] Data-quality deterioration does not fully break the signal
- [ ] Simpler alternatives have been compared

## Gate 5 — Promotion

A Challenger can be proposed for Champion only when the research record documents measurable improvement, acceptable risk, reproducibility, and a clear reason to replace the current Champion.

A strong single backtest is not sufficient evidence.
