"""Canonical Task Payload contract for production tasks."""
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
@dataclass
class TaskPayload:
    task_id:str
    production_id:str
    task_type:str
    prediction_id:str
    generated_at:str
    trading_date:str
    data_snapshot_id:str
    model_version:str
    report_id:str
    def to_dict(self): return asdict(self)
def build_payload(**kwargs):
    kwargs.setdefault("generated_at",datetime.now(timezone.utc).isoformat())
    return TaskPayload(**kwargs)
