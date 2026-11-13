#!/usr/bin/env python3
"""Zero-dependency BM25 + Synonym Graph search engine for AI-SLOP UI/UX PRO-MAX v2.0."""

from __future__ import annotations

import csv
import math
import re
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence

SKILL_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = SKILL_ROOT / "data"
STACKS_DIR = DATA_DIR / "stacks"

DOMAIN_FILES: Dict[str, str] = {
    "style": "styles.csv",
    "styles": "styles.csv",
    "palette": "palettes.csv",
    "palettes": "palettes.csv",
    "color": "palettes.csv",
    "colors": "palettes.csv",
    "typography": "typography.csv",
    "font": "typography.csv",
    "fonts": "typography.csv",
    "ux": "ux-antipatterns.csv",
    "antipatterns": "ux-antipatterns.csv",
    "rules": "ux-antipatterns.csv",
    "buzzwords": "buzzwords.csv",
    "copy": "buzzwords.csv",
    "components": "components.csv",
    "component": "components.csv",
    "ui": "components.csv",
    "charts": "charts.csv",
    "chart": "charts.csv",
    "personas": "personas.csv",
    "testimonials": "personas.csv",
    "icons": "icons.csv",
    "emoji": "icons.csv",
    "motion": "motion.csv",
    "animation": "motion.csv",
    "reasoning": "reasoning.csv",
    "product": "reasoning.csv",
}

CANONICAL_DOMAINS: List[str] = [
    "style",
    "palette",
    "typography",
    "ux",
    "buzzwords",
    "components",
    "charts",
    "personas",
    "icons",
    "motion",
    "reasoning",
]

AVAILABLE_ERAS: List[str] = [
    "auto",
    "2024-nebula",
    "2025-bento",
    "2026-editorial",
    "cyber-acid",
    "shadcn-default",
    "ai-wrapper",
    "web3-hype",
]

AVAILABLE_STACKS: List[str] = [
    "html-tailwind",
    "react-tailwind",
    "nextjs-shadcn",
    "vue",
    "nuxt",
    "svelte",
    "astro",
    "angular",
    "solid",
    "swiftui",
    "flutter",
    "threejs",
]

SYNONYM_MAP: Dict[str, List[str]] = {
    "purple": ["indigo", "violet", "nebula", "pink"],
    "editorial": ["cream", "terracotta", "serif", "anthropic", "broadsheet"],
    "brutalist": ["terminal", "acid", "cyber", "mono", "hairline"],
    "terminal": ["cli", "cyber", "acid", "mono", "hacker"],
    "dashboard": ["analytics", "kpi", "metrics", "admin", "shadcn", "bi"],
    "fintech": ["bank", "stripe", "emerald", "card", "payments"],
    "crypto": ["web3", "defi", "solana", "token", "neon"],
    "chatbot": ["copilot", "agent", "prompt", "llm", "wrapper"],
    "bakery": ["local", "plumber", "mundane", "sourdough"],
    "plumber": ["local", "bakery", "mundane"],
    "pricing": ["plans", "tiers", "popular", "pro"],
}

BOOST_FIELDS = {
    "name": 3.2,
    "keywords": 3.8,
    "category": 2.6,
    "product_category": 3.8,
    "era": 2.8,
    "section": 2.2,
    "topic": 3.0,
    "concept": 2.8,
    "chart_type": 2.5,
}

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "how",
    "in", "is", "it", "of", "on", "or", "that", "the", "this", "to", "with",
}


def tokenize(text: str, expand_synonyms: bool = False) -> List[str]:
    """Lowercase alphanumeric tokenizer with stemming and optional synonym expansion."""
    if not text:
        return []
    raw = re.findall(r"[a-z0-9+#]+", text.lower())
    tokens: List[str] = []
    for tok in raw:
        if tok in STOPWORDS:
            continue
        tokens.append(tok)
        if len(tok) > 4 and tok.endswith("s"):
            tokens.append(tok[:-1])
        elif len(tok) > 5 and tok.endswith("ing"):
            tokens.append(tok[:-3])
        if expand_synonyms and tok in SYNONYM_MAP:
            tokens.extend(SYNONYM_MAP[tok])
    return tokens


