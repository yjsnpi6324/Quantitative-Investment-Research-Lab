# New Quantitative Method Discovery & Validation Prompt

## Purpose

Continuously discover potentially useful quantitative trading/research methods from current global sources, then filter, reproduce, validate, and govern them before they can influence production A-share prediction systems.

This prompt is an **execution protocol**, not the source of truth for model methodology. Durable methodology, validation rules, and accepted methods must be versioned in this repository.

## 1. Discover

Search broadly across:

- peer-reviewed papers and preprints;
- major quantitative-finance conferences and research venues;
- university research groups;
- reputable systematic-investing research;
- open-source implementations and benchmarks;
- official framework/model documentation;
- high-quality practitioner research;
- recent market-structure, factor, forecasting, portfolio, and ML research.

Prioritize recent and independently corroborated work, but retain older methods when they remain theoretically or empirically relevant.

## 2. Triage

For every candidate method, record:

- method name and source;
- publication/source date;
- original problem and market assumptions;
- required data and data frequency;
- signal construction;
- target/horizon;
- transaction-cost and liquidity assumptions;
- implementation availability;
- evidence quality;
- known limitations;
- relevance to A-share prediction/research.

Classify each candidate as **Reject / Observe / Reproduce / Challenger**.

Reject methods with obvious look-ahead bias, survivorship bias, leakage, unrealistic execution assumptions, unverifiable claims, or insufficient evidence unless the purpose is explicitly methodological study.

## 3. Reproduce before trusting

Do not treat a paper, GitHub repository, benchmark, or vendor claim as validated merely because reported performance is strong.

Where feasible:

1. reproduce the original setup;
2. verify data definitions and sample construction;
3. verify train/test chronology;
4. reproduce the reported metric within a reasonable tolerance;
5. document any implementation deviation.

If reproduction fails, record the failure rather than silently modifying the method until it works.

## 4. A-share adaptation

After reproduction, test whether the method survives A-share-specific conditions:

- T+1 trading and execution constraints;
- price limits;
- suspension and delisting issues;
- listing-history bias;
- industry/sector structure;
- changing market regimes;
- liquidity and turnover;
- transaction costs, slippage and impact;
- corporate actions;
- realistic information availability timestamps.

Adaptation must preserve the method's causal logic. Do not tune aggressively to historical A-share data merely to improve backtest results.

## 5. Validation hierarchy

Use a strict hierarchy:

`Research evidence → Reproduction → In-sample diagnostic → Walk-Forward → OOS → Robustness → Cost/slippage stress → Regime analysis → Challenger comparison`

Where appropriate use:

- purged / embargoed validation;
- CPCV;
- Monte Carlo / bootstrap;
- Deflated Sharpe Ratio;
- Probability of Backtest Overfitting;
- sensitivity analysis;
- placebo / permutation tests;
- parameter stability tests.

No single backtest is sufficient for promotion.

## 6. Comparison

Every Challenger must be compared against the current Champion and meaningful baselines under the same information cutoff, universe, costs, horizon, and evaluation protocol.

Evaluate not only return or hit rate, but also:

- directional accuracy;
- calibration;
- robustness;
- drawdown/risk where relevant;
- turnover/cost sensitivity;
- regime-conditioned performance;
- stability through time;
- complexity and operational burden;
- incremental information value.

A more complex method must demonstrate meaningful incremental value to justify adoption.

## 7. Governance

A candidate can become a production Champion only after sufficient evidence and explicit versioning.

Required states:

`Candidate → Rejected / Observed / Reproducing → Challenger → Validated Challenger → Champion`

A Challenger may remain in observation indefinitely. Failure does not mean deletion; retain the evidence and failure reason.

Never change the production Champion solely because of a short losing streak or a small-sample improvement.

## 8. Information provenance

Every accepted or tested method must retain:

- source URL/reference;
- access/publication date;
- source reliability assessment;
- code/data provenance where available;
- reproduction status;
- validation artifact reference;
- method version;
- decision and rationale.

If sources conflict, record the conflict and resolve it using evidence quality and reproducibility rather than authority alone.

## 9. Continuous discovery

Run discovery continuously and prioritize:

1. methods with strong recent evidence;
2. methods that address known failure modes in the current system;
3. methods with reproducible open implementations;
4. methods offering orthogonal information rather than redundant complexity;
5. methods that improve calibration, regime detection, robustness, or evaluation.

Retire stale tutorials, broken implementations, obsolete APIs, and methods whose evidence no longer survives current validation.

## 10. Output contract

Each discovery cycle should produce a concise research record containing:

- candidates discovered;
- candidates rejected and why;
- candidates reproduced;
- validation results;
- A-share adaptation findings;
- Challenger status;
- recommended next action;
- source and artifact references.

The output is research evidence, not an automatic trading instruction.

## Safety and integrity rules

- Never fabricate sources, results, data, or reproduction success.
- Never use future information in historical tests.
- Never overwrite an original prediction or validation record.
- Never promote a method from a single impressive result.
- Keep discovery, reproduction, evaluation, and production promotion as separate stages.
