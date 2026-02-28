---
name: normalizing-financial-statements
description: Standardizes raw financial statements into a consistent analysis schema. Use when the user asks for ratio analysis, trend comparison, or cross-company financial comparison.
---

# Normalizing Financial Statements

## When to use this skill
- When data comes from mixed sources and needs a single schema.
- When the user asks for multi-year trend analysis.
- When valuation or screening depends on comparable line items.

## Workflow

1. Plan
- Define required periods (TTM, FY, quarterly history).
- Define mandatory fields for income statement, balance sheet, and cash flow.

2. Validate
- Confirm units/currency for each source.
- Confirm period alignment (fiscal year vs calendar year).
- Confirm sign conventions (for example, capex usually reported as negative cash flow).

3. Execute
- Map source line items to canonical fields.
- Adjust one-time items if explicitly requested.
- Output normalized table plus transformation notes.

## Instructions

- Use a canonical schema with stable keys.
- Keep original value and normalized value traceable.
- Do not silently fill missing values; use `null` and explain.
- Distinguish reported metrics from adjusted metrics.

### Canonical fields (minimum)

- Revenue
- GrossProfit
- OperatingIncome
- NetIncome
- EBITDA (if available)
- OperatingCashFlow
- Capex
- FreeCashFlow
- CashAndEquivalents
- TotalDebt
- SharesOutstanding

### Validation checklist

- [ ] All periods use consistent units/currency
- [ ] Fiscal periods aligned
- [ ] Accounting identities checked (basic reasonableness)
- [ ] Missing fields documented
- [ ] Adjustments explicitly labeled

### Output template

```markdown
## Normalized Financials: <Company>

### Dataset Scope
- Periods: <...>
- Currency: <...>
- Unit: <...>

### Normalized Table
| Field | Period | Reported | Normalized | Notes |
|---|---:|---:|---:|---|
| Revenue | FY2025 | ... | ... | ... |

### Data Gaps
- <gap 1>

### Transform Notes
- <mapping or adjustment note>
```

## Error handling

- If units are unknown, stop and request clarification before ratio outputs.
- If a key field is missing, continue with partial model and mark confidence as reduced.
- If period mapping is ambiguous, return multiple candidate mappings and ask user to choose.

## Resources

- Filing extraction outputs from `parsing-sec-filings`

