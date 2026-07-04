# CI/CD Workflow Practical Reference

Use this file as the default workflow reference for trunk-based delivery with release branches.

## 1. Environment Contract

| Environment | Branch or Trigger | Deploy Type | Purpose |
|---|---|---|---|
| Staging | `main` | Auto | Integration and QA validation |
| Release Prep | `release/x.y` | N/A | Stabilization and critical fixes only |
| Production | `v*.*.*` tag | Manual or Auto | Customer-facing immutable release |

## 2. Standard Delivery Flow

### 2.1 Feature flow
1. Sync trunk:
```bash
git checkout main
git pull origin main
```
2. Create short-lived feature branch:
```bash
git checkout -b feat/<task-id>-<description>
```
3. Commit atomic changes and push for CI feedback.
4. Open PR/MR into `main` and use squash merge to keep history linear.

### 2.2 Release flow
1. Cut release branch from trunk:
```bash
git checkout -b release/1.2 main
git push origin release/1.2
```
2. Allow only critical fixes on `release/*`.
3. Run final QA on release candidate build.

### 2.3 Production flow
1. Tag from release branch:
```bash
git checkout release/1.2
git tag -a v1.2.0 -m "Release version 1.2.0"
git push origin v1.2.0
```
2. Deploy through tag-triggered production job.
3. Sync release fixes back to `main`.

### 2.4 Hotfix flow
1. Branch from affected tag or release branch:
```bash
git checkout -b hotfix/v1.2.1 v1.2.0
```
2. Apply minimal safe fix.
3. Tag and deploy patch release.
4. Merge or cherry-pick back to `main`.

## 3. Rollback Policy

Default policy: fix forward with `git revert`, or redeploy last known-good artifact.

### 3.1 Revert-based rollback
```bash
git revert <commit_id>
git push origin <target-branch>
```

### 3.2 Pipeline retry rollback
- GitLab: retry last successful production deploy job.
- GitHub: rerun last known-good production workflow run.

## 4. Guardrails
- Do not deploy production directly from feature branches.
- Keep release branches short-lived and focused on stabilization.
- Treat production tags as immutable release contracts.
- Ensure every hotfix is propagated back to trunk.

## 5. Soft Gate (Observability)
- `observability_report.md` is a manual sign-off artifact for release readiness.
- If any P0 flow is marked `needs_manual_signoff`, deployment is not auto-blocked by CI in this mode.
- Release owner must explicitly acknowledge residual risk before production tagging.

## 6. Related References
- `troubleshooting.md`: CI/CD failure patterns and mitigations.
- `gitlab-ci.yml`: Template pipeline for this delivery model.
