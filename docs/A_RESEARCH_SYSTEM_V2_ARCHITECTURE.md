# A-Research System V2 Architecture

## Status

Design and shadow-run phase. V1 remains the operational baseline until V2 passes evaluation and integrity checks.

## Goals

1. Separate prediction facts from human-readable reports.
2. Make GitHub Prediction Ledger the durable canonical fact layer.
3. Keep Notion as the human-facing project, database, dashboard, and review layer.
4. Keep Basic Market and AI Sector research contexts independent while sharing common evaluation infrastructure.
5. Make reconciliation and recovery mandatory, not best-effort.
6. Make Evaluation and Self-Audit first-class parts of every task run.
7. Preserve reproducibility through versioned schemas, methods, and model/rule versions.

## System layers

### L0 — Execution
GPT/task scheduler executes the research workflow.

### L1 — Research agents
- `A-CORE`: A-share basic-market research.
- `A-AI`: A-share AI-sector research.

The two agents have independent research context and outputs. They share common contracts for data quality, prediction schema, validation, evaluation, audit, and persistence.

### L2 — Canonical prediction facts
GitHub Prediction Ledger is the durable source of truth for original predictions and immutable prediction identity.

Identity key:

`date × task × record_type × model_version`

### L3 — Human-facing workspace
Notion contains dashboards, daily reports, project state, course material, review pages, and synchronized structured records. Notion is reconstructable from the GitHub ledger.

### L4 — Validation and Evaluation
Actual outcomes are appended after the original forecast. T+1/T+3/T+5 are trading-day horizons. Evaluation must distinguish missing predictions from wrong predictions.

### L5 — Audit and recovery
Reconciliation checks GitHub ↔ Notion. Integrity failures generate audit findings and recovery actions. No silent overwrite.

## Prediction lifecycle

`Research → Canonical Report → Prediction Ledger → Notion → Reconciliation → PDF mirror → Outcome → Validation → Error Attribution → Evaluation`

The original prediction is immutable. Later facts are append-only.

## Weekend lifecycle

Saturday:
`Weekly trading-day review → validation review → error attribution → next-week watchlist`

Sunday:
`Next-week coarse outlook → key scenarios → risks/catalysts → rough T+1/T+3/T+5 trading-day directions`

Weekend records are explicitly typed as weekly review or weekend outlook and are not silently counted as normal trading-day predictions.

## V1 → V2 migration policy

- No destructive migration during design.
- V1 remains the comparison baseline.
- V2 initially runs in shadow mode.
- V2 becomes Champion only after integrity, reproducibility, and predictive/evaluation quality are demonstrated.
- Historical records are never rewritten merely to fit the new schema.
- Unrecoverable historical predictions remain `MISSING_ORIGINAL_PREDICTION`.

## Non-goals

V2 does not introduce a new external database yet. PostgreSQL/warehouse adoption remains a later stage when data volume or query complexity justifies it.
