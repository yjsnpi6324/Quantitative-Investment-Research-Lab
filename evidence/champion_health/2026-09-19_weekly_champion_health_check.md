# Weekly Champion Health Check — 2026-09-19

## Scope
- Production lines: `BASIC-PROD-20260825-A` and `AI-PROD-20260825-A`
- Evidence cutoff: 2026-09-18 close
- FINAL predictions remain immutable; missing predictions are not fabricated.
- Performance denominators contain only FORMAL Evaluation Registry rows with verified Actual.

## Infrastructure pre-check
The repaired schema now exposes `Prediction Hash` plus structured T+1/T+3/T+5 Target Date fields, and main contains the repaired exchange-calendar / append-only Evaluation code from PR #16. However, no post-2026-09-19 FORMAL production prediction exists yet, so the new write path cannot be end-to-end certified in this weekly check.

All canonical FORMAL Prediction Registry rows currently present for these two production IDs through 2026-09-18 have no contemporaneous Prediction Hash and no structured target dates. They remain historical governance blockers (`BLOCKED_INVALID_HASH`) and are excluded from automatic scoring unless separately proven by explicit BACKFILL_PROVENANCE / MIGRATION_HASH evidence. No old prediction is re-hashed as if it had been locked at publication time.

## BASIC-PROD-20260825-A
- Champion: `BASIC-MSM / v2026-08-26`
- FORMAL evaluated samples: 2
- T+1: n=2, mean=0.50; T+3: n=0; T+5: n=0
- HIT / PARTIAL / MISS: 0 / 2 / 0
- Health Score: 50/100 working score carried forward; calibrated Stability/Robustness/Incremental-Value inputs are not populated, so no fake precision is introduced.
- State: WATCH; Champion retained.
- Previously identified matured-but-unclosed horizons are governance backlog, not model failures; after the immutable-hash repair they are treated as blocked historical candidates rather than silently scored.

## AI-PROD-20260825-A
- Champion: `AI-PLATE-MSM / v2026-08-26`
- FORMAL evaluated samples: 1
- T+1: n=0; T+3: n=1, mean=0.50; T+5: n=0
- HIT / PARTIAL / MISS: 0 / 1 / 0
- Health Score: 50/100 working score carried forward without fabricated precision.
- State: WATCH; Champion retained.
- Previously identified matured-but-unclosed horizons remain governance backlog and are excluded from performance denominators.

## Evidence and runtime integrity
- Notion Source Registry remains the canonical human-readable source registry; Firecrawl is WATCH / observational and not a canonical publisher.
- Supabase project is ACTIVE_HEALTHY. At check time: `task_runs=30`, `task_results=30`, `integration_events=39`, `integration_nodes=11`; latest task run/result timestamp is 2026-09-18 22:24:38Z and latest integration event/node update is 2026-09-19 00:43:39Z.
- Vercel project `quantitative-investment-research-lab` reports no runtime-error clusters in the preceding 7 days. Runtime health is not treated as prediction correctness.
- Main contains `docs/PLUGIN_ORCHESTRATION.md`, `docs/ADAPTER_INTEGRATION.md`, and `docs/AUTOMATED_SCORING_PIPELINE.md`, establishing current task/plugin boundaries and fail-closed Evaluation behavior.

## Challenger / baseline
No verified same-target, same-horizon, same-window Walk-Forward/OOS comparison with leakage checks and reproducible baseline binding is available. No Challenger Promotion Review is started.

## Governance decision
- BASIC: WATCH; no REVIEW / DOWNGRADE_REVIEW.
- AI: WATCH; no REVIEW / DOWNGRADE_REVIEW.
- Primary next gate: observe the first new FORMAL prediction generated after the 2026-09-19 repair and verify that Prediction Hash + three official-trading-day Target Dates persist successfully and later produce idempotent Evaluation closure.
- Historical missing-hash rows stay quarantined unless provenance migration is independently established.

## Monthly review
2026-09-19 is not the final Saturday of September 2026; Monthly Model Review is not triggered.
