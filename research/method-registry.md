# Method Registry

This registry is the durable index for forecasting and Agent methods. It is intentionally evidence-oriented.

| Method | Domain | Status | Evidence | Validation | Notes |
|---|---|---|---|---|---|
| Market-state classification | A-share | Active | Internal framework | Ongoing OOS | Determines whether downstream signals should be trusted |
| Sector relative-strength analysis | A-share | Active | Internal framework | Ongoing OOS | Used with market-state context |
| ETF constituent overlap analysis | A-share | Testing | Internal research | Needs broader historical test | Useful for identifying concentration and hidden factor exposure |
| Multi-signal ensemble | A-share | Testing | Quant/industry practice | OOS required | Prefer robust combinations over isolated indicators |
| Source-quality weighting | A-share | Active | Internal framework | Ongoing | Reliability is part of signal weighting |
| Tool-use evaluation | Agent | Active | Agent research | Task-specific | Evaluate selection, success, recovery, latency and cost |
| Memory retrieval evaluation | Agent | Testing | Agent research | Task-specific | Precision, recall, freshness and provenance matter |

## Lifecycle

`Active → Testing → Deprecated → Archived`

A method may move between states as new evidence arrives. Evaluation records should provide the evidence for material status changes.

## Promotion rule

No method becomes a core dependency merely because it is fashionable or well documented. Promotion requires measurable improvement on the target workload and reasonable robustness out of sample.

## Retirement rule

Downgrade or archive methods when they are stale, unreliable, duplicated, data-dependent in a fragile way, or consistently inferior to a simpler alternative.

## Evaluation link

Use `templates/evaluation.md` for formal evaluation records and `evaluation/README.md` for the measurement rules.