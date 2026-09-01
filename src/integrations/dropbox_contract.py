"""Canonical report-to-Dropbox asset contract and upload adapter."""
from src.assets.dedup_engine import build_dedup_result, content_hash

PATHS={
    "TASK-ASTOCK-DAILY":"03_Reports/Daily/Basic_Market",
    "TASK-AI-DAILY":"03_Reports/Daily/AI_Sector",
}

def target_path(task_id, filename):
    if task_id not in PATHS:
        raise ValueError("unknown task_id")
    return f"{PATHS[task_id]}/{filename}"

def prepare_asset(asset_id, task_id, filename, content:bytes, registry:list[dict]):
    asset={
        "asset_id":asset_id,
        "asset_type":"daily_report",
        "task_id":task_id,
        "canonical_path":target_path(task_id,filename),
        "content_hash":content_hash(content),
        "lifecycle_status":"ACTIVE",
    }
    return build_dedup_result(asset,registry)

def upload_asset(client, prepared_asset:dict, content:bytes):
    """Execute the final Dropbox write through an injected byte-preserving client.

    The client must expose upload(path:str, content:bytes) and return upload metadata.
    Upload is skipped when dedup marks the asset as duplicate.
    """
    if prepared_asset.get("duplicate") or prepared_asset.get("action") == "SKIP":
        return {"status":"SKIPPED_DUPLICATE","asset":prepared_asset}
    path=prepared_asset["canonical_path"]
    result=client.upload(path,content)
    return {
        "status":"UPLOADED",
        "asset":prepared_asset,
        "upload":result,
    }
