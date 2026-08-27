"""Deterministic production self-audit."""
from src.evaluation.immutable_ledger import verify_prediction
def run_self_audit(predictions,evaluations):
    findings=[]
    ids=set()
    for p in predictions:
        pid=p.get("prediction_id")
        if not pid or pid in ids: findings.append({"severity":"P0","issue":"duplicate_or_missing_prediction_id","prediction_id":pid})
        ids.add(pid)
        if not verify_prediction(p): findings.append({"severity":"P0","issue":"invalid_hash","prediction_id":pid})
        if int(p.get("horizon",1)) not in (1,3,5): findings.append({"severity":"P0","issue":"invalid_horizon","prediction_id":pid})
    evaluated={e.get("prediction_id") for e in evaluations}
    for p in predictions:
        if p.get("due") and p.get("prediction_id") not in evaluated: findings.append({"severity":"P2","issue":"missing_due_evaluation","prediction_id":p.get("prediction_id")})
    severity=max((f["severity"] for f in findings),key=lambda x:int(x[1]),default="P3")
    return {"severity":severity,"findings":findings,"prediction_count":len(predictions),"evaluation_count":len(evaluations)}
