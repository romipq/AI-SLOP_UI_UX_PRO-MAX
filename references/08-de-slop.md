# 08 — De-Slopping (the redemption arc)

The pack is satire, but the critique is real. De-slopping is not "remove everything until it's
boring" — it's *replacing decoration with hierarchy, and adjectives with facts*.

Use this file when the user says: "now make it tasteful", "make it look human", "fix the AI look",
or "why does this feel cheap?".

---

## 1. What actually makes it feel AI-generated

| Layer | The tell | Why it reads as slop |
| ----- | -------- | -------------------- |
| Color | Everything is a gradient | No hierarchy: if everything glows, nothing matters |
| Type | 72px hero, 16px everything else | No rhythm between levels |
| Layout | Nine sections, all equal weight | No editorial point of view |
| Copy | "10×", "seamless", "unlock" | Claims with no evidence; words with no meaning |
| Proof | Generic logos and perfect quotes | Unfalsifiable, therefore untrustworthy |
| Motion | Everything animates on scroll | Attention is spent on decoration, not content |
| Detail | Emoji everywhere | Signals "generated", not "designed" |

**The core diagnosis:** slop substitutes *effects* for *decisions*.

---

## 2. The de-slop decision tree

```
Does this element communicate information?
├── No  → delete it (orb, gradient, sparkle, badge)
└── Yes → Does it need decoration to be understood?
    ├── No  → make it quiet: 1px border, no glow, no blur
    └── Yes → does the decoration carry meaning?
        ├── Yes → keep, but reduce to one idea (e.g. gradient only on the key metric)
        └── No  → remove decoration, strengthen type/hierarchy instead
```

Then ask: **"Would a human designer defend this pixel?"** If not, it goes.

---

## 3. Ten-step migration

1. **Freeze the structure.** Keep the sections; they're usually fine. Rewrite, don't rebuild.
2. **Pick one accent.** Violet. Everything else becomes ink, paper, and a single muted gray.
3. **Kill gradient text.** Replace with solid ink. Use weight and size for emphasis.
4. **Remove 80% of the glow.** Keep it on the primary CTA only — or nowhere.
5. **Reduce radii.** 24–32px → 10–12px for cards, 8px for inputs, pill only for tags.
6. **Flatten the glass.** Solid surfaces with 1px borders beat blur in 90% of cases.
7. **Fix the type scale.** Hero 56px max, body 16–17px/1.6, labels 13px, one weight contrast.
8. **Rewrite copy.** Every claim gets a number, a mechanism, or gets deleted (§5).
9. **Replace proof.** Real logos (with permission), real quotes, real metrics, or none at all.
10. **Re-add one delight.** A single, well-crafted detail — a nice focus ring, a considered empty
    state, a 120ms button press. That's what "designed" feels like.

---

## 4. Palette and surfaces

| Slop | De-slopped |
| ---- | ---------- |
| `#0B0B14` + 3 orbs + mesh | `#0E0E10` flat, or warm `#FAFAF7` light |
| 4-stop gradient everywhere | 1 accent, 3 neutral steps |
| Glass cards | `#16161A` surfaces / `#FFF` with `#E7E5E4` border |
| Glow shadows | `0 1px 2px rgba(0,0,0,.06), 0 8px 24px -12px rgba(0,0,0,.12)` |
| 32px radii | 10–12px |
| Gradient buttons | Solid accent, 44px height, 8px radius |

Light mode usually reads more "human" for docs, dashboards, and B2B tools. Dark is fine when it's
flat and quiet.

---

## 5. Copy rewrites

| Slop | De-slopped |
| ---- | ---------- |
| "Supercharge your workflow with AI ✨" | "Cut standup prep from 40 minutes to 5" |
| "The all-in-one platform for modern teams" | "Issues, docs, and releases in one place" |
| "Trusted by 12,000+ teams" | "Used by 312 teams, including Figma and Ramp" (only if true) |
| "10× faster" | "Median build time: 42s → 9s" |
| "Seamlessly integrates with your stack" | "Works with GitHub, Linear, and Slack" |
| "Enterprise-grade security" | "SOC 2 Type II · SSO · data residency in EU/US" |
| "Start for free" | "Create a workspace — free for 3 users" |
| "Loved by teams everywhere" | One named quote with a role and company |
| "AI-powered insights" | "Flags PRs that touch >5 files without tests" |

Rules:
- Specific beats big. One real number beats ten round ones.
- Replace adjectives with mechanisms ("because").
- Delete any sentence that would survive on a competitor's site unchanged.
- Keep the second person, drop the exclamation marks.

---

## 6. Component swaps

| Slop component | De-slopped replacement |
| -------------- | ---------------------- |
| Announcement pill with "NEW" | Small text link in the nav: "Changelog →" |
| Avatar stack + 5 stars | "Used by 312 teams" plain text, or a real logo row |
| Emoji icon chip | 20px line icon, 1.5px stroke, muted color |
| Gradient pricing card + badge | Slightly raised card with a 1px accent border and "Recommended" label |
| Marquee logo wall | Static row, 5 logos, grayscale, 60% opacity |
| FAQ with glowing borders | Plain rows with a 1px divider |
| Final CTA panel with glow | Simple centered heading + one button |
| Cursor glow | nothing. please. |

---

## 7. Accessibility debts to repay

Slop frequently ships these bugs. Fix all of them:

- [ ] Muted text below 4.5:1 → use a darker gray (`#5B5578` on light, `#B4B4CC` on dark).
- [ ] Gradient text fails contrast → keep gradients off body copy; ensure the H1 is legible.
- [ ] Emoji-only buttons → `aria-label` + visible text.
- [ ] `div` buttons → real `<button>` / `<a>`.
- [ ] Focus rings removed → restore `:focus-visible` with 2px accent outline + 2px offset.
- [ ] Autoplay/marquee motion → honor `prefers-reduced-motion`.
- [ ] Placeholder as label → real `<label>`, `autocomplete`, `inputmode`.
- [ ] Icon-only nav → labels on mobile, `aria-label` everywhere.
- [ ] Low-contrast glass over busy backgrounds → raise the surface opacity.
- [ ] Text baked into images → real text.

---

## 8. What to keep from the slop

Not everything is a sin. These are genuinely good ideas that got overused:

- **Clear section rhythm** — hero → proof → features → price → FAQ → CTA is a proven sequence.
- **A single, confident accent color.**
- **One strong focal point per screen.**
- **Responsive bento grids** for heterogeneous content.
- **Small, honest motion** on interaction (150–250ms).
- **Social proof** — just make it real.
- **A great empty state** — the one place delight is always welcome.

De-slopping is subtraction plus *editorial judgment*, not the deletion of personality.

---

## 9. Verification

Re-run the rubric after de-slopping — the score should land **below 60**, deliberately. Then check:

- [ ] One accent color, one type family (two max).
- [ ] Hero ≤ 56px, body 16–17px, line-height ≥ 1.55.
- [ ] Contrast ≥ 4.5:1 for all text.
- [ ] At most two shadows in the whole page.
- [ ] Every number is real and sourced.
- [ ] Focus visible on every interactive element.
- [ ] Reduced motion respected.
- [ ] One intentional delight, everything else quiet.

A de-slopped page should feel like a *person* made a decision — not a model made a collage.
