"""Deterministic evaluation runner with immutable-ledger verification."""
from src.evaluation.immutable_ledger import verify_prediction
SCORES={"HIT":1.0,"PARTIAL":0.5,"MISS":0.0}
def score(result:str)->float:
    key=result.upper()
    if key not in SCORES: raise ValueError(f"invalid result: {result}")
    return SCORES[key]
def evaluate_due(prediction:dict, actual:dict, result:str, error_cause:str="")->dict:
    if not verify_prediction(prediction): raise ValueError("INVALID_HASH: prediction ledger verification failed")
    return {"evaluation_id":f"EVAL-{prediction['prediction_id']}","prediction_id":prediction["prediction_id"],"production_id":prediction["production_id"],"model_version":prediction["model_version"],"data_snapshot_id":prediction["data_snapshot_id"],"actual":actual,"result":result.upper(),"score":score(result),"error_cause":error_cause}
