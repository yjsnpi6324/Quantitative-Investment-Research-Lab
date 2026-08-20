# Quantitative Research Project Charter

> Updated: 2026-08-21

## Purpose

`Quantitative-Investment-Research-Lab` is the quantitative investment research and experimentation repository for the broader GPT research system.

It is not a generic AI Agent learning repository. Agent engineering belongs in `gpt-workspace`.

## Primary scope

1. A-share quantitative research
2. Factor discovery and evaluation
3. Model and strategy research
4. Backtesting and portfolio construction
5. Risk modelling
6. Data quality and research infrastructure
7. Walk-Forward / Out-of-Sample validation
8. Champion / Challenger model management
9. External quantitative project evaluation

## Operating model

`Research question → Data → Prototype → Backtest → Walk-Forward → OOS → Robustness → Challenger / Champion`

GPT coordinates research and reasoning. Notion records durable structured research history, evaluations, state and change logs. GitHub stores reproducible engineering and experimental artifacts.

## Model promotion

A method becomes a candidate Champion only after it demonstrates robust improvement against an explicit benchmark without relying on leakage, unrealistic execution assumptions, or unstable parameter fitting.

## Research states

`Research → Prototype → Challenger → Champion`

Retirement states:

`Deprecated → Archived`

## Mandatory validation concerns

Point-in-Time correctness, look-ahead bias, future functions, survivorship bias, data leakage, transaction costs, slippage, liquidity, turnover, parameter overfitting, multiple testing, Walk-Forward evaluation, OOS performance, regime shift, robustness, and data quality.

## Scope boundary

Do not use this repository as a database for transient operational state. Do not duplicate large Notion datasets unless they are required as reproducible research inputs or fixtures.
