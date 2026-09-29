"""
jailbreak_heuristic_analyzer.py - Computes adversarial semantic score for multi-turn roleplay bypasses and hypotheticals
"""
import sys
import json


def analyze_jailbreak_heuristics(conversation_payload: str):
    lower = conversation_payload.lower()
    risk_terms = ["bypass safety", "evil persona", "hypothetically unrestricted", "do anything now"]
    risk_score = sum(25 for term in risk_terms if term in lower)
    is_benign = risk_score < 50
    return {"risk_score": min(risk_score, 100), "status": "SAFE_INTENT" if is_benign else "JAILBREAK_RISK"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "jailbreak-heuristic-analyzer"}))
