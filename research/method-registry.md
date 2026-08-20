# Quantitative Method Registry

This registry is the durable index for quantitative forecasting and investment research methods. Agent-engineering methods belong in `gpt-workspace` unless they are directly required to evaluate the quantitative research workflow.

| Method | Domain | Status | Evidence | Validation | Notes |
|---|---|---|---|---|---|
| Market-state classification | A-share | Active | Internal framework | Ongoing OOS | Determines whether downstream signals should be trusted |
| Sector relative-strength analysis | A-share | Active | Internal framework | Ongoing OOS | Used with market-state context |
| ETF constituent overlap analysis | A-share | Testing | Internal research | Needs broader historical test | Identifies concentration and hidden factor exposure |
| Multi-signal ensemble | A-share | Testing | Quant/industry practice | OOS required | Prefer robust combinations over isolated indicators |
| Source-quality weighting | A-share | Active | Internal framework | Ongoing | Reliability is treated as part of signal weighting |

## Required evidence

A method record should make clear:

- research question and hypothesis
- data source and sample period
- Point-in-Time status
- leakage / future-function risk
- benchmark or current Champion
- backtest assumptions
- Walk-Forward and Out-of-Sample results where applicable
- robustness and sensitivity checks
- transaction costs, slippage, liquidity, and turnover
- known failure modes
- reproducibility information

## Promotion lifecycle

`Research → Prototype → Challenger → Champion`

Retirement states:

`Deprecated → Archived`

No method becomes a core dependency merely because it is fashionable, popular, or well documented. Promotion requires measurable improvement on the target workload and reasonable robustness out of sample.

## Retirement rule

Downgrade or archive methods when they are stale, unreliable, duplicated, fragile under realistic data or execution assumptions, or consistently inferior to a simpler alternative.