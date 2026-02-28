---
name: analyzing-business-quality
description: Evaluates long-horizon business quality using durable economics, governance signals, and capital allocation behavior. Use when the user asks about moat, quality, or long-term compounding potential.
---

# Analyzing Business Quality

## When to use this skill
- When the user asks whether a company is high quality over long horizons.
- When valuation depends on durability of margins and returns.
- When comparing multiple companies beyond headline growth rates.

## Workflow

1. Plan
- Define evaluation dimensions: moat, pricing power, reinvestment runway, balance-sheet resilience, governance.
- Set analysis horizon (for example, 5-10 years).

2. Validate
- Check that claims are grounded in filings, transcripts, or normalized financials.
- Check that time horizon and industry context are explicit.

3. Execute
- Score each dimension with evidence.
- Provide both supportive and contradictory signals.
- Conclude with confidence level and disconfirming triggers.

## Instructions

- Use evidence-first reasoning; no narrative-only conclusions.
- Separate structural advantages from cyclical tailwinds.
- Explicitly analyze capital allocation:
  - Reinvestment quality
  - Buybacks vs dilution
  - Debt usage discipline
- Include governance red flags if present:
  - Aggressive adjustments
  - Frequent guidance misses
  - Related-party concerns

### Quality checklist

- [ ] Moat evidence identified
- [ ] Unit economics and margin durability reviewed
- [ ] ROIC or return proxy trend reviewed
- [ ] Balance sheet resilience reviewed
- [ ] Governance quality reviewed
- [ ] Bear case included

### Output template

```markdown
## Business Quality Assessment: <Company>

### Dimension Scores (1-5)
- Moat durability: <score> | Evidence: <...>
- Pricing power: <score> | Evidence: <...>
- Capital allocation: <score> | Evidence: <...>
- Balance sheet resilience: <score> | Evidence: <...>
- Governance quality: <score> | Evidence: <...>

### Bull Case
- <point 1>

### Bear Case
- <point 1>

### Disconfirming Signals to Monitor
- <trigger 1>

### Overall Quality View
- Rating: <High/Medium/Low>
- Confidence: <High/Medium/Low>
```

## Error handling

- If evidence is insufficient, downgrade confidence and request missing sources.
- If recent data contradicts older thesis, prioritize newer evidence and explain.
- If management narrative conflicts with financial reality, present both and mark conflict.

## Resources

- `parsing-sec-filings`
- `normalizing-financial-statements`

