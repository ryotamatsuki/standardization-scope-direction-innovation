# Stage 9R — Repository / Reproducibility Synchronization

Date: 2026-09-06

Repository: `ryotamatsuki/standardization-scope-direction-innovation`

Active freeze: `SSDI-THEORY-FREEZE-2026-09-06-v2`

Canonical workflow: `ryotamatsuki/research-paper-workflow` **v1.3**, release commit `3e4e6a3f76d86058024d06f9710f942e21627386`.

Canonical template: `templates/STAGE_09_REPRODUCIBILITY_SETUP.md` at that release commit.

## 1. Starting remote/main SHA

- Starting remote `main`: `26d28b84dc3e0649c6c9f40e4fd706e23c0694ed`.
- Open pull requests at work start: none.
- Existing non-main branches observed: `stage7-5r-freeze-decision`, `stage7r-post-astra-repair`, `stage8r-amended-theory-freeze`, `stage9-reproducibility`, `stage10-paper-build`.
- Stage 9R branch: `stage9r-v13-reproducibility-sync`.
- No historical branch was reset, overwritten, or used as the work base.

Workflow v1.3 is a backward-compatible minor release. Stage numbering, freeze semantics, and normal routing are unchanged; its figure/table lifecycle is adopted from Stage 9R onward.

## 2. Repository tree

```text
.github/workflows/verify.yml
Makefile
README.md
requirements.txt

docs/
  THEORY_FREEZE.md
  THEORY_FREEZE_v1.md
  PROVENANCE.md
  EXPOSITION_OUTPUT_MANIFEST.json
  STAGE_07R_POST_ASTRA_REPAIR.md
  STAGE_075R_POST_ASTRA_FREEZE_DECISION.md
  STAGE_08R_AMENDED_THEORY_FREEZE.md
  STAGE_09R_REPRODUCIBILITY_SYNC.md
  THEORY_CHANGE_RECORD_2026-09-06_POST_ASTRA.md

paper/
  main.tex
  sections/

references/
  references.bib

scripts/
  symbolic_verify.py
  numerical_verify.py
  generate_exposition_outputs.py

tests/
  test_freeze_regressions.py
  test_stage9r_metadata.py

figures/
  README.md

tables/
  README.md
```

## 3. Build system

The Makefile exposes:

- `make symbolic` — symbolic identities;
- `make numerical` — numerical/global-deviation checkpoints;
- `make test` — pytest regression suite;
- `make verify` — symbolic + numerical + tests;
- `make exposition` — validate/regenerate the currently approved exposition-output set;
- `make paper` — LaTeX/BibTeX manuscript build;
- `make all` — complete local-equivalent gate: verification + exposition + paper.

The manuscript is modular LaTeX and the bibliography source is `references/references.bib`.

## 4. Verification scripts/tests

The existing model-verification code is retained without theory edits.

- `scripts/symbolic_verify.py`: quadratic private-allocation FOC, `dx^F/db`, coordinated symmetric allocation, `F''`, endpoint derivatives, threshold-polynomial identities, Bertrand price/profit identities.
- `scripts/numerical_verify.py`: canonical interior policy example, private allocation against grid optimization, unilateral price-deviation checks.
- `tests/test_freeze_regressions.py`: threshold endpoint signs, canonical interiority, `rho -> nu` mapping.
- `tests/test_stage9r_metadata.py`: active freeze/workflow metadata and the Stage-9R exposition manifest.

These implementation checks do not substitute for analytic proof; proposition authority remains `docs/THEORY_FREEZE.md`.

## 5. Environment/dependencies

CI uses Python 3.12. `requirements.txt` records:

- `sympy>=1.13,<2`;
- `pytest>=8,<9`;
- `numpy>=2,<3`.

The manuscript build installs TeX Live LaTeX base/recommended/extra and BibTeX-extra. No external data download is required for the current baseline verification or manuscript build.

