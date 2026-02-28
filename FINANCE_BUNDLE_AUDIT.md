# Finance Bundle Audit

## Scope

Audit target:
- `bundles/finance.yaml`
- All skills currently referenced by the finance bundle

Audit objective:
- Ensure skills are finance-domain aligned
- Detect engineering-only leakage
- Check evidence quality, review rigor, and long-term investing fit

---

## Verdict

`WARN` (acceptable for rollout after noted cautions)

Reason:
- Domain fit is now strong and mostly finance-pure.
- One skill is cross-domain meta tooling (`creating-skills-from-knowledge-folder`) and should be treated as an ops skill, not default analysis flow.

---

## Skill-by-Skill Assessment

| Skill | Verdict | Domain Fit | Notes |
|---|---|---|---|
| `planning-financial-analysis` | PASS | High | Good finance planning entrypoint, clear sequencing and gates. |
| `parsing-sec-filings` | PASS | High | Primary-source discipline is strong; citation contract is explicit. |
| `normalizing-financial-statements` | PASS | High | Strong schema/units controls; good anti-hallucination behavior. |
| `analyzing-business-quality` | PASS | High | Good long-horizon quality lens with bull/bear balance. |
| `valuing-company` | PASS | High | Proper scenario range and sensitivity mindset; avoids false precision. |
| `analyzing-macro-regime` | PASS | High | Good macro-to-investment mapping and invalidation triggers. |
| `managing-long-term-investment-policy` | PASS | High | Strong behavioral and policy guardrail framing. |
| `verifying-financial-conclusions` | PASS | High | Correctly enforces primary web sources and claim-level verification. |
| `reviewing-financial-analysis` | PASS | High | Findings-first review discipline and bias checks are appropriate. |
| `conducting-investment-postmortem` | PASS | High | Process-oriented postmortem with clear attribution taxonomy. |
| `creating-skills-from-knowledge-folder` | WARN | Medium | Useful global meta-skill, but not a day-to-day finance analysis module. Keep in bundle only if you intentionally want skill-authoring capabilities available in finance sessions. |

---

## Critical/High Findings

No `FAIL` findings.

No `Critical` findings.

No `High` findings.

---

## Medium Findings

1. Cross-domain meta skill inside finance flow
- Skill: `creating-skills-from-knowledge-folder`
- Impact: Can consume routing budget for skill-authoring tasks that are unrelated to normal financial analysis.
- Recommendation:
  - Option A: keep it in finance bundle but only trigger when user explicitly asks for skill generation.
  - Option B: move to a dedicated `ops` or `skill-authoring` bundle and invoke on demand.

---

## Bundle Composition Review

Current finance bundle composition is domain-correct and no longer contains engineering-only leakage such as:
- `planning-implementation`
- `handling-review`
- `conducting-postmortem` (engineering/ML version)

These have been replaced by finance-specific counterparts.

---

## Suggested Guardrails for Production Use

1. Keep `max_skill_reads` at 5 for finance bundle due to increased module count.
2. For final outputs, require:
- claim citations
- data timestamp
- confidence level
- contradiction/disconfirming evidence section
3. Enforce `verifying-financial-conclusions` before high-stakes final recommendations.

---

## Go/No-Go Recommendation

Go with caution:
- Ready for finance-agent rollout.
- Track real usage for 1-2 weeks and then decide whether to keep `creating-skills-from-knowledge-folder` inside finance bundle or split it to ops.

