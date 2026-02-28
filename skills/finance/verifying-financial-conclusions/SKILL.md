---
name: verifying-financial-conclusions
description: Verifies financial conclusions against primary web sources such as official company investor-relations pages and regulatory filings. Use when the user asks to fact-check analysis outputs, validate assumptions, or review summaries before final decisions.
---

# Verifying Financial Conclusions

## When to use this skill
- When a financial summary or recommendation needs source verification.
- When the user asks to check claims against official websites.
- Before finalizing high-stakes conclusions (valuation, thesis change, risk alerts).

## Workflow

1. Plan
- Identify which claims must be verified (numbers, dates, guidance, events, policies).
- Build a source priority list for each claim.

2. Validate
- Confirm source quality hierarchy:
  - Primary: SEC filings, company IR pages, official transcripts/releases
  - Secondary: Reputable data portals with citations
  - Tertiary: Commentary sources (use only for context, not final evidence)
- Confirm publication date and period relevance.

3. Execute
- Retrieve evidence for each claim from primary sources.
- Compare original claim vs verified value.
- Classify result: Confirmed / Partially Confirmed / Contradicted / Unverifiable.
- Produce a verification report with citations and correction actions.

## Instructions

- Prefer primary sources over all others.
- Include explicit source metadata:
  - URL
  - publication date
  - section/title anchor
  - retrieval timestamp
- If claim cannot be verified, mark as `Unverifiable` and lower confidence.
- Never overwrite contradictory evidence; preserve both and explain discrepancy.
- Respect site terms and access controls:
  - Do not bypass authentication/paywalls
  - Do not ignore robots/usage restrictions when scraping

### Verification checklist

- [ ] Claims list defined
- [ ] Primary source candidates mapped per claim
- [ ] Date/period consistency checked
- [ ] Evidence captured with metadata
- [ ] Claim status assigned
- [ ] Corrections and confidence updates applied

### Output template

```markdown
## Financial Conclusion Verification Report

### Verification Scope
- Claims reviewed: <count>
- Primary sources used: <list>

### Claim-Level Results
| Claim | Original | Verified | Status | Source |
|---|---|---|---|---|
| <claim 1> | ... | ... | Confirmed | <URL/date/section> |

### Contradictions / Gaps
- <item>

### Required Corrections
- <correction 1>

### Final Confidence
- Updated confidence: <High/Medium/Low>
```

## Error handling

- If primary sources are unavailable, return partial verification and mark confidence downgrade.
- If only secondary sources are available, label result as provisional.
- If source dates are stale for the analysis period, block final conclusion and request newer evidence.

## Resources

- `parsing-sec-filings`
- `reviewing-financial-analysis`

