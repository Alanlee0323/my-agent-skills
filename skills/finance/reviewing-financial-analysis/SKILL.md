---
name: reviewing-financial-analysis
description: Audits financial analysis outputs for evidence quality, assumption integrity, and bias control. Use when the user asks to review, challenge, or validate a thesis before decision-making.
---

# Reviewing Financial Analysis

## When to use this skill
- When a financial conclusion must be quality-checked before action.
- When the user asks for challenge, red-team, or assumption review.
- When analysis may be affected by narrative bias or stale data.

## Workflow

1. Plan
- Define what is being reviewed: model, memo, thesis, or recommendation.
- Define review dimensions: source quality, assumptions, method validity, risk completeness.

2. Validate
- Confirm every key claim has source evidence.
- Confirm assumptions are explicit and internally consistent.
- Confirm uncertainty is represented with ranges/scenarios.

3. Execute
- Produce a findings-first audit.
- Label issues by severity (Critical/High/Medium/Low).
- Provide concrete remediation steps.

## Instructions

- Prioritize factual integrity over persuasive writing.
- Reject single-point certainty when sensitivity is high.
- Require downside and disconfirming evidence.
- Flag these anti-patterns:
  - No citations for key claims
  - Narrative-only conclusions
  - Hidden assumptions
  - Recency bias
  - Confirmation bias

### Review checklist

- [ ] Evidence traceability check
- [ ] Assumption consistency check
- [ ] Method appropriateness check
- [ ] Sensitivity and scenario check
- [ ] Risk disclosure check
- [ ] Bias check

### Output template

```markdown
## Financial Analysis Audit

### Verdict
- Status: <PASS/WARN/FAIL>

### Findings (by severity)
1. [Critical] <issue> | Why it matters: <...> | Fix: <...>
2. [High] <issue> | Why it matters: <...> | Fix: <...>

### Confidence Statement
- Confidence: <High/Medium/Low>
- Primary uncertainty drivers: <...>
```

## Error handling

- If source evidence is missing, fail review until evidence is attached.
- If methods mismatch the question type, require method replacement.
- If uncertainty is underreported, block final recommendation.

## Resources

- `normalizing-financial-statements`
- `valuing-company`
- `analyzing-macro-regime`
- `analyzing-business-quality`

