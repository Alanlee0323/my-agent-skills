# 🛡️ Redaction & Data Protection Guide (Hardened)

Strict adherence to this guide is mandatory to prevent PII/Secret leaks.

## 1. Allowlist-First Policy (Non-Negotiable) ⚪
If a field is not explicitly on this list, it **MUST** be redacted.

### Safe Fields
- `order_id`, `transaction_id`, `trace_id`
- `status`, `stage`, `outcome`, `reason_code`
- `count`, `size`, `latency_ms`, `cpu_usage`
- `env`, `version`, `service_name`

### Sensitive / Conditional (Check Project Policy)
- `user_id`: May be considered PII in some jurisdictions (GDPR/CCPA). Use hashing if required.
- `resource_name`: Ensure it doesn't contain user names or IDs.

## 2. Global Hard Blacklist (NEVER LOG) 🛑
Intercept and redact these immediately:
- **Auth**: `password`, `token`, `api_key`, `auth_header`, `cookie`, `secret`, `private_key`.
- **Identity**: `email`, `phone`, `mobile`, `address`, `ssn`, `birth_date`, `credit_card`.
- **Payloads**: `request_body`, `response_body`. **Rule: Only log key-value summaries of specific safe fields.**

## 3. Data Sanitization Rules
- **No Raw Dumps**: Never use `str(request_object)` or `json.dumps(payload)`.
- **Truncation**: String fields exceeding 512 chars must be truncated.
- **Hashing**: If an ID must be tracked but is PII (like email), use salted SHA-256.
