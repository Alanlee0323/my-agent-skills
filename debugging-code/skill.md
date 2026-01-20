---
name: debugging-code
description: Triggers when runtime errors occur, tests fail, or the user asks to debug/fix code. Enforces Root Cause Analysis and Defensive Programming.
---

# Debugging & Error Handling Protocol

When the user requests a fix for an error, do not just patch the specific line. You must improve the system's resilience.

## Core Instructions (SOP)

### 1. 🛑 Stop & Analyze
- **Do NOT blind guess**: Do not output fix code immediately.
- **Analyze Traceback**: Read the error stack carefully. Identify:
    - Error Type (e.g., `AttributeError`, `KeyError`).
    - Exact Line Number.
    - **Variable State**: Hypothesize what the variable value might be (e.g., `None`, empty string, wrong Type).

### 2. 🔍 Root Cause Tracing
- **Reasoning Language**: You must perform your internal reasoning (Rubber Ducking) in **English** to ensure logical precision.
- **Communication Language**: You must explain the finding and talk to the user in **Traditional Chinese (繁體中文)**.
- **Context**: If the cause is unclear (e.g., missing logs), **do not guess**.
    - Ask the user to insert `print()` or `logging.debug()`.
    - Or ask for `repr()` of the variable.

### 3. 🛡️ Defense in Depth (Python Edition)
- **Fix & Fortify**:
    - Do not just mask errors with `try...except`. Check Pre-conditions first.
    - **Type Safety**: If fixing a function signature, enforce **Type Hints** (`typing` module).
    - **Logging**: Inside exception blocks, ensure `logger.exception()` is used, not just `pass`.
    - **Fail Safe**: Ensure Graceful Degradation (e.g., return default value instead of crash).

### 4. ✅ Verification
- **Proof of Work**: You must provide a verification method after the fix.
    - **Primary**: A short `assert` script or `pytest` case.
    - **Secondary**: A Python REPL reproduction sequence.

## Example Output Format

When debugging, structure your response as follows:

> **🧐 Analysis**
> [Analyze the root cause in Traditional Chinese. Mention variable states.]
>
> **🦆 Logic Trace**
> [Explain the logical chain of the error in Traditional Chinese.]
>
> **🛠️ Fix & Defense**
> [Provide the fix, including Type Hints and Error Handling.]
>
> **🧪 Verification**
> [Provide the test code.]
