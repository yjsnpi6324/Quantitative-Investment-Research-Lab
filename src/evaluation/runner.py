from __future__ import annotations

from datetime import date

from src.evaluation.auto_scoring import evaluate_due
from src.evaluation.immutable_ledger import verify_prediction
from src.evaluation.trading_calendar import HORIZON_STEPS, add_trading_days
from src.data_quality.gate import check
from src.evaluation.health_pipeline import run_health_pipeline

_HORIZON_FORECAST_KEYS = {
    "T+1": ("T+1", "t1_prediction", "future_1_prediction", "未来1日预测"),
    "T+3": ("T+3", "t3_prediction", "future_3_prediction", "未来3日预测"),
    "T+5": ("T+5", "t5_prediction", "future_5_prediction", "未来5日预测"),
}


def run_prediction(task_id, production_id, registry, market, ledger, policy):
    prod = registry.resolve_production(production_id)
    snapshot = market.get_data_snapshot(task_id, prod["as_of"])
    gate = check(
        snapshot,
        policy["production_gate"]["required_fields"],
        policy["production_gate"].get("max_age_days"),
    )
    if gate.status == "BLOCK":
        return {
            "status": "BLOCK",
            "reasons": gate.reasons,
            "task_id": task_id,
            "production_id": production_id,
        }
    return {
        "status": gate.status,
        "production": prod,
        "snapshot": snapshot,
        "task_id": task_id,
        "production_id": production_id,
    }


def _trading_date(prediction: dict) -> date:
    raw = prediction.get("trading_date") or prediction.get("Trading Date")
    if raw:
        return date.fromisoformat(str(raw)[:10])
    return date.fromisoformat(prediction["generated_at"][:10])


def _forecast_for_horizon(prediction: dict, label: str):
    forecasts = prediction.get("horizons")
    if isinstance(forecasts, dict) and label in forecasts:
        return forecasts[label]
    for key in _HORIZON_FORECAST_KEYS[label]:
        if key in prediction and prediction[key] not in (None, ""):
            return prediction[key]
    if prediction.get("horizon") in (
        label,
        HORIZON_STEPS[label],
        str(HORIZON_STEPS[label]),
    ):
        return prediction.get("prediction")
    return None


def expand_prediction_horizons(prediction: dict, calendar) -> list[dict]:
    """Expand one canonical row into per-horizon evaluation candidates."""
    base_date = _trading_date(prediction)
    out = []
    for label in HORIZON_STEPS:
        forecast = _forecast_for_horizon(prediction, label)
        if forecast in (None, ""):
            continue
        target = add_trading_days(base_date, label, calendar.is_trading_day)
        candidate = dict(prediction)
        candidate.update(
            {
                "horizon": label,
                "horizon_days": HORIZON_STEPS[label],
                "target_date": target.isoformat(),
                "prediction": forecast,
                "_source_prediction": prediction,
            }
        )
        out.append(candidate)
    return out


def _evaluation_exists(registry, candidate: dict) -> bool:
    if hasattr(registry, "has_evaluation"):
        return bool(
            registry.has_evaluation(
                candidate["prediction_id"], candidate["horizon"]
            )
        )
    if hasattr(registry, "list_evaluations"):
        evaluations = registry.list_evaluations(candidate["production_id"])
        return any(
            item.get("prediction_id") == candidate["prediction_id"]
            and str(item.get("horizon", "")).upper() == candidate["horizon"]
            for item in evaluations
        )
    return False


def run_due_evaluations(as_of, registry, market, calendar):
    """Close every matured horizon idempotently and append-only."""
    today = date.fromisoformat(as_of) if isinstance(as_of, str) else as_of
    out = []

    for prediction in registry.list_due_predictions(as_of):
        if not verify_prediction(prediction):
            out.append(
                {
                    "prediction_id": prediction.get("prediction_id"),
                    "status": "INVALID_HASH",
                }
            )
            continue

        candidates = expand_prediction_horizons(prediction, calendar)
        if not candidates:
            out.append(
                {
                    "prediction_id": prediction.get("prediction_id"),
                    "status": "NO_HORIZON_FORECASTS",
                }
            )
            continue

        for candidate in candidates:
            if today < date.fromisoformat(candidate["target_date"]):
                continue

            if _evaluation_exists(registry, candidate):
                out.append(
                    {
                        "prediction_id": candidate["prediction_id"],
                        "horizon": candidate["horizon"],
                        "status": "ALREADY_EVALUATED",
                    }
                )
                continue

            actual = market.get_actual(candidate)
            if not actual or actual.get("status") in {"MISSING", "UNVERIFIED"}:
                out.append(
                    {
                        "prediction_id": candidate["prediction_id"],
                        "horizon": candidate["horizon"],
                        "target_date": candidate["target_date"],
                        "status": "ACTUAL_UNAVAILABLE",
                    }
                )
                continue

            if actual.get("result") not in {"HIT", "PARTIAL", "MISS"}:
                out.append(
                    {
                        "prediction_id": candidate["prediction_id"],
                        "horizon": candidate["horizon"],
                        "target_date": candidate["target_date"],
                        "status": "ACTUAL_UNSCORED",
                    }
                )
                continue

            ev = evaluate_due(
                candidate,
                actual,
                actual["result"],
                actual.get("error_cause", ""),
            )
            registry.append_evaluation(ev)
            out.append(ev)

    return out


def run_model_self_check(production_id, registry, challenger_pass=False):
    predictions = registry.list_predictions(production_id)
    evaluations = registry.list_evaluations(production_id)
    result = run_health_pipeline(
        production_id, predictions, evaluations, challenger_pass
    )
    registry.update_health(production_id, result)
    if hasattr(registry, "append_audit"):
        registry.append_audit(result["audit"])
    return result
