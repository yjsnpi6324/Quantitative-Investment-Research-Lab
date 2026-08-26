# Prediction Evaluation System

## Purpose

The evaluation layer separates prediction facts from evaluation results and model governance.

## Canonical lifecycle

`Prediction → Outcome → Evaluation → Self-Audit → Diagnosis → Challenger → OOS → Champion / Downgrade / Deprecated`

## Storage responsibilities

- Notion: operational control plane and human-readable prediction history.
- GitHub: versioned schemas, reproducible evaluation code, durable datasets/snapshots, audit logs and reports.
- Parquet/DuckDB-compatible data: statistical computation layer; never overwrite the original prediction event.

## Required dimensions

Evaluate separately for T+1/T+3/T+5 trading days and by direction hit rate, confidence calibration/Brier score where applicable, market-regime-conditioned performance, task-specific performance, model/rule/data version, error attribution, rolling stability, sample size and missingness.

## Immutable prediction principle

A prediction is created once and locked. Verification is appended later. Evaluation must never rewrite the original forecast.

## Self-audit

Self-audit detects anomalies and degradation; it does not silently rewrite model parameters. Material model changes must pass Challenger → Walk-Forward → OOS → robustness validation before promotion.

## Minimum audit checks

1. Missing or duplicated prediction IDs.
2. Forecast timestamp after the information cutoff.
3. Outcome evaluated before the required trading horizon completed.
4. T+1/T+3/T+5 horizon mismatch.
5. Impossible or missing confidence values.
6. Model/rule/data version missing.
7. Source/data-quality failure.
8. Sudden rolling performance deterioration.
9. Calibration drift in high-confidence predictions.
10. Regime-specific failure clusters.
11. Basic Market vs AI Sector performance divergence.
12. Evaluation results inconsistent with locked prediction records.

## Governance

Audit findings create diagnostic records. They may trigger a Challenger experiment, source downgrade, data-quality intervention or task-health investigation. They do not directly alter historical predictions.
