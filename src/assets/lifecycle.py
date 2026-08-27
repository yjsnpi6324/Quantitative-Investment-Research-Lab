"""Asset Lifecycle Manager.

Controls ACTIVE/HISTORICAL/DEPRECATED/ARCHIVED transitions.
"""
from __future__ import annotations

VALID_STATES = {"ACTIVE", "HISTORICAL", "DEPRECATED", "ARCHIVED"}


def transition(asset: dict, new_state: str) -> dict:
    if new_state not in VALID_STATES:
        raise ValueError("invalid lifecycle state")
    updated = dict(asset)
    updated["lifecycle_status"] = new_state
    return updated


def recommend_state(asset: dict) -> str:
    if asset.get("deprecated"):
        return "DEPRECATED"
    if asset.get("superseded"):
        return "HISTORICAL"
    if asset.get("archived"):
        return "ARCHIVED"
    return "ACTIVE"
