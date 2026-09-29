# Explainability, Auditability & Decision Logic: GitPromptShield

This document details the transparent decision architecture, algorithmic criteria, data provenance, and operational boundaries of **GitPromptShield**, ensuring complete compliance with OpenGAP standards and Checkpoint 02 requirements.

---

## 1. Input Data and Data Sources Used

**GitPromptShield** ingests structured, machine-verifiable data artifacts from well-defined sources to ensure total repeatability:
- **Raw**: Raw user prompt strings and conversational message arrays.
- **LLM**: LLM inference completion buffers and streaming chunks.
- **OWASP**: OWASP Top 10 for LLM adversarial exploit signatures.
- **OpenGAP Specification Manifests**: Ingests `agent.yaml`, `RULES.md`, and local state from `memory/MEMORY.md`.

All data sources are parsed deterministically without dynamic external unverified calls, ensuring that evaluations reflect the exact state of the repository at the moment of inspection.

---

## 2. How It Decides and Reasoning Process

The decision pipeline operates through a multi-stage validation sequence designed to eliminate subjective ambiguity:

1. **Syntax & Schema Verification**: Ingested inputs are first validated against strict JSON and YAML schemas defined in `tools/`. Any malformed payloads are immediately rejected.
2. **Deterministic Metric Extraction**:
   - **scan_injection_patterns**: Uses `injection-pattern-scanner` to calculate detects instruction overrides, system prompt leak requests, and adversarial boundary markers.
   - **analyze_jailbreak_heuristics**: Uses `jailbreak-heuristic-analyzer` to calculate computes adversarial semantic score for multi-turn roleplay bypasses and hypotheticals.
   - **detect_secret_leaks**: Uses `secret-leak-detector` to calculate scans strings for high-entropy api tokens, private keys, and credential strings.
3. **Policy Boundary Checks**: Extracted metrics are evaluated against the non-negotiable rules defined in `RULES.md`.
4. **Verdict Synthesis**:
   - **`APPROVED`**: Issued when all criteria strictly pass thresholds, zero compliance violations are detected, and data integrity is certified.
   - **`NEEDS_REVIEW`**: Issued when borderline metrics or ambiguous edge cases require human supervisor assessment.
   - **`BLOCKED`**: Issued immediately upon detecting any violation of zero-tolerance rules, severe risk factors, or non-compliant parameters.

When an incoming prompt is inspected, the agent runs injection_pattern_scanner, jailbreak_heuristic_analyzer, and secret_leak_detector. If zero injection patterns and zero secrets are detected, it issues APPROVED. If suspicious token manipulation is found, it issues NEEDS_REVIEW. If an explicit jailbreak payload or API key leak is verified, it issues BLOCKED.

---

## 3. Constraints, Limitations, and Known Issues

To ensure reliable and safe operation, the following constraints and operational boundaries apply:
- **Runs**: Runs with deterministic regex and heuristic scoring (temperature = 0.1) to avoid non-deterministic security evasion.
- **Does**: Does not decrypt end-to-end encrypted user payloads prior to ingress API boundary.
- **Zero**: Zero false-positive tolerance for high-entropy secret token signatures.
- **Deterministic Execution Constraint**: All model prompts and evaluations must run with low temperature (`0.1`) to ensure predictable, reproducible scoring and eliminate hallucinated findings.
- **Human Authority**: The agent cannot self-execute irreversible external mutations; final approval is reserved strictly for human authorities as specified in `DUTIES.md`.
