"""Mainland A-share trading calendar.

The 2026 closures below are sourced from the official SSE/SZSE holiday schedules.
Weekends are always closed; unlike the civil calendar, make-up weekends are not
trading days unless an exchange explicitly announces otherwise.
"""
from __future__ import annotations

from datetime import date
from src.evaluation.trading_calendar import add_trading_days

OFFICIAL_SOURCES = (
    "https://www.sse.com.cn/disclosure/dealinstruc/closed/",
    "https://www.szse.cn/English/services/trading/calendar/",
)

MARKET_CLOSURES_2026 = frozenset(
    {
        date(2026, 1, 1), date(2026, 1, 2),
        date(2026, 2, 16), date(2026, 2, 17), date(2026, 2, 18),
        date(2026, 2, 19), date(2026, 2, 20), date(2026, 2, 23),
        date(2026, 4, 6),
        date(2026, 5, 1), date(2026, 5, 4), date(2026, 5, 5),
        date(2026, 6, 19),
        date(2026, 9, 25),
        date(2026, 10, 1), date(2026, 10, 2), date(2026, 10, 5),
        date(2026, 10, 6), date(2026, 10, 7),
    }
)


class AShareTradingCalendar:
    """Strict exchange calendar for supported A-share years."""

    def __init__(self, closures_by_year=None):
        self._closures = {2026: MARKET_CLOSURES_2026}
        if closures_by_year:
            self._closures.update(
                {year: frozenset(days) for year, days in closures_by_year.items()}
            )

    def is_trading_day(self, day: date) -> bool:
        if day.weekday() >= 5:
            return False
        if day.year not in self._closures:
            raise ValueError(
                f"UNSUPPORTED_TRADING_CALENDAR_YEAR:{day.year}; "
                "load an exchange-verified closure set before scheduling horizons"
            )
        return day not in self._closures[day.year]

    def add_trading_days(self, start: date, horizon):
        return add_trading_days(start, horizon, self.is_trading_day)
