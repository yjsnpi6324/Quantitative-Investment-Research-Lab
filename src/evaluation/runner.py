from __future__ import annotations
from src.evaluation.auto_scoring import evaluate_due
from src.evaluation.immutable_ledger import verify_prediction
from src.data_quality.gate import check

def run_prediction(task_id, production_id, registry, market, ledger, policy):
    prod=registry.resolve_production(production_id)
    snapshot=market.get_data_snapshot(task_id, prod["as_of"])
    gate=check(snapshot, policy["production_gate"]["required_fields"])
    if gate.status=="BLOCK": return {"status":"BLOCK","reasons":gate.reasons}
    return {"status":gate.status,"production":prod,"snapshot":snapshot}

def run_due_evaluations(as_of, registry, market):
    out=[]
    for prediction in registry.list_due_predictions(as_of):
        if not verify_prediction(prediction):
            out.append({"prediction_id":prediction.get("prediction_id"),"status":"INVALID_HASH"}); continue
        actual=market.get_actual(prediction)
        result=actual["result"]
        ev=evaluate_due(prediction,actual,result,actual.get("error_cause",""))
        registry.append_evaluation(ev); out.append(ev)
    return out
