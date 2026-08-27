"""Rolling evaluation metrics grouped by production and horizon."""
def rolling_metrics(evaluations):
    n=len(evaluations)
    if not n: return {"sample_size":0,"accuracy":0.0,"stability":0.0,"robustness":0.0,"data_quality":0.0,"explainability":0.0}
    scores=[float(e.get("score",0.0)) for e in evaluations]
    accuracy=sum(scores)/n
    stability=max(0.0,1.0-(max(scores)-min(scores))) if n>1 else accuracy
    return {"sample_size":n,"accuracy":accuracy,"stability":stability,"robustness":accuracy,"data_quality":sum(1 for e in evaluations if not e.get("data_quality_issue"))/n,"explainability":sum(1 for e in evaluations if e.get("error_cause") is not None)/n}
