# n8n Pack: Skills

## Purpose
This document defines the core procedures and techniques required to design resilient n8n workflows.

## Core Skills
| Skill | Usage |
|-------|-------|
| `n8n-workflow-design` | Structuring node connections |
| `n8n-webhook-flow` | Setting up trigger nodes |
| `webhook-receiver` | Validating incoming payloads |
| `error-retry-strategy` | Using the Error Trigger node |
| `api-contract-design` | Mapping HTTP Request nodes |
| `secure-logging-review` | Ensuring data privacy in logs |
| `environment-variable-management` | Using n8n credentials securely |
| `reporting-automation` | Sending summaries via email/Slack |
| `test-plan-create` | QA strategy |
| `troubleshooting-guide` | Documenting execution history checks |

## Optional Skills
(None defined by default).

## Skill Loading Logic
- Planning phase: Load `n8n-workflow-design`.
- Integration phase: Load `n8n-webhook-flow`, `webhook-receiver`, `api-contract-design`.
- Resilience phase: Load `error-retry-strategy`, `secure-logging-review`.

## Progressive Loading Notes
Only load `reporting-automation` if the workflow explicitly requires notifying humans.

## Validation Notes
`secure-logging-review` must be completed before an exported JSON file is committed to the repository.
