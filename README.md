# AI-SLOP UI/UX PRO-MAX ✨

> **Максимальный скилл для ИИ-агентов, который осознанно генерирует тот самый
> «интерфейс от нейросети»: фиолетовые градиенты, глассморфизм, эмодзи вместо иконок,
> размытые блобы, бессмысленные метрики и SaaS-копирайт без единого факта.**
>
> *An agent skill that deliberately generates the cliché "AI-generated" UI — at
> maximum craft, on purpose. Satire with a spec sheet.*

[![slop score](https://img.shields.io/badge/slop%20score-100%2F100-7C3AED?style=flat-square)](#метрика)
[![components](https://img.shields.io/badge/components-18-EC4899?style=flat-square)](#что-внутри)
[![license](https://img.shields.io/badge/license-MIT-22D3EE?style=flat-square)](LICENSE)

---

## Что это

Это **не** туториал «как сделать красиво» и **не** очередной UI-kit.

Это промпт-пак + дизайн-система + линтер, которые воспроизводят самый узнаваемый
визуальный клише 2023–2026 годов — и делают это **идеально**. Не «плохо», а именно
*усреднённо*: каждый элемент по отдельности сделан хорошо, а вместе они неотличимы
от десяти тысяч других лендингов.

Скилл полезен, когда нужно:

- 🎯 сгенерировать «типичный AI-стартап» намеренно (сатира, роаст, арт);
- 🧪 получить нейтральный бенчмарк, с которым можно сравнивать настоящий дизайн;
- 🧠 научить агента распознавать клише — и не воспроизводить их случайно;
- 🔍 разобрать чужой сайт по 100-балльной шкале «слопа»;
- 🛠 быстро собрать каркас лендинга, который точно никого не обидит.

> **Главный трюк:** чем точнее соблюдены правила, тем смешнее результат. Слоп — это
> не отсутствие ремесла, а ремесло, направленное на середину распределения.

---

## Быстрый старт

```bash
git clone https://github.com/romipq/AI-SLOP_UI_UX_PRO-MAX.git
cd AI-SLOP_UI_UX_PRO-MAX

# посмотреть максимальный слоп в браузере
python3 -m http.server 8000
# → http://localhost:8000/                       демо-хаб
# → http://localhost:8000/templates/landing.html
# → http://localhost:8000/templates/dashboard.html
# → http://localhost:8000/templates/components.html

# или просто
make demo

# измерить слоп
python3 scripts/slop_lint.py templates/landing.html
```

Скилл не требует зависимостей: линтер — чистый Python 3.9+, стили — чистый CSS,
шаблоны — один HTML-файл без сборки.

---

## Установка как скилл

Скилл — это обычный Markdown с YAML-frontmatter (`SKILL.md`). Его можно подключить
к любому агенту, который умеет читать файлы.

**Claude Code / Claude Agent Skills**

```bash
# проектный уровень
mkdir -p .claude/skills/ai-slop-ui-ux-pro-max
cp -r SKILL.md references assets scripts .claude/skills/ai-slop-ui-ux-pro-max/

# или глобально
mkdir -p ~/.claude/skills/ai-slop-ui-ux-pro-max
cp -r SKILL.md references assets scripts ~/.claude/skills/ai-slop-ui-ux-pro-max/
```

**Cursor**

```bash
mkdir -p .cursor/rules
cp SKILL.md .cursor/rules/ai-slop.mdc
```

**Любой другой агент (ChatGPT, Gemini, локальные модели)**

Возьмите системный промпт из [`examples/prompts.md`](examples/prompts.md) §2 —
он самодостаточен и не требует доступа к репозиторию.

**Проверка, что скилл подключился**

```
Сделай лендинг для AI-сервиса встреч в стиле AI-SLOP PRO-MAX, уровень L5.
```

Агент должен выдать тёмную страницу со стеклянной навигацией, градиентным H1,
эмодзи-иконками, тремя тарифами и «Most Popular ⭐» — и запустить линтер.

---

## Что внутри

```
AI-SLOP_UI_UX_PRO-MAX/
├── SKILL.md                      ← доктрина, воркфлоу, контракт вывода
├── index.html                    демо-хаб (открывать первым)
├── references/
│   ├── 00-manifesto.md           теория слопа, таксономия признаков
│   ├── 01-color.md               палитра и токены
│   ├── 02-gradients.md           меш, конические, анимированные градиенты
│   ├── 03-glass.md               рецепты стекла, слои, fallback'и
│   ├── 04-typography.md          Inter, шкала, градиентный текст
│   ├── 05-layout.md              12 секций, сетки, ритм
│   ├── 06-copy.md                движок buzzwords (EN + RU)
│   ├── 07-emoji.md               эмодзи как иконочная система
│   ├── 08-motion.md              анимации, тайминги, reduced motion
│   ├── 09-components.md          18 канонических компонентов
│   ├── 10-slop-score.md          рубрика на 100 баллов
│   └── 11-escape-hatch.md        антидот: как рас-слопить сайт
├── assets/
│   ├── slop.css                  полная дизайн-система (~1 000 строк)
│   └── slop-tokens.json          машиночитаемые токены (W3C DTCG)
├── templates/
│   ├── landing.html              L5-лендинг, 100/100
│   ├── dashboard.html            L5-дашборд, 94/100
│   └── components.html           галерея всех компонентов, 100/100
├── scripts/
│   └── slop_lint.py              скорер без зависимостей
└── examples/
    └── prompts.md                11 готовых промптов
```

---

## Доктрина: S.L.O.P.

| | Рычаг | Что это |
|---|---|---|
| **S** | **Saturated gradients** | фиолетовый → индиго → розовый, всегда `135deg`, всегда текстом на H1 |
| **L** | **Layered glass** | `rgba(255,255,255,.04)` + `backdrop-filter: blur(20px)` + рамка 8% белого |
| **O** | **Omnipresent emoji** | ✨ 🚀 ⚡ 🧠 🔄 🛡️ — вся иконочная система |
| **P** | **Peak buzzwords** | seamless, effortless, next-gen, AI-powered, 10x, at scale |

### 10 неизменных законов

1. Каждая поверхность — стекло.
2. Фиолетовый — цвет интеллекта.
3. H1 — всегда градиентный текст.
4. Если есть эмодзи, SVG не нужен.
5. Каждое существительное получает прилагательное.
6. Движение доказывает, что продукт жив.
7. Тарифов ровно три, средний — «Most Popular ⭐».
8. Социальное доказательство вымышленное, но уверенное.
9. Числа круглые, крупные и необъяснимые.
10. Пустого места не остаётся — туда идёт размытый блоб.

### Уровни

| Уровень | Название | Оценка |
|---|---|---|
| L1 | Honest MVP | 20–35 |
| L2 | Seed Round | 36–55 |
| L3 | Series A | 56–70 |
| L4 | Unicorn | 71–88 |
| **L5** | **PRO-MAX / AGI-grade** | **89–100** |

---

## Метрика

`scripts/slop_lint.py` считает 100 баллов по семи категориям и вычитает штрафы
за сломанную доступность и отсутствие маркировки сатиры.

```
  AI-SLOP PRO-MAX · slop-lint v2.0.0
  ────────────────────────────────────────────────────────────
  templates/landing.html

   100/100   S   AGI-grade
  ████████████████████████████████████████████████  100%

  Gradient    20/20  ████████████████████
  Glass       18/18  ████████████████████
  Emoji       15/15  ████████████████████
  Buzzwords   20/20  ████████████████████
  Structure   12/12  ████████████████████
  Motion       8/8   ████████████████████
  Proof        7/7   ████████████████████
  ...
  Maximum slop achieved. Indistinguishable from the training set. ✨
```

```bash
# обычный отчёт
python3 scripts/slop_lint.py templates/landing.html

# подробно: что найдено и чего не хватает
python3 scripts/slop_lint.py templates/landing.html --verbose

# JSON для CI/дашбордов
python3 scripts/slop_lint.py templates/ --json > slop-report.json

# CI-гейт: упасть, если слоп ниже 90
python3 scripts/slop_lint.py templates/landing.html --min-score 90
```

Линтер умеет:

- читать `.html`, `.css`, `.jsx`, `.tsx`, `.vue`, `.svelte`, `.astro`;
- подтягивать подключённые локальные CSS (`<link rel="stylesheet">`, `@import`);
- отделять разметку от дизайн-системы, чтобы классы из CSS не «фальшивили» структуру;
- показывать бонусные признаки (✨, grain, AI-пузырь, SOC 2) и штрафы.

---

## Шаблоны

| Файл | Что это | Оценка |
|---|---|---|
| [`templates/landing.html`](templates/landing.html) | полный L5-лендинг: hero, логотипы, 6 фич, 3 шага, метрики, отзывы, тарифы, FAQ, CTA, футер | **100/100** |
| [`templates/dashboard.html`](templates/dashboard.html) | L5-дашборд: сайдбар, KPI, график, AI-копайлот, таблица агентов, фид | **94/100** |
| [`templates/components.html`](templates/components.html) | все 18 компонентов на одной странице | **100/100** |

Все шаблоны самодостаточны (кроме общего `assets/slop.css`) и адаптивны.

---

## Промпты

[`examples/prompts.md`](examples/prompts.md) — 11 готовых промптов: системный,
параметризованный, русский, роаст, де-слоп, React/Tailwind-порт, цикл «сделай хуже»
и гардрейлы.

Пример:

```
Use the AI-SLOP PRO-MAX skill. Build a landing page for an AI meeting-notes app
at level L5. Run scripts/slop_lint.py and iterate until the score is ≥ 95.
```

---

## Антидот

Слоп — это диагноз, а не приговор. Если клиент говорит «это не про нас»,
откройте [`references/11-escape-hatch.md`](references/11-escape-hatch.md): там
восемь движений, которые превращают безликую страницу в бренд, и тест
«закрой логотип — назовёшь компанию?».

```bash
python3 scripts/slop_lint.py ваш-сайт.html --verbose
# > 70 на странице, которая должна быть брендом, — это проблема конкретики
```

---

## Этика

Пак создан как **сатира и инструмент анализа**. Поэтому:

- каждый шаблон помечен комментарием «generated aesthetic / satire»;
- все имена, логотипы и метрики вымышлены;
- запрещено выдавать результат за оригинальный бренд-дизайн;
- запрещено применять эстетику к медицине, праву, финансам и безопасности —
  лоск подразумевает доверие, которого у контента нет;
- доступность остаётся обязательной: контраст AA, `:focus-visible`,
  `prefers-reduced-motion`. Слоп — это стиль, а не сломанный продукт.

---

## English TL;DR

**AI-SLOP UI/UX PRO-MAX** is an agent skill + design system + linter that generates
the maximum-strength "AI startup" aesthetic on purpose: 135° violet→pink gradients,
glassmorphism, emoji icons, blur blobs, fictional proof and buzzword copy.

- `SKILL.md` — doctrine, 8-step workflow, output contract.
- `references/` — 12 deep-dive files (color, gradients, glass, type, layout, copy
  in EN + RU, emoji, motion, 18 components, scoring, de-slopping).
- `assets/slop.css` — the whole system; `slop-tokens.json` — W3C tokens.
- `templates/` — a 100/100 landing page, a 94/100 dashboard, a component gallery.
- `scripts/slop_lint.py` — stdlib-only scoring of any HTML/CSS/JSX on a 100-point
  rubric, with a CI gate (`--min-score`).

```bash
python3 -m http.server 8000                       # see the templates
python3 scripts/slop_lint.py templates/landing.html --verbose
```

MIT. Satire. Label your output. Keep it accessible.

---

## Лицензия

[MIT](LICENSE) © 2026 romipq

Сделано с ❤️, ✨ и абсолютно нулевой оригинальностью. В этом и смысл.
