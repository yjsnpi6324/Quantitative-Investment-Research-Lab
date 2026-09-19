# Weekly Champion Health Check — 2026-09-19

## Scope
- Production lines: `BASIC-PROD-20260825-A` and `AI-PROD-20260825-A`
- Evidence cutoff: 2026-09-18 close
- Inputs: Notion Champion / Evaluation / Prediction / Source / Model / Experiment registries plus GitHub Production Ledger and Evidence Layer
- FINAL predictions remain immutable. Missing predictions are not fabricated. Matured horizons without FORMAL Evaluation rows are tracked as backlog and excluded from score denominators.

## BASIC-PROD-20260825-A
- Champion: `BASIC-MSM / v2026-08-26`
- FORMAL evaluations: 2
- T+1: n=2, mean=0.50
- T+3: n=0
- T+5: n=0
- HIT / PARTIAL / MISS: 0 / 2 / 0
- Working Health Score: 50/100, carried forward because calibrated stability/robustness inputs remain unavailable
- State: WATCH; Champion retained
- Matured but unclosed canonical horizons since 2026-08-27: T+1=7, T+3=5, T+5=4
- Calendar defect: `PRED-BASIC-20260916-001` labels T+3=2026-09-18 and T+5=2026-09-22; strict future-trading-day dates are 2026-09-21 and 2026-09-23. Do not rewrite the locked prediction; quarantine the bad scheduling metadata from Evaluation automation.

## AI-PROD-20260825-A
- Champion: `AI-PLATE-MSM / v2026-08-26`
- FORMAL evaluations: 1
- T+1: n=0
- T+3: n=1, mean=0.50
- T+5: n=0
- HIT / PARTIAL / MISS: 0 / 1 / 0
- Working Health Score: 50/100, carried forward without fabricated precision
- State: WATCH; Champion retained
- Matured but unclosed canonical horizons since 2026-08-27: T+1=9, T+3=7, T+5=5
- Calendar defect: `PRED-AI-20260918-01` labels T+5=2026-09-25. SSE/SZSE 2026 holiday schedules close the A-share market on 2026-09-25 and resume 2026-09-28, so strict T+5 is 2026-09-28. Preserve the locked prediction and quarantine the bad scheduling metadata.

## Data quality / evidence integrity
- Source Registry has five ACTIVE production sources: 3 A-grade and 2 B-grade.
- Firecrawl is a new WATCH / observational discovery source, not a canonical production publisher.
- Production Ledger files are present through 2026-09-18.
- Inspected backfill ledger JSON for BASIC 2026-09-16 and AI 2026-09-18 has `content_hash=null`, limiting byte-level provenance verification.
- Main-branch Champion Health evidence was stale at 2026-08-29. This branch is based on `health-check-2026-09-12` so the pending 2026-09-12 evidence and this 2026-09-19 evidence can enter main together.
- `src/evaluation/health_score.py` remains a skeleton with weights for accuracy/stability/robustness/data_quality/explainability but without populated calibrated inputs. Documentation lists Incremental Value as a dimension while the code does not explicitly weight it.

## Challenger / baseline
- Five registered Challengers remain TESTING / UNVALIDATED with zero validated T+1/T+3/T+5 samples.
- `EXP-BASELINE-001` and `EXP-BASELINE-002` remain EXPERIMENT with dataset binding, reproducibility and result verification pending.
- No verified same-window incremental-value ranking is possible.
- No Challenger Promotion Review is started.

## Governance decision
- BASIC: WATCH, no REVIEW or DOWNGRADE_REVIEW.
- AI: WATCH, no REVIEW or DOWNGRADE_REVIEW.
- Primary remediation: close Evaluation backlog; add exchange-calendar validation for horizon scheduling; complete content hashes/provenance; merge Evidence Layer history.
- No Champion state change is justified by current model-performance evidence.

## Sync
- Notion Champion Registry updated to health-check date 2026-09-19.
- Notion governance page created: `Champion Health Check｜2026-09-19`.
- This Evidence Layer record is proposed via branch/PR; merge status is tracked separately.

## Monthly review
2026-09-19 is not the final Saturday of September 2026. Monthly Model Review is not triggered.
