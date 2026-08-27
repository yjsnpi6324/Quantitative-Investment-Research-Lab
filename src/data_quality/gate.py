"""Production data quality gate."""
from dataclasses import dataclass
@dataclass
class GateResult:
    status:str; reasons:list[str]
def check(snapshot:dict, required:list[str], max_age_days:int|None=None)->GateResult:
    reasons=[]
    for k in required:
        if snapshot.get(k) in (None,""): reasons.append(f"missing:{k}")
    if snapshot.get("date_mismatch"): reasons.append("date_mismatch")
    if snapshot.get("source_conflict"): reasons.append("source_conflict")
    if snapshot.get("anomaly"): reasons.append("anomaly")
    critical=any(x.startswith("missing:") for x in reasons) or "date_mismatch" in reasons
    return GateResult("BLOCK" if critical else "WARNING" if reasons else "PASS",reasons)
