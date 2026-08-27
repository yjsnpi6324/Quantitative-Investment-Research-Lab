"""Asset Dedup Engine.

Provides checksum based duplicate detection while preserving Asset ID history.
"""
from __future__ import annotations
import hashlib


def content_hash(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def find_duplicate(asset_hash: str, registry: list[dict]) -> dict | None:
    for asset in registry:
        if asset.get("content_hash") == asset_hash:
            return asset
    return None


def build_dedup_result(asset: dict, registry: list[dict]) -> dict:
    existing = find_duplicate(asset["content_hash"], registry)
    if existing:
        return {"duplicate": True, "canonical_asset_id": existing["asset_id"], "asset": asset}
    return {"duplicate": False, "canonical_asset_id": asset["asset_id"], "asset": asset}
