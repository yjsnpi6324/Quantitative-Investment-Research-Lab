# A-share Research Agent — Operations & Delivery Standard

> Status: Active baseline
> Updated: 2026-08-26

## 1. Separation of execution contexts

The Basic Market (`基本盘`) forecast and AI-sector (`AI板块`) forecast are separate research tasks and must not rely on shared conversational history for execution.

They may share the research substrate:
- data-quality rules
- source registry
- research methods
- Challenger/Champion evaluation
- historical verification
- Notion prediction database
- Quantitative-Investment-Research-Lab

They must not share task-local conversational state, temporary reasoning, or report-generation context.

If the platform cannot provide independent chat threads for scheduled tasks, the system must use the closest available independent execution context rather than silently treating the shared chat as a research state store.

## 2. Canonical report principle

Each forecast run produces one canonical report object. Chat and PDF are delivery surfaces, not the source of truth.

Canonical flow:

`Task → Research → Canonical Report → Notion / Chat / PDF`

The canonical report must contain:
- trading-day status
- market/sector state
- core drivers
- T+1/T+3/T+5 trading-day forecasts
- confidence
- invalidation/risk conditions
- source/data-quality notes
- model/rule version
- verification status when applicable

## 3. PDF delivery

PDF is a reproducible publication mirror of the canonical report.

A PDF failure must never imply loss of research data. The report must remain recoverable from the structured Notion record and, where appropriate, GitHub research assets.

A PDF is considered successfully delivered only when:
1. generation completes;
2. the file has a stable accessible reference;
3. the file can be opened by the user;
4. the content matches the canonical report.

## 4. Notion storage

Use one unified prediction data source for cross-task analysis, with separate views for Basic Market and AI-sector forecasts.

Prediction records must preserve original forecasts. Later runs may append verification and error attribution but must not rewrite the original prediction.

Required evaluation dimensions include:
- T+1 / T+3 / T+5
- direction hit rate
- confidence/calibration
- market-state-conditioned performance
- error attribution
- model/rule version

## 5. GitHub research layer

`Quantitative-Investment-Research-Lab` is the durable research and engineering layer. `gpt-workspace` is the execution/integration layer.

External methods remain Challenger candidates until they pass:

`reproduce → A-share adaptation → backtest → walk-forward → OOS → robustness`

No method becomes Champion merely because an external paper, repository, or prompt produces plausible results.

## 6. Source registry and data governance

Maintain source provenance, timestamp, freshness, validation status and reliability. On non-trading days, prioritize source review, data governance, historical verification and method maintenance.

When important values cannot be adequately cross-validated, do not fabricate or silently fill them.

## 7. Task health checks

A scheduled task is healthy only if the full chain succeeds:

`trigger → data → research → forecast → canonical report → Notion → PDF delivery → verification state`

A task that runs but fails downstream delivery is a partial failure, not a successful run.

## 8. Cleanup policy

Historical chats must not be treated as the system of record. Do not delete legacy forecast chats until the canonical report, Notion history, GitHub research assets and delivery path have been verified.

Once the new pipeline is stable, legacy chats may be archived/deleted as UI history without affecting the research record.
