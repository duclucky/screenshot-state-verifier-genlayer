import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY_FILES = ["status_page_claim.json", "dapp_ui_claim.json", "ambiguous_claim.json"]

class VerificationPolicyTests(unittest.TestCase):
    def test_claim_examples_are_valid_json(self):
        for filename in POLICY_FILES:
            data = json.loads((ROOT / "examples" / filename).read_text())
            self.assertIn("url", data)
            self.assertIn("claim", data)
            self.assertIn("expected_visual_state", data)
            self.assertIn("verification_policy", data)
            self.assertIsInstance(data["verification_policy"], dict)

    def test_policy_contains_required_review_controls(self):
        for filename in POLICY_FILES:
            policy = json.loads((ROOT / "examples" / filename).read_text())["verification_policy"]
            self.assertIn("risk_flags", policy)
            self.assertIn("manual_review_if", policy)
            self.assertIsInstance(policy["risk_flags"], list)
            self.assertIsInstance(policy["manual_review_if"], list)

if __name__ == "__main__":
    unittest.main()
