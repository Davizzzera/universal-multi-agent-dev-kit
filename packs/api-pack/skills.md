# API Pack: Skills

## Purpose
This document defines the core procedures and techniques required to implement and secure backend APIs.

## Core Skills
| Skill | Usage |
|-------|-------|
| `api-contract-design` | Defining OpenAPI/Swagger specs |
| `rest-api-implementation` | Building the logic |
| `request-validation` | Input schema checking (e.g. Zod, Joi) |
| `error-handling-standard` | Consistent HTTP status codes |
| `webhook-receiver` | Verifying signatures |
| `pagination-filtering-sorting` | Large dataset endpoints |
| `auth-flow-design` | Login/OAuth mechanics |
| `role-based-access-control` | RBAC/Permissions |
| `auth-security-audit` | Checking for bypasses |
| `database-schema-design` | Table definitions |
| `migration-create` | Safe ALTER TABLE scripts |
| `input-sanitization` | Preventing XSS/SQLi |
| `authz-review` | Ensuring users only see their data |
| `build-validation` | Linting and compiling |
| `integration-test-create` | Testing endpoints |

## Optional Skills
(None defined by default).

## Skill Loading Logic
- Planning phase: Load `api-contract-design`, `auth-flow-design`, `database-schema-design`.
- Implementation phase: Load `rest-api-implementation`, `request-validation`, `error-handling-standard`.
- Security phase: Load `auth-security-audit`, `authz-review`, `input-sanitization`.

## Progressive Loading Notes
Security skills (`authz-review`, `input-sanitization`) must always be loaded when modifying endpoints that accept user input or access the database.

## Validation Notes
`integration-test-create` and `build-validation` are strictly required before delivery.
