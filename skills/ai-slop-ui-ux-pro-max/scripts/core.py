#!/usr/bin/env python3
"""Zero-dependency BM25 search & CSV loader for AI-SLOP UI/UX PRO-MAX."""

from __future__ import annotations

import csv
import math
import re
from collections import Counter
from pathlib import Path
from typing import Dict, List, Optional, Sequence

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
    "buzzwords": "buzzwords.csv",
    "copy": "buzzwords.csv",
    "components": "components.csv",
    "component": "components.csv",
    "ui": "components.csv",
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
    "buzzwords",
    "components",
    "personas",
    "icons",
    "motion",
    "reasoning",
]

AVAILABLE_STACKS: List[str] = [
    "html-tailwind",
    "react-tailwind",
    "nextjs-shadcn",
    "vue",
    "svelte",
    "astro",
]

BOOST_FIELDS = {
    "name": 3.0,
    "keywords": 3.5,
    "category": 2.5,
    "product_category": 3.5,
    "era": 2.5,
    "section": 2.0,
    "topic": 3.0,
    "concept": 2.5,
}

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "how",
    "in", "is", "it", "of", "on", "or", "that", "the", "this", "to", "with",
}


def tokenize(text: str) -> List[str]:
    """Lowercase alphanumeric/hyphen tokenizer with lightweight stemming."""
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
    return tokens


def load_csv_rows(csv_path: Path) -> List[Dict[str, str]]:
    """Load UTF-8 CSV into a list of clean string dicts."""
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
    }
    resolved = aliases.get(key, key)
    if resolved not in AVAILABLE_STACKS:
        valid = ", ".join(AVAILABLE_STACKS)
        raise ValueError(f"Unknown stack '{stack}'. Valid stacks: {valid}")
    return load_csv_rows(STACKS_DIR / f"{resolved}.csv")


def bm25_search(
    rows: Sequence[Dict[str, str]],
    query: str,
    top_n: int = 5,
    era_filter: Optional[str] = None,
    k1: float = 1.5,
    b: float = 0.75,
) -> List[Dict[str, str]]:
    """Rank CSV rows with field-weighted Okapi BM25."""
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

    query_tokens = tokenize(query)
    if not query_tokens:
        return candidates[:top_n]

    doc_tokens_list: List[Counter[str]] = []
    doc_lengths: List[float] = []
    df: Counter[str] = Counter()

    for row in candidates:
        weighted_Counter: Counter[str] = Counter()
        total_len = 0.0
        for field, value in row.items():
            weight = BOOST_FIELDS.get(field, 1.0)
            toks = tokenize(value)
            for tok in toks:
                weighted_Counter[tok] += weight
                total_len += weight
        doc_tokens_list.append(weighted_Counter)
        doc_lengths.append(max(total_len, 1.0))
        for tok in weighted_Counter.keys():
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
                # Partial prefix bonus for compound words (e.g. "fintech" / "fin")
                for dtok, freq in tf_map.items():
                    if len(qtok) >= 4 and (dtok.startswith(qtok) or qtok.startswith(dtok)):
                        score += 0.35 * min(freq, 3.0)
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
