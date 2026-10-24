from __future__ import annotations

from datetime import date
from collections import Counter

from src.evaluation.a_share_calendar import AShareTradingCalendar
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

    canonical = prediction.get("prediction")
    if isinstance(canonical, dict) and label in canonical:
        return canonical[label]

    for key in _HORIZON_FORECAST_KEYS[label]:
        if key in prediction and prediction[key] not in (None, ""):
            return prediction[key]

    if prediction.get("horizon") in (
        label,
        HORIZON_STEPS[label],
        str(HORIZON_STEPS[label]),
    ):
        return canonical
    return None


def expand_prediction_horizons(prediction: dict, calendar) -> list[dict]:
    """Expand one canonical row into per-horizon evaluation candidates."""
    base_date = _trading_date(prediction)
    out = []
    for label in HORIZON_STEPS:
        forecast = _forecast_for_horizon(prediction, label)
        if forecast in (None, ""):
            continue
        targets = prediction.get("target_dates", {})
        short = label.lower().replace("+", "")
        saved = [targets[k] for k in (label, short) if k in targets]
        saved += [prediction[k] for k in (f"{short}_target_date", f"{label} Target Date") if k in prediction]
        if prediction.get("horizon") in (label, HORIZON_STEPS[label], str(HORIZON_STEPS[label])) and "target_date" in prediction:
            saved.append(prediction["target_date"])
        if saved:
            if len(set(saved)) != 1:
                raise ValueError("conflicting persisted target dates")
            target = date.fromisoformat(saved[0])
        else:
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
    raise RuntimeError("registry cannot check evaluation identity")


def _candidate_predictions(registry, as_of):
    if hasattr(registry, "list_evaluation_candidates"):
        return registry.list_evaluation_candidates(as_of)
    return registry.list_due_predictions(as_of)


def _outcome(record, status, **details):
    return {**{key: record.get(key) for key in
               ("prediction_id", "report_id", "task_id", "production_id", "horizon", "target_date")},
            "status": status, **details}


def _prepare_prediction(prediction, calendar):
    # Missing-source markers are observations, never fabricated predictions.
    if prediction.get("status") == "SOURCE_FINAL_NOT_FOUND":
        return [], _outcome(prediction, "SOURCE_FINAL_NOT_FOUND")
    if prediction.get("hash_schema_version"):
        return [], _outcome(prediction, "UNSUPPORTED_HASH_SCHEMA")
    try:
        if not verify_prediction(prediction):
            return [], _outcome(prediction, "INVALID_HASH")
        candidates = expand_prediction_horizons(prediction, calendar)
    except (ValueError, TypeError, KeyError, AttributeError) as exc:
        return [], _outcome(prediction, "INVALID_PREDICTION", error_type=type(exc).__name__)
    return candidates, None if candidates else _outcome(prediction, "NO_HORIZON_FORECASTS")


def run_due_evaluations(as_of, registry, market, calendar=None):
    """Return closed evaluations and separate skip diagnostics; append only closures."""
    calendar = calendar or getattr(market, "calendar", None) or AShareTradingCalendar()
    today = date.fromisoformat(as_of) if isinstance(as_of, str) else as_of
    out = []
    seen = {}
    for prediction in _candidate_predictions(registry, as_of):
        candidates, blocker = _prepare_prediction(prediction, calendar)
        if blocker:
            out.append(blocker)
        for candidate in candidates:
            if today < date.fromisoformat(candidate["target_date"]):
                out.append(_outcome(candidate, "NOT_DUE"))
                continue
            key = (candidate["prediction_id"], candidate["horizon"])
            stage = "EVALUATION_LOOKUP_FAILED"
            try:
                if key in seen or _evaluation_exists(registry, candidate):
                    out.append(_outcome(candidate, seen.get(key, "ALREADY_EVALUATED")))
                    continue
                stage = "ACTUAL_LOOKUP_FAILED"
                actual = market.get_actual(candidate)
                if not actual or actual.get("status") in {"MISSING", "UNVERIFIED"}:
                    out.append(_outcome(candidate, "ACTUAL_UNAVAILABLE"))
                    continue
                if not isinstance(actual.get("result"), str) or actual["result"] not in {"HIT", "PARTIAL", "MISS"}:
                    out.append(_outcome(candidate, "ACTUAL_UNSCORED"))
                    continue
                stage = "EVALUATION_FAILED"
                ev = evaluate_due(candidate, actual, actual["result"], actual.get("error_cause", ""))
                stage = "APPEND_OUTCOME_UNKNOWN"
                # Do not retry a write whose outcome may be uncertain in this run.
                seen[key] = "APPEND_OUTCOME_UNKNOWN"
                registry.append_evaluation(ev)
                seen[key] = "ALREADY_EVALUATED"
                out.append(ev)
            except Exception as exc:
                out.append(_outcome(candidate, stage, error_type=type(exc).__name__))
    return out


def summarize_evaluations(outcomes):
    """Keep production lines and record/window diagnostics out of scored counts."""
    from src.evaluation.metrics import is_scored_evaluation
    groups = {}
    for row in outcomes:
        group = groups.setdefault(row.get("production_id"), {
            "evaluated": 0, "results": Counter(), "window_statuses": Counter(),
            "record_statuses": Counter(),
        })
        if is_scored_evaluation(row):
            group["evaluated"] += 1
            group["results"][row["result"]] += 1
        else:
            scope = "window_statuses" if row.get("horizon") else "record_statuses"
            group[scope][row.get("status", "UNCLASSIFIED")] += 1
    return groups


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
