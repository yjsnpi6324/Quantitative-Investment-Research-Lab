"""Market-data adapter boundary. Provider-specific implementations belong outside governance logic."""
from __future__ import annotations

from src.evaluation.a_share_calendar import AShareTradingCalendar


class ProviderMarketDataAdapter:
    def __init__(self, provider, calendar=None):
        self.provider = provider
        self.calendar = calendar or AShareTradingCalendar()

    def get_actual(self, prediction):
        return self.provider.actual_for_prediction(prediction)

    def get_data_snapshot(self, task_id, as_of):
        return self.provider.snapshot(task_id, as_of)

    def target_date(self, trading_date, horizon):
        return self.calendar.add_trading_days(trading_date, horizon)
