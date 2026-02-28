---
name: parsing-sec-filings
description: Extracts structured facts from SEC filings and earnings documents. Use when the user mentions 10-K, 10-Q, 8-K, EDGAR, MD&A, risk factors, or filing-based financial analysis.
---

# Parsing SEC Filings

## When to use this skill
- When the task requires reading 10-K, 10-Q, or 8-K filings.
- When the user asks for filing-based facts, not market rumors.
- When downstream valuation or quality analysis needs source-grounded evidence.

## Workflow

1. Plan
- Confirm ticker, legal entity, period, and required filing types.
- Define required sections before reading: Business, Risk Factors, MD&A, Financial Statements, Footnotes.

2. Validate
- Verify source is SEC EDGAR (or explicitly stated official filing source).
- Verify filing date, period end date, and accession number.
- Verify company identity (ticker to CIK or issuer name).

3. Execute
- Extract only relevant sections for the user question.
- Build a structured evidence table with section name, short quote, and filing citation.
- Separate hard facts from management narrative.

## Instructions

- Always attach citations in this format:
  - `source: <form type> | <filing date> | <accession or URL> | <section>`
- Prefer the latest annual filing plus latest quarterly filing when both are relevant.
- If the user asks trend questions, compare at least two periods.
- Normalize number units (thousands/millions) before reporting.
- Explicitly flag language that is forward-looking or non-GAAP.

### Extraction checklist

- [ ] Correct issuer and reporting period
- [ ] Correct filing type(s)
- [ ] Core sections captured
- [ ] Key accounting notes captured (debt, SBC, goodwill, contingencies)
- [ ] Citations attached to every key claim

### Output template

```markdown
## Filing Extraction Summary: <Company> (<Period>)

### Key Facts
- <fact 1> (source: ...)
- <fact 2> (source: ...)

### Management Narrative (Needs Judgment)
- <statement 1> (source: ...)

### Data Quality Notes
- Missing sections: <none or list>
- Unit normalization assumptions: <notes>
```

## Error handling

- If a required filing is missing, state exactly which form/period is unavailable.
- If sources conflict, present both values with citations and mark as unresolved.
- If filing text cannot be parsed, return partial extraction with a clear gap list.

## Resources

- SEC EDGAR official search and APIs

