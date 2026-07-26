from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools/verify_book1_revision.py"
SPEC = importlib.util.spec_from_file_location("verify_book1_revision_report", SCRIPT)
assert SPEC and SPEC.loader
verification = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = verification
SPEC.loader.exec_module(verification)


class FinalVerificationReportStateTests(unittest.TestCase):
    def test_generator_records_cleared_final_package(self) -> None:
        verification.main()
        report = verification.REPORT.read_text(encoding="utf-8")
        self.assertIn("publication_ready_upload_ready", report)
        self.assertIn("PR #92", report)
        self.assertIn("No manuscript or package defect remains open", report)
        self.assertNotIn("proofread_and_production_required", report)
        self.assertNotIn("proofs still require generation", report)


if __name__ == "__main__":
    unittest.main()
