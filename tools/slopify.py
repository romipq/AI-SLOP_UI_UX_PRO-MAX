#!/usr/bin/env python3
"""slopify.py — turn a tasteful page into certified AI slop.

Takes any HTML file, injects the full slop design system, adds the mandatory
floating widgets, wraps the H1 in a gradient, and replaces a handful of honest
words with venture-backed synonyms. Then it lints its own output.

Usage:
    python3 tools/slopify.py examples/00-before.html
    python3 tools/slopify.py site/index.html --out site/index.slop.html
    python3 tools/slopify.py page.html --css assets/slop.css --no-copy

MIT © 2026 romipq
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

try:
    from slop_lint import score_file
except ImportError:  # pragma: no cover
    score_file = None

# Word → buzzword. Applied once per word, max 6 substitutions per page, so the
# output stays readable enough to be funny.
REPLACEMENTS = [
    (r"\bfast\b", "lightning-fast"),
    (r"\bquick\b", "blazing-fast"),
    (r"\beasy\b", "effortless"),
    (r"\bsimple\b", "effortless"),
    (r"\buse\b", "leverage"),
    (r"\bhelp\b", "empower"),
    (r"\bimprove\b", "supercharge"),
    (r"\bbetter\b", "10x better"),
    (r"\bsecure\b", "enterprise-grade"),
    (r"\bmodern\b", "cutting-edge"),
    (r"\bstart\b", "supercharge"),
    (r"\bscale\b", "scale effortlessly"),
]

WIDGETS = """
  <div class="scroll-progress" id="slopProgress"></div>

  <div class="slop-watermark">SLOPIFIED · AI-SLOP PRO-MAX</div>

  <button class="chat-bubble" id="slopChatBtn" aria-label="Open AI chat">✨</button>
  <div class="chat-window" id="slopChat">
    <div class="chat-head">
      <span class="icon icon--sm">🤖</span>
      <div>
        <div style="font-size:.86rem;font-weight:700;">AI Assistant</div>
        <div style="font-size:.68rem;color:var(--slop-dim);">● Online · replies in seconds</div>
      </div>
    </div>
    <div class="chat-msg">Hi! 👋 I'm your AI-powered assistant. How can I help you supercharge your workflow today?</div>
    <div class="field"><input type="text" placeholder="Ask AI anything..." aria-label="Ask AI" />
      <button class="btn btn-primary btn-sm" type="button">Send</button></div>
  </div>

  <div class="cookie" id="slopCookie">
    <div>🍪 We use cookies to enhance your experience. By continuing you agree to our
      <a href="#" style="color:#c4b5fd;">Cookie Policy</a>.</div>
    <div class="flex gap-2">
      <div class="btn btn-primary btn-sm" onclick="document.getElementById('slopCookie').classList.add('hide')">Accept all</div>
      <button class="btn btn-ghost btn-sm" onclick="document.getElementById('slopCookie').classList.add('hide')">Manage</button>
    </div>
  </div>
"""

SCRIPT = """
  <script>
    (function () {
      var bar = document.getElementById('slopProgress');
      addEventListener('scroll', function () {
        var h = document.documentElement;
        bar.style.width = (h.scrollTop / (h.scrollHeight - h.clientHeight) * 100) + '%';
      }, { passive: true });
      var chat = document.getElementById('slopChat');
      document.getElementById('slopChatBtn').addEventListener('click', function () {
        chat.classList.toggle('open');
      });
    })();
  </script>
