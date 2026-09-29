# Separation of Duties (SOD) & Operational Boundaries

To ensure robust compliance, security, and verification, **GitPromptShield** implements a strict tripartite Separation of Duties architecture.

---

### 1. Maker
* **Assigned Entity**: `GitPromptShield Automation Engine`
* **Responsibilities**:
  * Inspects incoming prompt tokens, detects jailbreak syntax patterns, and audits response strings for leaked credentials.
  * Ingests raw repository data, configurations, and input artifacts.
  * Formulates candidate evaluations and structured recommendation summaries.
  * Records execution logs into `memory/audit.log`.

---

### 2. Checker
* **Assigned Entity**: `GitPromptShield Verification & Policy Enforcer`
* **Responsibilities**:
  * Validates sanitization rules against OWASP Top 10 for LLMs and asserts strict perimeter defense.
  * Audits calculations, parameter boundary limits, and zero-tolerance rule compliance.
  * Asserts schema validity on all output manifests.
  * Issues preliminary assessment: `APPROVED`, `BLOCKED`, or `NEEDS_REVIEW`.

---

### 3. Approver
* **Assigned Entity**: `Chief Information Security Officer (CISO) / AppSec Lead (Reserved for human review).`
* **Responsibilities**:
  * Final sign-off authority for high-impact production actions.
  * Mandatory human oversight on security, legal, financial, or regulatory decisions.
  * Reviews unresolvable edge cases and policy override exceptions.
