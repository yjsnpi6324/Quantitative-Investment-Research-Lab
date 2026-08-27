"""Production data quality gate."""
from dataclasses import dataclass
from datetime import datetime, timezone
@dataclass
class GateResult: status:str; reasons:list[str]
def _parse(value):
    if isinstance(value,datetime): return value.astimezone(timezone.utc)
    if isinstance(value,str): return datetime.fromisoformat(value.replace("Z","+00:00")).astimezone(timezone.utc)
    return None
def check(snapshot,required,max_age_days=None,now=None):
    reasons=[]
    for k in required:
        if snapshot.get(k) in (None,""): reasons.append(f"missing:{k}")
    for k in ("date_mismatch","source_conflict","anomaly"):
        if snapshot.get(k): reasons.append(k)
    if max_age_days is not None:
        ts=_parse(snapshot.get("snapshot_at") or snapshot.get("as_of"))
        if ts is None: reasons.append("missing:snapshot_timestamp")
        elif ((now or datetime.now(timezone.utc)).astimezone(timezone.utc)-ts).total_seconds()>max_age_days*86400: reasons.append("stale_data")
    critical=any(x.startswith("missing:") for x in reasons) or "date_mismatch" in reasons
    return GateResult("BLOCK" if critical else "WARNING" if reasons else "PASS",reasons)
