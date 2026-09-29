"""
injection_pattern_scanner.py - Detects instruction overrides, system prompt leak requests, and adversarial boundary markers
"""
import sys
import json


def scan_injection_patterns(prompt_text: str):
    import re
    patterns = [r"ignore (all )?previous instructions", r"system prompt", r"you are now (dan|unrestricted)", r"disregard (rules|safety)"]
    found = [p for p in patterns if re.search(p, prompt_text, re.IGNORECASE)]
    is_safe = len(found) == 0
    return {"is_safe": is_safe, "violations": found, "status": "CLEAN_PROMPT" if is_safe else "INJECTION_BLOCKED"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "injection-pattern-scanner"}))
