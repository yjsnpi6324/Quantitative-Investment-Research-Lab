"""Evaluation -> metrics -> health -> audit -> lifecycle pipeline."""
from src.evaluation.metrics import rolling_metrics
from src.evaluation.health_score import champion_health_score
from src.evaluation.self_audit_runner import run_self_audit
from src.evaluation.lifecycle import lifecycle_decision
def run_health_pipeline(production_id,predictions,evaluations,challenger_pass=False):
    metrics=rolling_metrics(evaluations)
    health=champion_health_score(metrics)
    audit=run_self_audit(predictions,evaluations)
    decision=lifecycle_decision(health,challenger_pass)
    if audit["severity"]=="P0": decision="INVESTIGATE"
    elif audit["severity"]=="P1" and decision=="HEALTHY": decision="WATCH"
    return {"production_id":production_id,"metrics":metrics,"health_score":health,"audit":audit,"lifecycle_decision":decision}
