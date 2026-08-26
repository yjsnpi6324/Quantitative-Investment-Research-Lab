# Self-Validation Checklist — 2026-08-26

## Structural validation

- [x] Prediction evaluation layer documented.
- [x] Immutable prediction ledger schema created.
- [x] Evaluation record schema created.
- [x] Self-audit rules created.
- [x] Notion self-audit/statistics control database created.

## Integrity rules

- Original forecasts remain immutable.
- Evaluation is append-only relative to prediction facts.
- Audit findings do not silently modify models or historical predictions.
- T+1/T+3/T+5 are trading-day horizons.
- Every material metric must carry sample size and version context.

## Remaining runtime validation

The platform-level scheduled-task chat-thread isolation and PDF user-accessibility cannot be proven by repository structure alone. These remain runtime acceptance tests and must stay open until a real scheduled run produces two isolated contexts and user-openable PDF references.

## Acceptance gate

Do not mark the full system as production-stable until:

1. a Basic Market run passes the complete chain;
2. an AI Sector run passes the complete chain;
3. their execution contexts are demonstrably isolated;
4. both canonical reports reach Notion;
5. both PDFs are independently openable;
6. evaluation records reconcile to locked predictions;
7. self-audit produces no unresolved P0/P1 integrity issue.
