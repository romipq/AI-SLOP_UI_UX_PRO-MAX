# Why every AI page looks the same

*A serious note inside an unserious repository.*

The violet gradient is not a bug in the model. It is the model working exactly as
designed, on a distribution that is narrower than it looks.

---

## 1. The mode is the message

Language models generate likely continuations. When you ask for "a modern SaaS landing
page", the most likely continuation is not an original design — it is the **average** of
every landing page the model has seen: Dribbble shots, Product Hunt launches, template
marketplaces, Tailwind examples, shadcn demos, a thousand "10 SaaS websites that convert"
listicles.

Averages are smooth. Averages are safe. Averages look like a violet gradient with a
glass card on top, because that is what the majority of the training distribution looks
like at low resolution.

Design is high-dimensional: hierarchy, rhythm, contrast, brand, copy, motion, accessibility.
Models are asked to output it in one shot, from a prompt with no brand, no audience
research and no constraints. The safest high-probability point in that space is the
generic one. **The slop is the maximum-likelihood design.**

---

## 2. Seven causes, not one

1. **Mode-seeking decoding.** Sampling the most probable tokens produces the most
   probable page. Originality lives in the tails, and the tails are penalized.
2. **Preference tuning for "polished".** Human raters reward screenshots that look
   finished. Gradients, glass and glow read as "finished" in a thumbnail.
3. **Component defaults.** Tailwind, shadcn, MUI and Bootstrap ship with sensible
   radii, neutral borders and system fonts. Overriding them is work; the default is slop-adjacent.
4. **Evaluation by screenshot.** Agents and benchmarks are scored on a single render.
   Sections that require interaction, copy that requires context, and restraint that
   requires comparison all disappear at that resolution.
5. **Risk aversion.** "Supercharge your workflow" is unfalsifiable. "Cuts invoice
   processing from 4 hours to 20 minutes" is a claim that can be wrong. Models prefer
   the sentence that cannot fail.
6. **Cheap composability.** A gradient is one line. A design system is a week. Emoji are
   free. A real illustration is not.
7. **The feedback loop.** AI-generated pages are now training data for the next model.
   The average is being averaged with itself.

None of these are fixed by a better prompt. They are fixed by constraints: a brand, a
user, a real number, a reason to be different.

---

## 3. Why a satire skill

Naming a cliché precisely is the first step to escaping it. "It looks AI-generated" is a
feeling; **"gradient text, five hues, glass nav, three invented testimonials, 99.9%
uptime"** is a diagnosis.

This repository takes the diagnosis to its logical maximum:

- a skill that generates the clichés on demand, so they can be studied;
- a design system that encodes them as tokens;
- a linter that scores them across 90 weighted signals;
- examples that are intentionally, measurably bad.

The joke is not that AI makes ugly pages. The joke is that the ugliness is **predictable
enough to be engineered and graded**.

---

## 4. What SLOP-100 is and isn't

**It is:**
- a measure of *recognizability*, not quality;
- a way to compare two pages without arguing about taste;
- a teaching device: every point comes with a receipt;
- a mirror: point it at a production site and see what it says.

**It isn't:**
- a design review (contrast, performance, content strategy are out of scope);
- a moral judgement (a page can be sloppy and successful);
- a universal standard (the weights encode 2023–2025 internet taste, which will age);
- a substitute for user research, which no linter can replace.

A beautiful page can score 60 because it uses a violet accent and Inter. A human can make
ugly slop at 20. The score measures the **signals**, and signals are proxies.

---

## 5. The dangerous part is not the gradient

Gradients are harmless. The parts worth caring about are:

- **Invented social proof.** Fake logos, fake testimonials, fake "10,000+ teams" — these
  are not aesthetic choices, they are false claims with a friendly typeface.
- **Simulated accessibility.** A page that *looks* friendly while using div buttons,
  dead links and unlabeled icons excludes people while performing care.
- **The confidence gap.** "Powered by GPT-5" on a product that calls a small classifier,
  "99.9% uptime" on a service with no status page, "enterprise-grade security" on a
  prototype. The aesthetic of reliability without the substance is the actual slop.

This repository makes those choices visible by scoring them. It does not recommend them.

---

## 6. If you want out

The inverse checklist is short:

1. **One accent color.** Not five.
2. **One surface.** Glass on everything means glass on nothing.
3. **Real copy.** A specific number, a named customer, a sentence about a mechanism.
4. **Fewer sections.** Nine sections is a funnel; three is a page.
5. **A font choice with a reason.** Inter is fine. Inter + Poppins + an italic serif is a costume.
6. **Motion with a job.** Reveal on scroll is fine. Pulse forever is a nervous tic.
7. **Accessible by default.** Real buttons, visible focus, alt text, 4.5:1.
8. **Delete the testimonial you can't source.** The page will survive.

The fastest way to make an AI page not look AI-made is to give it something only a human
with context could know: a real constraint, a real customer, a real opinion.

---

## 7. The last joke

The linter is 90 heuristics, 9 categories and a 100-point scale. It can tell you that a
page looks machine-made with a confidence the page itself does not deserve.

Which is, of course, exactly what slop does.

---

*Further reading inside the repo: `references/06-anti-patterns.md` for the inverse
checklist, `references/07-slop-score.md` for the rubric and its limitations.*
