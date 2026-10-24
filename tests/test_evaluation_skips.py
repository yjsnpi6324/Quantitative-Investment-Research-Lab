import copy
import json
from pathlib import Path
import unittest
from unittest.mock import Mock

from test_evaluation_closure import FakeRegistry, FakeMarket, locked_prediction
from src.evaluation.runner import run_due_evaluations, summarize_evaluations
from src.evaluation.backlog import scan_evaluation_backlog
from src.evaluation.metrics import rolling_metrics, is_scored_evaluation
from src.evaluation.self_audit_runner import run_self_audit
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


class PersistedClosureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        root = Path(__file__).resolve().parents[1]
        cls.rows = [json.loads(path.read_text()) for path in
                    sorted((root / "evaluation-ledger").rglob("*.json"))]
        cls.ai = next(row for row in cls.rows
                      if row["evaluation_id"] == "EVAL-AI-20260930-T1")

    def test_real_closed_ledger_is_counted_by_all_consumers(self):
        self.assertEqual(self.ai['status'], 'FORMAL_CLOSED')
        self.assertTrue(is_scored_evaluation(self.ai))
        self.assertEqual(rolling_metrics([self.ai])['accuracy'], 0.5)
        self.assertEqual(run_self_audit([], [self.ai])['evaluation_count'], 1)
        summary = summarize_evaluations([self.ai])[self.ai['production_id']]
        self.assertEqual(summary['evaluated'], 1)
        self.assertEqual(summary['results'], {'PARTIAL': 1})
        self.assertEqual(rolling_metrics(self.rows)['sample_size'], len(self.rows))
        self.assertEqual(run_self_audit([], self.rows)['evaluation_count'], len(self.rows))

    def test_workflow_states_are_not_inferred_from_score(self):
        states = ['pending', 'partial', 'invalid', 'PENDING', 'NOT_DUE',
                  'SOURCE_FINAL_NOT_FOUND', 'ACTUAL_UNSCORED', 'ACTUAL_UNAVAILABLE',
                  'ALREADY_EVALUATED', 'APPEND_OUTCOME_UNKNOWN', 'UNKNOWN', [], False]
        for state in states:
            with self.subTest(status=state):
                row = dict(self.ai, status=state)
                self.assertFalse(is_scored_evaluation(row))
                self.assertEqual(rolling_metrics([row])['sample_size'], 0)
                self.assertEqual(run_self_audit([], [row])['evaluation_count'], 0)
                if isinstance(state, str):
                    self.assertEqual(summarize_evaluations([row])[row['production_id']]['evaluated'], 0)
                self.assertEqual(score_horizon([{'Result': 'HIT', 'status': state}]), 0)

    def test_verified_schema_and_legacy_require_valid_result_and_score(self):
        for status in ('FORMAL_CLOSED', 'verified', None, ''):
            with self.subTest(status=status):
                row = dict(self.ai, status=status)
                self.assertTrue(is_scored_evaluation(row))
                self.assertEqual(score_horizon([{'Result': 'PARTIAL', 'status': status}]), 0.5)
                for changes in ({'result': None}, {'result': 'pending'},
                                {'score': None}, {'score': 1}, {'evaluation_id': ''}):
                    self.assertFalse(is_scored_evaluation(dict(row, **changes)))
