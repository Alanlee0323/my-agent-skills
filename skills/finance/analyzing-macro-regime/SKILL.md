---
name: analyzing-macro-regime
description: Interprets macroeconomic regime shifts and links them to sector and valuation implications. Use when the user asks about inflation, rates, growth cycles, policy stance, or macro risk scenarios.
---

# Analyzing Macro Regime

## When to use this skill
- When the user asks for top-down macro context.
- When investment conclusions need rate/inflation/growth framing.
- When scenario planning requires macro sensitivity.

## Workflow

1. Plan
- Define the regime question (inflationary slowdown, disinflationary growth, recession risk, etc.).
- Select required indicators before analysis.

2. Validate
- Confirm indicator timestamps and release windows.
- Confirm geography and period consistency.

3. Execute
- Build a compact regime view from indicators.
- Translate regime into sector/asset implications.
- List leading indicators that could invalidate the view.

## Instructions

- Use a fixed indicator set unless user scope says otherwise:
  - Inflation trend
  - Policy rate and real rate direction
  - Labor market momentum
  - Growth momentum
  - Credit/financial conditions
- Distinguish level vs direction (high inflation vs falling inflation).
- Separate cyclical signals from structural narratives.
- Tie macro view to valuation impact, not just story.

### Regime checklist

- [ ] Indicator dates and sources stated
- [ ] Current regime hypothesis stated
- [ ] Alternative regime stated
- [ ] Portfolio or sector implications stated
- [ ] Invalidation triggers stated

### Output template

```markdown
## Macro Regime Assessment

### Current Regime Hypothesis
- <regime label>
- Confidence: <High/Medium/Low>

### Indicator Snapshot
| Indicator | Latest | Direction | Interpretation |
|---|---:|---|---|
| Inflation | ... | ... | ... |
| Policy Rate | ... | ... | ... |

### Investment Implications
- Sector tilt: <...>
- Valuation pressure/support: <...>

### Invalidation Triggers
- <trigger 1>
```

## Error handling

- If key macro data is stale, state staleness and reduce confidence.
- If indicators conflict, present competing regime views.
- If user asks for precision not supported by data, provide scenario ranges instead.

## Resources

- Official macro data sources (for example: FRED, BEA, BLS)

