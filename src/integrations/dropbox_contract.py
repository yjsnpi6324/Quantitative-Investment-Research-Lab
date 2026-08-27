"""Canonical report-to-Dropbox asset contract."""
from src.assets.dedup_engine import build_dedup_result, content_hash
PATHS={"TASK-ASTOCK-DAILY":"03_Reports/Daily/Basic_Market","TASK-AI-DAILY":"03_Reports/Daily/AI_Sector"}
def target_path(task_id, filename):
    if task_id not in PATHS: raise ValueError("unknown task_id")
    return f"{PATHS[task_id]}/{filename}"
def prepare_asset(asset_id, task_id, filename, content:bytes, registry:list[dict]):
    asset={"asset_id":asset_id,"asset_type":"daily_report","task_id":task_id,"canonical_path":target_path(task_id,filename),"content_hash":content_hash(content),"lifecycle_status":"ACTIVE"}
    return build_dedup_result(asset,registry)
