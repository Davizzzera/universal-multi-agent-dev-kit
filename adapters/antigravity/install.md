# Antigravity Adapter Installation

There are multiple ways to use the Universal Multi-Agent Development Kit with Antigravity AI depending on your project needs.

## Installation Options

1. **Integrated:** Copy the full `.agent/` directory into your existing project. 
   This brings the entire ruleset, templates, and scripts locally into your codebase.
2. **Reference:** Keep this repository cloned nearby, and simply paste prompt examples into Antigravity referencing the central location.
3. **Packs (Future):** Use specialized packs that install a subset of agents/skills tailored for specific domains (like web apps, APIs, etc.).

## Recommended Installation (For Now)

Until the CLI installer is built, the recommended method is copying the core directory into your project and establishing the entrypoint.

### Step 1: Clone the Kit
```bash
git clone https://github.com/Davizzzera/universal-multi-agent-dev-kit.git
```

### Step 2: Copy the `.agent` Directory
Copy the `.agent/` folder into the root of your target project.

**Windows PowerShell:**
```powershell
Copy-Item -Path ".\universal-multi-agent-dev-kit\.agent" -Destination ".\your-project-path\" -Recurse
```

**macOS/Linux (bash):**
```bash
cp -r ./universal-multi-agent-dev-kit/.agent /path/to/your/project/
```

### Step 3: Establish the Entrypoint
Copy `adapters/antigravity/AGENTS.md` into your project root (or inside your `.agent` folder). 
Use its contents as the primary system prompt or instruction file for Antigravity when starting a new session.

## Validation Requirement

To ensure the integrity of the kit, we use Python validation scripts.
- **Python 3.10+** is recommended for validation scripts.
- No external Python dependencies are required (standard library only).

### Post-Install Validation

Once copied, verify your installation:

If both Node.js and Python are available:
```bash
npm run verify
```

If only Python is available:
```bash
python .agent/scripts/verify_all.py
```

### Fallback Note
If Python is **not installed**, the kit can still be read and utilized by Antigravity, 
but automated validation scripts will not run until Python is configured on the host machine. 
You should rely on manual validation in this case.
