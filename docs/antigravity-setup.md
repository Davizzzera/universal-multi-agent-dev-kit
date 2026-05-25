# Antigravity Setup

> How to configure the Universal Multi-Agent Development Kit for use with Antigravity.

---

## Status

> **TODO — Phase v0.5.0**
>
> The Antigravity adapter is planned for Phase v0.5.0 of the project roadmap. This document will be updated with full setup instructions when the adapter is implemented.

---

## What Will the Antigravity Adapter Provide?

When implemented, the Antigravity adapter will:

1. **Entry Point Configuration:** Define how Antigravity discovers and reads the agent system.
2. **Tool Mapping:** Map kit concepts (agents, skills, workflows) to Antigravity's capabilities.
3. **Rule Enforcement:** Translate kit rules into Antigravity-compatible constraints.
4. **Workflow Integration:** Enable Antigravity to follow kit workflows during task execution.
5. **Validation Hooks:** Connect kit validation to Antigravity's review process.

---

## Planned Adapter Location

```
adapters/
└── antigravity/
    ├── README.md          → Adapter documentation
    ├── config.md          → Configuration file
    ├── entry-point.md     → Entry point for Antigravity
    └── mapping.md         → Concept mapping reference
```

---

## Interim Usage

While the adapter is not yet implemented, you can use Antigravity with this kit by:

1. Cloning this repository into your project workspace.
2. Instructing Antigravity to read `.agent/AGENTS.md` as its starting point.
3. Referencing specific agents, skills, or workflows in your prompts.

This manual approach works but lacks the automated integration the adapter will provide.

---

## See Also

- [Getting Started](getting-started.md)
- [Orchestration Model](orchestration-model.md)
- [Roadmap](roadmap.md)
