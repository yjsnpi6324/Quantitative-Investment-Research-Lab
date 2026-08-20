# Research System Sync

This document defines how Project, Task, Notion, and GitHub cooperate.

## System roles

| Layer | Source of truth |
|---|---|
| Project | Goals, scope, research context, long-term direction |
| Task | Next executable action, recurring trigger, maintenance work |
| Notion | Structured state, predictions, validation, model/Skill evaluation, decisions |
| GitHub | Code, reproducible experiments, methods, documents, version history |

## Research lifecycle

`Project → Task → Research → GitHub Experiment → Evaluation → Notion Result → Method Registry → Next Task`

## Rules

1. A Task must point to a concrete research or maintenance outcome.
2. Engineering artifacts belong in GitHub and should be traceable to a task.
3. Research conclusions belong in Notion after validation; reproducible implementation belongs in GitHub.
4. Material method-status changes update both Notion's evaluation/change log and `research/method-registry.md`.
5. Locked predictions are immutable; validation and error attribution are appended separately.
6. External methods enter as challengers and require out-of-sample evidence before promotion.
7. Conflicting information is preserved and investigated rather than silently overwritten.

## Current canonical experiment

**Market-State Classification** is the first standardized experiment. Its complete path should be used as the template for subsequent A-share research.

## Repositories

- `yjsnpi6324/Quantitative-Investment-Research-Lab` — research, methods, experiments, evaluation
- `yjsnpi6324/gpt-workspace` — GPT integration, tools, automation, runtime
