# Contributing

## Purpose
This repository is the quantitative investment research and experimentation lab. General GPT / Agent engineering belongs in `gpt-workspace`.

## Working rules
- Prefer reproducible experiments over vague notes.
- Record data sources, assumptions, validation status, and conclusions.
- Separate stable research principles from hypotheses and experimental results.
- Check Point-in-Time correctness and leakage risks before trusting results.
- Treat external methods as candidates until independently validated.
- Keep changes focused; avoid premature framework building.
- Never commit secrets, credentials, personal data, or local datasets containing sensitive information.

## Research lifecycle
`discover → evaluate → prototype → backtest → validate → challenger → champion`

Retirement lifecycle:
`deprecated → archived`

## Commit style
Use concise, action-oriented commit messages, for example:
- `docs: clarify validation protocol`
- `research: add factor experiment`
- `feat: add backtest component`
- `fix: correct point-in-time handling`
- `refactor: simplify research module`
