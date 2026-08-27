"""Market-data adapter boundary. Provider-specific implementations belong outside governance logic."""
from __future__ import annotations

class ProviderMarketDataAdapter:
    def __init__(self, provider, calendar): self.provider,self.calendar=provider,calendar
    def get_actual(self, prediction):
        return self.provider.actual_for_prediction(prediction)
    def get_data_snapshot(self, task_id, as_of):
        return self.provider.snapshot(task_id, as_of)
    def is_due(self, generated_date, horizon):
        return self.calendar.add_trading_days(generated_date,horizon)
