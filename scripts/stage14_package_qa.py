#!/usr/bin/env python3
"""Fail-closed package QA for the IJIO Stage-14 submission set."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def fail(msg: str) -> None:
    raise SystemExit(f"STAGE14_QA_FAIL: {msg}")


def read(rel: str) -> str:
    path = ROOT / rel
    if not path.exists():
        fail(f"missing required file: {rel}")
    return path.read_text(encoding="utf-8")


required = [
    "paper/main.tex",
    "paper/sections/01_introduction.tex",
    "paper/sections/03_equilibrium.tex",
    "paper/sections/08_declarations.tex",
    "paper/sections/appendix.tex",
    "references/references.bib",
    "figures/policy_regime_map.pdf",
    "submission/ijio_title_page.tex",
    "submission/ijio_highlights.txt",
    "submission/ijio_cover_letter.md",
    "submission/ijio_submission_metadata.md",
    "submission/ijio_declarations.md",
]
for rel in required:
    if not (ROOT / rel).exists():
        fail(f"missing required file: {rel}")

main = read("paper/main.tex")
if "\\author{}" not in main:
    fail("review manuscript is not explicitly anonymous via \\author{}")
if "\\input{sections/08_declarations}" not in main:
    fail("declarations section is not included")
if main.index("\\input{sections/08_declarations}") > main.index("\\bibliography"):
    fail("AI/declarations section must precede references")

m = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", main, flags=re.S)
if not m:
    fail("abstract not found")
abstract = re.sub(r"\\&", "&", m.group(1))
abstract = re.sub(r"\\[A-Za-z]+(?:\[[^\]]*\])?(?:\{[^{}]*\})?", " ", abstract)
abstract_words = re.findall(r"\b[\w'’-]+\b", abstract)
if len(abstract_words) > 250:
    fail(f"abstract exceeds 250-word indexed IJIO limit: {len(abstract_words)}")

highlights = [ln.strip() for ln in read("submission/ijio_highlights.txt").splitlines() if ln.strip()]
if not 3 <= len(highlights) <= 5:
    fail(f"expected 3-5 highlights, found {len(highlights)}")
for idx, line in enumerate(highlights, 1):
    normalized = line[1:].strip() if line.startswith("-") else line
    if len(normalized) > 85:
        fail(f"highlight {idx} exceeds 85 characters: {len(normalized)}")

production_texts = []
for path in sorted((ROOT / "paper").rglob("*.tex")):
    production_texts.append((path.relative_to(ROOT).as_posix(), path.read_text(encoding="utf-8")))
for rel in ["submission/ijio_title_page.tex", "submission/ijio_cover_letter.md", "submission/ijio_highlights.txt"]:
    production_texts.append((rel, read(rel)))
for rel, text in production_texts:
    for token in ["TODO", "FIXME", "TBD --", "USER INPUT REQUIRED", "[Corresponding author]", "[Affiliation]", "[Email]"]:
        if token in text:
            fail(f"placeholder {token!r} remains in {rel}")

caption_text = read("paper/sections/03_equilibrium.tex")
if "conditional on the global continuation restriction~\\eqref{eq:R}" not in caption_text:
    fail("Figure 1 caption does not state the (R) scope condition")

appendix = read("paper/sections/appendix.tex")
if "unique global pure-strategy Nash equilibrium" not in appendix:
    fail("price-equilibrium uniqueness wording is not restricted to pure strategies")

bib = read("references/references.bib")
bib_keys = re.findall(r"@[A-Za-z]+\s*\{\s*([^,\s]+)\s*,", bib)
if len(bib_keys) != len(set(bib_keys)):
    fail("duplicate bibliography keys detected")
bib_key_set = set(bib_keys)

cite_keys: set[str] = set()
for _, text in production_texts:
    for group in re.findall(r"\\cite\w*\{([^}]+)\}", text):
        cite_keys.update(k.strip() for k in group.split(",") if k.strip())
missing = sorted(cite_keys - bib_key_set)
if missing:
    fail("unresolved citation keys: " + ", ".join(missing))

for rel in ["submission/ijio_title_page.tex", "submission/ijio_cover_letter.md", "submission/ijio_submission_metadata.md"]:
    text = read(rel)
    for expected in ["Ryota Matsuki", "Independent Researcher", "790-0853, Matsuyama, Ehime, Japan", "ryota.matsuki@gmail.com", "0009-0005-2329-531X"]:
        if expected not in text:
            fail(f"verified author metadata missing from {rel}: {expected}")

for rel in required:
    path = ROOT / rel
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    print(f"SHA256 {digest}  {rel}")

print(f"ABSTRACT_WORDS={len(abstract_words)}")
print("HIGHLIGHT_LENGTHS=" + ",".join(str(len((h[1:].strip() if h.startswith('-') else h))) for h in highlights))
print(f"CITATION_KEYS={len(cite_keys)}; BIB_KEYS={len(bib_key_set)}")
print("STAGE14_PACKAGE_QA=PASS")
