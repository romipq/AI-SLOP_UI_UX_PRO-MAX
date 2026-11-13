# AI-SLOP UI/UX PRO-MAX ✨

**Максимальный skill для ИИ-агентов, который намеренно генерирует самый узнаваемый
«ИИ-дизайн»: фиолетовые градиенты, glassmorphism, эмодзи вместо иконок, выдуманные
отзывы и копирайтинг из мира SaaS.**

И — чтобы это не осталось вкусовщиной — **линтер SLOP-100**, который измеряет слоп
по 90 сигналам в 9 категориях и ставит оценку от 0 до 100.

[![License: MIT](https://img.shields.io/badge/license-MIT-8b5cf6.svg)](LICENSE)
[![SLOP-100](https://img.shields.io/badge/SLOP--100-100%2F100-e11d9b.svg)](#slop-100)
[![signals](https://img.shields.io/badge/signals-90-6366f1.svg)](#slop-100)
[![deps](https://img.shields.io/badge/dependencies-0-34d399.svg)](#быстрый-старт)
[![satire](https://img.shields.io/badge/purpose-satire-fbbf24.svg)](#дисклеймер)

---

## Что это

Обычный AI-агент, которого просят «сделай современный лендинг», выдаёт один и тот же
фиолетовый градиент. Этот репозиторий берёт этот факт и доводит его до максимума:
skill-файл, дизайн-система, 9 справочников, 16 брифингов, три CLI-инструмента и четыре
работающих примера — всё, чтобы производить сертифицированный слоп **намеренно** и
**с оценкой**.

Это сатира. Инструменты — настоящие.

```
  ✦ SLOP-100 · AI-SLOP UI/UX PRO-MAX ✦
  COLOR       ██████████████████ 100%  (18/18)
  GLASS       ██████████████████ 100%  (11/11)
  COPY        ██████████████████ 100%  (20/20)
  …
  SLOP SCORE  100/100   S+ — PEAK SLOP · museum-grade
  ✅ PERFECT SLOP. No notes. Ship it before someone adds good taste.
```

---

## Быстрый старт

```bash
git clone https://github.com/romipq/AI-SLOP_UI_UX_PRO-MAX.git
cd AI-SLOP_UI_UX_PRO-MAX

# 1. Проверить, что всё работает
python3 tools/slop_lint.py examples/01-max-landing.html

# 2. Посмотреть галерею
python3 -m http.server 8000
# → http://localhost:8000

# 3. Слопифицировать приличный сайт (16 → 93 за одну команду)
python3 tools/slopify.py examples/00-before.html
```

Установка как skill: [`docs/INSTALL.md`](docs/INSTALL.md) · Claude Code, Cursor,
ChatGPT, любой API-агент.

---

## SLOP-100

Девять категорий, бюджеты которых в сумме дают ровно 100. Поэтому «сотка» требует
ширины: одними градиентами её не взять.

| Категория | Бюджет | Что считает |
|-----------|--------|-------------|
| **Copy** | 20 | AI-powered, seamless, supercharge, 10x, выдуманные бренды |
| **Color** | 18 | градиенты, gradient text, glow, 4+ оттенка |
| **Structure** | 12 | отзывы, тарифы, FAQ, cookie, чат-виджет |
| **Shape** | 11 | пилюли 9999px, bento, две CTA, радиусы 28px |
| **Glass** | 11 | blur, прозрачность, рамки, noise, mix-blend |
| **Emoji** | 9 | ✨ 🚀 💜 и эмодзи в заголовках и иконках |
| **Motion** | 8 | float, pulse, shimmer, marquee, reveal |
| **Type** | 7 | Inter + Poppins, 800, tight tracking, clamp() |
| **A11Y sins** | 4 | div-кнопки, мёртвые ссылки, outline: none |

**Оценки:** `95+ S+` · `90 S` · `80 A` · `65 B` · `45 C` · `25 D` · `<25 F — вкус обнаружен`.

Полная рубрика со всеми 90 сигналами: [`references/07-slop-score.md`](references/07-slop-score.md).
Она генерируется из кода линтера, поэтому не расходится с ним.

---

## Что внутри

```
├── SKILL.md                  ← сам skill: манифест, цикл S.L.O.P., 12 заповедей
├── index.html                ← музей-лендинг пака (100/100)
├── assets/slop.css           ← каноническая дизайн-система
├── tokens/
│   ├── slop.tokens.json      ← токены: цвета, градиенты, типографика, motion
│   └── tailwind.slop.js      ← пресет Tailwind
├── references/
│   ├── 01-design-tokens.md   ← точные значения
│   ├── 02-components.md      ← 20+ компонентов с разметкой
│   ├── 03-copywriting.md     ← формулы, лексикон, отзывы, метрики
│   ├── 04-motion.md          ← кейфреймы и 8 обязательных эффектов
│   ├── 05-emoji-iconography.md
│   ├── 06-anti-patterns.md   ← обратный чек-лист: как испортить хороший дизайн
│   ├── 07-slop-score.md      ← рубрика SLOP-100 (автогенерация)
│   ├── 08-stacks.md          ← Tailwind, React, Vue, email, mobile
│   └── 09-copy-ru.md         ← русский и украинский слоп
├── prompts/
│   ├── system-prompt.md      ← компактный промпт для вставки
│   ├── briefs.md             ← 16 готовых брифингов
│   ├── levels.md             ← LITE / CLASSIC / MAX / NUCLEAR
│   └── roast.md              ← режим «прожарки» реального UI
├── tools/
│   ├── slop_lint.py          ← 90 сигналов, 9 категорий, JSON, CI-гейт
│   ├── slopify.py            ← приличный сайт → слоп
│   ├── slop_gen.py           ← генератор фейкового стартапа
│   └── gen_rubric.py         ← обновляет документацию рубрики
├── examples/                 ← 6 страниц, включая «до/после»
└── docs/
    ├── INSTALL.md            ← установка во все агенты
    ├── PHILOSOPHY.md         ← почему всё выглядит одинаково
    └── CHEATSHEET.md         ← одна страница на печать
```

---

## Примеры

| Файл | Что это | SLOP-100 |
|------|---------|----------|
| [`index.html`](index.html) | Музей пака — лендинг о слопе, сделанный слопом | **100/100** |
| [`examples/01-max-landing.html`](examples/01-max-landing.html) | Nexora AI: 13 секций, чат, cookie, бегущая строка | **100/100** |
| [`examples/02-dashboard.html`](examples/02-dashboard.html) | Аналитический дашборд с «AI Insights» | **100/100** |
| [`examples/03-auth.html`](examples/03-auth.html) | Экран входа с вращающимся conic-орбом | **100/100** |
| [`examples/04-slopified.html`](examples/04-slopified.html) | Результат `slopify.py` над приличным сайтом | **93/100** |
| [`examples/00-before.html`](examples/00-before.html) | Контрольная группа: сдержанный сайт студии | **16/100** |

Все страницы открываются как есть, без сборки. Чтобы посмотреть сразу всё:

```bash
python3 -m http.server 8000
```

---

## Инструменты

```bash
# Оценка
python3 tools/slop_lint.py page.html
python3 tools/slop_lint.py page.html --json
python3 tools/slop_lint.py page.html --min 90   # exit 1, если меньше
python3 tools/slop_lint.py --list               # все 90 сигналов

# Слопификация (инжектит CSS, виджеты и заменяет 6 честных слов)
python3 tools/slopify.py index.html --out index.slop.html

# Фейковый стартап
python3 tools/slop_gen.py --seed 42
python3 tools/slop_gen.py --json > brand.json
```

Линтер читает подключённые локальные CSS-файлы, поэтому страница, которая использует
`assets/slop.css`, оценивается целиком — но контентные сигналы считаются только по HTML.

**CI:**

```yaml
- name: Certified slop
  run: python3 tools/slop_lint.py dist/index.html --min 90
```

---

## Уровни

| Уровень | Цель | Секций | Эмодзи | Для чего |
|---------|------|--------|--------|----------|
| **LITE** | 45+ | 4–5 | 1–2 | правдоподобная пародия |
| **CLASSIC** | 70+ | 7–9 | 3–5 | «каждый второй шаблон» |
| **MAX** | 90+ | 10–14 | 8–15 | канонический вывод (по умолчанию) |
| **NUCLEAR** | 100 | 14+ | 15+ | музей, преподавание, шутки |

Подробно: [`prompts/levels.md`](prompts/levels.md).

---

## Установка

```bash
./install.sh                    # symlink в ~/.claude/skills
./install.sh --copy             # копия
./install.sh --target .claude/skills
./install.sh --uninstall
```

Claude Code, claude.ai, ChatGPT, Cursor, Copilot и любой API-агент:
[`docs/INSTALL.md`](docs/INSTALL.md).

---

## Дисклеймер

Это **сатира и учебный инструмент**. Примеры намеренно нарушают правила доступности,
показывают выдуманные отзывы, логотипы и метрики. Не выдавайте их за реальные, не
используйте в продакшене и не применяйте для обмана пользователей.

Ценность проекта — в обратной стороне: когда клише названы и посчитаны, их проще
увидеть и не повторять. Почему это происходит — в [`docs/PHILOSOPHY.md`](docs/PHILOSOPHY.md).

---

## English

**AI-SLOP UI/UX PRO-MAX** is an agent skill + prompt pack that deliberately generates the
most recognizable "AI-made" UI/UX — violet gradients, forced glassmorphism, emoji icon
tiles, fake social proof and SaaS buzzword copy — plus **SLOP-100**, a 90-signal linter
that scores any page on how AI-generated it looks.

It's satire with real tooling: a drop-in `SKILL.md`, a design system, 9 references,
16 briefs, 3 CLI tools and 4 runnable examples. Works with Claude Code, Cursor, ChatGPT
and any agent that can read a folder.

```bash
python3 tools/slop_lint.py examples/01-max-landing.html   # 100/100
python3 tools/slopify.py examples/00-before.html           # 16 → 93
```

Everything is fictional by design. Read [`docs/PHILOSOPHY.md`](docs/PHILOSOPHY.md) for the
serious argument underneath the joke.

---

## Лицензия

MIT © 2026 [romipq](https://github.com/romipq). См. [`LICENSE`](LICENSE).

Сделано с ❤️ и, конечно, фиолетовым градиентом.
