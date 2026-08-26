# System of Records

## Purpose

This document defines the permanent responsibility boundaries between GPT, Tasks/Automations, Notion, and GitHub. It is the governing map for cross-system reads and writes.

## 1. GPT / Orchestrator

**Role:** reasoning, orchestration, execution and reconciliation.

GPT may read and write the systems below, coordinate workflows, diagnose failures, and synthesize research. GPT does not silently treat temporary chat content as durable truth.

When sources conflict, GPT must identify the conflict and apply the source-of-record rules below rather than silently choosing a convenient copy.

## 2. Task / Automation

**Role:** scheduling and execution control.

Owns:
- schedule and recurrence;
- trigger conditions;
- task-specific execution prompt;
- execution context and delivery target.

Does not own:
- research truth;
- historical prediction records;
- experiment evidence;
- model promotion decisions.

A Task may discover a candidate research method and submit it through the Research Intake Contract, but discovery does not authorize production adoption.

## 3. Notion / Control Plane

**Role:** operational state, human-readable control surface and decision ledger.

Owns:
- project/task status;
- prediction records and validation status;
- monthly/quarterly/semiannual reviews;
- self-audit status;
- method/Skill registry and adoption status;
- key decisions and governance summaries;
- navigation and human-readable dashboards.

Notion is not the canonical home for source code, full experiment implementations, or reproducibility artifacts.

## 4. GitHub / Research Source of Truth

**Role:** durable research and engineering source of truth.

Owns:
- research protocols;
- source/research intake contracts;
- code and implementation;
- experiment specifications and artifacts;
- data contracts/schemas;
- Evaluation and validation rules;
- model/method versions;
- reproducibility evidence;
- Challenger/Champion research evidence.

GitHub is not the task scheduler and should not be used as a duplicate operational database.

## 5. Canonical Report

For each daily prediction run, one Canonical Report is created first. Chat, PDF and Notion presentation are delivery/operational representations of that report. They must not independently invent a second version of the daily research.

## 6. Cross-system write rules

| Information | System of Record | Other systems |
|---|---|---|
| Schedule / trigger | Task | Notion status/reference |
| Task execution prompt | Task | GitHub/Notion may document version |
| Daily prediction fact | Notion | GitHub may retain research artifact |
| Prediction evaluation | Notion | GitHub owns evaluation implementation/rules |
| Research method | GitHub | Notion registry/summary |
| Code / experiment | GitHub | Notion link/summary |
| Model version | GitHub | Notion active-status record |
| Governance decision | Notion | GitHub evidence/reference |
| Research intake | GitHub | Notion status/reference |
| Self-audit finding | Notion | GitHub methodology/evidence where applicable |

## 7. Conflict resolution

1. Research implementation/evidence conflict → GitHub wins after verification.
2. Operational status/decision conflict → Notion wins after verification.
3. Schedule/prompt conflict → active Task configuration wins for execution; GitHub may hold the governed reference version.
4. Historical prediction conflict → immutable original prediction record wins; never rewrite it to match later analysis.
5. If a conflict cannot be resolved, mark it explicitly as an audit issue rather than guessing.

## 8. Integrity principles

- One fact, one owner.
- Cross-system copies are references or summaries, not competing sources of truth.
- Never silently overwrite historical evidence.
- Never promote a method because a Task discovered it.
- Every production method must have versioned research/evaluation evidence.
- Every material system change should be traceable to a versioned rule, Task change, GitHub commit, or Notion decision.
