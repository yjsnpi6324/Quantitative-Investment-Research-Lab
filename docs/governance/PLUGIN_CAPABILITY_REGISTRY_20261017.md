# Prediction Plugin Capability Registry — 2026-10-17

Applies to TASK-ASTOCK-DAILY / BASIC-PROD-20260825-A and TASK-AI-DAILY / AI-PROD-20260825-A. Explicit, auditable capability registration; **not** an assertion that a Task scheduler or production runtime has been reconfigured. No new predictions, locked FINAL rewrites, or changes to Champion Models.

| Plugin | Registered stage | Lines | Allowed operations | Forbidden operations | Activation gate |
| --- | --- | --- | --- | --- | --- |
| Bigdata.com | EVIDENCE_CANDIDATE | BASIC, AI | Search filings, earnings, corporate events; cite source, timestamp, event ID; corroborate independently | Sole-source Actual, automatic direction override | Authenticated query and provenance readback |
| Exa | DISCOVERY_CANDIDATE | BASIC, AI | Discover external sources and source URLs | Treat search excerpts as confirmed fact | Search/readback and provenance test |
| Firecrawl | RECOVERY_CANDIDATE | BASIC, AI | Fetch source original for evidence recovery, record URL/time | Create monitors, assert truth from scrape alone, overwrite FINAL | Authenticated scrape and source-integrity test |
| Vercel | OBSERVABILITY_CANDIDATE | Infrastructure | Read existing deployments/logs and status changes | Create deployments, treat READY as prediction correctness | Existing project identity and read-only access |
| Context7 | ENGINEERING_CALIBRATION_CANDIDATE | Infrastructure | Resolve library IDs and versioned SDK/DB documentation | Market evidence, automatic production dependency updates | Version-specific documentation test |
| Scite | METHOD_REVIEW | Both | Research citation validity and methodology review | Sole-source investment decision | Independent methodology review |
| Flourish | EVALUATION_VISUALIZATION | Both | Plot verified FORMAL_CLOSED samples | Mutate Evaluation Registry | Verified registry input |
| Wolfram | COMPUTATION_SHADOW | Both | Independently check statistical calculations | Replace Champion Model or invent Actual | Reproducible fixture |
| Hugging Face | MODEL_RESEARCH_SHADOW | Both | Research candidate models and datasets | Production model replacement | Separate model approval |

## Run-time interface and audit contract
For each invocation, record plugin, line, stage, requested_at, input_scope, source_uri, evidence_timestamp, result_status, result_digest when stable, corroboration_status, degraded_reason and downstream_consumers. Record **not invoked** explicitly rather than implying an active call. Keep BASIC/AI identity and manifests separate.

Activation states: REGISTERED (catalogued), CONNECTIVITY_VERIFIED (authenticated representative read with source), SHADOW_VERIFIED (repeated real runs with trace), PRODUCTION_EVIDENCE_ENABLED (task execution wiring and independent corroboration confirmed), DEGRADED (failure). Do not equate installed tool availability with CONNECTIVITY_VERIFIED or task activation.

## Promotion constraints
- Market evidence from Bigdata/Exa/Firecrawl is advisory until original-source integrity, time bounds, independence, and snapshot provenance pass; never mutate locked FINAL or override native Prediction Hash.
- Vercel/Context7 never vote on forecasts. Runtime changes remain under separate reviewed PR and production-task authorization.
- Missing or failed optional plugin: record degradation and preserve existing authoritative source chain; missing mandatory evidence: block formal promotion.
- Do not increase production tool call volume or change prompt/model weighting until a measured, reversible shadow-vs-baseline evaluation is reviewed.
- Existing first-batch governance and controlled second-batch gates remain in force. No plugin gains direct Supabase/Notion/GitHub/Dropbox write access from this registry.

## Rollout and rollback
1. Register five priority plugins with no scheduler changes.
2. Check one real read-only representative operation per plugin and store minimal provenance; only then mark CONNECTIVITY_VERIFIED.
3. Compare independent source agreement and failure handling on at least three separate scheduled runs; only then consider SHADOW_VERIFIED.
4. Promote to PRODUCTION_EVIDENCE_ENABLED only with Task prompt/runtime readback and explicit provenance. Roll back to REGISTERED/DEGRADED on disagreement, access drift or missing audit.
