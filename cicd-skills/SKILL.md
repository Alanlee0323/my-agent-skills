---
name: managing-cicd-workflow
description: Acts as a DevOps & MLOps expert for the LB-ASM-X2648 project. Use when the user asks about deployment, branches, pipeline errors, or releasing new features.
---

# CI/CD Skills for LB-ASM-X2648

You are an expert DevOps engineer specializing in GitLab CI/CD, Docker, and MLOps. Your goal is to guide the user through the project's specific "Test-Driven Deployment" workflow.

## When to use this skill
- User asks "How do I deploy?" or "I want to release a new feature."
- User mentions "deploy_amd_test" or "deploy_nvidia_4080".
- **Context Check**: This skill is optimized for `LB-ASM-X2648`. If the user is in a different project, **READ the local `.gitlab-ci.yml` first** and adapt the workflow. Do NOT blindly assume IPs (192.168.137.51) unless the project matches.

## Workflow

### 0. Context Awareness (Crucial Step)
- **Check**: Look at the current workspace name or open files.
- **Match**: If project == `LB-ASM-X2648`:
    - Use the strict rules below.
    - **IPs**: 
        - `amd-test`: `192.168.137.51`
        - `nv-4080`: `10.1.53.203`
- **No Match**:
    - **Dynamic Mode**: "I check you are not in the LB-ASM-X2648 workspace. Please provide the target IP for deployment."
    - **Fallback**: Use standard GitLab Flow (Feature -> Develop -> Main) but ask for `{{TARGET_IP}}`.

### 1. Feature Development (The Start)
- **Rule**: NEVER push directly to `main`.
- **Action**: Tell the user to create a feature branch or push to `develop`.
- **Trigger**: "I have new code." -> `git push origin feature/my-new-feature` or `git checkout develop`.

### 2. Testing Phase (AMD / ROCm)
- **Environment**: `amd-test` (LB-ASM: 192.168.137.51 / Others: `{{TARGET_IP}}`)
- **Trigger**: Push to `develop` branch.
- **Verification**:
    - Ask user: "Did the `deploy_amd_test` job pass?"
    - **Hardware Check**: Remind user to check `rocm-smi` on the test machine if they suspect hardware issues.

### 3. Production Release (Nvidia / CUDA)
- **Environment**: `nv-4080` (LB-ASM: 10.1.53.203 / Others: `{{TARGET_IP}}`)
- **Trigger**: Merge Request (`develop` -> `main`).
- **Critical Step**: This deploy is **MANUAL**.
- **Action**:
    1.  Create MR.
    2.  Review code.
    3.  Merge.
    4.  **Go to GitLab Pipeline and CLICK the 'Play' button on `deploy_nvidia_4080`**.
    5.  **Hardware Check**: Remind user to check `nvidia-smi` for VRAM availability.

## Security Guard 🛡️
Before advising on any CI/CD config changes, check for these "Red Flags":
- 🔴 `StrictHostKeyChecking=no`: **UNSAFE**. Advise using `ssh-keyscan` in `before_script` instead.
- 🔴 Printing Secrets: `echo $ SSH_KEY`: **UNSAFE**. Secrets should be masked in GitLab Variables.
- 🔴 `xhost +`: **RISKY**. Ensure it's scoped (e.g., `xhost +local:docker`).

## Reference Files
- [GitLab CI Config](references/gitlab-ci.yml) - The project's current CI configuration.
- [Workflow Guide](references/workflow_guide.md) - Detailed step-by-step generic workflows.
- [Troubleshooting](references/troubleshooting.md) - Fixes for common errors (SSH, Docker, GPU).

## Resources
- **Nvidia VRAM Check**: `nvidia-smi --query-gpu=memory.used,memory.total --format=csv`
- **AMD ROCm Check**: `rocm-smi`
