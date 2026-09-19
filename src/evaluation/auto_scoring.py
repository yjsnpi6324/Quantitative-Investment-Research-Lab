"""Deterministic evaluation runner with immutable-ledger verification."""
from __future__ import annotations

from datetime import datetime, timezone

from src.evaluation.immutable_ledger import verify_prediction
from src.evaluation.trading_calendar import normalize_horizon

SCORES = {"HIT": 1.0, "PARTIAL": 0.5, "MISS": 0.0}


def score(result: str) -> float:
    key = result.upper()
    if key not in SCORES:
        raise ValueError(f"invalid result: {result}")
    return SCORES[key]


def evaluate_due(prediction: dict, actual: dict, result: str, error_cause: str = "") -> dict:
    """Create one append-only horizon evaluation."""
    source_prediction = prediction.get("_source_prediction", prediction)
    if not verify_prediction(source_prediction):
        raise ValueError("INVALID_HASH: prediction ledger verification failed")

    label, _ = normalize_horizon(prediction["horizon"])
    suffix = label.replace("+", "")
    return {
        "evaluation_id": f"EVAL-{prediction['prediction_id']}-{suffix}",
        "prediction_id": prediction["prediction_id"],
        "production_id": prediction["production_id"],
        "model_version": prediction["model_version"],
        "data_snapshot_id": prediction["data_snapshot_id"],
        "horizon": label,
        "target_date": prediction["target_date"],
        "prediction": prediction["prediction"],
        "actual": actual,
        "result": result.upper(),
        "score": score(result),
        "error_cause": error_cause,
        "evaluated_at": datetime.now(timezone.utc).isoformat(),
    }
