"""Offline evidence checks only; never authorizes research or production execution."""
from __future__ import annotations

import argparse
from datetime import date, datetime, timedelta
import hashlib
import json
import math
from urllib.parse import urlparse
from zoneinfo import ZoneInfo
from pathlib import Path
import re


FEATURES = ["z20", "z60", "sigma20", "drawdown60", "breadth60", "dispersion1"]
# These gates are not implemented here. No input, approval string or fixture flag
# may turn this partial scaffold into an experiment execution authorization.
EXECUTION_BLOCKERS = (
    "PROTOCOL_IMPLEMENTATION: draft protocol D1-D7, labels, 20:00 cutoff and raw-to-feature PIT replay are not validated",
    "SPLIT_IMPLEMENTATION: 756/126/126 windows, >=4 development tests, H5+E5 embargo, 252-session OOS and outcome availability are not validated",
    "MODEL_IMPLEMENTATION: B0/B1/C, training-only scaling, fallback, convergence and future-sentinel tests are not implemented",
    "EVIDENCE_AUTHENTICITY: local hashes and review strings do not establish real data, provider rights, reviewer identity or untouched OOS",
    "RUN_IMPLEMENTATION: dependency lock, reproducible execution and protocol G0-G5 evaluation are not implemented",
)


def report(errors, fixture):
    """Separate contract-test success from scientific/execution readiness."""
    return {
        "status": "evidence_checks_passed" if fixture and not errors else "blocked",
        "scope": "fixture" if fixture else "research",
        "readiness": "evidence_checks_only",
        "evidence_checks_passed": not errors,
        "execution_allowed": False,
        "blockers": list(errors) + ([] if fixture else list(EXECUTION_BLOCKERS)),
        "execution_blockers": list(EXECUTION_BLOCKERS),
    }


def calendar_source_bindings(sources):
    """Bind source meaning as well as bytes; preserve manifest source order."""
    return [{"year": s["year"], "exchange": s["exchange"], "url": s["url"],
             "artifact": s["artifact"]} for s in sources]


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def timestamp(value):
    result = datetime.fromisoformat(value)
    assert result.tzinfo is not None, "timezone required"
    return result


