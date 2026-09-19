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
- The evaluation runner recomputes target dates from Trading Date and the exchange calendar, so bad historical labels cannot silently drive scoring.

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
