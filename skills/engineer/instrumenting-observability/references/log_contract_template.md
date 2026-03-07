# 📄 Log Contract Template

Use this template to define the observability agreement before instrumentation.

## 1. Core Fields (Required for ALL logs)
These fields ensure basic traceability and system state.
- `timestamp`: ISO8601 with timezone.
- `level`: INFO, WARN, ERROR, FATAL.
- `event`: `<domain>.<action>.<stage>` (e.g., `order.payment.start`).
- `service`: Service name.
- `env`: production, staging, dev.
- `version`: Git commit hash or version tag.

## 2. Contextual Fields (When Applicable)
Include these based on the operation type.

### For Request/Response Flows:
- `trace_id`: End-to-end correlation ID.
- `request_id`: Individual request ID.
- `latency_ms`: Duration of the operation.
- `outcome`: `success` or `failure`.

### For Decision Points & Logic:
- `decision_reason`: Human-readable reason for choosing a branch.
- `reason_code`: Machine-readable code (e.g., `INSUFFICIENT_FUNDS`).
- `params_snapshot`: Redacted key-value pairs (Allowlist-only).

### For Exceptions:
- `error_class`: Exception type name.
- `error_code`: Domain-specific error code.
- `message`: Sanitized error message (PII-free).

## 3. Sampling Policy
- **High-Frequency Loops**: Aggregate (e.g., "processed 100 items") or sample 1%.
- **Health Checks**: Log only on state change (UP -> DOWN).
