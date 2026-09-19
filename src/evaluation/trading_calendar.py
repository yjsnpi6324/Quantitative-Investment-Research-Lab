"""Trading-day horizon scheduling utilities."""
from __future__ import annotations

from datetime import date, timedelta

HORIZON_STEPS = {"T+1": 1, "T+3": 3, "T+5": 5}


def normalize_horizon(horizon: str | int) -> tuple[str, int]:
    """Return canonical horizon label and trading-day step count."""
    if isinstance(horizon, int):
        if horizon not in HORIZON_STEPS.values():
            raise ValueError(f"unsupported horizon: {horizon}")
        return f"T+{horizon}", horizon

    label = str(horizon).strip().upper()
    if label in HORIZON_STEPS:
        return label, HORIZON_STEPS[label]
    if label.isdigit():
        return normalize_horizon(int(label))
    raise ValueError(f"unsupported horizon: {horizon}")


def add_trading_days(start: date, horizon: str | int, is_trading_day) -> date:
    """Advance strictly by exchange trading days, excluding the start date."""
    _, steps = normalize_horizon(horizon)
    d = start
    seen = 0
    while seen < steps:
        d += timedelta(days=1)
        if is_trading_day(d):
            seen += 1
    return d


def horizon_targets(start: date, is_trading_day) -> dict[str, date]:
    """Build canonical T+1/T+3/T+5 target dates from one trading date."""
    return {
        label: add_trading_days(start, label, is_trading_day)
        for label in HORIZON_STEPS
    }


def is_due(trading_date: date, horizon: str | int, as_of: date, is_trading_day) -> bool:
    """A horizon is due only when its exchange trading target date has arrived."""
    return as_of >= add_trading_days(trading_date, horizon, is_trading_day)
