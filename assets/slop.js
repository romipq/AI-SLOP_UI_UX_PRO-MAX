/* ============================================================================
   AI-SLOP UI/UX PRO MAX — behavior layer
   No dependencies. Progressive enhancement: if it fails, the page still works.
   ========================================================================== */
(() => {
  "use strict";

  const $ = (sel, root = document) => root.querySelector(sel);
  const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* -------------------------------------------------------------------------
     1. Sticky navbar state
     ---------------------------------------------------------------------- */
  const nav = $(".nav");
  if (nav) {
    const onScroll = () => nav.classList.toggle("is-stuck", window.scrollY > 12);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* -------------------------------------------------------------------------
     1b. Mobile menu
     ---------------------------------------------------------------------- */
  const navToggle = $(".nav__toggle");
  const mobileMenu = $("#mobile-menu");
  if (navToggle && mobileMenu) {
    const setMenu = (open) => {
      mobileMenu.hidden = !open;
      navToggle.setAttribute("aria-expanded", String(open));
      navToggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
      navToggle.querySelector("span").textContent = open ? "✕" : "☰";
    };

    navToggle.addEventListener("click", () => setMenu(mobileMenu.hidden));
    mobileMenu.addEventListener("click", (e) => {
      if (e.target.closest("a")) setMenu(false);
    });
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && !mobileMenu.hidden) {
        setMenu(false);
        navToggle.focus();
      }
    });
  }

  /* -------------------------------------------------------------------------
     2. Reveal on scroll (respects reduced motion via CSS too)
     ---------------------------------------------------------------------- */
  const revealables = $$(".reveal");
  if (revealables.length) {
    if (!("IntersectionObserver" in window) || reduceMotion) {
      revealables.forEach((el) => el.classList.add("is-visible"));
    } else {
      const io = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              entry.target.classList.add("is-visible");
              io.unobserve(entry.target);
            }
          });
        },
        { rootMargin: "0px 0px -8% 0px", threshold: 0.08 }
      );
      revealables.forEach((el, i) => {
        if (!el.style.getPropertyValue("--delay")) {
          el.style.setProperty("--delay", `${Math.min(i % 4, 3) * 70}ms`);
        }
        io.observe(el);
      });
    }
  }

  /* -------------------------------------------------------------------------
     3. Animated counters — because every stat must count up
     ---------------------------------------------------------------------- */
  const counters = $$("[data-count]");
  const runCounter = (el) => {
    const target = parseFloat(el.dataset.count);
    const decimals = (el.dataset.count.split(".")[1] || "").length;
    const suffix = el.dataset.suffix || "";
    const prefix = el.dataset.prefix || "";
    const duration = reduceMotion ? 0 : 1400;
    const start = performance.now();
    const ease = (t) => 1 - Math.pow(1 - t, 3);

    const tick = (now) => {
      const p = duration === 0 ? 1 : Math.min(1, (now - start) / duration);
      const value = target * ease(p);
      const display = decimals
        ? value.toFixed(decimals)
        : Math.round(value).toLocaleString("en-US");
      el.textContent = prefix + display + suffix;
      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };

  if (counters.length) {
    if (!("IntersectionObserver" in window)) {
      counters.forEach(runCounter);
    } else {
      const cio = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              runCounter(entry.target);
              cio.unobserve(entry.target);
            }
          });
        },
        { threshold: 0.6 }
      );
      counters.forEach((c) => cio.observe(c));
    }
  }

  /* -------------------------------------------------------------------------
     4. Marquee — clone children once for a seamless -50% loop
     ---------------------------------------------------------------------- */
  $$(".marquee__track").forEach((track) => {
    if (track.dataset.cloned === "true") return;
    track.innerHTML += track.innerHTML;
    track.dataset.cloned = "true";
    track.setAttribute("aria-hidden", "false");
  });

  /* -------------------------------------------------------------------------
     5. Cursor glow + card spotlight
     ---------------------------------------------------------------------- */
  const glow = $(".cursor-glow");
  if (glow && !reduceMotion && window.matchMedia("(hover: hover)").matches) {
    let raf = 0;
    let x = 0;
    let y = 0;
    window.addEventListener(
      "pointermove",
      (e) => {
        x = e.clientX;
        y = e.clientY;
        if (raf) return;
        raf = requestAnimationFrame(() => {
          glow.style.transform = `translate(${x}px, ${y}px) translate(-50%, -50%)`;
          raf = 0;
        });
      },
      { passive: true }
    );
  }

  $$(".card").forEach((card) => {
    card.addEventListener("pointermove", (e) => {
      const r = card.getBoundingClientRect();
      card.style.setProperty("--mx", `${((e.clientX - r.left) / r.width) * 100}%`);
      card.style.setProperty("--my", `${((e.clientY - r.top) / r.height) * 100}%`);
    });
  });

  /* -------------------------------------------------------------------------
     6. Billing toggle — monthly / annual, with the sacred "Save 20%"
     ---------------------------------------------------------------------- */
  const billing = $("[data-billing]");
  if (billing) {
    const prices = $$("[data-price]");
    const setMode = (mode) => {
      billing.dataset.billing = mode;
      $$("[data-billing-option]").forEach((btn) => {
        btn.setAttribute("aria-pressed", String(btn.dataset.billingOption === mode));
      });
      prices.forEach((el) => {
        const value = mode === "annual" ? el.dataset.priceAnnual : el.dataset.priceMonthly;
        el.textContent = value;
      });
    };
    billing.addEventListener("click", (e) => {
      const btn = e.target.closest("[data-billing-option]");
      if (btn) setMode(btn.dataset.billingOption);
    });
    setMode(billing.dataset.billing || "monthly");
  }

  /* -------------------------------------------------------------------------
     7. Accordion etiquette: open one, close the rest
     ---------------------------------------------------------------------- */
  const faq = $(".faq");
  if (faq) {
    faq.addEventListener("toggle", (e) => {
      const item = e.target;
      if (!(item instanceof HTMLDetailsElement) || !item.open) return;
      $$("details[open]", faq).forEach((other) => {
        if (other !== item) other.open = false;
      });
    }, true);
  }

  /* -------------------------------------------------------------------------
     8. Toast — the "✨ You're on the list!" of our people
     ---------------------------------------------------------------------- */
  const toast = $(".toast");
  let toastTimer = 0;
  const showToast = (message) => {
    if (!toast) return;
    const textEl = toast.querySelector("[data-toast-text]");
    if (message && textEl) textEl.textContent = message;
    toast.classList.add("is-visible");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => toast.classList.remove("is-visible"), 3200);
  };

  $$("form[data-slop-form]").forEach((form) => {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const message = form.dataset.success || "✨ You're on the list! Check your inbox.";
      showToast(message);
      form.reset();
    });
  });

  /* -------------------------------------------------------------------------
     9. Slop dial — live intensity control (1…5)
     ---------------------------------------------------------------------- */
  const dial = $(".slop-toggle");
  if (dial) {
    const label = $("[data-slop-value]", dial);
    const root = document.documentElement;
    const clamp = (n) => Math.max(1, Math.min(5, n));

    const apply = (level, persist = true) => {
      const next = clamp(level);
      root.dataset.slop = String(next);
      if (label) label.textContent = String(next);
      if (persist) {
        try {
          localStorage.setItem("slop-level", String(next));
        } catch (_) {}
      }
    };

    let start = parseInt(root.dataset.slop || "5", 10);
    try {
      const saved = parseInt(localStorage.getItem("slop-level") || "", 10);
      if (Number.isFinite(saved)) start = saved;
    } catch (_) {}
    apply(Number.isFinite(start) ? start : 5, false);

    dial.addEventListener("click", (e) => {
      const btn = e.target.closest("[data-slop-step]");
      if (!btn) return;
      apply(parseInt(root.dataset.slop || "5", 10) + parseInt(btn.dataset.slopStep, 10));
    });

    dial.addEventListener("keydown", (e) => {
      if (e.key === "ArrowRight" || e.key === "ArrowUp") {
        e.preventDefault();
        apply(parseInt(root.dataset.slop || "5", 10) + 1);
      }
      if (e.key === "ArrowLeft" || e.key === "ArrowDown") {
        e.preventDefault();
        apply(parseInt(root.dataset.slop || "5", 10) - 1);
      }
    });
  }

  /* -------------------------------------------------------------------------
     10. Tiny public API for agents / console tinkering
     ---------------------------------------------------------------------- */
  window.Slop = {
    showToast,
    setLevel(level) {
      document.documentElement.dataset.slop = String(Math.max(1, Math.min(5, level)));
      const label = document.querySelector("[data-slop-value]");
      if (label) label.textContent = String(Math.max(1, Math.min(5, level)));
    },
  };
})();
