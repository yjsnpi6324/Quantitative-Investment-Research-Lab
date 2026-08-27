"""Automatic asset lifecycle transition rules."""

TRANSITIONS = {
    "ACTIVE": {"HISTORICAL", "DEPRECATED"},
    "HISTORICAL": {"ARCHIVED"},
    "DEPRECATED": {"ARCHIVED"},
    "ARCHIVED": set(),
}


def can_transition(current: str, target: str) -> bool:
    return target in TRANSITIONS.get(current, set())


def next_state(asset: dict, event: str) -> str:
    current = asset.get("lifecycle_status", "ACTIVE")
    rules = {
        "superseded": "HISTORICAL",
        "invalidated": "DEPRECATED",
        "retention_expired": "ARCHIVED",
    }
    target = rules.get(event, current)
    return target if can_transition(current, target) else current
