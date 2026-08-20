# Workspace Architecture

## Layer model

```text
GPT
  │
  ├── research / synthesis / decisions
  │
  ▼
Notion
  │
  ├── roadmap / tasks / knowledge / project state
  │
  ▼
GitHub
  │
  ├── code / experiments / documents / version history
  │
  ▼
Execution & Evaluation
  │
  └── results feed back into GPT + Notion
```

## Responsibilities

### GPT

- Investigate new technologies and research.
- Compare approaches and identify useful changes.
- Turn research into implementation plans.
- Review experiment results.
- Propose updates when existing approaches become obsolete.

### Notion

- Maintain the learning roadmap.
- Track tasks and project status.
- Store synthesized knowledge and decisions.
- Link goals to concrete GitHub artifacts.

### GitHub

- Store executable code and reproducible experiments.
- Version important documentation and configurations.
- Preserve implementation history.
- Provide the engineering source of truth for completed work.

## Promotion flow

A resource or idea should move through these stages:

1. **Discovered** — potentially useful material is found.
2. **Evaluated** — credibility, freshness, applicability, and implementation quality are checked.
3. **Selected** — useful material is added to the learning roadmap.
4. **Implemented** — concepts are tested in a project or experiment.
5. **Validated** — results are recorded with limitations.
6. **Maintained** — outdated methods are downgraded, replaced, or archived.

## Design rule

Do not optimize for the number of resources collected. Optimize for the number of reliable capabilities that can actually be demonstrated, reproduced, and improved.
