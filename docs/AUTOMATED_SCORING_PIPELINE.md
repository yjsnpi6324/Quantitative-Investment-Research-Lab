# Automated Scoring Pipeline Design v1.0

## Purpose

Convert Evaluation Registry records into repeatable model health signals.

## Flow

Evaluation Registry
→ Horizon Score
→ Rolling Performance
→ Champion Health Score
→ Lifecycle Decision

## Evaluation scoring

HIT: 1.0
PARTIAL: 0.5
MISS: 0.0

## Rolling metrics

Track separately:

- T+1 accuracy
- T+3 accuracy
- T+5 accuracy
- Direction accuracy
- Structure accuracy
- Risk detection accuracy

## Champion Health Score

Suggested weighted dimensions:

- Prediction quality
- Stability across regimes
- Robustness
- Data quality
- Explainability
- Incremental value versus Challenger

## Decision logic

Healthy:
Continue production.

Watch:
Performance degradation detected. Continue observation.

Review:
Root cause analysis required.

Downgrade:
Qualified Challenger replaces current Champion.

## Safety rules

- Never replace a Champion from a single miss.
- Never promote from backtest-only evidence.
- Preserve immutable prediction history.
- Separate model improvement from data leakage correction.

## Future implementation

This specification can later become a scheduled evaluation service using Evaluation Registry as the source of truth.
