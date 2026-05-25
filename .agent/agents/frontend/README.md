# Frontend Agents

> User interface implementation, React development, UI/UX design, design systems, responsive layouts and accessibility.

---

## Purpose
This category contains specialist agents focused on user interface implementation, react development, ui/ux design, design systems, responsive layouts and accessibility.

## When Used
These agents are invoked by the Task Router when a request involves frontend domain work.

## Orchestration
Coordinated by: Universal Orchestrator, Task Router, Conflict Controller.

## Agents

| Agent | Primary Responsibility | When Used | Main Output |
|-------|------------------------|-----------|-------------|
| [Frontend Specialist](frontend-specialist.agent.md) | Implement and improve user interfaces using existing project patterns. | frontend specialist tasks. | AgentOutputContract |
| [React Specialist](react-specialist.agent.md) | Handle React-specific implementation, components, hooks, state and Vite/Next patterns. | react specialist tasks. | AgentOutputContract |
| [Ui Ux Designer](ui-ux-designer.agent.md) | Improve usability, hierarchy, interaction flow and user experience. | ui ux designer tasks. | AgentOutputContract |
| [Design System Specialist](design-system-specialist.agent.md) | Maintain visual consistency through tokens, reusable patterns and component standards. | design system specialist tasks. | AgentOutputContract |
| [Responsive Layout Specialist](responsive-layout-specialist.agent.md) | Ensure layouts work across desktop, tablet and mobile. | responsive layout specialist tasks. | AgentOutputContract |
| [Accessibility Specialist](accessibility-specialist.agent.md) | Improve accessibility, semantic structure, keyboard navigation and readability. | accessibility specialist tasks. | AgentOutputContract |

---

## Rules
All agents in this category must follow:
- `.agent/rules/global-rules.md`
- `.agent/rules/agent-boundaries.md`
- `.agent/rules/file-ownership.md`
- `.agent/rules/output-contract-rules.md`
- `.agent/rules/validation-rules.md`
