# Quantitative Research Architecture

## System boundary

```text
GPT
  │ research / reasoning / orchestration
  ▼
gpt-workspace
  │ prompts / skills / workflows / automation / integrations
  ▼
Quantitative-Investment-Research-Lab
  │ data / factors / models / strategies / backtests / risk / validation
  ▼
Notion
  │ structured research history / forecasts / evaluation / state / change log
  ▼
GPT Research Agent
```

## Responsibilities

### GPT
- Investigate research questions.
- Compare methods and evidence.
- Orchestrate research and review.
- Interpret experiment results.

### gpt-workspace
- Define reusable Agent capabilities.
- Run research workflows and automation.
- Manage integrations and tool execution.

### Quantitative-Investment-Research-Lab
- Implement reproducible quantitative experiments.
- Store factor/model/strategy research artifacts.
- Run backtests and temporal validation.
- Record Challenger and Champion evidence.

### Notion
- Maintain durable structured records and operational state.
- Store forecast history, model evaluation, decisions, and change logs.

## Research promotion

`Question → Research → Prototype → Backtest → Walk-Forward → OOS → Robustness → Challenger → Champion`

Retired work remains traceable through `Deprecated → Archived` rather than being silently deleted.

## Design rule

Do not create framework layers, data stores, or abstractions without a demonstrated research workload that needs them. Prefer small reproducible components over premature platform engineering.
