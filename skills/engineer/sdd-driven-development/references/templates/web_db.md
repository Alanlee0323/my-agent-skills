# Web DB Schema SDD Template

## 1. Data Model Summary
- Business entities:
- Ownership boundaries:
- Expected data volume:

## 2. Table Definitions
For each table, define:
- Table name:
- Columns (type, nullable, default):
- Primary key:
- Unique constraints:

## 3. Relationships
- 1:1 relations:
- 1:N relations:
- M:N join tables:
- Delete/update strategy (`RESTRICT`, `CASCADE`, etc.):

## 4. Query and Index Plan
- High-frequency query patterns:
- Required indexes:
- Expected cardinality/selectivity:

## 5. Migration Strategy
- Forward migration:
- Backward compatibility:
- Rollback strategy:
- Data backfill strategy:

## 6. Data Integrity and Security
- Constraints/checks:
- PII handling and masking:
- Retention and archival policy:

## 7. Acceptance Criteria (EARS)
- When `<record created with valid data>`, the system shall `<persist and return stable id>`.
- If `<duplicate unique key>`, the system shall `<reject with deterministic error>`.
- When `<parent deleted>`, the system shall `<apply defined FK behavior>`.

