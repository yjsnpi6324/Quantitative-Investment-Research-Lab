"""Asset Lifecycle Manager with guarded transitions."""
from src.assets.archive_policy import can_transition
VALID_STATES={"ACTIVE","HISTORICAL","DEPRECATED","ARCHIVED"}
def transition(asset,new_state):
    current=asset.get("lifecycle_status","ACTIVE")
    if new_state not in VALID_STATES: raise ValueError("invalid lifecycle state")
    if not can_transition(current,new_state): raise ValueError(f"illegal lifecycle transition: {current}->{new_state}")
    updated=dict(asset); updated["lifecycle_status"]=new_state; return updated
def recommend_state(asset):
    if asset.get("deprecated"): return "DEPRECATED"
    if asset.get("superseded"): return "HISTORICAL"
    if asset.get("archived"): return "ARCHIVED"
    return asset.get("lifecycle_status","ACTIVE")
