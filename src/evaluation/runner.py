from __future__ import annotations
from datetime import date
from src.evaluation.auto_scoring import evaluate_due
from src.evaluation.immutable_ledger import verify_prediction
from src.evaluation.trading_calendar import is_due
from src.data_quality.gate import check
from src.evaluation.health_pipeline import run_health_pipeline

def run_prediction(task_id, production_id, registry, market, ledger, policy):
    prod=registry.resolve_production(production_id)
    snapshot=market.get_data_snapshot(task_id, prod["as_of"])
    gate=check(snapshot, policy["production_gate"]["required_fields"], policy["production_gate"].get("max_age_days"))
    if gate.status=="BLOCK": return {"status":"BLOCK","reasons":gate.reasons,"task_id":task_id,"production_id":production_id}
    return {"status":gate.status,"production":prod,"snapshot":snapshot,"task_id":task_id,"production_id":production_id}

def run_due_evaluations(as_of, registry, market, calendar):
    today=date.fromisoformat(as_of) if isinstance(as_of,str) else as_of
    out=[]
    for prediction in registry.list_due_predictions(as_of):
        if not verify_prediction(prediction): out.append({"prediction_id":prediction.get("prediction_id"),"status":"INVALID_HASH"}); continue
        generated=date.fromisoformat(prediction["generated_at"][:10]); horizon=int(prediction.get("horizon",1))
        if not is_due(generated,horizon,today,calendar.is_trading_day): out.append({"prediction_id":prediction["prediction_id"],"status":"NOT_DUE"}); continue
        actual=market.get_actual(prediction); ev=evaluate_due(prediction,actual,actual["result"],actual.get("error_cause",""))
        registry.append_evaluation(ev); out.append(ev)
    return out

def run_model_self_check(production_id, registry, challenger_pass=False):
    predictions=registry.list_predictions(production_id)
    evaluations=registry.list_evaluations(production_id)
    result=run_health_pipeline(production_id,predictions,evaluations,challenger_pass)
    registry.update_health(production_id,result)
    if hasattr(registry,"append_audit"): registry.append_audit(result["audit"])
    return result
