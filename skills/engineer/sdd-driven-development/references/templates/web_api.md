# Web API SDD Template

## 1. API Summary
- Feature name:
- Base path:
- Auth model:

## 2. Endpoint Contract
| Endpoint | Method | Purpose | Auth | Idempotent |
|---|---|---|---|---|
| `/...` | `GET/POST/...` | | | |

## 3. Request Schema
- Required fields:
- Optional fields:
- Validation rules (type/range/format):

## 4. Response Schema
- Success payload:
- Error payload:
- Pagination/sorting/filter contract:

## 5. Status Codes and Errors
| Case | Status | Error Code | Message |
|---|---|---|---|
| Success | 200 | - | - |
| Validation failure | 400 | | |
| Unauthorized | 401 | | |
| Forbidden | 403 | | |
| Not found | 404 | | |
| Conflict | 409 | | |
| Server error | 500 | | |

## 6. Non-Functional Requirements
- Latency target:
- Throughput target:
- Rate limit:
- Retry and timeout policy:

## 7. Security
- Input sanitization:
- Secret handling:
- Audit logging:
- Data classification:

## 8. Acceptance Criteria (EARS)
- When `<valid request>`, the system shall `<return expected response>`.
- If `<invalid field>`, the system shall `<return 400 with structured error>`.
- When `<unauthorized request>`, the system shall `<return 401>`.

