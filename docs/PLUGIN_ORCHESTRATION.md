# Plugin Orchestration Baseline — 2026-09-19

This document defines the role boundaries for external tools used by the A-share Research Agent production and governance system.

## Core production and persistence

### Supabase — ACTIVE_CORE
Role: machine-state and persistence node.

Use for verified task runs, task results, integration events, integration-node state and other structured runtime metadata. Always inspect the real schema before writes. Do not create synthetic records for health checks or keepalive purposes.

### Notion — canonical human-readable registry
Role: human-readable Prediction / Evaluation / Champion / Source / governance registry plus Handoff mailbox.

New FORMAL predictions after the 2026-09-19 infrastructure repair should persist:
- Prediction Hash
- T+1 Target Date
- T+3 Target Date
- T+5 Target Date

The original FINAL prediction body remains immutable.

### GitHub — versioned engineering and evidence ledger
Repository: `yjsnpi6324/Quantitative-Investment-Research-Lab`

Use branch -> minimal change -> self-check -> commit -> PR -> review. Do not treat branch or PR state as main-branch persistence. Production ledger, evaluation evidence and governance rules remain auditable here.

### Dropbox — archive
Role: complete Markdown / JSON archival copies and structured evidence bundles. Existing conflicting objects are never silently overwritten.

## Evidence and research layer

### Bigdata.com — financial / event evidence
Use for market, company, industry, filings, earnings calls, macro and overseas-mapping evidence, including Actual validation. Important facts should be cross-checked against official disclosures or another approved source. A single Bigdata item must not directly determine Prediction direction or Evaluation result.

### Firecrawl — WATCH / SHADOW ingestion
Use for primary webpage, IR, policy attachment, association document, white paper, README, Issue and merged-PR retrieval.

A successful scrape is not fact verification. Firecrawl is not a canonical publisher and must not self-promote from WATCH to ACTIVE. Do not create Firecrawl monitors or additional scheduled tasks unless explicitly approved.

### Public Equity Investing — Research / Thesis
When runtime-accessible, use for structured company / industry / ETF / valuation / catalyst / risk research. It contributes hypotheses and counter-evidence, not final market truth.

### Data — Evaluation / Analytics
When runtime-accessible, use for Prediction Ledger analytics, matured samples, horizon statistics, HIT / PARTIAL / MISS, error attribution and source-increment analysis. It must never overwrite locked Prediction history.

## Method validation

### Scite — Scientific / Method Validation
Use for quantitative factors, regime detection, forecasting evaluation, time-series methods, machine-learning-in-finance methods and Champion / Challenger research.

Academic support is auxiliary evidence only. Publication count or supporting citations do not replace real out-of-sample Prediction / Evaluation performance.

### Context7 — Engineering Calibration
Use only for current SDK / API / dependency documentation when engineering compatibility matters, including Supabase, Vercel, OpenAI SDK, Next.js, Python / JavaScript packages and MCP implementations.

Context7 is not a market, company or macro evidence source.

## Runtime and observability

### Vercel — Runtime / Observability
Observe existing deployments, build failures, runtime errors and agent-run traces. Do not manufacture deployments for governance checks.

`VERCEL_READY` means the runtime is healthy; it does not mean the Prediction is correct.

### Flourish — Visualization
Consume only already-verified structured data for dashboards and visual analysis. Visualization failures do not block FINAL production or Evaluation.

## Evaluation infrastructure rules

The 2026-09-19 infrastructure repair is now canonical:

1. T+1 / T+3 / T+5 are strict A-share trading-day horizons.
2. New FORMAL predictions must carry immutable Prediction Hash and structured target dates.
3. One canonical prediction row may contain all three horizons; the Evaluation runner expands them independently.
4. Evaluation is idempotent by `(Prediction ID, Horizon)`.
5. Missing or unverified Actual stays pending; it is never converted into a fabricated MISS.
6. Historical predictions missing contemporaneous hashes are classified `BLOCKED_INVALID_HASH`.
7. Historical provenance repair must be explicitly labeled `BACKFILL_PROVENANCE` / `MIGRATION_HASH`; it must not pretend the record was locked at publication time.
8. Governance backlog states are separate from model-performance states.

## Current runtime visibility

As of 2026-09-19, tool namespaces are visible for:
- Bigdata.com
- Firecrawl
- Supabase
- Vercel
- Context7
- Scite
- Flourish

Availability of Public Equity Investing / Data must still be verified at the runtime action level before production reliance.

## Task mapping

- A股基本盘日报预测 / A股AI板块日报预测: research production, evidence synthesis, Notion Handoff only.
- 日报多节点治理 V2.4: persistence, provenance, Evaluation backlog, repair, runtime observability.
- Champion 周度健康检查 V2.1: model health, method validation, Challenger / Baseline comparison, governance-health separation.
- AI Agent 每日学习 V2: engineering learning and real-project practice; it must not contaminate production records.
