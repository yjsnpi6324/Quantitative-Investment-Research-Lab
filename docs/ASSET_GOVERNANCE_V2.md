# Asset Governance v2

## Asset Dedup Engine

All governed assets should calculate a checksum. Identical content reuses the canonical Asset ID and records duplicate relationships instead of creating competing copies.

## Asset Lifecycle Manager

Lifecycle states:

- ACTIVE: current production asset
- HISTORICAL: replaced but useful for evidence
- DEPRECATED: no longer recommended
- ARCHIVED: retained only for long-term storage

## Pipeline

Generate → Classify → Deduplicate → Lifecycle Decision → Store → Register

Storage ownership remains:

- GitHub: code and reproducibility
- Notion: registry metadata and decisions
- Dropbox: binary assets, reports, snapshots and large artifacts
