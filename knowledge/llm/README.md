# LLM Foundations for Agents

## Scope

Model capabilities that materially affect agent behavior:

- reasoning and instruction following
- tool calling
- structured output
- long-context processing
- multimodal input/output
- latency and cost trade-offs
- context-window management
- model routing and fallback

## Engineering principle

Do not evaluate an LLM only as a chatbot. Evaluate it inside the complete agent loop, including context construction, tools, state, verification, latency, cost, and failure recovery.

## Data policy

Keep model-specific claims versioned and dated. Model behavior, pricing, context limits, and tool APIs can change quickly and must not be treated as permanent facts.
