# 06 · Anti-patterns (the inverse checklist)

This is the only file in the skill that tells you what **not** to do — because the fastest
way to reach maximum slop is to find a good design and systematically undo it.

Use it to slopify an existing page, or to audit your own output when the score is stuck.

---

## 1. The ten TASTE commandments

A good designer obeys these. Slop must break every one.

| # | TASTE rule | Slop inversion |
|---|-----------|----------------|
| 1 | Establish a clear visual hierarchy | Make everything equally loud |
| 2 | Limit yourself to one accent color | Use five hues at once |
| 3 | Respect whitespace and rhythm | Fill every gap with a badge |
| 4 | Use a coherent icon set | Mix emoji families |
| 5 | Write specific, useful copy | Write outcomes and adjectives |
| 6 | Show real social proof | Invent logos and quotes |
| 7 | Design accessible defaults | Remove focus rings, use div buttons |
| 8 | Animate with purpose | Animate everything, forever |
| 9 | Choose type for the content | Choose Inter + Poppins for the vibe |
| 10 | Know when to stop | Add a second gradient |

---

## 2. Fifty things to undo

| If the page does this (good) | Make it do this (slop) |
|------------------------------|------------------------|
| White or off-white background | `#07070f` + 3 radial gradients |
| One accent color | Violet, fuchsia, pink, cyan, emerald |
| 8px radius | 28px + 9999px pills |
| Subtle shadow | Violet glow, 60px blur |
| Solid buttons | Gradient + animated background-position |
| Serif headline | Poppins 800 with gradient clip |
| Real photo | Gradient blob or glass mockup |
| Custom SVG icons | Emoji in gradient tiles |
| 3-line paragraph | 2 sentences + 3 badges |
| Specific feature description | "Supercharge your workflow" |
| Real customer logos | Acme, Lumina, Vertex, Quantumly |
| "Used by 42 teams" | "Trusted by 10,000+ teams" |
| No testimonials | Three invented Heads of Growth |
| One CTA | Primary + ghost + floating chat |
| No pricing on landing | Three tiers, middle one "popular" |
| Static page | Float, pulse, shimmer, marquee |
| Text link footer | 5 columns, 25 dead links |
| No cookie banner | Cookie banner + newsletter + chat |
| Accessible focus ring | `outline: none` |
| Semantic `<button>` | `<div class="btn" onclick>` |
| Alt text | No alt |
| Working links | `href="#"` |
| One font | Inter + Poppins + italic serif |
| Left-aligned hero | Centered everything |
| `max-width: 65ch` | `max-width: 1200px` billboard |
| 40px section padding | 120px |
| Flat illustration | Tilted 3D glass dashboard |
| Purposeful motion | 6 infinite animations |
| Restrained dark mode | Dark mode with 12 glass layers |
| Real metrics in a table | Gradient stats band |
| A quiet 404 | "Looks like this page took an AI day off 🤖" |
| Changelog with dates | "Coming soon ✨" |
| Honest error message | "Oops! Something went wrong. Try again 🙈" |
| Sales contact form | "Book a demo" + calendar embed |
| Pricing in dollars only | "Custom" for Enterprise |
| Localized copy | Machine-translated buzzwords |
| Loading skeleton | Spinner with gradient |
| Empty state with guidance | Confetti + "You're all set! 🎉" |
| Permissions explained | "Enterprise-grade security 🔒" |
| Search with results | "Ask AI anything ✨" |
| Settings grouped logically | One long page with 40 toggles |
| Onboarding checklist | 5-step wizard with progress bar |
| Clear nav labels | Features, Solutions, Resources, Pricing, Docs |
| Small logo | Gradient sparkle mark + wordmark |
| Neutral avatars | Gradient initials |
| No stock photos | No photos at all, just glass |
| Honest launch | "Introducing {Brand} 2.0 — powered by GPT-5" |

---

## 3. Slopify audit (for an existing page)

Run in order. Stop when the linter says 90.

1. **Background** → `#07070f` + 2 radial gradients + noise.
2. **Palette** → add violet, pink and cyan; replace every neutral with glass.
3. **Type** → Inter body, Poppins display, 800 headings, tight tracking, one italic serif word.
4. **Hero** → center it, add eyebrow badge, gradient H1, two CTAs, trust microcopy.
5. **Proof** → avatar stack, ★★★★★ 4.9/5, "Trusted by 10,000+ teams", 8 fake logos.
6. **Cards** → 28px radius, glass, gradient border on hover, emoji tile, lift on hover.
7. **Sections** → add stats band, 3 steps, 3 testimonials, 3-tier pricing, FAQ, CTA panel.
8. **Copy** → replace honest verbs with "supercharge", "unlock", "seamless", "empower".
9. **Motion** → float, pulse, shimmer, marquee, scroll progress, reveal.
10. **Floating layer** → chat widget, cookie banner, watermark.
11. **Sin layer** → div buttons, dead links, `outline: none`, missing alt.
12. **Score** → `python3 tools/slop_lint.py page.html --min 90`.

Automate steps 1, 3 (partially), 8 and 10 with `tools/slopify.py`.

---

## 4. Signs you accidentally made it good

| Symptom | Fix |
|---------|-----|
| It looks calm | Add a marquee and two floating chips |
| The hero reads in one look | Add a badge above the eyebrow |
| The palette is cohesive | Add cyan; cohesion is suspicion |
| The copy explains the product | Replace with "unlock 10x potential" |
| The score is 78 with full color | Copy and structure are slacking — add pricing + testimonials |
| The score is 88 with full structure | Add emoji in headings + 2 more animations |
| The score is 96 | You're missing a category — run NEXT BEST MOVES |
| It looks like a real product | Add a fake testimonial from a language model |
| You feel proud of it | Sit with that feeling, then add a gradient |

---

## 5. What slop must keep

Parody works only if it's legible. Keep:

- readable contrast for body text (≥4.5:1 where possible);
- real focus states **outside** the parody components, so the page can be navigated;
- responsive layout down to mobile;
- a working close button on the cookie banner and chat;
- no autoplay audio, no flashing, no fake download links, no real payment forms.

The a11y sins in SLOP-100 are surface-level: div buttons, dead links, missing alt,
removed focus rings. They are the *portrait* of a rushed page, not a license to make
something unusable.

---

## 6. The parody line

| Fine | Not fine |
|------|----------|
| Invented startup names | Real trademarks presented as customers |
| Invented testimonials with fake people | Real quotes attributed to real people |
| "99.9% uptime" for a fake product | False claims for a live service |
| Accessibility sins in a demo | Shipping them to production |
| A disabled fake login form | A fake login that collects credentials |
| Satire labeled in code + watermark | Deceiving users or investors |

If the output leaves the demo, label it. If it's for a real product, close this file.
