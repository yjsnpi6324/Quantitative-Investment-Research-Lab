# AI System Project Charter

> Updated: 2026-08-21

## Purpose

`ai-agent-lab` is the main research and engineering repository for the user's long-running AI system. It is not a generic tutorial collection.

The repository serves three connected directions:

1. AI Agent learning and research
2. A-share AI / 基本盘 prediction research
3. The GPT + Notion + GitHub operating system

## Operating model

`Task → Skill → Agent`

GPT is the coordinator. Notion is the operational control plane for plans, tasks, projects and state. GitHub is the versioned technical/research layer. The two repositories are implementation assets of the same system, not isolated projects.

## Research loop

`Data → Market State → Sector/Theme → Prediction → Verification → Review → Method Upgrade`

The same closed-loop principle applies to Agent research:

`Question → Research → Experiment → Evaluate → Record → Reuse → Retire`

## Decision authority

Routine maintenance may be performed autonomously: improve structure, update resources, remove stale material, add better methods, and revise documentation. Major changes to goals, architecture, or core methodology should be versioned and surfaced explicitly.

## RAG policy

Do not introduce a dedicated RAG layer merely for appearance. Add retrieval infrastructure only when a concrete workload demonstrates that direct structured retrieval, GitHub search, Notion retrieval, or task-local context is insufficient.
