#!/usr/bin/env node
/**
 * slop-score — score an HTML page against the AI-SLOP UI/UX 100-point rubric.
 *
 * Usage:
 *   node tools/slop-score.mjs demo/index.html
 *   node tools/slop-score.mjs demo/index.html --json
 *   node tools/slop-score.mjs demo/index.html --fail-under 90
 *   node tools/slop-score.mjs demo/index.html --quiet
 *
 * No dependencies. Reads inline styles/scripts plus local linked CSS/JS.
 */

import { readFileSync, existsSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { pathToFileURL } from "node:url";

const BUZZWORDS = [
  "supercharge", "seamless", "seamlessly", "effortless", "effortlessly", "unlock",
  "empower", "streamline", "accelerate", "elevate", "reimagine", "revolutionize",
  "orchestrate", "automate", "unify", "amplify", "turbocharge", "future-proof",
  "all-in-one", "ai-powered", "agentic", "cutting-edge", "next-generation",
  "world-class", "enterprise-grade", "blazing-fast", "frictionless", "10x", "10×",
  "single source of truth", "infinite possibilities", "modern teams", "future of work",
  "game-changer", "with the power of ai", "full potential", "busywork", "silos",
];

const REAL_TRADEMARKS = [
  "stripe", "openai", "vercel", "notion", "slack", "figma", "shopify", "intercom",
  "salesforce", "hubspot", "google", "microsoft", "apple", "amazon", "meta",
  "facebook", "linear", "supabase", "dropbox", "airbnb", "uber", "netflix",
];

const clamp = (n, min, max) => Math.max(min, Math.min(max, n));
const countMatches = (haystack, re) => (haystack.match(re) || []).length;
const has = (haystack, re) => re.test(haystack);

function readLocal(root, relPath) {
  try {
    const clean = relPath.split("?")[0].split("#")[0];
    if (!clean || /^(https?:)?\/\//.test(clean) || clean.startsWith("data:")) return "";
    const full = resolve(root, clean);
    return existsSync(full) ? readFileSync(full, "utf8") : "";
  } catch {
    return "";
  }
}

function extractAssets(html, root) {
  let css = "";
  let js = "";

  for (const m of html.matchAll(/<style[^>]*>([\s\S]*?)<\/style>/gi)) css += `\n${m[1]}`;
  for (const m of html.matchAll(/<link[^>]+rel=["']stylesheet["'][^>]*>/gi)) {
    const href = /href=["']([^"']+)["']/i.exec(m[0]);
    if (href) css += `\n${readLocal(root, href[1])}`;
  }
  for (const m of html.matchAll(/<script[^>]*>([\s\S]*?)<\/script>/gi)) js += `\n${m[1]}`;
  for (const m of html.matchAll(/<script[^>]+src=["']([^"']+)["'][^>]*>/gi)) {
    js += `\n${readLocal(root, m[1])}`;
  }
  return { css, js };
}

function visibleText(html) {
  return html
    .replace(/<script[\s\S]*?<\/script>/gi, " ")
    .replace(/<style[\s\S]*?<\/style>/gi, " ")
    .replace(/<!--[\s\S]*?-->/g, " ")
    .replace(/<[^>]+>/g, " ")
    .replace(/&[a-z]+;/gi, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function category(name, max, checks) {
  const score = checks.reduce((sum, c) => sum + (c.ok ? c.pts : 0), 0);
  return { name, max, score, checks };
}

export function scoreHtml(html, { root = process.cwd(), file = "<inline>" } = {}) {
  const { css, js } = extractAssets(html, root);
  const all = `${html}\n${css}\n${js}`;
  const text = visibleText(html);
  const lowerText = text.toLowerCase();
  const lowerAll = all.toLowerCase();

  const gradientCount = countMatches(css || html, /(linear|radial|conic)-gradient/gi);
  const glassCount = countMatches(css, /backdrop-filter\s*:/gi);
  const buzzHits = BUZZWORDS.filter((w) => lowerAll.includes(w));
  const mediaQueries = countMatches(css, /@media[^{]+\{/gi);
  const priceCards = countMatches(html, /class=["'][^"']*price-card/gi);
  const quotes = countMatches(html, /<blockquote/gi);
  const stars = countMatches(html, /★/g);
  const ariaCount = countMatches(html, /\b(aria-label|aria-labelledby|alt)=["'][^"']+/gi);

  const ids = new Set(Array.from(html.matchAll(/\bid=["']([^"']+)["']/gi)).map((m) => m[1]));
  const hashLinks = Array.from(html.matchAll(/href=["']#([^"']+)["']/gi)).map((m) => m[1]);
  const deadAnchors = hashLinks.filter((h) => h && !ids.has(h));
  const localRefs = [
    ...Array.from(html.matchAll(/(?:src|href)=["']([^"'#][^"']*)["']/gi)).map((m) => m[1]),
  ].filter((p) => !/^(https?:)?\/\//.test(p) && !p.startsWith("data:") && !p.startsWith("mailto:"));
  const missingRefs = localRefs.filter((p) => !existsSync(resolve(root, p.split("?")[0])));

  const trademarkHits = REAL_TRADEMARKS.filter((t) => lowerText.includes(t));
  const hasLorem = has(lowerAll, /lorem ipsum|feature\s*1\b|your headline|placeholder text|dolor sit amet/);

  const categories = [
    category("Gradient chroma", 10, [
      { label: "Gradient text on a heading", pts: 3, ok: has(all, /background-clip\s*:\s*text|-webkit-text-fill-color\s*:\s*transparent/i) },
      { label: "Violet + pink + cyan all present", pts: 2, ok: ["8b5cf6|7c3aed|6366f1|a855f7", "ec4899|d946ef|db2777|f472b6", "22d3ee|06b6d4|38bdf8|67e8f9"].every((p) => has(lowerAll, new RegExp(p))) },
      { label: "Gradient CTA", pts: 2, ok: has(all, /(btn--primary|\.cta|button)[^{]*\{[^}]*gradient|--grad-cta/i) },
      { label: "3+ gradient surfaces / animated gradient", pts: 2, ok: gradientCount >= 3 },
      { label: "Gradient on a phrase, not everything", pts: 1, ok: has(html, /<(h1|h2)[^>]*>[\s\S]{0,400}?(grad-text|gradient-text|text-transparent)/i) },
    ]),

    category("Glass & depth", 10, [
      { label: "backdrop-filter blur", pts: 4, ok: has(css, /backdrop-filter\s*:[^;]*blur/i) },
      { label: "1px translucent border", pts: 2, ok: has(css, /border[^;]*rgba\(\s*255\s*,\s*255\s*,\s*255\s*,\s*0?\.\d+\s*\)/i) },
      { label: "Layered / glow shadow", pts: 2, ok: has(css, /box-shadow\s*:[^;]*rgba/i) },
      { label: "3+ glass surfaces", pts: 2, ok: glassCount >= 3 },
    ]),

    category("Atmosphere", 10, [
      { label: "Blurred orbs / color blobs", pts: 3, ok: has(all, /(class=["'][^"']*\borb|\.orb\b)/i) && has(css, /blur/i) },
      { label: "Mesh gradient background", pts: 2, ok: has(all, /mesh|grad-mesh/i) },
      { label: "Noise / grain overlay", pts: 2, ok: has(all, /feturbulence|noise|grain/i) },
      { label: "Grid or dot pattern", pts: 2, ok: has(all, /slop-grid|background-image[^;]*(to right|to bottom)|background-size\s*:\s*64px/i) },
      { label: "Hero visual glow / orb image", pts: 1, ok: has(all, /orb-image|<img[^>]+orb|app-frame/i) },
    ]),

    category("Typography", 10, [
      { label: "Fluid clamp() type", pts: 2, ok: has(css, /clamp\(/i) },
      { label: "Negative letter-spacing", pts: 2, ok: has(css, /letter-spacing\s*:\s*-0?\.0[1-9]/i) },
      { label: "Uppercase wide-tracked eyebrow", pts: 2, ok: has(all, /(class=["'][^"']*eyebrow|\.eyebrow)/i) && has(css, /letter-spacing\s*:\s*0?\.1[0-9]em/i) },
      { label: "Display ≥ 56px", pts: 2, ok: has(css, /--text-hero|font-size\s*:\s*(5[6-9]|[6-9]\d|1\d\d)px/i) },
      { label: "Modern sans (Inter/Geist/Satoshi/Manrope)", pts: 2, ok: has(all, /inter|geist|satoshi|manrope|jakarta/i) },
    ]),

    category("Layout & structure", 10, [
      { label: "Sticky nav", pts: 3, ok: has(css, /position\s*:\s*sticky/i) },
      {
        label: "Container 1120–1360px",
        pts: 2,
        ok:
          has(css, /max-width\s*:\s*(var\(--container[^)]*\)|1(1[2-9]\d|2\d\d|3[0-6]\d)px)/i) ||
          has(css, /--container(?:-wide)?\s*:\s*1(1[2-9]\d|2\d\d|3[0-6]\d)px/i),
      },
      { label: "Section rhythm ≥ 72px", pts: 2, ok: has(css, /--section-y|padding-block\s*:\s*(7[2-9]|[89]\d|1\d\d)px/i) },
      { label: "Bento / asymmetric 12-col grid", pts: 2, ok: has(css + html, /repeat\(12|span-?(3|4|6|8)\b|card--span/i) },
      { label: "2+ responsive breakpoints", pts: 1, ok: mediaQueries >= 2 },
    ]),

    category("Components", 10, [
      { label: "Announcement pill / badge", pts: 2, ok: has(html, /class=["'][^"']*\bpill\b/i) && has(html, /(new|beta|launch|coming)/i) },
      { label: "Dual CTA (primary + ghost)", pts: 2, ok: has(html, /btn--primary/i) && has(html, /btn--ghost/i) },
      { label: "3 pricing tiers with featured", pts: 2, ok: priceCards >= 3 && has(html, /price-card--featured|badge-popular|most popular/i) },
      { label: "FAQ accordion", pts: 2, ok: has(html, /<details|class=["'][^"']*faq/i) },
      { label: "Avatar stack", pts: 1, ok: has(html, /avatar-stack|class=["'][^"']*\bavatar\b/i) },
      { label: "Toast / modal / empty state", pts: 1, ok: has(html, /class=["'][^"']*(toast|modal|empty-state)/i) },
    ]),

    category("Copy", 10, [
      { label: `≥ 8 distinct buzzwords (${buzzHits.length} found)`, pts: 3, ok: buzzHits.length >= 8, detail: buzzHits.join(", ") },
      { label: '"10×" / "AI-powered" / "agentic" in hero area', pts: 2, ok: has(visibleText(html.slice(0, html.indexOf("</section>") + 10)).toLowerCase(), /10×|10x|ai-powered|agentic/) },
      { label: "Benefit-driven H1 with gradient phrase", pts: 2, ok: has(html, /<h1[\s\S]{0,500}<\/h1>/i) && has(html, /<(h1)[^>]*>[\s\S]{0,500}?(grad-text|gradient|10×|faster|supercharge)/i) },
      { label: "No lorem ipsum / placeholders", pts: 2, ok: !hasLorem },
      { label: "Outcome-based CTA labels", pts: 1, ok: countMatches(text, /\b(Start|Get started|Try|Join|Book|Watch|Build|Claim|Talk to)\b/gi) >= 2 },
    ]),

    category("Social proof", 10, [
      { label: "Fake logo wall / marquee", pts: 2, ok: has(html, /logo-wall|marquee|class=["'][^"']*\blogo\b/i) },
      { label: "Testimonial quotes", pts: 2, ok: quotes >= 2 },
      { label: "Star ratings", pts: 2, ok: stars >= 3 },
      { label: "Stats / counters", pts: 2, ok: has(html + js, /data-count|class=["'][^"']*\bstat\b/i) },
      { label: "Trust microcopy", pts: 2, ok: has(lowerText, /no credit card|soc\s*2|trusted by|loved by|\d[\d,]{2,}\+?\s*(teams|users|customers)/) },
    ]),

    category("Motion", 10, [
      { label: "Scroll reveal", pts: 2, ok: has(all, /\.reveal|intersectionobserver/i) },
      { label: "Marquee animation", pts: 2, ok: has(css, /@keyframes[^{]*marquee|animation[^;]*marquee/i) },
      { label: "Animated counters", pts: 2, ok: has(js, /data-count|runCounter|requestAnimationFrame/i) },
      { label: "Hover transform / glow", pts: 2, ok: has(css, /:hover[^{]*\{[^}]*(transform|box-shadow)/i) },
      { label: "Ambient animation (float/sheen/pulse)", pts: 1, ok: has(css, /slop-float|slop-sheen|slop-pulse|@keyframes\s+float|@keyframes\s+shimmer/i) },
      { label: "prefers-reduced-motion handling", pts: 1, ok: has(css, /prefers-reduced-motion/i) },
    ]),

    category("Craft & ethics", 10, [
      { label: "Title + meta description in slop voice", pts: 2, ok: has(html, /<title>[^<]{10,}<\/title>/i) && has(html, /<meta[^>]+name=["']description["'][^>]+content=["'][^"']{20,}/i) },
      { label: "lang + viewport meta", pts: 2, ok: has(html, /<html[^>]+lang=["'][a-z-]+/i) && has(html, /name=["']viewport["']/i) },
      { label: "alt / aria labels (5+)", pts: 2, ok: ariaCount >= 5 },
      { label: "No real trademarks or people", pts: 2, ok: trademarkHits.length === 0, detail: trademarkHits.length ? `found: ${trademarkHits.join(", ")}` : "" },
      { label: "No dead anchors or missing assets", pts: 2, ok: deadAnchors.length === 0 && missingRefs.length === 0, detail: [...deadAnchors.map((a) => `#${a}`), ...missingRefs.map((r) => r)].join(", ") },
    ]),
  ];

  const total = categories.reduce((s, c) => s + c.score, 0);
  const max = categories.reduce((s, c) => s + c.max, 0);
  const verdict =
    total >= 95 ? "Peak slop" :
    total >= 90 ? "Certified slop" :
    total >= 80 ? "Slop-adjacent" :
    total >= 65 ? "Diet slop" :
    total >= 40 ? "Corporate minimalism" :
    "De-slopped";

  const weakest = [...categories].sort((a, b) => a.score / a.max - b.score / b.max).slice(0, 3);

  return {
    file,
    total: clamp(total, 0, max),
    max,
    verdict,
    categories,
    buzzwords: buzzHits,
    weakest: weakest.map((c) => ({ name: c.name, score: c.score, max: c.max })),
  };
}

const BAR = (score, max) => {
  const filled = Math.round((score / max) * 10);
  return "█".repeat(filled) + "░".repeat(10 - filled);
};

export function formatReport(result) {
  const lines = [];
  lines.push("");
  lines.push(`  AI-SLOP UI/UX PRO MAX — scorecard`);
  lines.push(`  file: ${result.file}`);
  lines.push("");
  for (const c of result.categories) {
    lines.push(`  ${BAR(c.score, c.max)}  ${String(c.score).padStart(2)}/${c.max}  ${c.name}`);
    for (const check of c.checks) {
      const mark = check.ok ? "✓" : "·";
      const detail = !check.ok && check.detail ? `  (${check.detail})` : "";
      lines.push(`      ${mark} ${check.label}${detail}`);
    }
  }
  lines.push("");
  lines.push(`  TOTAL   ${result.total}/${result.max}   ${result.verdict}`);
  if (result.total < 95) {
    lines.push(`  weakest: ${result.weakest.map((w) => `${w.name} ${w.score}/${w.max}`).join(" · ")}`);
  }
  lines.push("");
  return lines.join("\n");
}

function main(argv) {
  const args = argv.slice(2);
  const file = args.find((a) => !a.startsWith("--"));
  if (!file) {
    console.error("Usage: node tools/slop-score.mjs <file.html> [--json] [--quiet] [--fail-under 90]");
    process.exit(2);
  }
  const failIdx = args.indexOf("--fail-under");
  const failUnder = failIdx > -1 ? Number(args[failIdx + 1]) : null;
  const json = args.includes("--json");
  const quiet = args.includes("--quiet");

  const abs = resolve(process.cwd(), file);
  if (!existsSync(abs)) {
    console.error(`File not found: ${file}`);
    process.exit(2);
  }

  const result = scoreHtml(readFileSync(abs, "utf8"), { root: dirname(abs), file });

  if (json) console.log(JSON.stringify(result, null, 2));
  else if (!quiet) console.log(formatReport(result));

  if (failUnder !== null && result.total < failUnder) {
    if (!json && !quiet) console.log(`  ✗ below --fail-under ${failUnder}\n`);
    process.exit(1);
  }
}

if (import.meta.url === pathToFileURL(process.argv[1] || "").href) main(process.argv);
