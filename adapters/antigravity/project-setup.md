# Project Setup with Antigravity

This guide explains how to integrate the Universal Multi-Agent Development Kit into a target project.

## Recommended Target Structure

When injecting the kit into an existing project, it should live at the root alongside your source code.

```text
your-project-root/
├── .agent/                 <-- The core kit directory
│   ├── agents/
│   ├── indexes/
│   ├── memory/             <-- Project-specific memory files
│   ├── rules/
│   ├── scripts/
│   ├── skills/
│   ├── templates/
│   └── workflows/
├── AGENTS.md               <-- The Antigravity entrypoint (copied from adapters/antigravity/)
├── src/                    <-- Your application code
├── package.json
└── README.md
```

## How to Customize

You can (and should) customize certain areas to fit your specific project:

- **Project Context (`.agent/memory/`):** Add files here describing your project architecture, business logic, and current goals. 
  Antigravity will read these to gain context.
- **File Ownership (`.agent/rules/file-ownership.md`):** Update the ownership matrix to map specialist agents to your actual project folders 
  (e.g., map the Frontend Specialist to `src/components/`).
- **Allowed Agents:** You can restrict the Task Router to only use specific agents by modifying your prompts or adding project-level rules.
- **Language Conventions:** Update global rules if your project uses a specific language (e.g., "All chat responses in Portuguese, all code in English").
- **Validation Commands:** Update workflows or rules to point to your project's actual test commands (e.g., `pytest`, `npm test`, `cargo test`).

## What NOT to Customize

To maintain the safety and integrity of the kit, do **NOT** customize:

- **Global Safety Rules:** Do not remove restrictions on destructive actions.
- **Output Contract Rules:** Do not change the requirement for explicit handoffs and summaries.
- **Defensive Security Boundaries:** Do not remove the requirement for security reviews on sensitive changes.
- **No-Secrets Policy:** Do not alter the rule prohibiting the commit of hardcoded credentials.
