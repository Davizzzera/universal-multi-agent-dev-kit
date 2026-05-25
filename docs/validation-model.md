# Validation Model

> How validation works in the Universal Multi-Agent Development Kit.

---

## Validation Philosophy

Validation is not an afterthought — it is a core principle of the multi-agent system. Every operation, at every level, must be validated before it is considered complete.

The validation model follows a **trust-but-verify** approach: agents are expected to produce correct results, but independent validation agents verify the output.

---

## Validation Levels

### Level 1: Component Validation

Each individual component (agent, skill, workflow) is validated in isolation:

| Check                     | Description                                        |
|---------------------------|----------------------------------------------------|
| Schema compliance         | The component follows its defined structure.       |
| Required fields present   | All mandatory fields are populated.                |
| References resolved       | All referenced components exist.                   |
| No circular dependencies  | No component depends on itself, directly or indirectly. |
| Naming conventions        | File names and identifiers follow conventions.     |

### Level 2: Integration Validation

The system is validated as a whole to ensure components work together:

| Check                     | Description                                        |
|---------------------------|----------------------------------------------------|
| Workflow completeness     | All workflow steps reference valid agents/skills.  |
| Agent skill availability  | All agent-declared skills exist.                   |
| Rule consistency          | No rules contradict each other.                    |
| No orphaned components    | Every component is referenced by at least one workflow. |
| Dependency resolution     | All inter-agent dependencies can be satisfied.     |

### Level 3: Repository Validation

The repository structure and content are validated:

| Check                     | Description                                        |
|---------------------------|----------------------------------------------------|
| Folder structure          | All required directories exist.                    |
| Required files            | All required files are present and non-empty.      |
| No secrets                | No credentials, tokens, or keys in any file.       |
| No unexpected files       | No unrecognized files outside the expected structure. |
| Documentation completeness| All components have corresponding documentation.   |
| Git hygiene               | No untracked files, clean commit history.          |

---

## Validation Agents

Validation is performed by specialized agents:

| Agent            | Focus                                               |
|------------------|------------------------------------------------------|
| QA Agent         | Functional correctness and completeness.             |
| Security Agent   | Secrets detection, vulnerability scanning, hardening.|
| Style Agent      | Code formatting, naming conventions, consistency.    |
| Structure Agent  | Repository organization and file placement.          |

These agents run in **parallel** during the validation phase, as their checks are independent.

---

## Validation Scripts

Automated validation scripts are located in `.agent/scripts/` and provide machine-executable checks:

| Script               | Purpose                                             |
|----------------------|-----------------------------------------------------|
| `verify_all.py`      | Runs all validation checks.                         |
| `generate_index.py`  | Generates machine-readable indexes.                 |

> **Note:** Validation scripts will be implemented in Phase 4 (v0.4.0).

---

## Validation Workflow

```
Implementation Complete
        │
        ▼
┌───────────────────────────────────┐
│      VALIDATION GATE              │
│                                   │
│  ┌──────────┐  ┌──────────────┐  │
│  │ QA Agent │  │Security Agent│  │
│  └────┬─────┘  └──────┬───────┘  │
│       │               │          │
│  ┌────┴─────┐  ┌──────┴───────┐  │
│  │Style Agent│  │Structure    │  │
│  │          │  │Agent        │  │
│  └────┬─────┘  └──────┬───────┘  │
│       │               │          │
│       └───────┬───────┘          │
│               │                  │
│         All Pass?                │
│          │    │                  │
│         Yes   No                 │
│          │    │                  │
│          │    └──→ Report Issues │
│          │         & Block       │
│          ▼                       │
│    Proceed to                    │
│    Final Review                  │
└───────────────────────────────────┘
```

---

## Validation Criteria

### Pass Criteria
- All required checks pass.
- No critical issues detected.
- No secrets or credentials found.
- All referenced components exist.

### Warning Criteria
- Non-critical style issues.
- Missing optional documentation.
- Performance suggestions.

### Fail Criteria
- Secrets or credentials detected.
- Required files missing.
- Broken references.
- Security vulnerabilities found.
- Structure violations.

---

## Current Status

> **Foundation Phase (v0.1.0):** The validation philosophy and model are documented. Validation scripts and agent implementations will be created in Phases 2–4.
