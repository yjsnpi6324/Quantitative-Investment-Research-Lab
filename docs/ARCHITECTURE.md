# Workspace Architecture

## Layer model

```text
GPT
  │
  ├── research / reasoning / orchestration / decisions
  │
  ▼
Notion
  │
  ├── roadmap / tasks / projects / operational state
  │
  ▼
GitHub
  │
  ├── research lab: methods / experiments / durable knowledge
  └── gpt-workspace: tools / integrations / automation / runtime
  │
  ▼
Execution & Evaluation
  │
  └── results feed back into GPT + Notion + the relevant GitHub artifact
```

## Responsibilities

### GPT

- Investigate technologies, financial research methods and new evidence.
- Compare approaches and identify useful changes.
- Turn research into implementation plans.
- Orchestrate skills and tools.
- Review experiment and forecast results.
- Propose updates when existing approaches become obsolete.

### Notion

- Maintain roadmaps and operational plans.
- Track tasks, projects and state.
- Store synthesized decisions and human-readable coordination records.
- Link goals to concrete GitHub artifacts.

### Quantitative-Investment-Research-Lab

- Store quantitative and A-share research.
- Maintain methods, experiments and evaluations.
- Preserve durable technical knowledge and reproducible findings.
- Track method lifecycle and evidence.

### gpt-workspace

- Store GPT-facing tools and reusable wrappers.
- Implement connectors, automations and runtime components.
- Maintain integration tests and operational workflows.

## Promotion flow

A resource, method or idea should move through these stages:

1. **Discovered** — potentially useful material is found.
2. **Evaluated** — credibility, freshness, applicability and implementation quality are checked.
3. **Selected** — useful material enters the relevant research or engineering track.
4. **Implemented** — concepts are tested in a project or experiment.
5. **Validated** — results are recorded with limitations.
6. **Maintained** — outdated methods are downgraded, replaced or archived.

## Design rule

Do not optimize for the number of resources collected. Optimize for the number of reliable capabilities and research methods that can actually be demonstrated, reproduced and improved.
