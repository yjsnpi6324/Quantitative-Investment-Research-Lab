# Dropbox Asset Index Contract

## Purpose

Dropbox is the project's **Source of Record for large files, binary assets, immutable data snapshots and long-term archive packages**.

This contract defines how Dropbox assets are named, indexed, linked and governed without creating competing copies in Notion or GitHub.

## 1. Ownership boundary

Dropbox owns the asset bytes when an artifact is unsuitable for GitHub or Notion, including:

- PDF reports and formal export packages;
- raw datasets and large data extracts;
- point-in-time data snapshots;
- model files, weights and large binaries;
- workflow files and large generated outputs;
- large experiment artifacts;
- historical archive packages.

Notion owns the human-readable operational record and asset registry metadata.

GitHub owns the code, generation procedure, schema, reproducibility instructions and versioned research specification.

Task owns scheduling and execution timing.

GPT coordinates creation, verification and cross-system linking.

## 2. Canonical directory structure

```
/A股量化研究系统
├── 00_System
│   ├── Architecture
│   └── Asset_Index
├── 01_Raw_Data
│   ├── China
│   ├── Global
│   └── Snapshots
├── 02_Research_Artifacts
│   ├── Basic_Market
│   ├── AI_Sector
│   └── Quant_Methods
├── 03_Reports
│   ├── Daily
│   │   ├── Basic_Market
│   │   └── AI_Sector
│   ├── Monthly
│   ├── Quarterly
│   └── Semiannual
├── 04_Models_and_Large_Assets
│   ├── Model_Files
│   ├── Workflows
│   └── Large_Outputs
└── 99_Archive
    ├── Historical
    └── Deprecated
```

## 3. Asset identity

Every governed asset should have:

- `asset_id` — stable identifier;
- `asset_type`;
- `canonical_path`;
- `created_at`;
- `source_run_or_task`;
- `related_prediction_or_research_id`;
- `method/model version` where applicable;
- `integrity marker` such as checksum where practical;
- `lifecycle_status`: ACTIVE / HISTORICAL / DEPRECATED / ARCHIVED;
- `owner_system`: Dropbox.

A rename must not create a new asset identity unless the content changes materially.

## 4. Naming conventions

### Daily reports

- `YYYY-MM-DD｜基本盘预测｜<version>.<ext>`
- `YYYY-MM-DD｜AI板块预测｜<version>.<ext>`

Non-trading-day reviews:

- `YYYY-MM-DD｜非交易日复盘｜基本盘｜<version>.<ext>`
- `YYYY-MM-DD｜非交易日复盘｜AI板块｜<version>.<ext>`

### Periodic reviews

- `YYYY-MM｜月度预测复盘｜<scope>.<ext>`
- `YYYY-QN｜季度预测复盘｜<scope>.<ext>`
- `YYYY-HN｜半年预测复盘｜<scope>.<ext>`

### Data snapshots

`<dataset_or_source>｜asof-YYYY-MM-DDTHHMMSSZ｜<vintage_or_version>.<ext>`

## 5. Notion asset registry

For every material Dropbox asset, Notion should maintain an index record containing at minimum:

- Asset ID;
- display name;
- asset type;
- Dropbox canonical path or stable reference;
- created time;
- coverage/as-of time;
- related Task;
- related prediction/research/method;
- GitHub source reference;
- version;
- lifecycle status;
- integrity/check result where available.

Notion stores metadata and links, not duplicate large binaries.

## 6. GitHub linkage

GitHub documents may reference a Dropbox asset by:

- Asset ID;
- canonical Dropbox path;
- optional shared link where access policy permits;
- checksum/version for reproducibility.

Do not commit large binaries merely to duplicate Dropbox.

## 7. Write pipeline

`Generate → Verify asset exists → Validate filename/path → Register Asset ID → Write Dropbox → Verify metadata → Update Notion registry → Link GitHub procedure/evidence where applicable`

A Notion record must not claim an asset exists until Dropbox existence has been verified.

## 8. Report delivery rule

For a daily report:

1. create the Canonical Report;
2. export/generate the file;
3. write the file to its Dropbox canonical folder;
4. verify the Dropbox asset;
5. update Notion with the verified asset reference;
6. expose the report in chat or other delivery surfaces.

This replaces any workflow that reports a PDF as complete before durable storage is verified.

## 9. Lifecycle and deduplication

- identical assets should be deduplicated by content where practical;
- superseded assets are marked HISTORICAL or DEPRECATED, not silently overwritten;
- archive moves preserve the Asset ID and registry history;
- raw snapshots required for reproducibility must not be replaced with revised data without preserving vintage metadata.

## 10. Conflict rules

- binary/file existence and byte-level identity → Dropbox wins;
- research procedure/version → GitHub wins;
- operational status and decision → Notion wins;
- schedule/trigger → Task wins.

If the Notion registry references a missing Dropbox asset, mark it as an asset-integrity incident and repair the link rather than pretending the asset exists.

## 11. Integrity principles

- One binary asset, one canonical storage location.
- One Asset ID across all systems.
- No silent overwrite of historical artifacts.
- No fabricated asset links.
- Verify write success before downstream references.
- Prefer indexes and references over duplicate uploads.
