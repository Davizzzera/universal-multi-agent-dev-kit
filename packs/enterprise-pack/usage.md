# Enterprise Pack: Usage

## How to use this pack
1. Determine the scope and risk level of your enterprise task.
2. Select this pack in your prompt to inform the Orchestrator.
3. Always start with the `plan` workflow.
4. Specify your governance requirements (rollback plan, TDR, security review).

## Recommended Prompt Structure
- **Context:** Brief intro to the business system.
- **Goal:** Feature or refactor description.
- **Pack:** `enterprise-pack`.
- **Workflow:** The chosen workflow.
- **Scope:** Which modules are allowed.
- **Governance:** Rollback plan, TDR, multi-reviewer sign-off requirements.
- **Validation:** Full regression + security + production-readiness.

## Step-by-Step Usage
1. Ask the AI to `plan` the change, including a rollback plan and TDR.
2. Review and approve the plan.
3. Instruct the AI to `coordinate` the implementation across modules.
4. Ask the AI to run `security-review` and `verify`.
5. Ask the AI to prepare the `release` (version bump, changelog).
6. Review the release candidate.
7. Instruct the AI to `deploy`.

## How to use with Antigravity
Include the pack reference in your initial prompt. Antigravity will map this pack to its internal context and pre-load the full governance agent ensemble (Software Architect, Risk Analyst, Security Reviewer, Release Manager, etc.).

## How to validate
For an Enterprise pack, validation usually means:
- Full regression test suite.
- Security audit report.
- Production-readiness checklist.
- Rollback plan document.
- Technical Decision Record.

## Common Mistakes
- Deploying to production without a rollback plan.
- Skipping the planning phase for "small" changes that turn out to be large.
- Not involving the `risk-analyst` for cross-module refactors.
- Treating enterprise tasks like small features and skipping governance.
