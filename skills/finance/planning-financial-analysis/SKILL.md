---
name: planning-financial-analysis
description: Translates financial research questions into an executable analysis plan. Use when the user asks how to analyze a company, macro theme, or investment thesis in a structured and auditable way.
---

# Planning Financial Analysis

## When to use this skill
- When the user asks for a financial analysis plan before conclusions.
- When a thesis requires clear scope, data sources, and validation order.
- When multiple analysis modules must be sequenced (filings, normalization, valuation, macro).

## Workflow

1. Plan
- Clarify objective: screening, deep-dive, thesis validation, or monitoring.
- Define scope: company universe, period, geography, and output format.
- Define required modules and sequence.

2. Validate
- Confirm data availability and freshness constraints.
- Confirm assumptions and decision criteria.
- Confirm what "done" means for this request.

3. Execute
- Produce a step-by-step plan with explicit deliverables.
- Include validation checkpoints and stop conditions.
- Assign confidence gates before final recommendation.

## Instructions

- Do not jump to valuation before data quality checks.
- Separate analysis tasks from judgment tasks.
- Keep each step atomic and auditable.
- Prefer this module order unless user overrides:
  - filings extraction
  - statement normalization
  - business quality assessment
  - valuation
  - macro regime overlay
  - long-term policy fit

### Planning checklist

- [ ] Objective and scope documented
- [ ] Data sources and time window documented
- [ ] Module sequence documented
- [ ] Validation gates documented
- [ ] Final output contract documented

### Output template

```markdown
## Financial Analysis Plan

### Objective
- <objective>

### Scope
- Company/Universe: <...>
- Period: <...>
- Geography: <...>

### Execution Steps
1. <step> -> Deliverable: <...>
2. <step> -> Deliverable: <...>

### Validation Gates
- Gate 1: <criteria>
- Gate 2: <criteria>

### Final Output Contract
- Required sections: <...>
```

## Error handling

- If scope is ambiguous, stop and request scope lock before analysis.
- If key data source is unavailable, provide fallback plan and confidence downgrade.
- If objective conflicts with constraints, present two feasible alternatives.

## Resources

- `parsing-sec-filings`
- `normalizing-financial-statements`
- `valuing-company`
- `analyzing-macro-regime`

