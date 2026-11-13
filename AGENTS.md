# AGENTS.md — Repository Guide for `romipq/AI-SLOP_UI_UX_PRO-MAX`

This repository hosts the **AI-SLOP UI/UX PRO-MAX** agent skill pack, local BM25 slop design intelligence engine, multi-IDE rule installer, and copy-paste prompt collection.

## Structure
- `skills/ai-slop-ui-ux-pro-max/` — Flagship skill (`SKILL.md`), CSV databases (`data/`), deep-dive docs (`references/`), and zero-dependency Python 3 CLI (`scripts/slop.py`).
- `skills/ai-slop-copywriter/` — Companion skill for English & Russian SaaS buzzword copywriting.
- `skills/ai-slop-slopifier/` — Companion skill for refactoring human-designed UI into certified AI Slop.
- `prompts/` — Standalone EN & RU system prompts and one-shot prompts.
- `rules/` — Drop-in rules for Cursor, Windsurf, GitHub Copilot, and Claude/Codex.
- `bin/cli.mjs` — Zero-dependency Node.js installer CLI.
- `examples/nexusflow-ai-showcase.html` — Self-contained interactive Level 1→11 AI-Slop UI showcase.

## Running Tests
```bash
python3 -m unittest discover -s skills/ai-slop-ui-ux-pro-max/scripts/tests -v
```
