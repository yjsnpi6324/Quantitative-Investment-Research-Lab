"""Evaluation backlog inspection without mutating prediction history."""
from __future__ import annotations

from datetime import date

from src.evaluation.a_share_calendar import AShareTradingCalendar
from src.evaluation.runner import _prepare_prediction, _evaluation_exists, _candidate_predictions, _outcome


def scan_evaluation_backlog(as_of, registry, calendar=None):
    """Return matured, unclosed horizons plus explicit blockers."""
    calendar = calendar or AShareTradingCalendar()
    today = date.fromisoformat(as_of) if isinstance(as_of, str) else as_of
    rows = []

    for prediction in _candidate_predictions(registry, as_of):
        candidates, blocker = _prepare_prediction(prediction, calendar)
        if blocker:
            if blocker["status"] == "INVALID_HASH":
                blocker["status"] = "BLOCKED_INVALID_HASH"
            rows.append(blocker)
        for candidate in candidates:
            if today < date.fromisoformat(candidate["target_date"]):
                continue
            try:
                if _evaluation_exists(registry, candidate):
                    continue
            except Exception as exc:
                rows.append(_outcome(candidate, "EVALUATION_LOOKUP_FAILED", error_type=type(exc).__name__))
                continue
            rows.append(
                {
                    "prediction_id": candidate["prediction_id"],
                    "production_id": candidate["production_id"],
                    "horizon": candidate["horizon"],
                    "target_date": candidate["target_date"],
                    "status": "DUE_UNCLOSED",
                }
            )
    return rows
