#!/usr/bin/env node
/**
 * ✨ AI-SLOP UI/UX PRO-MAX — Zero-Dependency Multi-Agent Installer CLI
 * Usage:
 *   npx github:romipq/AI-SLOP_UI_UX_PRO-MAX init --ai claude|cursor|windsurf|copilot|codex|opencode|all [--dir .]
 *   npx github:romipq/AI-SLOP_UI_UX_PRO-MAX list
 */

import { cpSync, existsSync, mkdirSync, copyFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, '..');
const SKILLS_SRC = join(REPO_ROOT, 'skills');
const RULES_SRC = join(REPO_ROOT, 'rules');

const SKILL_NAMES = [
  'ai-slop-ui-ux-pro-max',
  'ai-slop-copywriter',
  'ai-slop-slopifier',
];

const PLATFORMS = {
  claude: {
    label: 'Claude Code (.claude/skills/)',
    install(targetDir) {
      const dest = join(targetDir, '.claude', 'skills');
      mkdirSync(dest, { recursive: true });
      for (const name of SKILL_NAMES) {
        cpSync(join(SKILLS_SRC, name), join(dest, name), { recursive: true });
      }
      return [dest];
    },
  },
  cursor: {
    label: 'Cursor (.cursor/skills/ + .cursor/rules/)',
    install(targetDir) {
      const skillsDest = join(targetDir, '.cursor', 'skills');
      const rulesDest = join(targetDir, '.cursor', 'rules');
      mkdirSync(skillsDest, { recursive: true });
      mkdirSync(rulesDest, { recursive: true });
      for (const name of SKILL_NAMES) {
        cpSync(join(SKILLS_SRC, name), join(skillsDest, name), { recursive: true });
      }
      copyFileSync(
        join(RULES_SRC, 'cursor', 'ai-slop-ui-ux-pro-max.mdc'),
        join(rulesDest, 'ai-slop-ui-ux-pro-max.mdc')
      );
      return [skillsDest, join(rulesDest, 'ai-slop-ui-ux-pro-max.mdc')];
    },
  },
  codex: {
    label: 'Codex / Universal Agent Skills (.agents/skills/)',
    install(targetDir) {
      const dest = join(targetDir, '.agents', 'skills');
      mkdirSync(dest, { recursive: true });
      for (const name of SKILL_NAMES) {
        cpSync(join(SKILLS_SRC, name), join(dest, name), { recursive: true });
      }
      return [dest];
    },
  },
  opencode: {
    label: 'OpenCode (.opencode/skills/)',
    install(targetDir) {
      const dest = join(targetDir, '.opencode', 'skills');
      mkdirSync(dest, { recursive: true });
      for (const name of SKILL_NAMES) {
        cpSync(join(SKILLS_SRC, name), join(dest, name), { recursive: true });
      }
      return [dest];
    },
  },
  windsurf: {
    label: 'Windsurf (.windsurfrules)',
    install(targetDir) {
      const destFile = join(targetDir, '.windsurfrules');
      copyFileSync(join(RULES_SRC, 'windsurf', '.windsurfrules'), destFile);
      return [destFile];
    },
  },
  copilot: {
    label: 'GitHub Copilot (.github/copilot-instructions.md)',
    install(targetDir) {
      const ghDir = join(targetDir, '.github');
      mkdirSync(ghDir, { recursive: true });
      const destFile = join(ghDir, 'copilot-instructions.md');
      copyFileSync(join(RULES_SRC, 'copilot', 'copilot-instructions.md'), destFile);
      return [destFile];
    },
  },
};

function printBanner() {
  console.log(`
✨================================================================✨
   AI-SLOP UI/UX PRO-MAX v1.0.0 — Maximum Vibe-Coding Installer
   Indigo-Purple-Pink · Blur-3xl Orbs · Glassmorphism · 10x Copy
✨================================================================✨`);
}

function printHelp() {
  printBanner();
  console.log(`
Usage:
  ai-slop-pro-max init [--ai <platform>] [--dir <project-dir>]
  ai-slop-pro-max list

Platforms (--ai):
  claude     Install skills to .claude/skills/
  cursor     Install skills to .cursor/skills/ + rule to .cursor/rules/
  codex      Install skills to .agents/skills/
  opencode   Install skills to .opencode/skills/
  windsurf   Copy .windsurfrules to project root
  copilot    Copy .github/copilot-instructions.md
  all        Install across ALL supported AI platforms!

Tip: You can also install via the standard Agent Skills CLI:
  npx skills add romipq/AI-SLOP_UI_UX_PRO-MAX
`);
}

function parseArgs(argv) {
  const args = { command: argv[0] || 'help', ai: 'claude', dir: process.cwd() };
  for (let i = 1; i < argv.length; i++) {
    const a = argv[i];
    if ((a === '--ai' || a === '-a') && argv[i + 1]) {
      args.ai = argv[++i].toLowerCase();
    } else if ((a === '--dir' || a === '-d') && argv[i + 1]) {
      args.dir = resolve(argv[++i]);
    } else if (a === '--help' || a === '-h') {
      args.command = 'help';
    }
  }
  return args;
}

const args = parseArgs(process.argv.slice(2));

if (args.command === 'list') {
  printBanner();
  console.log('\n📦 Included Skills:');
  for (const s of SKILL_NAMES) console.log(`  - ${s}`);
  console.log('\n🤖 Supported AI Platforms:');
  for (const [k, v] of Object.entries(PLATFORMS)) {
    console.log(`  - ${k.padEnd(10)} → ${v.label}`);
  }
  process.exit(0);
}

if (args.command === 'init') {
  printBanner();
  if (!existsSync(args.dir)) {
    mkdirSync(args.dir, { recursive: true });
  }
  const selected =
    args.ai === 'all' ? Object.keys(PLATFORMS) : args.ai.split(',').map((s) => s.trim());

  for (const key of selected) {
    const handler = PLATFORMS[key];
    if (!handler) {
      console.error(`❌ Unknown platform: '${key}'. Valid: ${Object.keys(PLATFORMS).join(', ')}, all`);
      process.exit(1);
    }
    const paths = handler.install(args.dir);
    console.log(`✅ Installed for ${handler.label}:`);
    for (const p of paths) console.log(`   → ${p}`);
  }
  console.log('\n🚀 Ready to Supercharge Your UI with Maximum AI Slop →\n');
  process.exit(0);
}

printHelp();
