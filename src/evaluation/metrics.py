"""Rolling evaluation metrics grouped by production and horizon."""
from src.evaluation.auto_scoring import SCORES


# Persisted ledger closure and evaluation_record.schema.json verification state.
# "partial" is a workflow state, not the scored Result "PARTIAL".
CLOSED_STATUSES = frozenset({"FORMAL_CLOSED", "verified"})


def has_closed_status(row):
    status = row.get("status")
    # The legacy Python evaluator emits no status field.
    return status is None or (isinstance(status, str) and
                              (status == "" or status in CLOSED_STATUSES))


def is_scored_evaluation(row):
    result = row.get("result")
    return (has_closed_status(row) and bool(row.get("evaluation_id"))
            and isinstance(result, str) and result in SCORES
            and row.get("score") == SCORES[result])


def rolling_metrics(evaluations):
    evaluations = [row for row in evaluations if is_scored_evaluation(row)]
    n=len(evaluations)
    if not n: return {"sample_size":0,"accuracy":0.0,"stability":0.0,"robustness":0.0,"data_quality":0.0,"explainability":0.0}
    scores=[float(e.get("score",0.0)) for e in evaluations]
    accuracy=sum(scores)/n
    stability=max(0.0,1.0-(max(scores)-min(scores))) if n>1 else accuracy
    return {"sample_size":n,"accuracy":accuracy,"stability":stability,"robustness":accuracy,"data_quality":sum(1 for e in evaluations if not e.get("data_quality_issue"))/n,"explainability":sum(1 for e in evaluations if e.get("error_cause") is not None)/n}
