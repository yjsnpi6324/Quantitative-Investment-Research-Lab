"""Canonical production write orchestration for task outputs.

External sinks are injected so the production runner can be tested without coupling
domain logic to a specific Notion or Dropbox SDK.
"""
from src.integrations.notion_contract import build_record
from src.integrations.dropbox_contract import prepare_asset, upload_asset

def persist_prediction(payload:dict, extra:dict, notion_sink):
    """Validate and write one canonical Prediction Registry record."""
    record=build_record(payload, **extra)
    result=notion_sink.write_prediction(record)
    return {"status":"NOTION_WRITTEN","record":record,"result":result}

def persist_report(asset_id:str, task_id:str, filename:str, content:bytes,
                   asset_registry:list[dict], dropbox_client):
    """Prepare, deduplicate and upload one canonical report asset."""
    prepared=prepare_asset(asset_id,task_id,filename,content,asset_registry)
    return upload_asset(dropbox_client,prepared,content)

def persist_production_bundle(payload:dict, prediction_extra:dict, notion_sink,
                              asset_id:str, filename:str, report_content:bytes,
                              asset_registry:list[dict], dropbox_client):
    """Write machine prediction first, then the human-readable report asset.

    Returns explicit per-sink outcomes so callers can detect partial failure.
    """
    notion=persist_prediction(payload,prediction_extra,notion_sink)
    dropbox=persist_report(
        asset_id,payload["task_id"],filename,report_content,
        asset_registry,dropbox_client
    )
    return {"notion":notion,"dropbox":dropbox}
