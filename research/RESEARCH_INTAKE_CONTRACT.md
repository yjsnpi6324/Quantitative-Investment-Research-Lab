# Research Intake Contract

## Purpose

Define the standard handoff from discovery Tasks to `Quantitative-Investment-Research-Lab` for newly discovered quantitative trading/research methods.

The contract separates **discovery** from **research validation** and prevents an unverified method from directly changing a production prediction system.

## Roles

- **Discovery Task / Scout:** searches current global sources, identifies candidates, performs initial triage, and submits an intake record.
- **Research Lab:** owns reproduction, A-share adaptation, experiments, validation artifacts, and method versioning.
- **Evaluation / Self-Audit:** measures evidence quality, detects methodological or execution problems, and records audit findings.
- **Production Tasks:** Basic Market and AI Sector consume only explicitly approved Validated Challenger / Champion methods relevant to their own task.

## Candidate lifecycle

`DISCOVERED → TRIAGED → REPRODUCING → A_SHARE_ADAPTATION → VALIDATING → CHALLENGER → VALIDATED → CHAMPION`

Possible exits at any stage: `REJECTED`, `OBSERVED`, `DEPRECATED`.

No production Task may consume a method whose status is only `DISCOVERED`, `TRIAGED`, `REPRODUCING`, or `OBSERVED`.

## Required intake fields

Every submitted candidate should include:

- `candidate_id` — stable identifier, e.g. `QMETHOD-2026-0001`;
- `method_name`;
- `discovered_at`;
- `source_url` or durable source reference;
- `publication/source_date`;
- `source_type`;
- `source_reliability`;
- `original_claim`;
- `market/universe`;
- `signal_definition`;
- `target` and `horizon`;
- `required_data` and frequency;
- `execution/cost assumptions`;
- `implementation/code reference` when available;
- `why_interesting`;
- `known_limitations`;
- `A_share_relevance`;
- `initial_bias/leakage risks`;
- `discovery_task_id`;
- `suggested_priority`.

## Intake decision

The discovery Task must assign one initial recommendation:

- **REJECT** — obvious invalidity, unverifiable claim, severe leakage/bias, or insufficient evidence.
- **OBSERVE** — interesting but currently insufficient evidence or implementation.
- **REPRODUCE** — enough evidence to attempt independent reproduction.
- **CHALLENGER_CANDIDATE** — strong enough to enter the formal validation pipeline.

The recommendation is not a production decision.

## GitHub handoff

Once a candidate is accepted for research, create a durable research record in this repository and link back to the originating Task.

Minimum durable record:

```text
candidate_id
method_name
status
source(s)
discovery_task_id
research_record
implementation_reference
validation_artifacts
current_version
last_evaluated_at
owner/agent
next_action
```

Use the repository as the durable research source of truth. Notion may contain the human-readable status and decision summary; it must not silently diverge from the GitHub research record.

## Production handoff

A validated method may be proposed to a production Task only when:

1. reproduction is documented;
2. A-share adaptation is documented where applicable;
3. Walk-Forward/OOS and required robustness tests pass the relevant gates;
4. comparison against the current Champion and baselines is complete;
5. the method has a versioned validation artifact;
6. the task-specific relevance is established;
7. Evaluation / governance records the decision.

A method validated for the Basic Market task is **not automatically validated for AI Sector**, and vice versa.

## Feedback loop

Production results must flow back into research:

`Production Prediction → Outcome → Evaluation → Self-Audit → Method Performance → Research Feedback`

If a method degrades in production, open an audit/research event. Do not silently edit the historical method or original prediction record.

## Integrity rules

- Never fabricate source discovery, reproduction, or validation.
- Never backfill a candidate's evidence using future information.
- Never overwrite the original intake record.
- Never promote based on one attractive backtest or a small sample.
- Preserve rejected methods and failure reasons when they provide reusable evidence.
- Keep discovery, validation, and production authority separate.
