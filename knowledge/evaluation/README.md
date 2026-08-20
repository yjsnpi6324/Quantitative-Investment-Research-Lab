# Agent Evaluation

Agent evaluation should measure the system, not just the underlying model.

## Evaluation layers

- task success rate
- factual correctness
- tool-selection accuracy
- tool execution success
- planning quality
- recovery from failure
- instruction adherence
- latency
- token and monetary cost
- reproducibility

## Benchmark rule

External benchmarks are useful for comparison but are not sufficient for production decisions. Maintain a small private evaluation set representing the actual workflows the system must perform.

## Required experiment record

Every meaningful benchmark should record:

- model/version
- prompt or policy version
- tools available
- context sources
- dataset/evaluation set
- success criteria
- sample size
- results
- known failure modes
- date
