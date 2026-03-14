---
name: conducting-investment-postmortem
description: Performs post-mortem analysis on investment decisions to improve long-term process quality. Use when a thesis fails, underperforms expectations, or requires systematic process upgrades.
---

# Conducting Investment Post-Mortem

## When to use this skill
- After a thesis outcome materially diverges from expectations.
- After large drawdowns, unexpected underperformance, or forced exits.
- When the user asks to capture lessons and upgrade investment process.

## Workflow

1. Plan
- Define case boundary: entry thesis, holding period, expected milestones, actual outcomes.
- Define post-mortem questions before judging results.

2. Validate
- Reconstruct decision context using only time-consistent information.
- Separate process error from outcome variance.
- Verify attribution across thesis, macro, valuation, and execution.

3. Execute
- Produce root-cause analysis with evidence.
- Map each root cause to process-level guardrails.
- Update policy proposals for future decisions.

## Instructions

- Do not judge solely by PnL outcome; evaluate decision quality.
- Distinguish:
  - Thesis error
  - Valuation error
  - Macro regime mismatch
  - Position sizing/risk management error
  - Execution discipline error
- Convert lessons into concrete rule updates, not generic advice.

### Post-mortem checklist

- [ ] Original thesis and assumptions reconstructed
- [ ] Outcome vs expectation gap quantified
- [ ] Root causes categorized
- [ ] Process changes proposed
- [ ] Monitoring triggers updated

### Output template

```markdown
## Investment Post-Mortem: <Case>

### Expected vs Actual
- Expected: <...>
- Actual: <...>
- Gap: <...>

### Root Cause Analysis
1. Thesis error: <...>
2. Valuation error: <...>
3. Risk management error: <...>

### Process Upgrades
- New pre-entry check: <...>
- New sizing rule: <...>
- New invalidation trigger: <...>

### Forward Protocol
- What will be done differently next time: <...>
```

## Error handling

- If historical decision context is incomplete, explicitly mark unknowns.
- If attribution is ambiguous, present ranked hypotheses with confidence levels.
- If proposed rule changes conflict with long-term policy, escalate and resolve policy first.

## Resources

- `managing-long-term-investment-policy`
- `reviewing-financial-analysis`
- `analyzing-macro-regime`
- `attributing-portfolio-performance`（協同技能：系統性績效歸因作為 postmortem 的量化輸入）
- `sizing-portfolio-positions`（協同技能：檢討倉位規模是否為虧損主因）

