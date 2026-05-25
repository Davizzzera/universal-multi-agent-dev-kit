# Ecommerce Pack: Skills

## Purpose
This document defines the core procedures and techniques required to implement commerce features securely and consistently.

## Core Skills
| Skill | Usage |
|-------|-------|
| `project-intake` | Initial discovery |
| `business-context-extraction` | Understanding the commerce goals |
| `database-schema-design` | Table/collection changes |
| `api-contract-design` | Designing JSON structures |
| `rest-api-implementation` | Building endpoints |
| `react-component-create` | Building UI |
| `frontend-api-integration` | Connecting UI to API |
| `loading-empty-error-states` | Handling network delays |
| `data-cleaning` | Normalizing imported products |
| `deduplication-rules` | Preventing duplicate SKUs |
| `product-copy-guidance` | Writing item descriptions |
| `cta-copywriting` | Designing actionable buttons |
| `conversion-audit` | Reviewing user flow |
| `build-validation` | Running npm run build |
| `security-release-checklist` | Final security check |

## Optional Skills
(None defined by default).

## Skill Loading Logic
- Planning phase: Load `project-intake`, `business-context-extraction`.
- Frontend phase: Load `react-component-create`, `frontend-api-integration`, `loading-empty-error-states`, `cta-copywriting`.
- Backend phase: Load `api-contract-design`, `rest-api-implementation`, `database-schema-design`.

## Progressive Loading Notes
Security skills must be loaded if modifying the cart or checkout logic.

## Validation Notes
`build-validation` and `security-release-checklist` are strictly required before any commerce task can be considered complete.
