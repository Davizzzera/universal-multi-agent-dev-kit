# Antigravity Adapter

> The official adapter for integrating the Universal Multi-Agent Development Kit with Antigravity AI workflows.

---

## What is this?

This adapter connects the **Universal Multi-Agent Development Kit** to **Antigravity AI workflows**. 

The core repository (`.agent/`) remains completely tool-agnostic. It defines the rules, agents, skills, and workflows. This adapter provides the **Antigravity-specific instructions** on *how* to load and use those agnostic definitions inside the Antigravity assistant.

## Recommended Usage Model

1. **Copy or reference** the `.agent/` directory in your project.
2. **Use `adapters/antigravity/AGENTS.md`** as your Antigravity entrypoint instructions. You can paste it into Antigravity's system prompt or reference it directly.
3. **Ask Antigravity** to use workflows from `.agent/workflows/`.
4. **Ask Antigravity** to select agents and skills using the Universal Orchestrator.
5. **Validate before finishing**. Antigravity will automatically rely on validation scripts and independent checks before delivering final results.

## Adapter Files

| File | Purpose |
|------|---------|
| `AGENTS.md` | The ready-to-copy entrypoint instruction file for Antigravity. |
| `adapter-manifest.json` | Capabilities and requirements manifest. |
| `install.md` | Installation and setup guide. |
| `usage.md` | General usage guide. |
| `quick-start.md` | Practical quick start guide. |
| `project-setup.md` | Project structure and customization guide. |
| `integration-rules.md` | Specific integration rules for Antigravity. |
| `prompt-library.md` | Reusable prompt patterns. |
| `troubleshooting.md` | Common issues and safe fixes. |
| `examples/*.prompt.md` | Ready-to-copy example prompts. |

## Safety Notes

When operating Antigravity with this kit, remember:
- **Do not expose secrets.** Ensure `.gitignore` and `.env` files are properly managed.
- **Do not allow broad rewrites.** Keep scope tightly controlled using the Scope Guardian agent.
- **Use validation-first delivery.** Do not accept code without proof of successful validation.
- **Parallelize discovery, serialize conflicting edits, parallelize verification.** Let Antigravity read freely, but write carefully.

## Quick Command Reference

*(Note: A dedicated CLI installer is planned for a future phase. For now, use Git and standard commands to clone and copy the `.agent` folder.)*

```bash
# Verify the integrity of the kit
npm run verify

# Regenerate indexes
npm run generate:index
```
