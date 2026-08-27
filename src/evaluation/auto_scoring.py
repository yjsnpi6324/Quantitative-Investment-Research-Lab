"""Deterministic evaluation runner. Adapters supply due predictions and actual outcomes."""
SCORES={"HIT":1.0,"PARTIAL":0.5,"MISS":0.0}
def score(result:str)->float:
    return SCORES[result.upper()]
def evaluate_due(prediction:dict, actual:dict, result:str, error_cause:str="")->dict:
    if not prediction.get("prediction_hash"): raise ValueError("prediction must be locked")
    if prediction.get("prediction_hash") is None: raise ValueError("missing immutable ledger")
    return {"evaluation_id":f"EVAL-{prediction['prediction_id']}","prediction_id":prediction["prediction_id"],"production_id":prediction["production_id"],"model_version":prediction["model_version"],"actual":actual,"result":result.upper(),"score":score(result),"error_cause":error_cause}
