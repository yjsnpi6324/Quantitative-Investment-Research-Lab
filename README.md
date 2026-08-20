# Quantitative Investment Research Lab

> A quantitative investment research laboratory for A-share research, model development, backtesting, validation, and ongoing Champion / Challenger evaluation.

## Project role

This repository is the **quantitative research and experimentation layer** of the broader GPT research system. It is a research laboratory, not a generic AI Agent learning repository and not a replacement for Notion.

It is intentionally separate from `gpt-workspace`:

- `gpt-workspace` — how GPT and Research Agents work: prompts, skills, workflows, automation, integrations, and reusable engineering assets.
- `Quantitative-Investment-Research-Lab` — what the investment models and research methods are: factors, models, strategies, experiments, backtests, risk, portfolio construction, and validation.

## Responsibilities

- A-share quantitative research
- Alpha factor research and mining
- Technical, fundamental, sentiment, and macro factors
- Market regime / state identification
- Machine-learning and time-series models
- Backtesting and portfolio research
- Risk modelling and portfolio optimization
- Data quality and research infrastructure
- Benchmarking and model evaluation
- Champion / Challenger experimentation
- External open-source quantitative project evaluation

## Validation discipline

A method is not promoted to the formal prediction system because it has a strong single backtest, a popular GitHub repository, or an attractive paper.

Research should explicitly consider:

- Point-in-Time data
- Look-ahead / future-function bias
- Survivorship bias
- Data leakage
- Transaction costs and slippage
- Liquidity and turnover
- Parameter overfitting
- Multiple testing
- Walk-Forward evaluation
- Out-of-Sample performance
- Regime shifts
- Robustness and cross-validation
- Data quality

## Research lifecycle

`Research → Prototype → Backtest → Walk-Forward → OOS → Robustness → Challenger → Champion`

Failed or superseded work remains useful when its scope and conclusion are documented:

`Challenger → Deprecated → Archived`

## External project intake

External repositories, papers, and methods may be evaluated, but adoption requires checking applicability to A-shares, data requirements, market-structure assumptions, leakage risks, reproducibility, licensing, maintenance burden, and out-of-sample evidence.

## Relationship with the broader workspace

- **GPT** — research, reasoning, decision-making, and orchestration.
- **Project / Task** — current scope and execution triggers.
- **Notion** — durable structured records, forecast history, model evaluation, state, and change logs.
- **File Library** — research materials, rules, Skill definitions, and historical source files.
- **gpt-workspace** — GPT / Research Agent engineering layer.
- **Quantitative-Investment-Research-Lab** — quantitative research implementation and experiments.

## Current phase

**Phase 1 — laboratory baseline.**

The current priority is to establish a clean research boundary and reproducible validation discipline without prematurely creating a large framework or many empty directories.
