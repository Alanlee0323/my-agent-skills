# CI/CD Workflow Guide for LB-ASM-X2648

## Overview
This project uses a "Test-Driven Deployment" strategy. Code must pass through the `develop` branch (on AMD hardware) before reaching `main` (on Nvidia hardware).

## Environments

| Environment | Branch | Host IP | Hardware Profile | Trigger |
| :--- | :--- | :--- | :--- | :--- |
| **amd-test** | `develop` | `192.168.137.51` | `rocm` (AMD GPU) | **Auto** on push |
| **nv-4080** | `main` | `10.1.53.203` | `cuda` (Nvidia GPU) | **Manual** after MR |

## Step-by-Step Workflows

### 1. Daily Development (Feature Flow)
1.  **Start**: Create a new branch from `develop`.
    ```bash
    git checkout develop
    git pull origin develop
    git checkout -b feat/my-new-feature
    ```
2.  **Work**: Code, test locally.
3.  **Push**: Push to GitLab.
    ```bash
    git push origin feat/my-new-feature
    ```
4.  **Merge to Develop**: Create a Merge Request (MR) from `feat/my-new-feature` to `develop`.
5.  **Auto Deploy**: Once merged, GitLab CI will automatically run `deploy_amd_test`.
6.  **Verify**: Log in to 192.168.137.51 or check the Artifacts in GitLab to confirm it works.

### 2. Production Release (Release Flow)
1.  **Pre-requisite**: Ensure `develop` is stable.
2.  **Create MR**: create MR from `develop` to `main`.
3.  **Approve**: Manager or Peer Review.
4.  **Merge**: Click Merge.
5.  **Wait**: The pipeline for `main` will be created usually in "Pending" or "Manual" state.
6.  **Deploy**: Go to CI/CD -> Pipelines. Find the latest `main` pipeline. Click the **Play** (▶️) button on `deploy_nvidia_4080`.

### 3. Hotfix (Emergency Fix)
1.  **Start**: Branch from `main` (because `develop` might have unstable new features).
    ```bash
    git checkout main
    git pull origin main
    git checkout -b hotfix/critical-bug
    ```
2.  **Fix**: Apply the fix.
3.  **Deploy to Test**: Temporarily push this hotfix branch to `develop` (or merge to develop) to test on AMD first.
4.  **Merge to Main**: MR `hotfix` -> `main`. Deploy manually.
5.  **Backport**: MR `hotfix` -> `develop` to ensure the fix exists in future versions.

### 4. Rollback (Emergency Restore)
**If the new version crashes on production:**

#### Method A: GitLab Retry (Fastest)
1.  Go to CI/CD -> Pipelines.
2.  Find the **Previous Successful Pipeline** (the one before the crash).
3.  Click **Retry** on the `deploy_nvidia_4080` job.
4.  This redeploys the old Docker image.

#### Method B: Git Revert (Cleanest)
1.  `git revert -m 1 <commit-hash-of-bad-merge>`
2.  Push to `main`.
3.  Deploy manually.
