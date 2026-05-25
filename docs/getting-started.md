# Getting Started

> How to use the Universal Multi-Agent Development Kit in your projects.

---

## Overview

The Universal Multi-Agent Development Kit is a structured framework of agents, skills, workflows, and rules that AI coding tools can follow to assist you with software engineering tasks.

This kit is **not installed as a dependency**. It is a repository of structured instructions that AI assistants read and execute.

---

## Prerequisites

- Git installed on your system.
- An AI coding tool that supports reading structured agent files (e.g., Antigravity, Claude Code, Cursor, Codex).
- A project repository where you want to apply the kit.

---

## Quick Start

### Step 1: Clone the Kit

```bash
git clone https://github.com/Davizzzera/universal-multi-agent-dev-kit.git
```

### Step 2: Understand the Structure

The kit is organized into four main areas:

- **`.agent/`** — The core agent system. Start with `.agent/AGENTS.md`.
- **`adapters/`** — Tool-specific integrations. Choose the adapter for your AI tool.
- **`packs/`** — Optional project-type packs. Select packs relevant to your project.
- **`docs/`** — Documentation for understanding and contributing.

### Step 3: Configure Your AI Tool

Each AI coding tool has its own adapter in `adapters/`. The adapter provides the specific configuration needed for your tool to read and follow the kit.

> **Note:** Adapter implementations will be available starting from v0.5.0. See [antigravity-setup.md](antigravity-setup.md) for the Antigravity adapter status.

### Step 4: Start Working

Once configured, your AI coding tool will:

1. Read the agent system from `.agent/AGENTS.md`.
2. Follow the orchestration model for task execution.
3. Use the appropriate skills for each task.
4. Validate results before completing work.

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
| [Examples](examples.md)                          | Conceptual usage examples.               |
| [Roadmap](roadmap.md)                            | Project development roadmap.             |

---

## Current Status

> **Foundation Phase (v0.1.0):** The kit structure is established. Core agents, skills, workflows, and adapters will be implemented in subsequent phases. You can explore the structure and documentation now to understand how the kit will work.
