"""Canonical write contract for Notion prediction records."""
REQUIRED_FIELDS=("task_id","production_id","prediction_id","report_id","model_version","data_snapshot_id","generated_at")
def validate_record(record:dict):
    missing=[k for k in REQUIRED_FIELDS if record.get(k) in (None,"")]
    if missing: raise ValueError("missing Notion contract fields: "+",".join(missing))
    return True
def build_record(payload:dict, **extra):
    record={k:payload.get(k) for k in REQUIRED_FIELDS}
    record.update(extra)
    validate_record(record)
    return record
