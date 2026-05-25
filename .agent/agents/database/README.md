# Database Agents

> Database schema design, SQL optimization, migration management and data quality assurance.

---

## Purpose
This category contains specialist agents focused on database schema design, sql optimization, migration management and data quality assurance.

## When Used
These agents are invoked by the Task Router when a request involves database domain work.

## Orchestration
Coordinated by: Universal Orchestrator, Task Router, Conflict Controller, Scope Guardian.

## Agents

| Agent | Primary Responsibility | When Used | Main Output |
|-------|------------------------|-----------|-------------|
| [Database Specialist](database-specialist.agent.md) | Design and maintain database schemas, relationships, constraints and data integrity. | database specialist tasks. | AgentOutputContract |
| [Sql Specialist](sql-specialist.agent.md) | Create, review and optimize SQL queries. | sql specialist tasks. | AgentOutputContract |
| [Migration Specialist](migration-specialist.agent.md) | Create and review safe, reversible and versioned database migrations. | migration specialist tasks. | AgentOutputContract |
| [Data Quality Specialist](data-quality-specialist.agent.md) | Validate, clean and improve data quality across files, databases and pipelines. | data quality specialist tasks. | AgentOutputContract |

---

## Rules
All agents in this category must follow:
- `.agent/rules/global-rules.md`
- `.agent/rules/agent-boundaries.md`
- `.agent/rules/file-ownership.md`
- `.agent/rules/output-contract-rules.md`
- `.agent/rules/validation-rules.md`
