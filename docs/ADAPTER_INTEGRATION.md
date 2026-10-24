# Adapter Integration

The governance core is provider-neutral.

## Runtime chain

Task -> Production ID -> RegistryAdapter -> MarketDataAdapter -> Data Quality Gate -> locked Prediction -> LedgerAdapter.

Every new canonical Prediction Registry write MUST be locked before persistence and carry a verifiable prediction hash.

## Horizon scheduling

T+1/T+3/T+5 are strict future A-share trading-day horizons, not calendar-day offsets and not generic weekdays.

- Runtime defaults to AShareTradingCalendar unless an exchange-verified calendar is injected.
- Unsupported calendar years fail closed instead of silently assuming weekdays.
- Holiday closures are sourced from official SSE/SZSE schedules.
- One canonical Prediction Registry row may contain all T+1/T+3/T+5 forecasts.
- The production writer persists structured target dates alongside the immutable prediction hash.
- The evaluation runner preserves persisted target dates. Conflicting or malformed persisted dates block the record; only absent dates are derived from Trading Date and the exchange calendar. Never rewrite historical dates to resolve a conflict.

## Evaluation closure

At each governance run:

RegistryAdapter -> evaluation candidates -> immutable hash verification -> horizon expansion -> exchange-calendar due check -> duplicate check -> MarketDataAdapter verified actual -> Evaluation -> append-only Registry update.

Rules:

1. (prediction_id, horizon) is idempotent and must never be evaluated twice.
2. Missing or unverified actuals remain pending; they are not converted into a fabricated MISS.
3. Locked prediction text is never rewritten when a scheduling defect is discovered.
4. Historical rows without a valid immutable hash are surfaced as blockers by the backlog scanner and require governance repair before automatic scoring.
5. Health scoring consumes only FORMAL closed evaluations.
6. scan_evaluation_backlog exposes every matured, unclosed horizon or its explicit blocker.

## Current implementation

The repository contains concrete adapter boundaries for Notion, GitHub evidence ledger and market data. Provider credentials and account-bound API clients are injected at runtime rather than stored in the repository.

## Production rule

No adapter may overwrite a locked prediction. Registry writes for evaluations are append-only.

## Skip diagnostics and reporting

`run_due_evaluations` returns evaluations alongside diagnostics. Only successfully
appended evaluations have `evaluation_id`, `result`, and `score`; diagnostics are
never appended as completed evaluations. Persist the returned diagnostics in the
caller’s existing append-only run receipt, not in the Evaluation Registry.

- `SOURCE_FINAL_NOT_FOUND`: a registry candidate with this existing `status`
  represents an observed missing source, not a prediction. Carry its report and
  production identity through unchanged. The runner cannot discover absent rows;
  the caller must supply known source-gap observations.
- `NOT_DUE`: target date is in the future; no actual lookup is performed.
- `ACTUAL_UNAVAILABLE`: absent, MISSING, or UNVERIFIED actual.
- `ACTUAL_UNSCORED`: actual exists but lacks an exact HIT/PARTIAL/MISS result.
- `INVALID_HASH`, `INVALID_PREDICTION`, `NO_HORIZON_FORECASTS`, and
  `UNSUPPORTED_HASH_SCHEMA`: leave the source untouched for investigation.
- Lookup/evaluation exceptions identify their failed stage and exception type;
  other candidates continue. `APPEND_OUTCOME_UNKNOWN` must be reconciled by
  identity before retry; it is neither a confirmed failure nor a completion.

`summarize_evaluations` groups by production ID and separately counts evaluated
windows, results, window diagnostics, and record diagnostics. Do not use the
length of runner output as a completion count. `rolling_metrics` and self-audit
counts exclude diagnostics and incomplete/invalid score records. Scored records
must have an evaluation ID, a legal Result and its matching score, plus an explicit
closed state (`FORMAL_CLOSED` in persisted ledger records or `verified` in the
evaluation schema), or the legacy Python evaluator's absent/empty status. The
schema workflow state `partial` is not a closed Result `PARTIAL`; pending, invalid,
unknown and skip states remain excluded even if stale result/score fields exist. The legacy
`score_horizon` ignores rows without a legal Result instead of treating them as
zero-score misses. Missing production identity stays in an unknown group; do not
infer AI/BASIC identity from the delivery chat name.

Registry adapters must provide durable identity lookup and atomic uniqueness for
(prediction_id, horizon). Missing lookup support fails closed. In-run duplicate
suppression also prevents immediate retry after uncertain append results; remote
atomicity remains the injected client's responsibility.

## Verified implementation boundary (2026-10-24)

The repository Python path is `persist_prediction` -> `lock_prediction` (legacy
REQUIRED_FIELDS payload), and injected registry candidates -> `run_due_evaluations`
-> `evaluate_due` -> injected `append_evaluation`. No repository implementation
connects production schema-v1 canonical artifacts to that legacy hash payload.
Explicit schema-version candidates are therefore reported unsupported, not
rehash-converted. This difference is not evidence of the production root cause.
Native Hash, canonical artifacts and historical FINALs are unchanged.

The supplied October 23 audit baseline is 24 source gaps (AI 14 + BASIC 10),
and 72 Native windows (31 evaluated + 24 due unclosed + 17 not due). These are
separate populations, not 24 successful repairs. RPT-AI-20261019-001 remains a
missing original FINAL; a BASIC report in the AI chat cannot substitute for it.
This patch does not re-query production or rewrite the historical audit receipt.

The scoring code maps supplied Result values only; it does not interpret prose.
Any future qualitative scoring rule must have an explicit version, applicability
start, and approved criteria fixed before its predictions. Missing historical
rules stay unscored. This patch selects no thresholds or production model.

Validation: `python -m unittest discover -s tests -v` uses local fake registries
and markets only. No production database, schedules, permissions or credentials
are accessed or changed.
