/**
 * Tests for slop-score. Run with: node --test tools/
 */
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync, writeFileSync, mkdtempSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";
import { scoreHtml } from "./slop-score.mjs";

const here = dirname(fileURLToPath(import.meta.url));
const repoRoot = resolve(here, "..");
const script = join(here, "slop-score.mjs");
const demoPath = join(repoRoot, "demo/index.html");
const demo = readFileSync(demoPath, "utf8");

const CLEAN_PAGE = `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Docs</title>
  <style>
    body { font-family: Georgia, serif; max-width: 680px; margin: 0 auto; color: #222; background: #fff; }
    h1 { font-size: 32px; font-weight: 400; }
    a { color: #0645ad; }
    pre { background: #f6f6f6; padding: 16px; border-radius: 4px; }
  </style>
</head>
<body>
  <h1>Getting started</h1>
  <p>Install the package and run the command. Read the <a href="#usage">usage notes</a>.</p>
  <h2 id="usage">Usage</h2>
  <pre>npm install thing</pre>
</body>
</html>`;

const scoreDemo = () => scoreHtml(demo, { root: join(repoRoot, "demo"), file: demoPath });

test("demo scores peak slop", () => {
  const result = scoreDemo();
  assert.ok(result.total >= 90, `expected >= 90, got ${result.total}`);
  assert.equal(result.total, 100);
  assert.equal(result.verdict, "Peak slop");
});

test("demo passes every category", () => {
  for (const cat of scoreDemo().categories) {
    assert.equal(cat.score, cat.max, `${cat.name} lost points: ${cat.checks.filter((c) => !c.ok).map((c) => c.label)}`);
  }
});

test("flat documentation page scores as de-slopped", () => {
  const result = scoreHtml(CLEAN_PAGE, { root: repoRoot, file: "clean.html" });
  assert.ok(result.total < 40, `expected < 40, got ${result.total}`);
  assert.equal(result.verdict, "De-slopped");
});

test("lorem ipsum and real trademarks are penalised", () => {
  const bad = CLEAN_PAGE.replace("Install the package", "Lorem ipsum dolor sit amet").replace("Docs", "Stripe clone");
  const result = scoreHtml(bad, { root: repoRoot, file: "bad.html" });
  const copy = result.categories.find((c) => c.name === "Copy");
  const craft = result.categories.find((c) => c.name === "Craft & ethics");
  assert.equal(copy.checks.find((c) => c.label.includes("lorem")).ok, false);
  assert.equal(craft.checks.find((c) => c.label.includes("trademarks")).ok, false);
});

test("--json emits machine-readable output", () => {
  const out = spawnSync(process.execPath, [script, demoPath, "--json"], { encoding: "utf8" });
  assert.equal(out.status, 0);
  const parsed = JSON.parse(out.stdout);
  assert.equal(parsed.total, 100);
  assert.equal(parsed.categories.length, 10);
});

test("--fail-under exits non-zero when the page misses the bar", () => {
  const dir = mkdtempSync(join(tmpdir(), "slop-"));
  const file = join(dir, "clean.html");
  writeFileSync(file, CLEAN_PAGE);
  const out = spawnSync(process.execPath, [script, file, "--quiet", "--fail-under", "90"], { encoding: "utf8" });
  assert.equal(out.status, 1);
});

test("missing file exits with code 2", () => {
  const out = spawnSync(process.execPath, [script, "does-not-exist.html", "--quiet"], { encoding: "utf8" });
  assert.equal(out.status, 2);
});
