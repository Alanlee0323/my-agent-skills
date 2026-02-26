# CI/CD Workflow Guide — Trunk-Based with Branch for Release

## Overview
This guide describes a generic trunk-based development workflow with release branches. All feature work merges into `main` (the trunk); releases are cut as `release/*` branches for stabilisation.

## Environments (Template)

| Environment | Branch Pattern | Trigger | Notes |
| :--- | :--- | :--- | :--- |
| **dev/staging** | `main` or `release/*` | Auto on push | Runs lint + test + build |
| **production** | `release/*` tag | Manual or tag-based | Requires approval |

> **Note**: Actual host IPs, job names, and hardware profiles are defined in the project-specific override (`./skills/cicd-skills/SKILL.md`). Do NOT hardcode here.

## Step-by-Step Workflows

### 1. Daily Development (Feature Flow)
1.  **Start**: Create a short-lived branch from `main`.
    ```bash
    git checkout main
    git pull origin main
    git checkout -b feat/<description>
    ```
2.  **Work**: Code, test locally. Keep branch alive < 3 days.
3.  **Push**: Push to remote.
    ```bash
    git push origin feat/<description>
    ```
4.  **Open MR/PR**: Target `main`. CI runs automatically on the MR pipeline.
5.  **Review**: At least 1 approval required.
6.  **Merge**: Squash-merge or rebase-merge to keep `main` linear.

### 2. Release Preparation (Release Flow)
1.  **Cut branch**: When `main` is feature-complete for a version:
    ```bash
    git checkout -b release/<version> main
    git push origin release/<version>
    ```
2.  **Stabilise**: Only bug fixes via MR to `release/<version>`. No new features.
3.  **CI deploys** `release/*` to staging automatically.
4.  **QA**: Validate on staging environment.
5.  **Tag**:
    ```bash
    git tag v<version>
    git push origin v<version>
    ```
6.  **Production deploy**: Triggered by tag (auto or manual per project policy).
7.  **Back-merge**: Merge `release/<version>` back to `main` to capture fixes.

### 3. Hotfix (Emergency Fix)
1.  **Start**: Branch from the affected `release/*` (or `main` if no active release).
    ```bash
    git checkout -b hotfix/<issue> release/<version>
    ```
2.  **Fix**: Apply minimal change.
3.  **MR to release branch**: Merge, tag patch version `v<version>.1`.
4.  **Cherry-pick to main**: Ensure the fix propagates to trunk.

### 4. Rollback (Emergency Restore)
**If the new version crashes on production:**

#### Method A: Pipeline Retry (Fastest)
1.  Find the **previous successful pipeline** in CI/CD dashboard.
2.  Click **Retry** on the production deploy job.

#### Method B: Git Revert (Cleanest)
1.  `git revert <bad-commit>` on the release branch.
2.  Push and let pipeline redeploy.
3.  Always rollback first, investigate second.
