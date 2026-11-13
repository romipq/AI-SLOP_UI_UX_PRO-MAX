/**
 * Asset/integration checks. Run with: npm test
 */
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync, existsSync, readdirSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const root = resolve(here, "..");

const read = (p) => readFileSync(join(root, p), "utf8");
const tokens = read("assets/slop-tokens.css");
const css = read("assets/slop.css");
const html = read("demo/index.html");

test("every CSS custom property used is defined", () => {
  const defined = new Set([
    ...tokens.matchAll(/(--[a-z0-9-]+)\s*:/g),
    ...css.matchAll(/(--[a-z0-9-]+)\s*:/g),
  ].map((m) => m[1]));
  const runtimeOnly = new Set(["--mx", "--my", "--delay"]);
  const used = new Set([...css.matchAll(/var\((--[a-z0-9-]+)/g)].map((m) => m[1]));
  const missing = [...used].filter((v) => !defined.has(v) && !runtimeOnly.has(v));
  assert.deepEqual(missing, []);
});

test("the slop dial defines all five levels", () => {
  for (const level of [1, 2, 3, 4, 5]) {
    assert.match(tokens, new RegExp(`\\[data-slop="${level}"\\]`), `missing level ${level}`);
  }
});

test("dark and light themes both exist", () => {
  assert.match(tokens, /\[data-theme="light"\]/);
});

test("demo assets referenced by markup exist", () => {
  const refs = [...html.matchAll(/(?:src|href)="([^"]+)"/g)].map((m) => m[1]);
  const local = refs.filter((r) => !/^(https?:|#|data:|mailto:)/.test(r));
  const missing = local.filter((r) => !existsSync(resolve(root, "demo", r.split("?")[0])));
  assert.deepEqual(missing, []);
});

test("every reference doc is linked from SKILL.md", () => {
  const skill = read("SKILL.md");
  const files = readdirSync(join(root, "references")).filter((f) => f.endsWith(".md"));
  const unlinked = files.filter((f) => !skill.includes(`references/${f}`));
  assert.deepEqual(unlinked, []);
});

test("SKILL.md has valid-looking frontmatter", () => {
  const skill = read("SKILL.md");
  assert.match(skill, /^---\n/);
  assert.match(skill, /\nname: [a-z0-9-]+\n/);
  assert.match(skill, /\ndescription: .{40,}\n/);
  const description = /description: (.*)/.exec(skill)[1];
  assert.ok(description.length <= 1024, "description must stay under 1024 chars");
});

test("no lorem ipsum in shipped markup", () => {
  assert.doesNotMatch(html, /lorem ipsum/i);
  assert.doesNotMatch(html, /feature\s*1\b/i);
  assert.doesNotMatch(html, /your headline here/i);
});
