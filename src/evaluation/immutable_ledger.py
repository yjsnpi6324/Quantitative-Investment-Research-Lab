"""Immutable prediction ledger primitives."""
from __future__ import annotations
import hashlib, json
from datetime import datetime, timezone

REQUIRED_FIELDS=("prediction_id","task_id","production_id","model_version","generated_at","data_snapshot_id","prediction")

def canonical_payload(record: dict) -> str:
    missing=[k for k in REQUIRED_FIELDS if k not in record]
    if missing: raise ValueError(f"missing fields: {missing}")
    return json.dumps({k:record[k] for k in REQUIRED_FIELDS},ensure_ascii=False,sort_keys=True,separators=(",",":"))

def prediction_hash(record: dict) -> str:
    return hashlib.sha256(canonical_payload(record).encode("utf-8")).hexdigest()

def lock_prediction(record: dict) -> dict:
    if record.get("prediction_hash"): raise ValueError("prediction already locked")
    locked=dict(record); locked["prediction_hash"]=prediction_hash(record); locked["locked_at"]=datetime.now(timezone.utc).isoformat()
    return locked

def verify_prediction(record: dict) -> bool:
    return bool(record.get("prediction_hash")) and record["prediction_hash"]==prediction_hash(record)
