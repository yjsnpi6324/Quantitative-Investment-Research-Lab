"""All evidence in these tests is SYNTHETIC, including mock reviewer receipts."""
import copy
from datetime import date, timedelta
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

AREA = Path(__file__).resolve().parents[1] / 'research/experiments/market-state-classification/experiment_001a'
SPEC = importlib.util.spec_from_file_location('experiment_preflight', AREA / 'preflight.py')
gate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(gate)


class PreflightTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.config_path = self.root / 'config.json'
        self.manifest_path = self.root / 'manifest.json'
        self.c = json.loads((AREA / 'config.draft.json').read_text())
        self.c.update(status='APPROVED', data_start='2025-11-01', data_end='2026-02-08',
                      calendar_end='2026-02-28',
                      walk_forward=[{'train': ['2025-11-01', '2025-11-20'],
                                     'validation': ['2025-12-01', '2025-12-10']},
                                    {'train': ['2025-11-01', '2025-12-10'],
                                     'validation': ['2025-12-20', '2025-12-30']}],
                      oos=['2026-01-10', '2026-02-08'])
        self.config_path.write_text(json.dumps(self.c))
        self.m = json.loads((AREA / 'manifest.template.json').read_text())
        self.m['snapshot_kind'] = 'synthetic'
        for key in ('protocol', 'source_receipt', 'protocol_qa'):
            self.m[key] = self.write(key, {'notice': 'SYNTHETIC fixture, not official or approved evidence'})
        self.m['protocol_review'] = self.review('protocol_review', {k: self.m[k]['sha256'] for k in ('protocol', 'source_receipt', 'protocol_qa')})
        self.m['parameter_approval'] = self.review('parameter_approval', {'config': gate.digest(self.config_path), 'protocol': self.m['protocol']['sha256']})
        self.m['provider'] = {'name': 'SYNTHETIC', 'authorization': self.write('authorization', {
            'provider': 'SYNTHETIC', 'research_use_allowed': True, 'source_uri': 'fixture://provider',
            'license_scope': 'test only', 'verified_at': '2026-10-24T00:00:00+00:00'})}
        days = [date(2025, 11, 1) + timedelta(days=i) for i in range(120)]
        # Explicit artificial sessions (including weekends), never a real exchange calendar.
        self.m['calendar'] = self.write('calendar', [{'date': d.isoformat(), 'is_open': d != date(2025, 11, 21)} for d in days])
        self.m['calendar_sources'] = [
            {'exchange': exchange, 'year': year, 'url': url,
             'artifact': self.write(f'{exchange}-{year}', {'notice': 'SYNTHETIC official-source stub'})}
            for year in (2025, 2026) for exchange, url in
            [('SSE', 'https://www.sse.com.cn/fixture'), ('SZSE', 'https://www.szse.cn/fixture')]]
        self.m['calendar_review'] = self.review('calendar_review', {'calendar': self.m['calendar']['sha256'], 'sources': [s['artifact']['sha256'] for s in self.m['calendar_sources']]})
        self.m['snapshot'] = self.write('snapshot', [
            {'date': d.isoformat(), 'as_of': f'{d}T16:00:00+08:00',
             'available_at': f'{d}T15:00:00+08:00', 'features': dict.fromkeys(self.c['features'], 1.0)}
            for d in days if d.isoformat() <= self.c['data_end'] and d != date(2025, 11, 21)])
        self.m['snapshot_receipt'] = self.write('snapshot_receipt', {
            'kind': 'synthetic', 'provider': 'SYNTHETIC', 'snapshot_sha256': self.m['snapshot']['sha256'],
            'source_uri': 'fixture://snapshot', 'retrieved_at': '2026-10-24T00:00:00+00:00',
            'raw_artifact': self.write('raw', {'notice': 'SYNTHETIC raw data'})})
        binding = {'config': gate.digest(self.config_path), 'snapshot': self.m['snapshot']['sha256']}
        self.m['pit_review'] = self.review('pit_review', {**binding, 'receipt': self.m['snapshot_receipt']['sha256']}, **dict.fromkeys(
            ['vintages', 'revisions', 'survivorship', 'constituents', 'corporate_actions', 'feature_lineage'], 'SYNTHETIC reviewed fixture'))
        self.m['oos_isolation'] = self.review('oos_isolation', binding, untouched=True,
            access_control=self.write('acl', {'notice': 'SYNTHETIC custody ACL'}),
            audit_log=self.write('audit', {'notice': 'SYNTHETIC access log'}),
            sealed_at='2025-01-01T00:00:00+00:00', first_model_selection_at='2025-02-01T00:00:00+00:00')
        self.m['freeze_review'] = self.review('freeze_review', {
            'config': gate.digest(self.config_path), **{k: self.m[k]['sha256'] for k in
            ('protocol', 'source_receipt', 'protocol_qa', 'protocol_review', 'calendar', 'snapshot',
             'snapshot_receipt', 'pit_review', 'calendar_review', 'parameter_approval', 'oos_isolation')},
            'provider_authorization': self.m['provider']['authorization']['sha256']})

    def write(self, name, data):
        path = self.root / (name + '.json')
        path.write_text(json.dumps(data))
        return {'path': path.name, 'sha256': gate.digest(path)}

    def review(self, name, bindings, **extra):
        return self.write(name, {'decision': 'approved', 'reviewer': 'SYNTHETIC_TEST_ONLY',
                                'reviewed_at': '2026-10-24T00:00:00+00:00', 'bindings': bindings, **extra})

    def run_gate(self, fixture=True):
        self.config_path.write_text(json.dumps(self.c))
        self.manifest_path.write_text(json.dumps(self.m))
        return gate.preflight(self.config_path, self.manifest_path, fixture=fixture)

    def blocked(self, prefix):
        result = self.run_gate()
        self.assertEqual(result['status'], 'blocked')
        self.assertFalse(result['execution_allowed'])
        self.assertTrue(any(b.startswith(prefix + ':') for b in result['blockers']), result)

    def test_synthetic_ready_never_allows_execution(self):
        result = self.run_gate()
        self.assertEqual(result, {'status': 'ready', 'scope': 'fixture', 'execution_allowed': False, 'blockers': []})

    def test_synthetic_rejected_in_real_mode(self):
        self.assertEqual(self.run_gate(fixture=False)['status'], 'blocked')

    def test_missing_required_evidence(self):
        original = copy.deepcopy(self.m)
        for field, prefix in [('protocol', 'PROTOCOL'), ('source_receipt', 'PROTOCOL'),
                              ('protocol_qa', 'PROTOCOL'), ('parameter_approval', 'PARAMETERS'),
                              ('calendar', 'CALENDAR'), ('calendar_review', 'CALENDAR'),
                              ('snapshot', 'SNAPSHOT_PIT'), ('snapshot_receipt', 'SNAPSHOT_PIT'), ('pit_review', 'SNAPSHOT_PIT'),
                              ('oos_isolation', 'OOS'), ('freeze_review', 'FREEZE')]:
            with self.subTest(field=field):
                self.m = copy.deepcopy(original)
                self.m[field] = None
                self.blocked(prefix)

    def test_provider_missing(self):
        self.m['provider']['name'] = None
        self.blocked('PROVIDER')

    def test_provider_authorization_missing(self):
        self.m['provider']['authorization'] = None
        self.blocked('PROVIDER')

    def test_draft_not_approved(self):
        self.c['status'] = 'DRAFT'
        self.blocked('PARAMETERS')

    def test_changed_config_invalidates_approval(self):
        self.c['models']['B1'] = {'threshold': 0.99}
        self.blocked('PARAMETERS')

    def test_invalid_hash(self):
        self.m['snapshot']['sha256'] = 'not-a-hash'
        self.blocked('SNAPSHOT_PIT')

    def test_forged_hash(self):
        self.m['snapshot']['sha256'] = '0' * 64
        self.blocked('SNAPSHOT_PIT')

    def test_missing_bytes(self):
        (self.root / self.m['snapshot']['path']).unlink()
        self.blocked('SNAPSHOT_PIT')

    def test_escape(self):
        self.m['protocol']['path'] = '../outside.json'
        self.blocked('PROTOCOL')

    def test_missing_historical_calendar(self):
        self.m['calendar_sources'] = [s for s in self.m['calendar_sources'] if s['year'] == 2026]
        self.blocked('CALENDAR')

    def test_unofficial_calendar(self):
        self.m['calendar_sources'][0]['url'] = 'https://sse.com.cn.evil.example/holidays'
        self.blocked('CALENDAR')

    def mutate_rows(self, key, fn):
        rows = json.loads((self.root / self.m[key]['path']).read_text())
        fn(rows)
        self.m[key] = self.write(key, rows)

    def test_missing_closed_day(self):
        self.mutate_rows('calendar', lambda rows: rows.pop(20))
        self.blocked('CALENDAR')

    def test_future_input(self):
        self.mutate_rows('snapshot', lambda rows: rows[0].update(available_at='2026-01-01T00:00:00+08:00'))
        self.blocked('SNAPSHOT_PIT')

    def test_target_in_inputs(self):
        self.mutate_rows('snapshot', lambda rows: rows[0].update(forward_return=0.1))
        self.blocked('SNAPSHOT_PIT')

    def test_naive_timestamp(self):
        self.mutate_rows('snapshot', lambda rows: rows[0].update(as_of='2025-11-01T16:00:00'))
        self.blocked('SNAPSHOT_PIT')

    def test_missing_snapshot_session(self):
        self.mutate_rows('snapshot', lambda rows: rows.pop())
        self.blocked('SNAPSHOT_PIT')

    def test_overlap(self):
        self.c['walk_forward'][0]['validation'][0] = '2025-11-22'
        self.blocked('OOS')

    def test_oos_label_buffer(self):
        self.c['oos'][1] = '2026-02-28'
        self.c['data_end'] = '2026-02-28'
        self.blocked('OOS')

    def test_missing_oos_audit_bytes(self):
        (self.root / 'audit.json').unlink()
        self.blocked('OOS')

    def test_missing_raw_snapshot(self):
        (self.root / 'raw.json').unlink()
        self.blocked('SNAPSHOT_PIT')

    def test_pit_review_cannot_be_empty_claim(self):
        self.mutate_rows('pit_review', lambda record: record.update(vintages=''))
        self.blocked('SNAPSHOT_PIT')

    def test_oos_sealed_after_selection(self):
        self.mutate_rows('oos_isolation', lambda record: record.update(sealed_at='2026-10-24T00:00:00+00:00'))
        self.blocked('OOS')

    def test_template_blocked(self):
        result = gate.preflight(AREA / 'config.draft.json', AREA / 'manifest.template.json')
        self.assertEqual(result['status'], 'blocked')
        self.assertEqual(len(result['blockers']), 7)

    def test_cli_exit_codes(self):
        self.run_gate()
        cmd = [sys.executable, str(AREA / 'preflight.py'), str(self.config_path), str(self.manifest_path)]
        self.assertEqual(subprocess.run(cmd + ['--fixture'], capture_output=True).returncode, 0)
        self.assertEqual(subprocess.run(cmd, capture_output=True).returncode, 2)
        self.assertEqual(subprocess.run([sys.executable, '-O', *cmd[1:]], capture_output=True).returncode, 2)

    def test_malformed_json(self):
        self.manifest_path.write_text('invalid')
        self.assertEqual(gate.preflight(self.config_path, self.manifest_path)['status'], 'blocked')


if __name__ == '__main__':
    unittest.main()
