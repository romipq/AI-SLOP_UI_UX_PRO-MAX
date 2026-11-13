#!/usr/bin/env node
/**
 * ✨ AI-SLOP UI/UX PRO-MAX v2.0.0 — Zero-Dependency Multi-Agent CLI & Runner
 *
 * Commands:
 *   ai-slop-pro-max init [--ai <platform>] [--dir <project-dir>]
 *   ai-slop-pro-max list
 *   ai-slop-pro-max doctor
 *   ai-slop-pro-max audit <target-path> [--min-score <n>]
 *   ai-slop-pro-max generate "<query>" [-p "Name"] [--slop-level 11] [--era auto]
 *   ai-slop-pro-max scaffold <landing|dashboard|waitlist|pricing|auth> [-o out.html]
 */

import { cpSync, existsSync, mkdirSync, copyFileSync } from 'node:fs';
import { spawnSync } from 'node:child_process';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, '..');
const SKILLS_SRC = join(REPO_ROOT, 'skills');
const RULES_SRC = join(REPO_ROOT, 'rules');
const SLOP_PY = join(SKILLS_SRC, 'ai-slop-ui-ux-pro-max', 'scripts', 'slop.py');

const SKILL_NAMES = [
  'ai-slop-ui-ux-pro-max',
  'ai-slop-copywriter',
  'ai-slop-slopifier',
  'ai-slop-components',
  'ai-slop-pitch-deck',
];

function copySkillsInto(destSkillsDir) {
  mkdirSync(destSkillsDir, { recursive: true });
  for (const name of SKILL_NAMES) {
    cpSync(join(SKILLS_SRC, name), join(destSkillsDir, name), { recursive: true });
  }
  return destSkillsDir;
}

const PLATFORMS = {
  claude: {
    label: 'Claude Code (.claude/skills/)',
    install: (dir) => [copySkillsInto(join(dir, '.claude', 'skills'))],
  },
  cursor: {
    label: 'Cursor (.cursor/skills/ + .cursor/rules/)',
    install(dir) {
      const s = copySkillsInto(join(dir, '.cursor', 'skills'));
      const rulesDest = join(dir, '.cursor', 'rules');
      mkdirSync(rulesDest, { recursive: true });
      const ruleFile = join(rulesDest, 'ai-slop-ui-ux-pro-max.mdc');
      copyFileSync(join(RULES_SRC, 'cursor', 'ai-slop-ui-ux-pro-max.mdc'), ruleFile);
      return [s, ruleFile];
    },
  },
  codex: {
    label: 'Codex / Universal Agent Skills (.agents/skills/)',
    install: (dir) => [copySkillsInto(join(dir, '.agents', 'skills'))],
  },
  opencode: {
    label: 'OpenCode (.opencode/skills/)',
    install: (dir) => [copySkillsInto(join(dir, '.opencode', 'skills'))],
  },
  gemini: {
    label: 'Gemini CLI (.gemini/skills/)',
    install: (dir) => [copySkillsInto(join(dir, '.gemini', 'skills'))],
  },
  cline: {
    label: 'Cline (.cline/skills/ + .clinerules)',
    install(dir) {
      const s = copySkillsInto(join(dir, '.cline', 'skills'));
      const destFile = join(dir, '.clinerules');
      copyFileSync(join(RULES_SRC, 'windsurf', '.windsurfrules'), destFile);
      return [s, destFile];
    },
  },
  roocode: {
    label: 'Roo Code (.roo/skills/)',
    install: (dir) => [copySkillsInto(join(dir, '.roo', 'skills'))],
  },
  kilocode: {
    label: 'Kilo Code (.kilocode/skills/)',
    install: (dir) => [copySkillsInto(join(dir, '.kilocode', 'skills'))],
  },
  windsurf: {
    label: 'Windsurf (.windsurfrules + .windsurf/skills/)',
    install(dir) {
      const s = copySkillsInto(join(dir, '.windsurf', 'skills'));
      const destFile = join(dir, '.windsurfrules');
      copyFileSync(join(RULES_SRC, 'windsurf', '.windsurfrules'), destFile);
      return [s, destFile];
    },
  },
  copilot: {
    label: 'GitHub Copilot (.github/copilot-instructions.md + .github/skills/)',
    install(dir) {
      const s = copySkillsInto(join(dir, '.github', 'skills'));
      const destFile = join(dir, '.github', 'copilot-instructions.md');
      copyFileSync(join(RULES_SRC, 'copilot', 'copilot-instructions.md'), destFile);
      return [s, destFile];
    },
  },
  amp: {
    label: 'Amp (.agents/skills/)',
    install: (dir) => [copySkillsInto(join(dir, '.agents', 'skills'))],
  },
  trae: {
    label: 'Trae (.trae/skills/)',
    install: (dir) => [copySkillsInto(join(dir, '.trae', 'skills'))],
  },
};

