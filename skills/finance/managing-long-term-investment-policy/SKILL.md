---
name: managing-long-term-investment-policy
description: Defines and maintains long-term investment policy guardrails. Use when the user asks for portfolio discipline, rebalancing rules, risk limits, or decision frameworks for multi-year investing.
---

# Managing Long-Term Investment Policy

## When to use this skill
- When the user wants a long-horizon investing framework.
- When decisions need consistency across market cycles.
- When emotion-driven decision risk needs guardrails.

## Workflow

1. Plan
- Define objective, time horizon, liquidity needs, and risk tolerance.
- Define policy structure before discussing specific securities.

2. Validate
- Confirm constraints are explicit (drawdown tolerance, max position size, diversification rules).
- Confirm assumptions are realistic for the stated horizon.

3. Execute
- Draft a policy checklist and decision rubric.
- Define rebalancing and monitoring cadence.
- Define "do not violate" rules.

## Instructions

- Prioritize process quality over short-term prediction.
- Require decision logs for thesis changes.
- Include base rules:
  - Position sizing limits
  - Rebalance bands and cadence
  - Thesis invalidation criteria
  - Maximum leverage or debt exposure constraints
- Force pre-mortem and downside scenarios before large allocation changes.

### Policy checklist

- [ ] Time horizon defined
- [ ] Risk budget defined
- [ ] Allocation rules defined
- [ ] Rebalancing rules defined
- [ ] Thesis update protocol defined
- [ ] Behavioral guardrails defined

### Output template

```markdown
## Long-Term Investment Policy

### Objective and Horizon
- Objective: ...
- Horizon: ...

### Risk and Allocation Rules
- Max position size: ...
- Target allocation bands: ...
- Max drawdown tolerance: ...

### Rebalancing Rules
- Cadence: ...
- Trigger bands: ...

### Thesis Governance
- Required evidence to add/increase: ...
- Invalidation triggers: ...
- Exit or reduce rules: ...
```

## Error handling

- If objectives and risk tolerance conflict, stop and request prioritization.
- If user asks for policy-breaking action, flag violation and present compliant alternative.
- If data quality is weak, defer action and state required evidence.

## Resources

- `valuing-company`
- `analyzing-macro-regime`
- `analyzing-business-quality`

