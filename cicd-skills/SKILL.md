---
name: managing-cicd-workflow
description: Generic trunk-based development with branch-for-release CI/CD workflow. Use when the user asks about deployment, branching strategy, pipeline errors, or releasing new features.
---

# CI/CD Workflow — Trunk-Based with Branch for Release

## When to use this skill
- User asks "How do I deploy?", "I want to release a new feature", or "Pipeline failed".
- User mentions branching strategy, release workflow, or CI/CD configuration.
- Triggers: "部署", "發版", "pipeline", "release branch", "hotfix", "deploy to production"

## Branching Model

```
main (trunk)  ──●──●──●──●──●──●──●──────────────
                │        │              ▲
                │        └─ release/1.2 ─┤─ tag v1.2.0
                │                        │─ cherry-pick hotfix
                └─ feat/xyz (short-lived)
```

- **`main`** is the single source of truth. All feature work merges here.
- **`release/*`** branches are cut from `main` when preparing a release. Only bug fixes and cherry-picks go here.
- **`feat/*`** branches are short-lived (< 3 days recommended). Merge back to `main` via MR/PR.
- **`hotfix/*`** branches fork from `release/*` or `main`, fix is cherry-picked to both.

## Workflow

### 0. Pre-Flight Check (MANDATORY)
Before any CI/CD advice:
1. **READ** the project's CI config (`.gitlab-ci.yml`, `.github/workflows/`, `Jenkinsfile`, etc.).
2. **IDENTIFY** environments, stages, and deployment targets from the config — do NOT assume.
3. **CHECK** if `./skills/cicd-skills/SKILL.md` exists for project-specific overrides. If present, defer to it for environment details.

### 1. Feature Development
- **Rule**: NEVER push directly to `main`.
- **Flow**:
  1. Branch from `main`: `git checkout -b feat/<description> main`
  2. Keep commits small and atomic.
  3. Push and open MR/PR targeting `main`.
  4. CI runs lint + test + build on the MR pipeline.
  5. Require at least 1 approval before merge.
- **Merge Strategy**: Prefer squash-merge or rebase to keep `main` linear.

### 2. Release Preparation
- **When**: Team decides `main` is feature-complete for a release.
- **Flow**:
  1. Cut branch: `git checkout -b release/<version> main`
  2. Only bug fixes allowed on this branch (no new features).
  3. CI deploys `release/*` to staging/pre-prod environment automatically.
  4. QA validates on staging.
  5. Tag: `git tag v<version>` on the release branch.
  6. Production deploy triggered by tag (auto or manual per project policy).
  7. Merge release branch back to `main` to capture any fixes.

### 3. Hotfix
- **Flow**:
  1. Branch from the affected `release/*` (or `main` if no active release): `git checkout -b hotfix/<issue> release/<version>`
  2. Apply minimal fix.
  3. MR to `release/*`, then cherry-pick to `main`.
  4. Tag a patch version: `v<version>.1`

### 4. Rollback
- **Method A — Pipeline Retry**: Re-run the last known-good deployment job.
- **Method B — Git Revert**: `git revert <bad-commit>`, push, let pipeline redeploy.
- **Rule**: Always rollback first, investigate second.

## Production Guard 🚨
**When** user asks to deploy directly to a production target:
1. **PAUSE**. Do NOT execute.
2. **VERIFY**: Is the target actually production? Check project-specific override or CI config.
3. **BLOCK** if bypassing pipeline: "Direct production deployment is blocked. Use the release pipeline."
4. **ALLOW** only if the action goes through the standard pipeline trigger (tag or manual job).

## Security Checklist 🛡️
Before advising on CI/CD config changes, scan for:
- 🔴 `StrictHostKeyChecking=no` → Replace with `ssh-keyscan` in `before_script`.
- 🔴 Secrets in logs (`echo $SECRET`) → Ensure CI variables are masked.
- 🔴 Overly permissive network access (`xhost +`) → Scope to specific containers.
- 🔴 Missing branch protection on `main` and `release/*` → Enforce required reviews.
- 🔴 No artifact expiration policy → Set `expire_in` to avoid storage bloat.

## Project-Specific Overrides
This skill provides the **generic workflow**. For project-specific details (IPs, job names, hardware, environment variables), check:
- `./skills/cicd-skills/SKILL.md` — project-local override (takes priority)
- If no override exists, ask the user for deployment targets before proceeding.

## Reference Files
- [Workflow Guide](references/workflow_guide.md) — Generic step-by-step workflows.
- [Troubleshooting](references/troubleshooting.md) — Common CI/CD error fixes.
