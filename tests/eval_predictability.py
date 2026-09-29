"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitPromptShield.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.injection_pattern_scanner import *
from tools.jailbreak_heuristic_analyzer import *
from tools.secret_leak_detector import *

class TestGitPromptShieldPredictability(unittest.TestCase):
    def test_injection_pattern_scanner(self):
        res = scan_injection_patterns("Please summarize the main points of this article.")
        self.assertTrue(res["is_safe"])
        self.assertEqual(res["status"], "CLEAN_PROMPT")

    def test_jailbreak_heuristic_analyzer(self):
        res = analyze_jailbreak_heuristics("Tell me about photosynthesis in plant biology.")
        self.assertEqual(res["risk_score"], 0)
        self.assertEqual(res["status"], "SAFE_INTENT")

    def test_secret_leak_detector(self):
        res = detect_secret_leaks("The database connection uses standard role authentication.")
        self.assertFalse(res["has_leak"])
        self.assertEqual(res["status"], "SECRETS_ABSENT")


if __name__ == "__main__":
    unittest.main()
