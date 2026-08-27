"""Canonical Asset Registry interface.

Keeps one Asset ID across GitHub, Notion and Dropbox.
"""
from dataclasses import dataclass
from datetime import datetime, timezone

@dataclass
class AssetRecord:
    asset_id: str
    asset_type: str
    canonical_path: str
    owner_system: str
    content_hash: str
    lifecycle_status: str = "ACTIVE"

class AssetRegistry:
    def __init__(self):
        self.records = {}

    def register(self, record: AssetRecord):
        if record.asset_id in self.records:
            raise ValueError("asset_id already exists")
        self.records[record.asset_id] = record
        return record

    def get(self, asset_id):
        return self.records.get(asset_id)
