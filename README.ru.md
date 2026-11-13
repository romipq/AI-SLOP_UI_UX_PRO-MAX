# ✨ AI-SLOP UI/UX PRO-MAX — Максимальный ИИ-Слоп Скилл 🚀

> **Язык / Language**: **[English (README.md)](./README.md)** · **Русский**

Максимальный набор скиллов для ИИ-агентов, локальный поисковый движок дизайн-клише и пак промптов, который **намеренно и с безупречным качеством кода** генерирует эталонный «нейросетевой вайб-код» UI/UX:
- 💜 Индиго-фиолетово-розовые градиенты (`from-indigo-500 via-purple-500 to-pink-500`) и плавающие пятна `blur-3xl`
- 🪟 Тотальный глассморфизм (`bg-white/5 backdrop-blur-xl border border-white/10 rounded-2xl`) на каждом блоке
- 🔤 Монокультура шрифта `Inter` / `Plus Jakarta Sans` + одно градиентное слово в каждом заголовке
- ✨ Передозировка эмодзи (`✨ 🚀 ⚡ 🧠 🔒 📈 🔥 🤖`) и иконок Lucide `<Sparkles />`
- 💬 Чистейший SaaS-баззворд копирайтинг (*«Ускорьте воркфлоу в 10 раз — бесшовно, за минуты, а не месяцы →»*, длинные тире `—`, `Без привязки карты · 14 дней бесплатно`)
- 💸 Тарифы `$0 / $29 ✨ САМЫЙ ПОПУЛЯРНЫЙ 🔥 / Custom` с тумблером `Выгода 20% 🔥`, отзывы от **Sarah Chen (VP of Product @ TechFlow)**, выдуманные логотипы `Acme Corp · QuantumAI · Synthetix` и непрошеная плавающая кнопка `✨ Спросить ИИ-копилота` в углу экрана!

---

## ⚡ Установка в 1 команду

### Вариант 1: Через стандартный Agent Skills CLI (Claude Code, Cursor, Codex, OpenCode, Windsurf, Copilot)
```bash
npx skills add romipq/AI-SLOP_UI_UX_PRO-MAX
```

### Вариант 2: Через встроенный CLI-установщик (без зависимостей)
```bash
npx github:romipq/AI-SLOP_UI_UX_PRO-MAX init --ai all
# Или точечно под вашу IDE: --ai claude | cursor | windsurf | copilot | codex | opencode
```

### Вариант 3: Готовые системные промпты (ChatGPT, Claude, Arena, v0, Bolt, Lovable)
- [`prompts/system-prompt-ru.md`](./prompts/system-prompt-ru.md) — **Максимальный системный промпт на русском языке**
- [`prompts/system-prompt-en.md`](./prompts/system-prompt-en.md) — Master System Prompt (English)
- [`prompts/one-shot-saas-landing.md`](./prompts/one-shot-saas-landing.md) — One-Shot генератор эталонного SaaS-лендинга
- [`prompts/one-shot-ai-dashboard.md`](./prompts/one-shot-ai-dashboard.md) — One-Shot генератор ИИ-дашборда
- [`prompts/slopify-existing-code.md`](./prompts/slopify-existing-code.md) — Промпт для превращения обычного человеческого UI в 100% ИИ-слоп

---

## 📦 Что внутри (3 полноценных Agent Skills)

1. **`ai-slop-ui-ux-pro-max`** — Главный движок слоп-дизайна: локальная база из 9 CSV-таблиц с поиском Okapi BM25, генератор дизайн-систем (`--design-system`), **крутилка уровня слопа от 1 до 11 (`--slop-level 11` — OMEGA SINGULARITY)**, выбор эпохи ИИ-слопа (`2024-nebula`, `2025-bento`, `2026-editorial`, `cyber-acid`, `shadcn-default`) и статический аудитор кода **Slop Score™ (0–100)**.
2. **`ai-slop-copywriter`** — Генератор нейро-маркетинговых текстов, длинных тире, оборотов *«Это не просто X — это Y»* и фейковых отзывов (поддерживает **русский** и **английский**!).
3. **`ai-slop-slopifier`** — Рефакторинг скучного человеческого дизайна в сертифицированный ИИ-слоп с оценкой **Grade S+ (95–100 баллов)** без поломки бизнес-логики.

---

## 🛠️ Примеры запуска движка `slop.py`

```bash
# Сгенерировать дизайн-систему 11-го уровня даже для локальной пекарни:
python3 skills/ai-slop-ui-ux-pro-max/scripts/slop.py "sourdough bakery" --design-system --slop-level 11 -p "ХлебПоток AI"

# Сгенерировать псевдо-эдиториал нео-слоп 2026 года (кремовый #F4F1EA + терракотовый курсив #D97757):
python3 skills/ai-slop-ui-ux-pro-max/scripts/slop.py "design studio" --design-system --era 2026-editorial -p "Atelier AI"

# Проверить любой HTML/React/Vue проект на официальный индекс ИИ-Слопа (0–100 баллов):
python3 skills/ai-slop-ui-ux-pro-max/scripts/slop.py --audit examples/nexusflow-ai-showcase.html
```

---

## 🎛️ Живое интерактивное демо (`100/100 Grade S+`)

Откройте [`examples/nexusflow-ai-showcase.html`](./examples/nexusflow-ai-showcase.html) — там встроен живой ползунок **Slop Dial (1 → 11)**, переключатель эпох ИИ-дизайна и мгновенное переключение языка **RU / EN**!

## 📄 Лицензия

MIT © [romipq](https://github.com/romipq)
