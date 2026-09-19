import unittest

from src.evaluation.a_share_calendar import AShareTradingCalendar
from src.evaluation.immutable_ledger import lock_prediction
from src.evaluation.runner import expand_prediction_horizons, run_due_evaluations


def locked_prediction():
    raw = {
        "prediction_id": "PRED-AI-20260918-01",
        "task_id": "TASK-AI-DAILY",
        "production_id": "AI-PROD-20260825-A",
        "model_version": "v2026-08-26",
        "generated_at": "2026-09-18T19:00:00+08:00",
        "trading_date": "2026-09-18",
        "data_snapshot_id": "AI-SNAPSHOT-20260918-1900",
        "prediction": {
            "T+1": "震荡偏强",
            "T+3": "结构性偏多",
            "T+5": "中性偏多",
        },
        "horizons": {
            "T+1": "震荡偏强",
            "T+3": "结构性偏多",
            "T+5": "中性偏多",
        },
    }
    return lock_prediction(raw)


class FakeRegistry:
    def __init__(self, prediction, existing=None):
        self.prediction = prediction
        self.existing = set(existing or [])
        self.appended = []

    def list_due_predictions(self, as_of):
        return [self.prediction]

    def has_evaluation(self, prediction_id, horizon):
        return (prediction_id, horizon) in self.existing

    def append_evaluation(self, evaluation):
        self.appended.append(evaluation)
        self.existing.add(
            (evaluation["prediction_id"], evaluation["horizon"])
        )


class FakeMarket:
    def get_actual(self, candidate):
        return {
            "status": "VERIFIED",
            "result": "HIT",
            "close_date": candidate["target_date"],
        }


class EvaluationClosureTests(unittest.TestCase):
    def setUp(self):
        self.calendar = AShareTradingCalendar()

    def test_expands_one_canonical_row_into_three_horizons(self):
        items = expand_prediction_horizons(
            locked_prediction(), self.calendar
        )
        self.assertEqual(
            [(x["horizon"], x["target_date"]) for x in items],
            [
                ("T+1", "2026-09-21"),
                ("T+3", "2026-09-23"),
                ("T+5", "2026-09-28"),
            ],
        )

    def test_closes_only_matured_horizons(self):
        registry = FakeRegistry(locked_prediction())
        result = run_due_evaluations(
            "2026-09-23", registry, FakeMarket(), self.calendar
        )
        closed = [x for x in result if x.get("evaluation_id")]
        self.assertEqual([x["horizon"] for x in closed], ["T+1", "T+3"])
        self.assertEqual(len(registry.appended), 2)

    def test_is_idempotent_by_prediction_and_horizon(self):
        pred = locked_prediction()
        registry = FakeRegistry(
            pred, existing={(pred["prediction_id"], "T+1")}
        )
        result = run_due_evaluations(
            "2026-09-21", registry, FakeMarket(), self.calendar
        )
        self.assertEqual(result[0]["status"], "ALREADY_EVALUATED")
        self.assertEqual(registry.appended, [])


if __name__ == "__main__":
    unittest.main()