"""


def protect_blocks(html: str):
    """Temporarily remove <script>/<style> so we never rewrite code."""
    vault = []

    def stash(m):
        vault.append(m.group(0))
        return f"@@SLOPBLOCK{len(vault) - 1}@@"

    protected = re.sub(
        r"<(script|style)\b[^>]*>.*?</\1>", stash, html, flags=re.S | re.I
    )
    return protected, vault


def restore_blocks(html: str, vault) -> str:
    for i, block in enumerate(vault):
        html = html.replace(f"@@SLOPBLOCK{i}@@", block)
    return html


def slopify_copy(html: str, limit: int = 6):
    protected, vault = protect_blocks(html)
    parts = re.split(r"(<[^>]+>)", protected)
    changes = 0
    for i, part in enumerate(parts):
        if not part or part.startswith("<"):
            continue
        for pattern, replacement in REPLACEMENTS:
            if changes >= limit:
                break
            part, n = re.subn(pattern, replacement, part, count=1, flags=re.I)
            changes += n
        parts[i] = part
        if changes >= limit:
            break
    return restore_blocks("".join(parts), vault), changes


def add_gradient_h1(html: str) -> str:
    def repl(m):
        attrs, inner = m.group(1), m.group(2)
        if "grad-text" in inner:
            return m.group(0)
        if "class=" in attrs:
            attrs = re.sub(r'class="([^"]*)"', r'class="\1 display"', attrs, count=1)
        else:
            attrs += ' class="display"'
        return f"<h1{attrs}><span class=\"grad-text\">{inner}</span></h1>"

    return re.sub(r"<h1([^>]*)>(.*?)</h1>", repl, html, flags=re.S | re.I)


def inject(html: str, css: str) -> str:
    style_tag = f"\n  <style>\n/* injected by slopify.py */\n{css}\n  </style>\n"

    if "</head>" in html.lower():
        idx = html.lower().rfind("</head>")
        html = html[:idx] + style_tag + html[idx:]
    elif "<body" in html.lower():
        idx = html.lower().find("<body")
        html = html[:idx] + style_tag + html[idx:]
    else:
        html = style_tag + html

    # body class
    def body_repl(m):
        attrs = m.group(1)
        if 'class="' in attrs:
            attrs = attrs.replace('class="', 'class="slopified ', 1)
        elif "class='" in attrs:
            attrs = attrs.replace("class='", "class='slopified ", 1)
        else:
            attrs += ' class="slopified"'
        return f"<body{attrs}>"

    html = re.sub(r"<body([^>]*)>", body_repl, html, count=1, flags=re.I)

    if "</body>" in html.lower():
        idx = html.lower().rfind("</body>")
        html = html[:idx] + WIDGETS + SCRIPT + html[idx:]
    else:
        html += WIDGETS + SCRIPT
    return html


def ensure_document(html: str) -> str:
    low = html.lower()
    if "<html" in low:
        return html
    return (
        "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
        "  <meta charset=\"UTF-8\" />\n"
        "  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />\n"
        "  <title>Slopified ✨</title>\n</head>\n<body>\n" + html + "\n</body>\n</html>\n"
    )


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Turn a tasteful HTML page into AI slop.")
    ap.add_argument("path", help="input .html file")
    ap.add_argument("--out", help="output path (default: <name>.slop.html)")
    ap.add_argument("--css", default=str(ROOT / "assets" / "slop.css"),
                    help="stylesheet to inject (default: assets/slop.css)")
    ap.add_argument("--no-copy", action="store_true", help="skip buzzword substitution")
    ap.add_argument("--quiet", action="store_true", help="don't print the score report")
    args = ap.parse_args(argv)

    src = Path(args.path)
    if not src.is_file():
        print(f"error: no such file: {src}", file=sys.stderr)
        return 2

    css_path = Path(args.css)
    if not css_path.is_file():
        print(f"error: no stylesheet at {css_path}", file=sys.stderr)
        return 2

    html = ensure_document(src.read_text(encoding="utf-8", errors="replace"))
    css = css_path.read_text(encoding="utf-8", errors="replace")

    before = score_file(src)["score"] if score_file and src.suffix == ".html" else None

    html = add_gradient_h1(html)
    changed = 0
    if not args.no_copy:
        html, changed = slopify_copy(html)
    html = inject(html, css)

    out = Path(args.out) if args.out else src.with_suffix(".slop.html")
    out.write_text(html, encoding="utf-8")

    after = score_file(out)["score"] if score_file else None

    if not args.quiet:
        print()
        print("  🪄 slopify.py — taste removed successfully")
        print("  " + "─" * 46)
        print(f"  in    {src}")
        print(f"  out   {out}")
        print(f"  css   {css_path.name} ({len(css) // 1024} KB injected)")
        if changed:
            print(f"  copy  {changed} honest word(s) replaced with synonyms")
        if before is not None and after is not None:
            print(f"  slop  {before}/100  →  {after}/100")
        print("  " + "─" * 46)
        print("  Next: python3 tools/slop_lint.py " + str(out))
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
