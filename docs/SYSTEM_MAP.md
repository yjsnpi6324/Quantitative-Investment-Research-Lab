# System Map

## Role
`ai-agent-lab` is the research and engineering knowledge/code layer for the user's AI Agent system.

## System boundaries

- **GPT**: reasoning, research, orchestration, decision-making, and execution planning.
- **Notion**: plans, tasks, project state, durable operational records, and human-readable knowledge management.
- **GitHub / ai-agent-lab**: code, experiments, technical documentation, reproducible research, and versioned engineering knowledge.
- **GitHub / gpt-workspace**: GPT-facing tools, automations, connectors, runtime experiments, and integration code.

## Sync principle
Notion tracks *what is being done and why*. GitHub tracks *how it is implemented and what was validated*. GPT coordinates the two.

## Quality loop
`plan → implement → test → validate → document → sync → review → iterate`

## Maintenance rule
A resource, method, dependency, or workflow should be downgraded or removed when it becomes obsolete, unreliable, duplicated, or consistently underperforms a better alternative.
