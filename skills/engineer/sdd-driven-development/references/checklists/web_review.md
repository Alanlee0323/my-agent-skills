# Web SDD Review Checklist

## API and contract
- [ ] Endpoint purpose and method are consistent.
- [ ] Request/response schemas are versionable.
- [ ] Error model is deterministic and documented.
- [ ] Auth/authz and rate limits are defined.

## Data and schema
- [ ] Table/field definitions are complete.
- [ ] Keys, indexes, and FK behavior are explicit.
- [ ] Migration and rollback paths are defined.

## UI/UX
- [ ] Key user flows and failure flows are covered.
- [ ] Component states include loading/empty/error.
- [ ] Accessibility constraints are specified.
- [ ] Responsive rules are specified for target breakpoints.

## Verification
- [ ] API tests cover success and failure paths.
- [ ] Integration tests cover boundary behavior.
- [ ] Manual validation checklist is present for UX behaviors.

