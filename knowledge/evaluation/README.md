# Evaluation Knowledge

This section contains evaluation principles that are shared by the broader research system but applied to different targets.

## Evaluation domains

### Quantitative model evaluation

Evaluate factors, models, strategies, and portfolio methods for:

- predictive or investment value against an explicit baseline
- Point-in-Time correctness
- look-ahead / future-function risk
- data leakage and survivorship bias
- transaction costs, slippage, liquidity, and turnover
- temporal validation, Walk-Forward, and Out-of-Sample performance
- parameter sensitivity and multiple-testing risk
- regime robustness and failure cases
- reproducibility and data provenance

Promotion is evidence-driven. A strong single backtest is not enough for Champion consideration.

### Research Agent evaluation

Evaluate the AI-assisted research system for:

- task success
- factual correctness
- tool-selection and tool-execution success
- instruction adherence
- planning and recovery quality
- reproducibility
- latency and cost
- provenance and evidence quality

Agent evaluation belongs here only when it is directly related to the quantitative research workflow. General GPT / Agent engineering evaluation belongs in `gpt-workspace`.

## Shared principle

External benchmarks are useful for comparison, but production decisions should also use a small evaluation set that represents the actual workload.

Every meaningful evaluation should record the target, version, data or evaluation set, success criteria, sample size, results, failure modes, and date.

## Boundary

This directory is not a replacement for Notion's durable evaluation history. GitHub stores reproducible evaluation definitions, fixtures, code, and methodological rules; Notion stores the operational history and longitudinal records.