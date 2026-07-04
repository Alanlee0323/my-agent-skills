---
name: maintaining-skill-library
description: Governance loop for this skill library. Defines the single-source-of-truth map, the validation workflow, the definition of done for adding or changing skills, the evolution-log convention, and the periodic drift audit. Use when adding, renaming, moving, or retiring a skill, when updating bundles or routing, or when the user asks 維護, 盤點, 一致性檢查, or library health.
version: 1.0.0
---

# Maintaining the Skill Library

This library grows by accretion (new skills after each learning) and decays by drift
(names, routes, bundles, and indexes silently diverging). This skill is the counter-force
to drift. **Run it whenever the library changes shape.**

## Single Source of Truth Map（唯一事實來源地圖）

Every fact has exactly one owning location. Everything else is derived and must be
regenerated or cross-checked — never hand-edited into agreement.

| Fact | Owner (source of truth) | Derived copies (must match) |
|---|---|---|
| Skill identifier | `SKILL.md` frontmatter `name` | folder name, `global-rules.md` routes, `bundles/*.yaml`, `SKILL_INDEX.md`, cross-references in other skills |
| Skill purpose & triggers | frontmatter `description` | `SKILL_INDEX.md`, readme commentary |
| Bundle composition | `bundles/*.yaml` | profiles, compiled adapters |
| Governance rules | `policies/base.yaml` + `global-rules.md` | — |
| Complete skill list | filesystem (`skills/**/SKILL.md`) | `SKILL_INDEX.md` (generated), readme inventory |

**Invariant: `name` == folder name == routing token.** One identifier, everywhere.

## The Validation Workflow（每次變更的必經之路）

```bash
python tools/validate_skills.py          # exit 0 = clean; non-zero lists violations
python tools/generate_skill_index.py     # regenerate SKILL_INDEX.md after any change
```

Run **before** starting (to confirm a clean baseline) and **after** finishing (to prove
the change introduced no drift). If the validator itself lacks a check that would have
caught your bug, add the check — the validator is the library's immune system and must
evolve with the defect classes actually observed.

## Definition of Done — adding or modifying a skill

A skill change is complete only when ALL of these hold:

- [ ] `SKILL.md` (uppercase) with valid frontmatter; `name` is gerund-form, matches folder name.
- [ ] Every file path referenced inside the skill exists in the repo (or is marked `TODO` with a placeholder README explaining what belongs there).
- [ ] Added to the appropriate `bundles/*.yaml` (or explicitly decided against — note why).
- [ ] Routing entry added to `global-rules.md` §1 if the skill should be directly triggerable.
- [ ] Reviewed via `reviewing-agent-skills`; `SKILL_AUDIT.md` written for new skills.
- [ ] Evolution Log entry appended (see convention below).
- [ ] `tools/validate_skills.py` passes; `SKILL_INDEX.md` regenerated.

## Evolution Log Convention（經驗傳承的載體）

Every skill ends with an `## Evolution Log` section. Each entry records **why** a rule
exists — this is the knowledge that survives model changes and personnel changes:

```markdown
## Evolution Log

- YYYY-MM-DD vX.Y.Z — <what changed> — 觸發事件: <the incident/lesson that motivated it>
```

Rules:
- Bump `version` in frontmatter with each substantive change (semver: guardrail additions
  are minor, rewrites are major, typo/link fixes are patch).
- The 觸發事件 field is mandatory for guardrail additions. A guardrail without its origin
  story becomes cargo cult within a year and gets deleted by someone who doesn't know
  why it was there.
- Postmortem write-backs (`conducting-postmortem`, `conducting-investment-postmortem`)
  MUST land as Evolution Log entries, not just inline edits.

## Renaming or Moving a Skill（高風險操作）

Identifiers are load-bearing. Renames must update every derived copy in one commit:

1. `grep -rn "<old-name>"` across the entire repo — enumerate all references first.
2. `git mv` the folder; update frontmatter `name`.
3. Update: `global-rules.md` routes, `bundles/*.yaml`, cross-references in other skills,
   and any adapter yaml under an `agents` directory inside the skill.
4. Run the validator; regenerate the index.
5. Note the rename in the skill's Evolution Log (old name included, for archaeology).

## Periodic Drift Audit（每季或每 10 個新 skill 執行一次）

Use `researching-deeply` methodology against the library itself:

1. **Consistency sweep**: run the validator; also manually diff `global-rules.md` §1
   against bundle contents — a MANDATORY route pointing at a skill missing from the
   bundle is a governance contradiction.
2. **Negative-space sweep**: count skills vs `SKILL_AUDIT.md` files; list skills whose
   referenced resources are placeholders still marked `TODO`.
3. **Staleness sweep**: skills referencing versioned externals (models, APIs, tool
   versions) — verify identifiers are still current (e.g., model names in `using-minimax`).
4. **Bundle-fit review**: re-run the `FINANCE_BUNDLE_AUDIT.md`-style review for any bundle
   whose composition changed since its last audit; date the audit header.
5. Write findings to a dated audit file; convert each accepted finding into either a fix
   commit or an Evolution Log entry explaining why it was declined.

## External Toolchain Registry（不在本 repo 的依賴）

The readme references tooling that lives outside this repo. Keep this table honest —
a future maintainer must be able to rebuild the whole system from this section:

| Tool | Role | Location | Status |
|---|---|---|---|
| `skill_scheduler.py` | Scans project + global skill layers, dedupes by name | consuming projects (not versioned here) | ⚠️ TODO: vendor a reference copy into `tools/` or document its canonical repo |
| `agent-bootstrap` | Compiles bundles/policies/profiles into per-agent adapters | external | ⚠️ TODO: same |

Until vendored, treat `policies/base.yaml` keys as *specification* (what the scheduler
should enforce), not as active enforcement.

## Anti-patterns（紅線）

- ❌ Hand-editing `SKILL_INDEX.md` — it is generated; edit the source frontmatter instead.
- ❌ Adding a routing rule in `global-rules.md` for a skill not present in any bundle.
- ❌ Fixing a name mismatch by editing only one of its N copies.
- ❌ Deleting a guardrail without reading its Evolution Log entry first.
- ❌ Letting a new skill skip `reviewing-agent-skills` because "it's small".

## Evolution Log

- 2026-07-04 v1.0.0 — Initial version — 觸發事件: full-library audit (Claude Fable 5 final
  session) found 7 drift defects accumulated between skill count 24→49 with no detection
  mechanism: routing name mismatch (`storytelling-financial-analysis-vincent` vs
  `translating-financial-analysis-vincent-style`), MANDATORY-routed skills absent from
  `finance.yaml`, stale readme links to `gemini-skill-*` folders, missing `tone-example/`
  corpora, `MiniMax-Text-01` leftovers, folder≠name in 7 skills, 2/49 audit coverage.
  This skill + `tools/validate_skills.py` exist so that entire defect class cannot recur silently.
