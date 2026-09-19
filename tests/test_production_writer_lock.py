import unittest

from src.evaluation.immutable_ledger import verify_prediction
from src.integrations.production_writer import persist_prediction


class Sink:
    def __init__(self):
        self.record = None

    def write_prediction(self, record):
        self.record = record
        return {"ok": True}


class ProductionWriterLockTests(unittest.TestCase):
    def test_prediction_is_locked_before_registry_write(self):
        payload = {
            "task_id": "TASK-AI-DAILY",
            "production_id": "AI-PROD-20260825-A",
            "prediction_id": "PRED-TEST-001",
            "report_id": "RPT-TEST-001",
            "model_version": "v-test",
            "data_snapshot_id": "SNAP-TEST",
            "generated_at": "2026-09-18T19:00:00+08:00",
        }
        extra = {
            "trading_date": "2026-09-18",
            "T+1": "a",
            "T+3": "b",
            "T+5": "c",
        }
        sink = Sink()
        result = persist_prediction(payload, extra, sink)
        self.assertTrue(verify_prediction(result["record"]))
        self.assertTrue(verify_prediction(sink.record))
        self.assertIn("prediction_hash", sink.record)


if __name__ == "__main__":
    unittest.main()
