# Repository Map

This repository is the durable **research, evaluation, data-contract and experiment layer** for the A-share Research Agent.

## Directory responsibilities

- `docs/` — architecture, operating rules, synchronization and governance.
- `research/` — reproducible research experiments and research specifications.
- `evaluation/` — prediction ledger contracts, metrics, periodic reviews and self-audit.
- `knowledge/` — durable research knowledge that belongs in version control.
- `templates/` — reusable experiment/evaluation templates.

## System boundary

This repository does **not** own GPT runtime orchestration or conversational delivery. That belongs to `gpt-workspace`.

Notion remains the human-readable control plane for project state, prediction history, decisions and registries.

## Source-of-truth rules

- Prediction facts: Prediction Ledger / Notion prediction record.
- Research code/specification: this repository.
- Runtime/integration: `gpt-workspace`.
- Project/task state: Notion.
- Chat/PDF: presentation/delivery layers, never authoritative facts.

## Research lifecycle

`Research Pool → Challenger → Reproduce → A-share Adaptation → Walk-Forward → OOS → Robustness → Champion / Downgrade / Deprecated`

Do not duplicate the same rule or research result across multiple files merely for convenience. Prefer one canonical document plus links.
