# Enterprise Pack

> A preset for larger, multi-domain, higher-risk projects requiring stronger governance, architecture, documentation, security and validation.

## Pack Overview
This pack curates the maximum-governance configuration of agents, skills, and workflows. It is designed for projects where failure is costly, where multiple teams or modules are involved, and where documentation, rollback plans, and production-readiness checks are non-negotiable.

## When to use this pack
- Enterprise systems
- Multi-module applications
- Internal business platforms
- Systems with sensitive data
- Projects with multiple agents and workflows
- Production-readiness reviews
- High-risk refactors

## When NOT to use this pack
- Small one-page edits
- Simple copy updates
- Very small tasks that do not need multi-agent coordination

## Recommended Agents
This pack utilizes architects, risk analysts, privacy reviewers, and release managers alongside all orchestration agents. See `agents.md` for the full list.

## Recommended Skills
This pack relies heavily on governance skills: rollback plans, technical decision records, production-readiness checks, and acceptance criteria. See `skills.md` for the full list.

## Recommended Workflows
This pack uses the full lifecycle of workflows, including `coordinate`, `release`, `deploy`, and `emergency-fix`. See `workflows.md` for the full list.

## Validation Expectations
Full regression testing, security reviews, and production-readiness checks are mandatory. Rollback plans must be documented before deployment.

## Safety and Scope Notes
- Multi-reviewer sign-off is required for any production-impacting change.
- Technical Decision Records (TDRs) should be created for any architectural decision.
- The `scope-guardian` must be active at all times to prevent scope creep.

## Example Use Cases
- "Refactor the authentication module across all microservices."
- "Perform a production-readiness review for the new billing system before release."

## Related Packs
- `web-app-pack`
- `api-pack`
