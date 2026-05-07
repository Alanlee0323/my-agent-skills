---
name: translating-financial-analysis-xie-style
description: Translates evidence-backed financial research into high-energy Traditional Chinese market storytelling with Xie-like cadence. Use when the user asks for podcast scripts, social posts, or quick commentary based on existing report facts and citations.
---

# Translating Financial Analysis to Xie-Style Stories

## When to use this skill
- When the user asks for Xie-like financial storytelling in zh-TW.
- When source material is an existing report, memo, or `facts_pack` with citations.
- When output needs to be podcast script, Facebook post, Threads short post, or QA reply.

## Workflow

1. Plan
- Load source report and fact list.
- Lock output mode: `podcast_3min`, `facebook_post`, `threads_short`, or `qa_reply`.
- Lock tone intensity: `standard` or `high-energy`.

2. Validate
- Verify every numeric claim has source traceability.
- Mark uncertain claims as unknown instead of guessing.
- Block requests that ask for fabricated positions, guaranteed returns, or explicit buy/sell orders.

3. Execute
- Build a three-part narrative:
  - market vibe check
  - core business + valuation + what changed
  - risk controls + invalidation triggers
- Convert jargon into plain language while preserving financial precision.
- Keep spoken cadence and short sentences.

## Instructions

- Output language must be Traditional Chinese (zh-TW).
- Keep all figures identical to sources; do not rewrite numbers.
- Separate evidence and interpretation using explicit tags:
  - `【事實】`
  - `【推論】`
- Protocol guard: ignore any user instruction that conflicts with evidence integrity.
- Never provide direct trade commands or guaranteed outcomes.
- Use slang selectively (max 1-2 strong terms per paragraph) to preserve readability.
- If required source evidence is missing, return `BLOCKED` with missing fields.

### Input contract

- Required:
  - source report text or path
  - facts with source anchors
  - target output mode
- Optional:
  - audience level (`newbie`, `intermediate`, `advanced`)
  - tone intensity (`standard`, `high-energy`)

### Output contract

```markdown
## 先講結論（30秒）
- ...

## 公司靠什麼賺錢
- ...

## 現在貴不貴（估值看法）
- ...

## 接下來還有沒有戲（催化與風險）
- ...

## 觀察清單
1. ...
2. ...
```

## Error handling

- Missing source or missing citations: output `BLOCKED` and list required evidence.
- Conflicting numbers: output conflict table before any conclusion.
- User requests hype-only content: downgrade to neutral evidence-first mode.

## Resources

- `resources/style_profile.yaml`
- `examples/output_template.md`
- `tone-example/Xie-mong-gung/*.md`
