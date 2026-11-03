"""Run: python3 test_evidence_gate.py /path/to/scripts/evidence_gate.py"""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(sys.argv.pop(1)).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[2] / '.agents/skills/dogal-ve-dogrulanmis-yazi/scripts/evidence_gate.py'
spec = importlib.util.spec_from_file_location('evidence_gate', SCRIPT)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


def sha(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()


class EvidenceGateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.draft = "Toplantı cuma 15.30'da.\n"
        self.source = "Duyuru: Toplantı cuma 15.30'da. Katılım isteğe bağlı."
        (self.root/'draft.txt').write_text(self.draft, encoding='utf-8')
        (self.root/'source.txt').write_text(self.source, encoding='utf-8')
        self.record = {'version': 1, 'draft_file': 'draft.txt', 'draft_sha256': sha(self.draft),
                       'sources': [{'id':'s1','kind':'provided','path':'source.txt','sha256':sha(self.source),'origin':'Sentetik test belgesi'}],
                       'segments':[{'text':self.draft,'kind':'fact','evidence':[{'source_id':'s1','quote':"Toplantı cuma 15.30'da."}]}]}

    def run_record(self, record=None):
        path = self.root/'audit.json'
        path.write_text(json.dumps(self.record if record is None else record, ensure_ascii=False), encoding='utf-8')
        return gate.audit(path)

    def assertFails(self, needle):
        result = self.run_record()
        self.assertEqual(result['status'], 'FAILED')
        self.assertIn(needle, result['error'])

    def test_valid_record_is_only_mechanical_success(self):
        result = self.run_record()
        self.assertEqual(result['status'], gate.PASS)
        self.assertIn('truth require semantic review', ' '.join(result['limitations']))

    def test_edited_final_draft_rejected(self):
        (self.root/'draft.txt').write_text('Toplantı pazartesi.', encoding='utf-8')
        self.assertFails('SHA256 mismatch')

    def test_edited_source_rejected(self):
        (self.root/'source.txt').write_text('Farklı kaynak', encoding='utf-8')
        self.assertFails('SHA256 mismatch')

    def test_fabricated_quote_rejected(self):
        self.record['segments'][0]['evidence'][0]['quote'] = 'Başarı yüzde 80 arttı.'
        self.assertFails('Quote absent')

    def test_missing_evidence_rejected(self):
        self.record['segments'][0]['evidence'] = []
        self.assertFails('needs evidence')

    def test_unrecorded_draft_suffix_rejected(self):
        self.record['segments'][0]['text'] = self.draft[:-1]
        self.assertFails('entire final draft')

    def test_unknown_source_rejected(self):
        self.record['segments'][0]['evidence'][0]['source_id'] = 'unknown'
        self.assertFails('Unknown evidence source')

    def test_duplicate_source_ids_rejected(self):
        self.record['sources'].append(copy.deepcopy(self.record['sources'][0]))
        self.assertFails('duplicate source id')

    def test_path_traversal_rejected(self):
        self.record['sources'][0]['path'] = '../outside.txt'
        self.assertFails('escapes audit directory')

    def test_absolute_path_rejected(self):
        self.record['draft_file'] = str(self.root/'draft.txt')
        self.assertFails('relative file path')

    def test_symlink_escape_rejected(self):
        with tempfile.TemporaryDirectory() as outside:
            target = Path(outside)/'outside.txt'
            target.write_text(self.source, encoding='utf-8')
            (self.root/'link.txt').symlink_to(target)
            self.record['sources'][0]['path'] = 'link.txt'
            self.assertFails('escapes audit directory')

    def test_invisible_character_rejected(self):
        value = self.draft + '\u200b'
        (self.root/'draft.txt').write_text(value, encoding='utf-8')
        self.record['draft_sha256'] = sha(value)
        self.assertFails('Invisible')

    def test_web_source_needs_timezone(self):
        self.record['sources'][0].update(kind='web', origin='https://example.org/source', retrieved_at='2026-11-03T12:00:00')
        self.assertFails('timezone')

    def test_well_formed_web_metadata_allowed_but_not_authenticated(self):
        self.record['sources'][0].update(kind='web', origin='https://example.org/source', retrieved_at='2026-11-03T12:00:00+00:00')
        self.assertEqual(self.run_record()['status'], gate.PASS)

    def test_malformed_json_and_duplicate_keys_rejected(self):
        path = self.root/'audit.json'
        for bad in ('{', '{"version":1,"version":1}'):
            with self.subTest(bad=bad):
                path.write_text(bad, encoding='utf-8')
                self.assertEqual(gate.audit(path)['status'], 'FAILED')

    def test_invalid_types_fail_cleanly(self):
        for field, value in [('version', True), ('segments', 'oops'), ('sources', None), ('draft_sha256', 123)]:
            with self.subTest(field=field):
                changed = copy.deepcopy(self.record)
                changed[field] = value
                self.assertEqual(self.run_record(changed)['status'], 'FAILED')

    def test_empty_draft_rejected(self):
        (self.root/'draft.txt').write_text('', encoding='utf-8')
        self.record['draft_sha256'] = sha('')
        self.assertFails('Empty draft')

    def test_semantically_false_claim_can_pass_mechanical_checks(self):
        # Critical negative control: the quote exists but contradicts the claim.
        false_claim = "Toplantı cuma 19.00'da.\n"
        (self.root/'draft.txt').write_text(false_claim, encoding='utf-8')
        self.record['draft_sha256'] = sha(false_claim)
        self.record['segments'][0]['text'] = false_claim
        self.assertEqual(self.run_record()['status'], gate.PASS)

    def test_misclassified_fact_can_pass_mechanical_checks(self):
        self.record['segments'][0].update(kind='other', evidence=[])
        self.assertEqual(self.run_record()['status'], gate.PASS)

    def test_cli_exit_codes_and_json(self):
        self.run_record()
        result = subprocess.run([sys.executable, str(SCRIPT), str(self.root/'audit.json')], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout)['status'], gate.PASS)
        result = subprocess.run([sys.executable, str(SCRIPT), str(self.root/'missing.json')], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertEqual(json.loads(result.stdout)['status'], 'FAILED')

    def test_large_source_rejected(self):
        (self.root/'source.txt').write_bytes(b'x' * (gate.LIMIT+1))
        self.assertFails('exceeds 4 MiB')


if __name__ == '__main__':
    unittest.main(verbosity=2)
