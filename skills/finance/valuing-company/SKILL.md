---
name: valuing-company
description: Builds transparent valuation ranges using scenario-based DCF and market multiple checks. Use when the user asks for intrinsic value, fair value range, margin of safety, or valuation sensitivity.
---

# Valuing Company

## When to use this skill
- When the user asks "Is this company undervalued or overvalued?"
- When a long-term thesis needs valuation discipline.
- When comparing base, bull, and bear assumptions.

## Workflow

1. Plan
- Define valuation methods (DCF plus relative multiple cross-check).
- Define scenario set (bear/base/bull) and key drivers.

2. Validate
- Verify assumptions have source support or explicit user-provided hypothesis.
- Verify terminal assumptions are economically plausible.
- Verify units and share counts align with normalized statements.

3. Execute
- Build scenario outputs with implied value per share.
- Run sensitivity checks (growth, margin, discount rate, terminal multiple).
- Report valuation range, not single-point certainty.

## Instructions

- Always disclose assumptions before conclusions.
- Use both intrinsic and relative lenses when possible.
- Include downside case and probability-weighted interpretation.
- Treat valuation as conditional, not deterministic.

### Minimum assumption table

- Revenue growth path
- Operating margin path
- Reinvestment or capex intensity
- Discount rate / cost of capital
- Terminal growth or exit multiple
- Net debt and diluted shares

### Valuation checklist

- [ ] Bear/base/bull scenarios included
- [ ] Sensitivity matrix included
- [ ] Margin of safety explicitly computed
- [ ] Risks that break the model identified
- [ ] Data recency timestamp included

### Output template

```markdown
## Valuation Summary: <Company>

### Assumptions
| Driver | Bear | Base | Bull |
|---|---:|---:|---:|
| Revenue CAGR | ... | ... | ... |
| Operating Margin | ... | ... | ... |
| Discount Rate | ... | ... | ... |

### Implied Value Per Share
- Bear: ...
- Base: ...
- Bull: ...

### Current Price Comparison
- Current: ...
- Base upside/downside: ...
- Margin of safety status: <Pass/Fail>

### Key Model Risks
- <risk 1>
```

## Error handling

- If critical inputs are missing, return a partial framework and list required inputs.
- If assumptions are internally inconsistent, stop and correct assumptions first.
- If results are highly sensitive, emphasize uncertainty and avoid definitive language.

## Resources

- `normalizing-financial-statements`
- `analyzing-business-quality`

