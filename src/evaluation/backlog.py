"""Evaluation backlog inspection without mutating prediction history."""
from __future__ import annotations

from datetime import date

from src.evaluation.a_share_calendar import AShareTradingCalendar
from src.evaluation.immutable_ledger import verify_prediction
from src.evaluation.runner import expand_prediction_horizons, _evaluation_exists, _candidate_predictions


def scan_evaluation_backlog(as_of, registry, calendar=None):
    """Return matured, unclosed horizons plus explicit blockers."""
    calendar = calendar or AShareTradingCalendar()
    today = date.fromisoformat(as_of) if isinstance(as_of, str) else as_of
    rows = []

    for prediction in _candidate_predictions(registry, as_of):
        if not verify_prediction(prediction):
            rows.append(
                {
                    "prediction_id": prediction.get("prediction_id"),
                    "status": "BLOCKED_INVALID_HASH",
                }
            )
            continue

        for candidate in expand_prediction_horizons(prediction, calendar):
            if today < date.fromisoformat(candidate["target_date"]):
                continue
            if _evaluation_exists(registry, candidate):
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
