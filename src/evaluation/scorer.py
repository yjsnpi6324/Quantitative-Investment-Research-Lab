"""Evaluation scoring skeleton.

Converts Evaluation Registry records into normalized scores.
"""

RESULT_SCORE = {
    "HIT": 1.0,
    "PARTIAL": 0.5,
    "MISS": 0.0,
}


def score_result(result: str) -> float:
    return RESULT_SCORE[result]


def score_horizon(records):
    records = [r for r in records if isinstance(r.get("Result"), str) and r["Result"] in RESULT_SCORE and not r.get("status")]
    if not records:
        return 0.0
    return sum(score_result(r.get("Result")) for r in records) / len(records)
