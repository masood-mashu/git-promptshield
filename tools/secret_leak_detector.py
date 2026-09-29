"""
secret_leak_detector.py - Scans strings for high-entropy API tokens, private keys, and credential strings
"""
import sys
import json


def detect_secret_leaks(text_content: str):
    import re
    patterns = [r"AKIA[0-9A-Z]{16}", r"ghp_[a-zA-Z0-9]{36}", r"-----BEGIN PRIVATE KEY-----"]
    found = [p for p in patterns if re.search(p, text_content)]
    has_leak = len(found) > 0
    return {"secrets_found": len(found), "has_leak": has_leak, "status": "LEAK_DETECTED" if has_leak else "SECRETS_ABSENT"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "secret-leak-detector"}))
