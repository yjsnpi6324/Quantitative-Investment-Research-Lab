# A-share Research Agent

## Role

This is the main research architecture for the A-share AI / 基本盘 prediction system.

## Control loop

`Task → Skill → Agent`

The Research Agent coordinates:

1. Data acquisition and source quality checks
2. Market-state identification
3. Sector / theme classification
4. Candidate and factor analysis
5. Forecast generation
6. Confidence and uncertainty assessment
7. Outcome verification
8. Daily/weekly review
9. Method and source-weight updates

## Three-layer design

### Data layer

Track market data, sector data, ETF constituent relationships, macro/context data, news/event signals, and source provenance. Every important input should retain timestamp, source, freshness, and validation status.

### Research layer

Maintain methods as explicit, testable skills rather than opaque prompt fragments. Compare methods against historical and out-of-sample results. Prefer robust ensembles over a single indicator.

### Decision layer

Produce forecasts with direction, confidence, evidence, invalidation conditions, and post-event score. Avoid presenting uncertain forecasts as facts.

## Skill lifecycle

`Active → Testing → Deprecated → Archived`

A method can be promoted when it demonstrates repeatable improvement on the relevant task and survives out-of-sample validation. It should be downgraded when performance decays, data quality deteriorates, or a simpler/better method dominates.

## Daily operating rule

First determine whether the A-share market is trading. On non-trading days, do not fabricate routine market forecasts; perform review, validation, method maintenance, and necessary information updates instead.

## Research discipline

External finance, academic, and quantitative methods are auxiliary evidence. They can challenge the current framework, but adoption requires validation against the system's own historical and out-of-sample tests.