def load_csv_rows(csv_path: Path) -> List[Dict[str, str]]:
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")
    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        rows: List[Dict[str, str]] = []
        for row in reader:
            cleaned = {
                (k.strip() if k else ""): (v.strip() if v else "")
                for k, v in row.items()
                if k is not None
            }
            if any(cleaned.values()):
                rows.append(cleaned)
        return rows


def load_domain(domain: str) -> List[Dict[str, str]]:
    key = domain.strip().lower()
    if key not in DOMAIN_FILES:
        valid = ", ".join(CANONICAL_DOMAINS)
        raise ValueError(f"Unknown domain '{domain}'. Valid domains: {valid}")
    return load_csv_rows(DATA_DIR / DOMAIN_FILES[key])


def load_stack(stack: str) -> List[Dict[str, str]]:
    key = stack.strip().lower()
    aliases = {
        "react": "react-tailwind",
        "nextjs": "nextjs-shadcn",
        "next": "nextjs-shadcn",
        "shadcn": "nextjs-shadcn",
        "html": "html-tailwind",
        "tailwind": "html-tailwind",
        "ios": "swiftui",
        "r3f": "threejs",
        "webgl": "threejs",
    }
    resolved = aliases.get(key, key)
    if resolved not in AVAILABLE_STACKS:
        valid = ", ".join(AVAILABLE_STACKS)
        raise ValueError(f"Unknown stack '{stack}'. Valid stacks: {valid}")
    return load_csv_rows(STACKS_DIR / f"{resolved}.csv")


def catalog_stats() -> Dict[str, Any]:
    domain_counts = {d: len(load_domain(d)) for d in CANONICAL_DOMAINS}
    stack_counts = {s: len(load_stack(s)) for s in AVAILABLE_STACKS}
    return {
        "domains": domain_counts,
        "stacks": stack_counts,
        "total_domain_rows": sum(domain_counts.values()),
        "total_stack_rows": sum(stack_counts.values()),
        "grand_total_rows": sum(domain_counts.values()) + sum(stack_counts.values()),
    }


def bm25_search(
    rows: Sequence[Dict[str, str]],
    query: str,
    top_n: int = 5,
    era_filter: Optional[str] = None,
    k1: float = 1.5,
    b: float = 0.75,
) -> List[Dict[str, str]]:
    """Rank CSV rows with field-weighted Okapi BM25 + synonym expansion."""
    candidates = list(rows)
    if era_filter and era_filter != "auto":
        filtered = [
            r for r in candidates
            if r.get("era", "").lower() == era_filter.lower()
        ]
        if filtered:
            candidates = filtered

    if not candidates:
        return []

    query_tokens = tokenize(query, expand_synonyms=True)
    if not query_tokens:
        return candidates[:top_n]

    doc_tokens_list: List[Counter[str]] = []
    doc_lengths: List[float] = []
    df: Counter[str] = Counter()

    for row in candidates:
        weighted: Counter[str] = Counter()
        total_len = 0.0
        for field, value in row.items():
            weight = BOOST_FIELDS.get(field, 1.0)
            for tok in tokenize(value, expand_synonyms=False):
                weighted[tok] += weight
                total_len += weight
        doc_tokens_list.append(weighted)
        doc_lengths.append(max(total_len, 1.0))
        for tok in weighted.keys():
            df[tok] += 1

    num_docs = len(candidates)
    avgdl = sum(doc_lengths) / num_docs

    scored: List[tuple[float, int, Dict[str, str]]] = []
    for idx, (row, tf_map, doc_len) in enumerate(
        zip(candidates, doc_tokens_list, doc_lengths)
    ):
        score = 0.0
        for qtok in query_tokens:
            if qtok not in tf_map:
                for dtok, freq in tf_map.items():
                    if len(qtok) >= 4 and (dtok.startswith(qtok) or qtok.startswith(dtok)):
                        score += 0.30 * min(freq, 3.0)
                continue
            doc_freq = df[qtok]
            idf = math.log(1.0 + (num_docs - doc_freq + 0.5) / (doc_freq + 0.5))
            tf = tf_map[qtok]
            denom = tf + k1 * (1.0 - b + b * (doc_len / avgdl))
            score += idf * ((tf * (k1 + 1.0)) / denom)
        if score > 0:
            out = dict(row)
            out["_score"] = f"{score:.3f}"
            scored.append((score, -idx, out))

    scored.sort(reverse=True)
    return [item[2] for item in scored[:top_n]]
