import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALID_VERDICTS = {"verified", "not_verified", "ambiguous", "page_unavailable", "requires_manual_review"}
REQUIRED_RESULT_FIELDS = {
    "verification_id", "url", "claim", "expected_visual_state", "verdict", "confidence",
    "visual_evidence_summary", "mismatch_reason", "requires_manual_review", "risk_flags",
    "validator_equivalence_note",
}

class ResultSchemaTests(unittest.TestCase):
    def test_expected_output_examples_have_required_fields(self):
        data = json.loads((ROOT / "examples" / "expected_outputs.json").read_text())
        for key in ["verified_example", "ambiguous_example"]:
            example = data[key]
            self.assertTrue(REQUIRED_RESULT_FIELDS.issubset(example.keys()))
            self.assertIn(example["verdict"], VALID_VERDICTS)
            self.assertIsInstance(example["requires_manual_review"], bool)
            self.assertIsInstance(example["risk_flags"], list)

    def test_valid_verdict_list_is_exact(self):
        data = json.loads((ROOT / "examples" / "expected_outputs.json").read_text())
        self.assertEqual(set(data["valid_verdicts"]), VALID_VERDICTS)

if __name__ == "__main__":
    unittest.main()
