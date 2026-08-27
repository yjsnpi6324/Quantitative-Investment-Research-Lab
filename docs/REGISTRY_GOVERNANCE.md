# Registry Governance Specification

## Purpose

This document defines the lifecycle governance layer for production quantitative research models.

## Registry chain

Source Registry
→ Model Registry
→ Champion Registry
→ Evaluation Registry
→ Self Audit / Evolution

## Source Registry

Tracks production data provenance:

- Source ID
- Source type
- Reliability grade
- Quality rules
- Production status

Rules:

- Prefer primary sources.
- Cross-check critical information.
- Do not inject uncertain data into production features.
- Deprecated sources remain archived for traceability.

## Model Registry

Tracks all model assets:

Roles:

- CHAMPION
- CHALLENGER
- EXPERIMENT
- DEPRECATED

Every model requires:

- Model ID
- Version
- Method description
- Validation evidence
- Source dependency

## Champion Registry

Production models are referenced by Production ID.

Promotion requires:

- Reproducible experiment
- Matching task definition
- Walk-Forward or OOS evidence
- Leakage checks
- Incremental value versus current Champion
- Robustness validation

## Evaluation Registry

Forecast evaluation is immutable:

- Original prediction is locked.
- Actual outcome is appended later.
- Error causes are recorded.
- Scores are accumulated over time.

Result states:

- HIT
- PARTIAL
- MISS

## Lifecycle

CHALLENGER
→ QUALIFIED
→ PROMOTION REVIEW
→ CHAMPION

CHAMPION
→ WATCH
→ DOWNGRADE REVIEW
→ DEPRECATED

## Design principle

Notion manages operational state and decisions.
GitHub stores durable methods, experiments, schemas and evidence.
