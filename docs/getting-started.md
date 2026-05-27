# Getting Started

> How to use the Universal Multi-Agent Development Kit in your projects.

---

## Overview

The Universal Multi-Agent Development Kit is a structured framework of agents, skills, workflows, 
and rules that AI coding tools can follow to assist you with software engineering tasks.

This kit is **not installed as a dependency**. It is a repository of structured instructions that AI assistants read and execute.

---

## Prerequisites

- Git installed on your system.
- An AI coding tool that supports reading structured agent files. Currently, the **Antigravity** adapter is officially supported.
- A project repository where you want to apply the kit.

---

## Quick Start (v0.1.0)

### 1. Clone the Kit

Clone the kit into your local environment:

```bash
git clone https://github.com/Davizzzera/universal-multi-agent-dev-kit.git
```

### 2. Review `.agent/AGENTS.md`

This is the main entry point for the AI. Open this file to understand the orchestration model, 
the available specialist agents, and how the kit enforces a validation-first workflow.

### 3. Use the Antigravity Adapter

If you are using Antigravity, open `adapters/antigravity/README.md`. 
You will find specific prompt examples in `adapters/antigravity/examples/` that instruct Antigravity to act as the Universal Orchestrator.

### 4. Apply to a Target Project

To start using this kit in an existing or new project, establish the **Auto-Orchestration Runtime Mode**:

1. Copy the `.agent/` folder into your target project.
2. Copy the `packs/` folder into your target project.
3. **Crucial Step**: Create a root `AGENTS.md` file by copying either `.agent/templates/default-project-agents-template.md` or `adapters/antigravity/AGENTS.md` to the root of your project.

This root file tells your AI tool to use the kit by default.

*Note: A CLI tool to automate this setup is planned for a future release.*

### 5. Use Workflows and Packs

When prompting your AI tool, specify a **Pack** and a **Workflow** to accelerate the process. For example:

> "Goal: Create a new user login page. Pack: `web-app-pack`. Workflow: `create-feature`."

The AI will look up the recommended agents and skills for that pack and execute the requested workflow.

### 6. Ask Naturally and Read the Trace

You don't need to manually orchestrate agents. You can ask naturally and require the AI to route automatically. At the end, the AI must provide an Execution Trace.

**Example Prompt:**
> "Fix the null reference bug in the auth service. I will not name agents manually. Automatically choose the appropriate agents, skills, and workflows. Provide a detailed Execution Trace after completion, including validation evidence."

**How to verify that the kit is actually being used:**
The user should look for registry-backed paths in the final response. 
- If the response only says "used agents" without paths, it is incomplete. 
- If the trace is only in an artifact, ask for inline registry evidence.

How to read the trace:
- **Workflow / Pack:** Confirms the context used with exact paths.
- **Agents/Skills Used:** Shows exactly which specialists touched the code with exact paths.
- **Execution Mode:** Indicates if the tool actually spawned subagents (parallelism) or just assumed roles.
- **Validation Evidence:** Ensures quality checks were run before completion.

### 7. Run Validation Scripts

The kit includes Python scripts to validate its internal structure. You can run:

```bash
npm run verify
```

**Python Limitation:** You must have **Python 3.10+** installed and available in your system's `PATH`. 
If Python is not configured, the validation scripts will fail to run, but the Markdown instructions will remain fully functional for the AI. 
**No external Python dependencies** (e.g., pip packages) are required.

---

## How It Works

1. You make a request to your AI coding tool.
2. The tool reads the kit's orchestration model.
3. The Universal Orchestrator coordinates specialist agents.
4. Agents use skills to perform their tasks.
5. Workflows define the execution order.
6. Validation agents review the results.
7. The final result is delivered.

---

## Key Documentation

| Document                                        | Description                              |
|-------------------------------------------------|------------------------------------------|
| [Agent Design](agent-design.md)                 | How agents are designed and structured.  |
| [Skill Design](skill-design.md)                 | How skills are designed and structured.  |
| [Workflow Design](workflow-design.md)            | How workflows are designed.              |
| [Orchestration Model](orchestration-model.md)    | How the multi-agent system works.        |
| [Validation Model](validation-model.md)          | How validation is handled.               |
| [Examples](examples.md)                          | Practical usage examples.                |
| [Roadmap](roadmap.md)                            | Project development roadmap.             |

---

## Current Status

> **v0.2.2 Execution Trace Release:** The complete foundational structure, orchestration model, 54 agents, 104 skills, 
> 18 workflows, 9 project packs, CI validation, and transparent Execution Trace are implemented and ready to use. 
> Future releases will add a CLI and additional adapters.