function findPython() {
  for (const bin of ['python3', 'python']) {
    const res = spawnSync(bin, ['--version'], { encoding: 'utf-8' });
    if (res.status === 0) return bin;
  }
  return null;
}

function runSlopPy(pyArgs) {
  const py = findPython();
  if (!py) {
    console.error('❌ Python 3 is required to run the Slop Intelligence Engine.');
    process.exit(1);
  }
  const res = spawnSync(py, [SLOP_PY, ...pyArgs], { stdio: 'inherit' });
  process.exit(res.status ?? 0);
}

function printBanner() {
  console.log(`
✨======================================================================✨
   AI-SLOP UI/UX PRO-MAX v2.0.0 — Deliberate Cliché Design Intelligence
   5 Agent Skills · 286 Searchable Records · 7 Slop Eras · Level 1–11
✨======================================================================✨`);
}

function printHelp() {
  printBanner();
  console.log(`
Usage:
  ai-slop-pro-max init [--ai <platform|all>] [--dir <project-dir>]
  ai-slop-pro-max list
  ai-slop-pro-max doctor
  ai-slop-pro-max audit <file-or-dir> [--min-score 85]
  ai-slop-pro-max generate "<query>" [-p "Name"] [--slop-level 11] [--era auto]
  ai-slop-pro-max scaffold <landing|dashboard|waitlist|pricing|auth> [-o out.html]

Supported AI Platforms (--ai):
  ${Object.keys(PLATFORMS).join(', ')}, all

Standard Agent Skills CLI also supported:
  npx skills add romipq/AI-SLOP_UI_UX_PRO-MAX
`);
}

const rawArgs = process.argv.slice(2);
const cmd = rawArgs[0] || 'help';

if (cmd === 'help' || cmd === '--help' || cmd === '-h') {
  printHelp();
  process.exit(0);
}

if (cmd === 'list') {
  printBanner();
  console.log('\n📦 Included Agent Skills (5-Skill Suite):');
  for (const s of SKILL_NAMES) console.log(`  - ${s}`);
  console.log('\n🤖 Supported AI Coding Platforms (12):');
  for (const [k, v] of Object.entries(PLATFORMS)) {
    console.log(`  - ${k.padEnd(10)} → ${v.label}`);
  }
  process.exit(0);
}

if (cmd === 'doctor') {
  printBanner();
  const py = findPython();
  console.log(`\n🩺 Python Runtime: ${py ? `✅ Found (${py})` : '❌ Missing Python 3'}`);
  console.log(`📂 Skills Bundle:  ${existsSync(SLOP_PY) ? '✅ Intact' : '❌ Missing slop.py'}`);
  if (py && existsSync(SLOP_PY)) {
    console.log('');
    runSlopPy(['--stats']);
  }
  process.exit(py ? 0 : 1);
}

if (cmd === 'audit') {
  const target = rawArgs[1];
  if (!target) {
    console.error('Usage: ai-slop-pro-max audit <file-or-dir> [--min-score <n>]');
    process.exit(1);
  }
  runSlopPy(['--audit', target, ...rawArgs.slice(2)]);
}

if (cmd === 'generate') {
  runSlopPy(['--design-system', ...rawArgs.slice(1)]);
}

if (cmd === 'scaffold') {
  const tpl = rawArgs[1];
  if (!tpl) {
    console.error('Usage: ai-slop-pro-max scaffold <landing|dashboard|waitlist|pricing|auth> [-o out.html]');
    process.exit(1);
  }
  runSlopPy(['--scaffold', tpl, ...rawArgs.slice(2)]);
}

if (cmd === 'init') {
  printBanner();
  let ai = 'claude';
  let dir = process.cwd();
  for (let i = 1; i < rawArgs.length; i++) {
    if ((rawArgs[i] === '--ai' || rawArgs[i] === '-a') && rawArgs[i + 1]) {
      ai = rawArgs[++i].toLowerCase();
    } else if ((rawArgs[i] === '--dir' || rawArgs[i] === '-d') && rawArgs[i + 1]) {
      dir = resolve(rawArgs[++i]);
    }
  }
  if (!existsSync(dir)) mkdirSync(dir, { recursive: true });
  const selected = ai === 'all' ? Object.keys(PLATFORMS) : ai.split(',').map((s) => s.trim());
  const seenPaths = new Set();

  for (const key of selected) {
    const handler = PLATFORMS[key];
    if (!handler) {
      console.error(`❌ Unknown platform '${key}'. Valid: ${Object.keys(PLATFORMS).join(', ')}, all`);
      process.exit(1);
    }
    const paths = handler.install(dir);
    console.log(`✅ Installed for ${handler.label}:`);
    for (const p of paths) {
      if (!seenPaths.has(p)) {
        console.log(`   → ${p}`);
        seenPaths.add(p);
      }
    }
  }
  console.log('\n🚀 Ready to Supercharge Your UI with Maximum AI Slop →\n');
  process.exit(0);
}

printHelp();
