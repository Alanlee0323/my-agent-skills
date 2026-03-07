# Debugging Practical Reference

Use this file when running root-cause analysis before applying a fix.

## 1. Goal
- Replace guess-based fixes with evidence-based diagnosis.
- Localize failure to a specific layer, state transition, and input condition.

## 2. Evidence-First Rules
- Verify input payloads, config values, and environment variables.
- Verify external dependencies (DB, cache, APIs, queues) with direct checks.
- Treat all assumptions as unverified until observed in logs, traces, or tests.

## 3. Isolation Strategy

### 3.1 Binary partition
- Split by subsystem: ingestion vs processing vs output.
- Split by boundary: frontend vs backend vs infra.
- Split by domain: logic defect vs state corruption vs data contract mismatch.

### 3.2 Upstream and downstream mapping
- Upstream: who calls this module and with what contract.
- Downstream: what consumers depend on this output and what can regress.

## 4. Observability Checklist
- Capture one failing request path with correlation/trace ID.
- Inspect logs before, during, and after the failure window.
- Compare local/staging/production configuration deltas when behavior diverges.

## 5. Fix Validation Checklist
- Reproduce failure with a deterministic test or command.
- Apply minimal fix that addresses the confirmed root cause.
- Re-run failing test and adjacent regression checks.
- Verify no contract break for identified downstream consumers.

## 6. Escalation Signals
- Failure is non-deterministic and cannot be reproduced reliably.
- Multiple candidate root causes remain after isolation.
- Observability gaps prevent confidence in root-cause confirmation.
