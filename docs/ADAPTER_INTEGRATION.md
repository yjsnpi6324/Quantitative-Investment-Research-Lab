# Adapter Integration

The governance core is provider-neutral.

## Runtime chain
Task -> Production ID -> RegistryAdapter -> MarketDataAdapter -> Data Quality Gate -> locked Prediction -> LedgerAdapter.

At T+1/T+3/T+5:
RegistryAdapter -> due predictions -> Ledger hash verification -> MarketDataAdapter actuals -> Evaluation -> Registry update.

## Current implementation
The repository now contains concrete adapter boundaries for Notion, GitHub evidence ledger and market data. Provider credentials and account-bound API clients are intentionally injected at runtime rather than stored in the repository.

## Production rule
No adapter may overwrite a locked prediction. Registry writes for evaluations are append-only.
