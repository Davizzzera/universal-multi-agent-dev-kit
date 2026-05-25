# Global Rules

> Non-negotiable rules that govern all agents, skills, workflows, and operations in the Universal Multi-Agent Development Kit.

---

## Purpose

This document defines the universal rules that every agent, skill, workflow, and contributor must follow. These rules are absolute — they cannot be bypassed, overridden, or ignored by any agent under any circumstance.

---

## Non-Negotiable Principles

1. **Read before you write.** Every agent must read and understand the current project context before making any change.
2. **Validate before you deliver.** No work is considered complete without validation evidence.
3. **Stay within scope.** Agents must only modify files and systems within their assigned scope.
4. **Preserve what exists.** Agents must not delete, rename, or restructure files unless explicitly instructed.
5. **Be honest.** Agents must never claim success without evidence, never invent features that do not exist, and never fabricate validation results.
6. **Be incremental.** Changes must be small, focused, and independently verifiable.
7. **Be safe.** Security, privacy, and data integrity are always prioritized over speed or convenience.

---

## Repository Language Rule

- All repository content must be written in **English**.
- This includes: file names, folder names, documentation, code comments, Markdown content, commit messages, package metadata, and GitHub content.
- Chat or verbal explanations to the user may be in any language the user requests.
- The repository itself is always in English.

---

## Scope Control

- Agents must only create, modify, or delete files that are explicitly within the scope of their current task.
- Agents must not create random or speculative files.
- Agents must not rename files or folders unless explicitly instructed.
- Agents must not change the project architecture unless explicitly instructed.
- Agents must not add external dependencies unless explicitly instructed and reviewed.
- Agents must not add generated junk files (build artifacts, cache files, logs, temporary files).

---

## Incremental Implementation Rule

- Every change must be incremental and independently verifiable.
- Large tasks must be broken into smaller, sequential steps.
- Each step must be validated before proceeding to the next.
- If a step fails, the agent must stop and report before continuing.

---

## Validation-First Rule

- No work is considered done until it is validated.
- Validation must include at least one form of evidence (command output, manual checklist, or documented reasoning).
- If automated validation is not possible, the agent must perform and document a manual validation.
- Agents must not say "it works" without proof.
- See [validation-rules.md](validation-rules.md) for detailed validation requirements.

---

## No Hallucination Rule

- Agents must never invent, fabricate, or assume information.
- If an agent does not know something, it must say so explicitly.
- Agents must not claim a file exists without checking.
- Agents must not claim a test passes without running it or documenting why it cannot be run.
- Agents must not create documentation for features that do not exist.
- Every claim must be backed by evidence from the current project state.

---

## No Unauthorized Architecture Changes

- The project architecture is defined in `.agent/ARCHITECTURE.md`.
- Agents must not change the architecture without explicit instruction from the user or the orchestrator.
- Adding new top-level directories, renaming core directories, or changing the file organization model requires explicit approval.
- Minor additions within existing directories (adding files to an existing folder) do not require architecture approval.

---

## No Secrets Rule

- No secrets, tokens, credentials, passwords, private keys, or API keys may be added to the repository.
- This applies to all files, including code, configuration, documentation, and comments.
- Environment variables with sensitive values must use `.env` files that are in `.gitignore`.
- Only `.env.example` files with placeholder values are allowed in the repository.
- See [security-rules.md](security-rules.md) for the complete security policy.

---

## No Offensive Security Rule

- All security content in this repository must be **defensive only**.
- Allowed: auditing, validation, hardening, secrets detection, dependency review, secure configuration, safe development practices.
- Prohibited: exploitation instructions, attack playbooks, credential harvesting, malware, persistence mechanisms, evasion techniques, unauthorized access instructions.
- See [security-rules.md](security-rules.md) for the complete policy.

---

## Required Agent Behavior

### Before Starting Work

1. Read the current project context (file structure, recent changes, relevant documentation).
2. Confirm the task scope and constraints.
3. Identify files that will be created or modified.
4. Check file ownership rules in [file-ownership.md](file-ownership.md).
5. Plan the execution approach.

### During Work

1. Follow the assigned workflow steps.
2. Use only assigned skills.
3. Respect parallel/sequential execution rules from [parallel-execution.md](parallel-execution.md).
4. Do not modify files outside scope.
5. Do not bypass validation gates.

### After Completing Work

1. Validate all changes.
2. Produce a structured output following [output-contract-rules.md](output-contract-rules.md).
3. Report any risks, limitations, or blockers.
4. Suggest the next step if applicable.

---

## Escalation Rules

Agents must escalate to the orchestrator or user when:

- The task is ambiguous and cannot be resolved from available context.
- Required access or permissions are missing.
- Authentication fails.
- A destructive operation is required (deleting files, dropping databases, reverting commits).
- The task conflicts with an existing rule.
- The agent encounters a blocker it cannot resolve.

Agents must **not** escalate for:

- Decisions that are clearly within their expertise and scope.
- Tasks that have clear instructions.
- Standard validation failures (handle them, do not escalate them).

---

## Definition of Done

A task is considered done when:

1. All requested changes are implemented.
2. All changes are validated with evidence.
3. No unauthorized files were created or modified.
4. No secrets or sensitive data were introduced.
5. Documentation is updated if applicable.
6. The output contract is fulfilled (see [output-contract-rules.md](output-contract-rules.md)).
7. The orchestrator or user has received the final report.

---

## Failure Handling

When an agent encounters a failure:

1. **Stop immediately.** Do not attempt to work around the failure blindly.
2. **Document the failure.** Record what happened, what was attempted, and what failed.
3. **Assess the impact.** Determine if the failure affects other tasks or agents.
4. **Report clearly.** Provide the failure details in the agent's output contract.
5. **Suggest recovery.** If possible, suggest a recovery path.
6. **Do not retry indefinitely.** If a retry fails twice, escalate.
7. **Preserve state.** Do not corrupt or lose work done before the failure.
