# Weekly Champion Health Check V2.3 + Monthly Model Review — 2026-09-26

## Decision

- `BASIC-PROD-20260825-A`: **WATCH**, Champion `BASIC-MSM / v2026-08-26` retained.
- `AI-PROD-20260825-A`: **WATCH**, Champion `AI-PLATE-MSM / v2026-08-26` retained.
- No `DOWNGRADE_REVIEW` and no Challenger Promotion Review.
- Existing Registry Health Score remains the unrecalculated 50/100 working score for both lines. The inputs required for a calibrated score remain incomplete.

## Scope and denominator

- Weekly focus: 2026-09-19 through 2026-09-26.
- Monthly review: 2026-09-01 through 2026-09-26 (last Saturday of the month).
- The strict V2.3 performance denominator contains only immutable, hash-verified, body-aligned, correctly scheduled, due predictions with verified Actual and no duplicate Evaluation.
- FINAL predictions are not modified. Missing predictions are not fabricated.
- Three legacy FORMAL Evaluation rows remain append-only audit records, but because their source predictions had no contemporaneous original hash, they are excluded from the V2.3 strict denominator.

## Hash infrastructure

| Classification | BASIC | AI | Total |
|---|---:|---:|---:|
| NATIVE_HASH_VERIFIED | 1 | 1 | 2 |
| MIGRATION_HASH_VERIFIED | 0 | 0 | 0 |
| HASH_MISMATCH_BLOCKED | 0 | 0 | 0 |
| BLOCKED_INVALID_HASH (formal historical predictions) | 8 | 10 | 18 |
| INFRASTRUCTURE_INCOMPLETE (missing source FINAL/Handoff runs) | 2 | 0 | 2 |
| NOT_APPLICABLE_REVIEW | 0 | 1 | 1 |

### Native verification

- `PRED-BASIC-20260923-001`: governance independently extracted the original Handoff Canonical JSON, applied Unicode NFC, ASCII-key-ordered single-line serialization, and recomputed SHA-256. Computed hash equals published hash:
  `fc0d3d72ca945aca3578331d35c98dc72f021403052a735e07b7e894a939384e`.
  `BODY_ALIGNMENT=VERIFIED`.
- `PRED-AI-20260924-01`: identical independent procedure. Computed hash equals published hash:
  `23cf45c7ec696833362a52046c7716e4271bc03a88f34eea3bedaff8c12b8d81`.
  `BODY_ALIGNMENT=VERIFIED`.
- Official SSE calendar confirms the 2026-09-25 through 2026-09-27 closure and reopening on 2026-09-28. Target dates are consistent:
  - BASIC: T+1 2026-09-24, T+3 2026-09-29, T+5 2026-10-08.
  - AI: T+1 2026-09-28, T+3 2026-09-30, T+5 2026-10-09.

## Evaluation status

| Production line | T+1 | T+3 | T+5 | Strict total | HIT/PARTIAL/MISS | Mean score |
|---|---:|---:|---:|---:|---|---:|
| BASIC | 1 | 0 | 0 | 1 | 0/1/0 | 0.50 |
| AI | 0 | 0 | 0 | 0 | 0/0/0 | N/A |

The single V2.3-valid closure is `EVAL-BASIC-20260923-T1`:

- Result: `PARTIAL`
- Score: `0.5`
- Verified Actual for 2026-09-24: Shanghai Composite -1.22%, Shenzhen Component -2.34%, ChiNext -2.68%, Shanghai/Shenzhen turnover about CNY 1.653tn, and 4,306 declining stocks.
- Error pattern: correct weak-direction and turnover-floor call, but materially underestimated loss magnitude, breadth deterioration, and pressure in large technology names.

Native backlog as of 2026-09-26:

- `FORMAL_CLOSED=1`
- `ALREADY_EVALUATED=1`
- `DUE_UNCLOSED=0`
- `ACTUAL_UNAVAILABLE=0`
- `HASH_MISMATCH_BLOCKED=0`
- BASIC T+3/T+5 and AI T+1/T+3/T+5 are not due.

Historical blocked backlog:

