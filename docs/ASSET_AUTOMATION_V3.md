# Asset Automation V3

## Asset Registry API

All material assets receive one stable Asset ID.

Ownership:

- GitHub: code, schema, reproducibility
- Notion: operational registry and decisions
- Dropbox: binary assets, reports, snapshots and large artifacts

## Lifecycle automation

States:

ACTIVE -> HISTORICAL -> ARCHIVED

ACTIVE -> DEPRECATED -> ARCHIVED

Rules:

- New production asset: ACTIVE
- Replaced version: HISTORICAL
- Invalid method or obsolete asset: DEPRECATED
- Retention completed: ARCHIVED

## Write pipeline

Generate -> Classify -> Deduplicate -> Register Asset ID -> Store -> Index -> Lifecycle Monitor

No system may silently overwrite an existing asset identity.