def preflight(config_path, manifest_path, *, fixture=False):
    if not __debug__:
        return report(["INPUT: Optimized Python disables validation; use normal Python"], fixture)
    errors = []
    try:
        config = json.loads(Path(config_path).read_text())
        manifest = json.loads(Path(manifest_path).read_text())
        assert isinstance(config, dict) and isinstance(manifest, dict)
    except (OSError, ValueError, AssertionError) as exc:
        return report([f"INPUT: {exc}"], fixture)
    root = Path(manifest_path).resolve().parent

    def evidence(ref, *, parse=True):
        assert isinstance(ref, dict), "missing evidence reference"
        sha = ref.get("sha256", "")
        assert isinstance(sha, str) and re.fullmatch(r"[0-9a-f]{64}", sha), "invalid SHA-256"
        relative = Path(ref["path"])
        assert not relative.is_absolute(), "evidence path must be relative"
        path = (root / relative).resolve()
        assert path.is_relative_to(root), "evidence escapes manifest directory"
        assert path.is_file() and path.stat().st_size > 0, "missing/empty evidence bytes"
        assert digest(path) == sha, "evidence hash mismatch"
        return json.loads(path.read_text()) if parse else path

    def check(code, fn):
        try:
            fn()
        except (AssertionError, KeyError, TypeError, ValueError, OSError, IndexError, AttributeError, OverflowError) as exc:
            errors.append(f"{code}: {exc}")

    def review(name, bindings):
        record = evidence(manifest.get(name))
        assert record["decision"] == "approved" and record["reviewer"].strip(), "review not approved"
        timestamp(record["reviewed_at"])
        assert record["bindings"] == bindings, "review does not bind current evidence"
        return record

    def protocol():
        for name in ("protocol", "source_receipt", "protocol_qa"):
            evidence(manifest.get(name), parse=False)
        review("protocol_review", {key: manifest[key]["sha256"] for key in
                                  ("protocol", "source_receipt", "protocol_qa")})

    def parameters():
        assert config["status"] == "APPROVED", "parameters remain DRAFT"
        assert config["states"] == ["Bull", "Neutral", "Bear"]
        assert config["high_vol_independent"] is True
        assert config["primary_horizon"] == 5 and config["secondary_horizons"] == [1, 3]
        assert config["label_inputs"] == "as_of_only"
        assert config["features"] == FEATURES, "protocol requires the fixed six ordered features"
        assert set(config["models"]) == {"B0", "B1", "C"}
        assert all(config["models"].values()), "missing baseline/candidate definitions"
        assert config["walk_forward"] and config["oos"], "missing split definitions"
        review("parameter_approval", {"config": digest(config_path),
                                      "protocol": manifest["protocol"]["sha256"]})

    def provider():
        assert isinstance(manifest["provider"]["name"], str) and manifest["provider"]["name"].strip(), "missing provider"
        record = evidence(manifest["provider"]["authorization"])
        assert record["provider"] == manifest["provider"]["name"]
        assert record["research_use_allowed"] is True
        assert record["source_uri"].strip() and record["license_scope"].strip()
        timestamp(record["verified_at"])

    calendar = {}

    def calendars():
        rows = evidence(manifest.get("calendar"))
        start, end = date.fromisoformat(config["data_start"]), date.fromisoformat(config["calendar_end"])
        assert start <= date.fromisoformat(config["data_end"]) <= end
        assert isinstance(rows, list) and rows, "missing daily calendar"
        for row in rows:
            day = date.fromisoformat(row["date"])
            assert day not in calendar, "duplicate calendar day"
            assert type(row["is_open"]) is bool, "calendar requires explicit open/closed"
            calendar[day] = row["is_open"]
        expected = {start + timedelta(days=i) for i in range((end - start).days + 1)}
        assert set(calendar) == expected, "calendar must cover every date including closures"
        sources = manifest["calendar_sources"]
        for year in range(start.year, end.year + 1):
            for exchange in ("SSE", "SZSE"):
                matches = [s for s in sources if s["year"] == year and s["exchange"] == exchange]
                assert matches, f"missing official {exchange} evidence for {year}"
                for source in matches:
                    host = urlparse(source["url"]).hostname or ""
                    domain = {"SSE": "sse.com.cn", "SZSE": "szse.cn"}[exchange]
                    assert host == domain or host.endswith("." + domain), "non-official calendar source"
                    evidence(source["artifact"], parse=False)
        review("calendar_review", {"calendar": manifest["calendar"]["sha256"],
                                   "sources": calendar_source_bindings(sources)})

    def snapshots():
        assert manifest["snapshot_kind"] == ("synthetic" if fixture else "real"), "real snapshot required"
        rows = evidence(manifest.get("snapshot"))
        assert rows and isinstance(rows, list), "empty snapshot"
        seen = set()
        for row in rows:
            assert set(row) == {"date", "as_of", "available_at", "features"}, "unexpected/future-target input field"
            day = date.fromisoformat(row["date"])
            assert day not in seen, "duplicate snapshot day"
            seen.add(day)
            cutoff = timestamp(row["as_of"])
            assert cutoff.astimezone(ZoneInfo("Asia/Shanghai")).date() == day and timestamp(row["available_at"]) <= cutoff, "future information"
            assert set(row["features"]) == set(config["features"]), "feature schema mismatch"
            assert all(type(v) in (int, float) and math.isfinite(v) for v in row["features"].values())
        expected = {d for d, opened in calendar.items() if opened and
                    config["data_start"] <= d.isoformat() <= config["data_end"]}
        assert expected and seen == expected, "snapshot/session coverage mismatch"
        receipt = evidence(manifest.get("snapshot_receipt"))
        assert receipt["kind"] == manifest["snapshot_kind"]
        assert receipt["provider"] == manifest["provider"]["name"]
        assert receipt["snapshot_sha256"] == manifest["snapshot"]["sha256"]
        assert receipt["source_uri"].strip()
        timestamp(receipt["retrieved_at"])
        evidence(receipt["raw_artifact"], parse=False)
        record = review("pit_review", {"snapshot": manifest["snapshot"]["sha256"],
                                       "config": digest(config_path),
                                       "receipt": manifest["snapshot_receipt"]["sha256"]})
        for key in ("vintages", "revisions", "survivorship", "constituents", "corporate_actions", "feature_lineage"):
            assert record[key].strip(), f"missing PIT review: {key}"

    def splits():
        assert config.get("walk_forward") and config.get("oos"), "missing walk-forward/OOS definitions"
        sessions = sorted(d for d, opened in calendar.items() if opened)
        def interval(pair):
            a, b = map(date.fromisoformat, pair)
            assert a in sessions and b in sessions and a <= b
            assert config["data_start"] <= a.isoformat() <= b.isoformat() <= config["data_end"]
            return a, b
        oos_start, oos_end = interval(config["oos"])
        previous = None
        assert config["walk_forward"], "no walk-forward folds"
        for fold in config["walk_forward"]:
            train_start, train_end = interval(fold["train"])
            valid_start, valid_end = interval(fold["validation"])
            assert sessions.index(train_end) + 5 < sessions.index(valid_start), "T+5 train-label leakage"
            assert sessions.index(valid_end) + 5 < sessions.index(oos_start), "validation/OOS leakage"
            assert previous is None or previous < valid_start, "overlapping/unsorted validation folds"
            previous = valid_end
        assert sessions.index(oos_end) + 5 < len(sessions), "missing T+5 calendar buffer"
        record = review("oos_isolation", {"config": digest(config_path),
                                          "snapshot": manifest["snapshot"]["sha256"]})
        assert record["untouched"] is True and record["access_control"] and record["audit_log"]
        evidence(record["access_control"], parse=False)
        evidence(record["audit_log"], parse=False)
        assert timestamp(record["sealed_at"]) <= timestamp(record["first_model_selection_at"]), "OOS sealed too late"

    def freeze():
        assert manifest.get("freeze_review"), "missing real freeze review"
        review("freeze_review", {"config": digest(config_path), **{
            key: manifest[key]["sha256"] for key in
            ("protocol", "source_receipt", "protocol_qa", "protocol_review", "calendar",
             "snapshot", "snapshot_receipt", "pit_review", "calendar_review", "parameter_approval", "oos_isolation")},
            "provider_authorization": manifest["provider"]["authorization"]["sha256"],
            "calendar_sources": calendar_source_bindings(manifest["calendar_sources"])})

    for code, fn in (("PROTOCOL", protocol), ("PARAMETERS", parameters), ("PROVIDER", provider),
                     ("CALENDAR", calendars), ("SNAPSHOT_PIT", snapshots), ("OOS", splits), ("FREEZE", freeze)):
        check(code, fn)
    return report(errors, fixture)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("config", type=Path)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--fixture", action="store_true", help="synthetic contract checks; never permits execution")
    args = parser.parse_args()
    result = preflight(args.config, args.manifest, fixture=args.fixture)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    raise SystemExit(0 if result["status"] == "evidence_checks_passed" else 2)
