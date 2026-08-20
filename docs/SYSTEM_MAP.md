# System Map

## Role
`Quantitative-Investment-Research-Lab` is the quantitative research and experimentation layer of the broader GPT research system.

## System boundaries

- **GPT**: reasoning, research, orchestration, decision-making, and execution planning.
- **Notion**: plans, tasks, project state, durable operational records, forecast history, model evaluation history, and change logs.
- **GitHub / gpt-workspace**: GPT-facing prompts, skills, workflows, automations, connectors, runtime experiments, and reusable AI engineering assets.
- **GitHub / Quantitative-Investment-Research-Lab**: quantitative research code, factors, models, strategies, backtests, validation, risk, portfolio research, reproducible experiments, and versioned research methodology.

## Research loop

`question → data → prototype → backtest → Walk-Forward → OOS → robustness → review → method upgrade`

## Promotion loop

`Research → Prototype → Challenger → Champion`

Failed or superseded methods remain useful when their scope and conclusion are documented:

`Deprecated → Archived`

## Sync principle

Notion tracks **what is being done, why it matters, and the longitudinal result**.

GitHub tracks **how it is implemented, reproduced, and validated**.

GPT coordinates the two.

## Quality loop

`plan → implement → test → validate → document → sync → review → iterate`

## Maintenance rule

A resource, method, dependency, or workflow should be downgraded, replaced, or archived when it becomes obsolete, unreliable, duplicated, fragile under realistic assumptions, or consistently inferior to a better alternative.
