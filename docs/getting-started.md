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

To use this kit on an existing project, simply copy the `.agent/`, `packs/`, and `adapters/` directories into the root of your target project repository. 

*Note: A CLI tool to automate this setup is planned for a future release.*

### 5. Use Workflows and Packs

When prompting your AI tool, specify a **Pack** and a **Workflow** to accelerate the process. For example:

> "Goal: Create a new user login page. Pack: `web-app-pack`. Workflow: `create-feature`."

The AI will look up the recommended agents and skills for that pack and execute the requested workflow.

### 6. Run Validation Scripts

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

> **v0.1.0 Foundation Release:** The complete foundational structure, orchestration model, 54 agents, 104 skills, 
> 18 workflows, 9 project packs, and the Antigravity adapter are implemented and ready to use. 
> Future releases will add a CLI and additional adapters.
