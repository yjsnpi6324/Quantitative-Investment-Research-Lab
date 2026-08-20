# System Map

## Role

`Quantitative-Investment-Research-Lab` is the research and engineering knowledge layer for the long-running system.

## System boundaries

- **GPT**: reasoning, research, orchestration, decision-making and execution planning.
- **Notion**: plans, tasks, project state, operational records and human-readable coordination.
- **GitHub / Quantitative-Investment-Research-Lab**: quantitative research, A-share research, experiments, methods, technical documentation and durable versioned knowledge.
- **GitHub / gpt-workspace**: GPT-facing tools, automations, connectors, runtime experiments and integration code.

## Sync principle

Notion tracks *what is being done and why*. The research lab tracks *what was researched, implemented and validated*. `gpt-workspace` tracks *how GPT connects to tools and executes integrations*. GPT coordinates the system.

## Quality loop

`plan → research/implement → test → validate → document → sync → review → iterate`

## Maintenance rule

A resource, method, dependency, or workflow should be downgraded or removed when it becomes obsolete, unreliable, duplicated, or consistently underperforms a better alternative.
