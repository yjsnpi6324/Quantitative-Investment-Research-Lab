# Agent Memory

## Memory layers

1. **Working memory** — the current context and immediate task state.
2. **Session memory** — information useful during one workflow or conversation.
3. **Long-term memory** — durable user preferences, project decisions, and validated knowledge.
4. **External memory** — searchable documents, databases, Git repositories, and other stores.

## Design rule

Memory should be selective. Storing everything creates retrieval noise, stale information, and unnecessary context cost. A useful memory system needs retention criteria, provenance, freshness, retrieval strategy, and a way to correct or invalidate old records.

## Evaluation dimensions

- retrieval precision
- retrieval recall
- freshness
- conflict handling
- provenance
- latency
- token/cost overhead
- forgetting and deletion behavior
