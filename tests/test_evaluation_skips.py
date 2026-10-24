import copy
import unittest
from unittest.mock import Mock

from test_evaluation_closure import FakeRegistry, FakeMarket, locked_prediction
from src.evaluation.runner import run_due_evaluations, summarize_evaluations
from src.evaluation.backlog import scan_evaluation_backlog
from src.evaluation.metrics import rolling_metrics
from src.evaluation.scorer import score_horizon, score_result


class SkipTests(unittest.TestCase):
    def run_rows(self, rows, market=None, as_of="2026-09-28"):
        registry = FakeRegistry(rows[0])
        registry.list_evaluation_candidates = lambda _: rows
        before = copy.deepcopy(rows)
        result = run_due_evaluations(as_of, registry, market or FakeMarket())
        self.assertEqual(rows, before)
        return registry, result

    def test_mixed_source_invalid_and_good_records(self):
        source = {"report_id": "RPT-AI-20261019-001", "production_id": "AI",
                  "status": "SOURCE_FINAL_NOT_FOUND"}
        bad = {"prediction_id": "broken", "prediction_hash": "x"}
        registry, result = self.run_rows([source, bad, locked_prediction()])
        self.assertEqual([r['status'] for r in result[:2]],
                         ['SOURCE_FINAL_NOT_FOUND', 'INVALID_PREDICTION'])
        self.assertEqual(len(registry.appended), 3)
        backlog = scan_evaluation_backlog('2026-09-28', registry)
        self.assertEqual(len(backlog), 2)

    def test_unavailable_unscored_and_good_horizons(self):
        market = Mock()
        market.calendar = None
        market.get_actual.side_effect = [None, {'status': 'VERIFIED'}, {'result': 'HIT'}]
        registry, result = self.run_rows([locked_prediction()], market)
        self.assertEqual([r.get('status') for r in result],
                         ['ACTUAL_UNAVAILABLE', 'ACTUAL_UNSCORED', None])
        self.assertEqual(len(registry.appended), 1)

    def test_invalid_results_and_unverified_market_are_not_scored(self):
        for actual in ({'result': 'UNKNOWN'}, {'result': []},
                       {'result': 'HIT', 'status': 'UNVERIFIED'}, {'status': 'MISSING'}):
            with self.subTest(actual=actual):
                market = FakeMarket()
                market.get_actual = lambda _: actual
                registry, result = self.run_rows([locked_prediction()], market)
                self.assertEqual(registry.appended, [])
                self.assertEqual(rolling_metrics(result)['sample_size'], 0)

    def test_market_error_does_not_stop_other_windows(self):
        market = Mock(calendar=None)
        market.get_actual.side_effect = [TimeoutError(), {'result': 'MISS'}, {'result': 'PARTIAL'}]
        registry, result = self.run_rows([locked_prediction()], market)
        self.assertEqual(result[0]['status'], 'ACTUAL_LOOKUP_FAILED')
        self.assertEqual(len(registry.appended), 2)

    def test_future_windows_and_repeat_run(self):
        registry, result = self.run_rows([locked_prediction()], as_of='2026-09-21')
        self.assertEqual([r.get('status') for r in result], [None, 'NOT_DUE', 'NOT_DUE'])
        again = run_due_evaluations('2026-09-21', registry, FakeMarket())
        self.assertEqual(again[0]['status'], 'ALREADY_EVALUATED')
        self.assertEqual(len(registry.appended), 1)
        self.assertEqual(rolling_metrics(again)['sample_size'], 0)

    def test_saved_dates_are_preserved_and_conflicts_block(self):
        pred = locked_prediction()
        pred['target_dates'] = {'T+1': '2026-10-30'}
        registry, result = self.run_rows([pred])
        self.assertEqual(result[0]['target_date'], '2026-10-30')
        self.assertEqual(result[0]['status'], 'NOT_DUE')
        pred['t1_target_date'] = '2026-09-21'
        registry, result = self.run_rows([pred])
        self.assertEqual(result[0]['status'], 'INVALID_PREDICTION')
        self.assertEqual(registry.appended, [])

    def test_schema_v1_not_rehashed_as_legacy(self):
        pred = locked_prediction()
        pred['hash_schema_version'] = 'prediction-hash-schema-v1'
        registry, result = self.run_rows([pred])
        self.assertEqual(result[0]['status'], 'UNSUPPORTED_HASH_SCHEMA')
        self.assertFalse(registry.appended)

    def test_unknown_append_not_retried_or_counted_as_success(self):
        pred = locked_prediction()
        registry = FakeRegistry(pred)
        registry.list_evaluation_candidates = lambda _: [pred, pred]
        registry.append_evaluation = Mock(side_effect=TimeoutError())
        result = run_due_evaluations('2026-09-28', registry, FakeMarket())
        self.assertEqual(registry.append_evaluation.call_count, 3)
        self.assertTrue(all(r['status'] == 'APPEND_OUTCOME_UNKNOWN' for r in result))
        self.assertEqual(rolling_metrics(result)['sample_size'], 0)

    def test_summary_separates_lines_records_windows_and_scores(self):
        registry, result = self.run_rows([locked_prediction()], as_of='2026-09-21')
        result += [{'production_id': 'BASIC', 'status': 'SOURCE_FINAL_NOT_FOUND'}]
        groups = summarize_evaluations(result)
        ai = groups['AI-PROD-20260825-A']
        self.assertEqual(ai['evaluated'], 1)
        self.assertEqual(ai['window_statuses'], {'NOT_DUE': 2})
        self.assertEqual(groups['BASIC']['evaluated'], 0)
        self.assertEqual(groups['BASIC']['record_statuses'], {'SOURCE_FINAL_NOT_FOUND': 1})
        self.assertEqual(rolling_metrics(result)['accuracy'], 1)
        self.assertEqual(rolling_metrics(result)['sample_size'], 1)
        self.assertEqual(score_horizon([{'Result': 'HIT'}, {'Result': None}]), 1)
        with self.assertRaises(KeyError):
            score_result('UNKNOWN')