- 18 formal historical predictions remain `BLOCKED_INVALID_HASH`.
- At least 52 associated horizons are due but blocked: BASIC 23, AI 29.
- Two 2026-09-18 T+5 horizons mature on 2026-09-28 and remain blocked.

## Governance and runtime health

### Notion

- Prediction Registry contains the two Native V3.5 rows with structured target dates.
- Champion Registry and Model Registry were updated to the strict V2.3 sample counts:
  - BASIC validated samples: 1.
  - AI validated samples: 0.
- Source Registry remains 5 ACTIVE production sources plus Firecrawl WATCH.

### GitHub

- BASIC PR #20 and AI PR #21 are merged to `main`; both full FINAL artifacts and canonical manifests are readable on main.
- AI has an append-only `GITHUB_MAIN_VERIFICATION` receipt.
- BASIC's older governance JSON still says `github=PR_PENDING` even though PR #20 is merged. This is disclosed as append-only status drift; the locked FINAL is unchanged.
- AI non-trading review PR #23 remains OPEN and mergeable; main sync is not claimed.

### Supabase

Read-only runtime facts at this check:

- project status: `ACTIVE_HEALTHY`
- `task_runs=39`
- `task_results=35`
- `integration_events=50`
- `integration_nodes=11`
- since 2026-09-19: 9 task runs succeeded, 0 task runs failed
- three recent integration failures explicitly record missing BASIC source FINAL/Handoff:
  - BASIC 2026-09-24 FORMAL Handoff missing
  - BASIC 2026-09-25 non-trading Handoff missing
  - BASIC 2026-09-24 missing recheck
- policy remains `DO_NOT_SYNTHESIZE_OR_BACKFILL_PREDICTION`.

### Vercel

No runtime-error clusters were found for `quantitative-investment-research-lab` during the previous seven days. Operational health is not treated as prediction accuracy.

## Source and version drift

- Champion model versions remain `v2026-08-26`.
- Production prompt is now `PROD-PROMPT-V3.5` for the two new Native predictions.
- No unregistered production-source substitution was found.
- Bigdata.com supplied corroborating 2026-09-24 Actual evidence.
- Firecrawl, Scite, Context7, Flourish, and optional PEI/Data supplied no evidence that changes a sample, score, or Champion decision in this run.

## Challenger and baseline

- Five registered Challengers remain at zero valid same-target, same-horizon OOS samples.
- Two baseline experiments still lack a bound dataset and reproducible comparison.
- No valid evidence of incremental value versus Champion and baseline exists.

## Monthly Model Review — September 2026

- BASIC: one strict-valid monthly sample, T+1 PARTIAL=0.5; no T+3/T+5 closure. Confidence is low.
- AI: zero strict-valid monthly samples. Accuracy and mean score are undefined.
- Health Score trend is not inferred from the unchanged 50/100 working score.
- The principal monthly improvement is infrastructure: first verified Native hashes, body alignment, and correct exchange-calendar targets.
- The principal monthly risks are the historical hash debt and missing BASIC source FINAL/Handoff records.

## Next hard gate

On 2026-09-28, evaluate AI T+1 only if Actual is independently verifiable, the hash/body/identity still match, and no duplicate Evaluation exists. The 2026-09-18 T+5 historical predictions remain blocked and must not enter the denominator.

## Evidence

- [BASIC V3.5 ledger](../../production-ledger/2026/09/23/RPT-BASIC-20260923-001.md)
- [BASIC canonical manifest](../../production-ledger/2026/09/23/RPT-BASIC-20260923-001.json)
- [AI V3.5 ledger](../../production-ledger/2026/09/24/RPT-AI-20260924-001.md)
- [AI canonical manifest](../../production-ledger/2026/09/24/RPT-AI-20260924-001.json)
- [AI main verification](../../production-ledger/2026/09/24/RPT-AI-20260924-001.main-verification.json)
- [SSE 2026 holiday schedule](https://www.sse.com.cn/disclosure/announcement/general/c/c_20251222_10802507.shtml)
- [Notion V2.3 report](https://app.notion.com/p/3e714471bc1b81388c06f8669b502204?pvs=204)
