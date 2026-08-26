# Documentation Index

Use this page to avoid duplicate or conflicting project documentation.

## Canonical documents

1. `PROJECT_CHARTER.md` — what the lab is and its durable boundaries.
2. `ARCHITECTURE.md` — research-system architecture.
3. `A_SHARE_RESEARCH_AGENT.md` — A-share prediction-agent operating design.
4. `OPERATIONS_AND_DELIVERY.md` — runtime, Canonical Report and delivery rules.
5. `RESEARCH_SYNC.md` — Project / Task / GitHub / Notion synchronization contract.
6. `REPOSITORY_MAP.md` — repository ownership and directory responsibilities.
7. `ROADMAP.md` — current research priorities and sequencing.
8. `SYSTEM_MAP.md` — compact visual/system reference; use architecture docs for authoritative rules.
9. `THREE_LONG_TERM_DIRECTIONS.md` — strategic reference for the research lab; AI Agent learning is maintained as a separate long-term system and does not override the lab scope.

## Evaluation

`evaluation/` is the canonical home for prediction evaluation, periodic reviews, self-audit and governance contracts.

## Research

`research/` is the canonical home for experiments and reproducible research specifications.

`research/NEW_QUANT_METHOD_DISCOVERY_PROMPT.md` is the canonical execution protocol for discovering, triaging, reproducing, validating and governing new quantitative methods found from global sources.

## Knowledge and templates

`knowledge/` stores durable research knowledge; `templates/` stores reusable templates.

## Scope boundary

`Quantitative-Investment-Research-Lab` owns A-share research, prediction evaluation, durable research engineering, and validated methods/skills adopted by that system. AI Agent learning curriculum, learning progress, resource selection, and learning experiments belong to the independent AI Agent learning system. `gpt-workspace` owns GPT-facing runtime and integration assets.

## Maintenance rule

When two documents conflict, prefer the higher-ranked canonical document above. Do not create a second document for an existing responsibility; update the canonical file instead. Historical documents are retained when they contain useful evidence, but obsolete rules should be marked Deprecated rather than silently reused.
