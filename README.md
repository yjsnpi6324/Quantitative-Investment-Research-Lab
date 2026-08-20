# Quantitative Investment Research Lab

> A continuously evolving research and engineering workspace for AI-assisted quantitative investment research.

## Purpose

This repository is the durable research and engineering layer for the long-running system. It connects research, methods, experiments, implementation notes, and reusable engineering patterns into one version-controlled workspace.

The primary application focus is A-share research, including market-state analysis, sector and theme research, forecasting, verification, source-quality evaluation, and method evolution. AI Agent research remains a supporting engineering direction because the research system itself is built around agentic capabilities.

The goal is not to collect resources indefinitely. Resources and methods are evaluated continuously: high-value and current material is promoted, obsolete or misleading material is deprecated, and practical experiments are kept alongside the theory they validate.

## Operating principles

- **Observe → Structure → Execute → Measure → Review → Improve**
- Prefer primary sources, official documentation, papers, and working implementations.
- Treat frameworks, tutorials and individual methods as replaceable; keep durable concepts and engineering principles.
- Record experiments and conclusions so future iterations can build on previous work.
- Promote methods only after measurable validation on the target workload, with appropriate out-of-sample testing.
- Downgrade or retire stale, unreliable, duplicated, or consistently inferior approaches.
- Keep GitHub focused on versioned research and engineering artifacts; use Notion for higher-level planning, tracking, and operational state.

## Workspace structure

```text
Quantitative-Investment-Research-Lab/
├── README.md
├── docs/
│   ├── ARCHITECTURE.md
│   ├── A_SHARE_RESEARCH_AGENT.md
│   ├── PROJECT_CHARTER.md
│   ├── ROADMAP.md
│   ├── SYSTEM_MAP.md
│   └── THREE_LONG_TERM_DIRECTIONS.md
├── knowledge/          # Durable technical and research knowledge
├── research/           # Methods, hypotheses, evaluations and research notes
├── experiments/        # Reproducible experiments and findings
├── templates/          # Standard research and experiment formats
└── .github/            # Repository automation and contribution configuration
```

## Current focus

1. A-share market-state, sector and theme research
2. Forecasting, verification and post-event scoring
3. Data/source quality and provenance
4. Quantitative methods, factors and robust ensembles
5. Agent capabilities that improve the research workflow
6. Evaluation, reliability, memory and context engineering
7. Reproducible experiments and method lifecycle management
8. Continuous frontier tracking and retirement of obsolete approaches

## Relationship with the broader system

- **GPT:** research, reasoning, synthesis, orchestration and execution planning.
- **Notion:** roadmap, tasks, project state, research synthesis and decisions.
- **GitHub / Quantitative-Investment-Research-Lab:** durable research, experiments, methods and versioned engineering knowledge.
- **GitHub / gpt-workspace:** GPT-facing tools, connectors, automations, runtime and integration implementation.

The objective is one connected operating loop rather than three disconnected tools.

## Status

**Active — continuously maintained.**
