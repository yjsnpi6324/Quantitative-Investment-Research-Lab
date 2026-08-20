# Quantitative Investment Research Lab — Project Charter

> Updated: 2026-08-21

## Purpose

`Quantitative-Investment-Research-Lab` is the main durable research and engineering repository for the long-running system. It is not a generic tutorial collection.

The repository serves three connected directions:

1. **Quantitative investment research**, with A-share research as the primary application domain.
2. **AI Agent research and engineering**, focused on capabilities that improve the research system and broader agent work.
3. **GPT + Notion + GitHub operating system**, where this repository is the research layer and `gpt-workspace` is the execution/integration layer.

## Operating model

`Task → Skill → Agent`

GPT is the coordinator. Notion is the operational control plane for plans, tasks, projects and state. GitHub is the versioned technical and research layer. The two GitHub repositories are complementary implementation assets of the same system, not isolated projects.

## Research loop

For A-share research:

`Data → Market State → Sector/Theme → Signals/Methods → Prediction → Verification → Review → Method Upgrade`

For Agent research:

`Question → Research → Experiment → Evaluate → Record → Reuse → Retire`

## Decision authority

Routine maintenance may be performed autonomously: improve structure, update resources, remove stale material, add better methods, and revise documentation. Major changes to goals, architecture, or core methodology should be versioned and surfaced explicitly.

## RAG policy

Do not introduce a dedicated RAG layer merely for appearance. Add retrieval infrastructure only when a concrete workload demonstrates that direct structured retrieval, GitHub search, Notion retrieval, or task-local context is insufficient.
