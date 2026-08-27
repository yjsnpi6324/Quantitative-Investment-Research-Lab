# Champion Health Score v1.0

## Purpose

Measure production model health without overreacting to short-term noise.

## Dimensions

| Dimension | Purpose |
|---|---|
| Accuracy | Direction and structure prediction quality |
| Stability | Performance across market regimes |
| Robustness | Resistance to overfitting and data changes |
| Explainability | Quality of error attribution |
| Data Quality | Reliability of input sources |
| Incremental Value | Advantage over baseline and challengers |

## Review cycle

- Monthly: operational review
- Quarterly: model lifecycle review
- Semi-annually: architecture review

## State transition

HEALTHY
→ WATCH
→ REVIEW
→ DOWNGRADE
→ DEPRECATED

## Principles

Do not replace a Champion based on one bad forecast.
Do not promote a Challenger based on insufficient evidence.
Evidence quality is more important than backtest performance alone.
