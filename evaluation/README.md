# Evaluation

Evaluation is the measurement layer between experiments and durable method decisions.

## Purpose

Record whether a method, skill, model, data source, or workflow actually improves the target workload. Evaluation should separate in-sample evidence from out-of-sample evidence and preserve enough provenance to reproduce the conclusion.

## Evaluation loop

`Experiment → Result → Score → Comparison → Decision`

## Minimum record

Every meaningful evaluation should identify:

- target task
- method or system version
- dataset / time window
- baseline
- metrics
- in-sample vs out-of-sample status
- result
- limitations / failure cases
- decision

## Decision vocabulary

- **Promote** — evidence supports wider use.
- **Keep Testing** — promising but insufficient evidence.
- **Downgrade** — performance or reliability has weakened.
- **Retire** — consistently inferior, obsolete, fragile, or no longer useful.

Evaluation results should feed back into `research/method-registry.md` when they materially change a method's status.