"""Canonical production write orchestration for task outputs.

External sinks are injected so the production runner can be tested without coupling
domain logic to a specific Notion or Dropbox SDK.
"""
from src.evaluation.immutable_ledger import lock_prediction
from src.integrations.notion_contract import build_record
from src.integrations.dropbox_contract import prepare_asset, upload_asset

_HORIZON_KEYS = {
    "T+1": ("T+1", "t1_prediction", "future_1_prediction", "未来1日预测"),
    "T+3": ("T+3", "t3_prediction", "future_3_prediction", "未来3日预测"),
    "T+5": ("T+5", "t5_prediction", "future_5_prediction", "未来5日预测"),
}


def _canonical_forecast(record: dict):
    if record.get("prediction") not in (None, ""):
        return record["prediction"]

    forecasts = {}
    for label, aliases in _HORIZON_KEYS.items():
        for key in aliases:
            if record.get(key) not in (None, ""):
                forecasts[label] = record[key]
                break

    if not forecasts:
        raise ValueError(
            "missing canonical forecast payload; provide prediction or horizon forecast fields"
        )
    return forecasts


def persist_prediction(payload: dict, extra: dict, notion_sink):
    """Validate, lock and write one canonical Prediction Registry record."""
    record = build_record(payload, **extra)
    record["prediction"] = _canonical_forecast(record)
    locked = lock_prediction(record)
    result = notion_sink.write_prediction(locked)
    return {"status": "NOTION_WRITTEN", "record": locked, "result": result}


def persist_report(
    asset_id: str,
    task_id: str,
    filename: str,
    content: bytes,
    asset_registry: list[dict],
    dropbox_client,
):
    """Prepare, deduplicate and upload one canonical report asset."""
    prepared = prepare_asset(
        asset_id, task_id, filename, content, asset_registry
    )
    return upload_asset(dropbox_client, prepared, content)


def persist_production_bundle(
    payload: dict,
    prediction_extra: dict,
    notion_sink,
    asset_id: str,
    filename: str,
    report_content: bytes,
    asset_registry: list[dict],
    dropbox_client,
):
    """Write machine prediction first, then the human-readable report asset."""
    notion = persist_prediction(payload, prediction_extra, notion_sink)
    dropbox = persist_report(
        asset_id,
        payload["task_id"],
        filename,
        report_content,
        asset_registry,
        dropbox_client,
    )
    return {"notion": notion, "dropbox": dropbox}
