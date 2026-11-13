# Install

No dependencies. Python 3.9+ only for the tools; the skill itself is just Markdown,
CSS and JSON.

```bash
git clone https://github.com/romipq/AI-SLOP_UI_UX_PRO-MAX.git
cd AI-SLOP_UI_UX_PRO-MAX
python3 tools/slop_lint.py examples/01-max-landing.html   # expect 100/100
```

---

## Claude Code

Skills live in folders containing a `SKILL.md`.

**Personal (all projects):**

```bash
mkdir -p ~/.claude/skills
ln -s "$(pwd)" ~/.claude/skills/ai-slop-ui-ux-pro-max
```

or copy instead of symlink:

```bash
cp -R . ~/.claude/skills/ai-slop-ui-ux-pro-max
```

**Project-scoped (committed with the repo):**

```bash
mkdir -p .claude/skills
ln -s ../../.. .claude/skills/ai-slop-ui-ux-pro-max   # or cp -R
```

Then in Claude Code:

```
/skills
```

You should see `ai-slop-ui-ux-pro-max` with the description from the frontmatter.
Ask: *"Use AI-SLOP PRO-MAX to build a MAX landing page for an AI note app."*

### Using the helper script

```bash
./install.sh                 # symlink into ~/.claude/skills
./install.sh --copy          # copy instead
./install.sh --target .claude/skills   # project-scoped
./install.sh --uninstall
```

---

## claude.ai / Claude apps

If Skills are available in your plan:

1. Zip the folder (keep `SKILL.md` at the root of the zip).
2. Upload it in **Settings → Capabilities → Skills**.
3. Ask for a page and mention "AI slop".

If Skills are not available, paste `prompts/system-prompt.md` into a Project's
custom instructions and attach `references/` as project knowledge.

---

## ChatGPT

**Custom GPT:**

1. Create a GPT → **Configure**.
2. Paste `prompts/system-prompt.md` into **Instructions**.
3. Upload `references/01-design-tokens.md`, `02-components.md`, `03-copywriting.md`,
   `04-motion.md` and `05-emoji-iconography.md` as knowledge.
4. Optionally add the action-free "code interpreter" for running the linter.

**Plain chat:** paste the same system prompt as your first message and ask for the page.

---

## Cursor

Create `.cursor/rules/ai-slop.mdc`:

```md
---
description: AI-SLOP UI/UX PRO-MAX — maximum-cliché AI design, on purpose
globs: ["**/*.html", "**/*.tsx", "**/*.css"]
alwaysApply: false
---

Read SKILL.md at the repo root, then follow it exactly.
For any UI request in this workspace, produce MAX-level slop and verify with:
python3 tools/slop_lint.py <file> --min 90
```

Or add a line to `AGENTS.md`:

```md
For satirical/parody UI work, use the skill in ./SKILL.md (AI-SLOP UI/UX PRO-MAX).
```

---

## GitHub Copilot

Add `.github/copilot-instructions.md`:

```md
When asked for satirical "AI-generated" UI, follow SKILL.md (AI-SLOP UI/UX PRO-MAX).
Target SLOP-100 ≥ 90. All brands and metrics must be fictional.
```

---

## Any API / agent framework

1. System prompt: `prompts/system-prompt.md`.
2. Retrieval: `references/*.md` (load 02 and 03 first; 01 for tokens).
3. Tool: expose `python3 tools/slop_lint.py {path} --json` as a function so the agent
   can self-correct.
4. Optional tool: `python3 tools/slopify.py {path}` and `tools/slop_gen.py --json`.

A minimal loop:

```
write → lint → if score < 90: read next_moves → edit → lint → deliver
```

---

## Verify the install

```bash
python3 tools/slop_lint.py examples/01-max-landing.html --quiet
# examples/01-max-landing.html: 100/100 — S+ — PEAK SLOP · museum-grade

python3 tools/slop_lint.py examples/00-before.html --quiet
# examples/00-before.html: 16/100 — F — human taste detected
```

If both match, everything works.

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `/skills` doesn't list it | `SKILL.md` must be at the folder root with valid YAML frontmatter |
| Linter ignores linked CSS | Only relative `<link href="…css">` is followed; absolute URLs are skipped |
| Score is lower than the example | You're scoring your file, not the example — check the path |
| Fonts don't load offline | Falls back to system sans; the score doesn't depend on fonts loading |
| `ModuleNotFoundError` in tools | Run from the repo root, or `python3 tools/slop_lint.py` with the file path |
| Windows symlink fails | Use `./install.sh --copy` or copy the folder manually |
| Skill triggers on serious work | Add "do not use for production" to your project rules |

---

## Uninstall

```bash
rm -rf ~/.claude/skills/ai-slop-ui-ux-pro-max
# or
./install.sh --uninstall
```

Nothing outside the skill folder is modified.