## 6. Figure/table pipeline under workflow v1.3

Workflow v1.3 requires the substantive Figure/Table Architecture Gate at Stage 10, not Stage 9. Stage 9R therefore creates the reproducible plumbing without inventing a visual before that gate.

`docs/EXPOSITION_OUTPUT_MANIFEST.json` records exactly zero approved quantitative outputs. `scripts/generate_exposition_outputs.py` validates the active freeze/workflow identifiers, the explicit empty set, and provenance directories `figures/` and `tables/`.

`make exposition` is the deterministic regeneration/validation target. At Stage 10R, every accepted quantitative figure/table must be generated from verified model objects or authoritative source data, listed in the manifest, and incorporated into this target and CI.

## 7. CI / local-equivalent gate status

GitHub Actions run `34021009478` completed successfully on the Stage 9R PR head.

All required steps passed:

1. Python dependency installation — **PASS**;
2. `make verify` — **PASS**;
3. `make exposition` — **PASS**;
4. TeX dependency installation — **PASS**;
5. `make paper` — **PASS**.

Thus the repository has a functioning reproducibility baseline under the v2 freeze and workflow v1.3.

## 8. Provenance locations

- Active theory: `docs/THEORY_FREEZE.md`.
- Historical v1 theory: `docs/THEORY_FREEZE_v1.md`.
- Theory repair: `docs/THEORY_CHANGE_RECORD_2026-09-06_POST_ASTRA.md`.
- Stage 7R / 7.5R / 8R decisions: corresponding `docs/` records.
- Workflow and remote-start metadata: `docs/PROVENANCE.md`.
- Figure/table output authority: `docs/EXPOSITION_OUTPUT_MANIFEST.json`.

The active workflow authority from Stage 9R onward is v1.3 / `3e4e6a3f76d86058024d06f9710f942e21627386`. Earlier v1.1/v1.2 references are historical provenance only.

## 9. Remaining blockers

There is **no reproducibility-infrastructure blocker**.

The current manuscript text remains substantively stale because it predates the v2 repair. Stage 9R deliberately does not edit manuscript claims. A successful `make paper` here establishes build reproducibility only, not manuscript-to-freeze consistency.

Stage 10R must remove the old unconstrained-`first best` language, repair general-technology quantifiers, remove the refuted generic `C^2` policy-curvature claim, narrow endogenous-total-R&D claims, restrict the fixed-allocation benchmark correctly, and close the documented appendix exposition gaps.

## 10. Exact Stage 10R writing contract under workflow v1.3

Stage 10R must use only `SSDI-THEORY-FREEZE-2026-09-06-v2` and re-fetch current remote state before substantial implementation cycles.

It must:

1. synchronize abstract, equilibrium propositions, welfare, robustness, related-literature boundary, conclusion, appendix, and then Introduction to v2;
2. make no unconstrained first-best claim;
3. state general concave comparative statics as global weak monotonicity with strict signs only under interiority;
4. restrict fixed-allocation welfare claims to fixed symmetric allocation;
5. retain the exact selective-standardization threshold/uniqueness theorem only for the quadratic baseline;
6. retain endogenous-total-R&D only for the conditional relative-return FOC;
7. close the price-boundary-equilibrium uniqueness exposition and add required KKT/corner language;
8. complete the **mandatory v1.3 Figure/Table Architecture Gate before finalizing the Introduction**;
9. assign every headline result one primary exposition vehicle;
10. implement every required quantitative figure/table reproducibly and update `docs/EXPOSITION_OUTPUT_MANIFEST.json` plus `make exposition`;
11. run `make all` and CI before declaring the repaired manuscript complete.

No new theorem, extension, assumption, welfare claim, or broader novelty claim is authorized.

## 11. Final Stage 9R verdict

`REPRODUCIBILITY BASELINE READY`

Proceed to **Stage 10R — v2 Manuscript Synchronization and v1.3 Figure/Table Architecture Gate**.
