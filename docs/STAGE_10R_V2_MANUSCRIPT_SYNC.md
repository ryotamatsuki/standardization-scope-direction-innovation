# Stage 10R — v2 Manuscript Synchronization and v1.3 Exposition Architecture

Date: 2026-09-06

Repository: `ryotamatsuki/standardization-scope-direction-innovation`

Starting main: `b975e42e4cba97ee6aa2cb177efa34df3f1c85d0`

Active freeze: `SSDI-THEORY-FREEZE-2026-09-06-v2`

Canonical workflow: `ryotamatsuki/research-paper-workflow` v1.3, release commit `3e4e6a3f76d86058024d06f9710f942e21627386`.

Canonical template: `templates/STAGE_10_PAPER_BUILD.md` at the same release commit.

Pre-stage editorial gate: `docs/TOP_JOURNAL_FIT_GATE_JET_GEB_2026-09-06.md`, verdict `KEEP SSDI v2 — NO JET/GEB THEORY ROLLBACK — PROCEED TO STAGE 10R`.

## 1. Stage objective

Synchronize the production manuscript to the repaired v2 theory freeze, remove every stale claim identified by the post-Astra repair, complete the missing proof exposition, and implement the mandatory workflow-v1.3 Figure/Table Architecture Gate without changing the frozen theory.

## 2. Section-by-section construction record

### Main source / abstract

File: `paper/main.tex`.

Changes:
- exposition-only title change to *Standardization Scope and Endogenous Innovation Portfolios*;
- abstract rewritten to remove `first best` language;
- general-technology claim weakened to global nonincreasing/nondecreasing allocation responses with strictness only under interiority;
- exact selective-standardization result explicitly identified as quadratic-baseline specific;
- `graphicx` added for the verified regime map.

Frozen inputs: P1, P2R, P3R, P4, P5R and explicit nonclaims in `docs/THEORY_FREEZE.md`.

### Section 1 — Introduction

File: `paper/sections/01_introduction.tex`.

Changes:
- removes the old unconstrained-first-best comparison;
- distinguishes fixed symmetric and coordinated symmetric-R&D benchmarks from decentralized endogenous composition;
- states general allocation monotonicity with correct weak/strict quantifiers;
- adds Bryan–Lemus (2017) as a direct innovation-direction boundary;
- sharpens the distinction from Acemoglu–Gancia–Zilibotti (2012);
- signposts the verified threshold regime map.

### Section 2 — Model

File: `paper/sections/02_model.tex`.

No substantive change was required. Timing, technology, demand, regularity condition `(R)`, and equilibrium concept already match v2. The Appendix now supplies the previously abbreviated global-boundary argument supporting the all-history price continuation statement.

### Section 3 — Equilibrium and policy theorem

File: `paper/sections/03_equilibrium.tex`.

Changes:
- retains the verified Bertrand solution and quadratic private allocation;
- rewrites the general-technology result using decreasing/increasing differences;
- makes global monotonicity weak and strict signs conditional on interiority;
- states the fixed benchmark explicitly for symmetric allocations only;
- retains the exact quadratic reduced-objective curvature and threshold theorem;
- replaces stale `b^{FULL}` notation by neutral `b^*`;
- adds Figure 1, the required regime map, with an explicit quadratic-baseline scope warning.

### Section 4 — Welfare and policy benchmarks

File: `paper/sections/04_welfare.tex`.

Changes:
- retitles the section from `First Best and Second Best` to `Welfare and Policy Benchmarks`;
- retains exact CS, PS, and welfare formulas;
- records that any fixed-capacity R&D resource cost is policy invariant;
- retains the direct-diffusion / endogenous-composition decomposition only in its proved interior quadratic setting;
- replaces the old first-best proposition by the coordinated symmetric-R&D benchmark with decentralized Bertrand pricing;
- explicitly demonstrates that decentralized Bertrand welfare lies below efficient-quantity welfare by a positive gap;
- explicitly states that the unrestricted social-planner problem is not solved.

### Section 5 — Approved robustness

File: `paper/sections/05_robustness.tex`.

Changes:
- deletes the rejected generic `C^2` policy-curvature/local-uniqueness robustness claim;
- deletes the rejected steep-capacity-cost policy-persistence claim;
- retains general concave technology only as weak global directional allocation robustness plus conditional strictness;
- retains incomplete transferability only as the approved effective-transferability reparameterization and directional wedge;
- retains endogenous total R&D only through the conditional relative FOC;
- narrows empirical language outside the quadratic/interior baseline;
- explicitly notes that realized transfer `b g(x^F(b))` need not be globally increasing.

### Section 6 — Related literature

File: `paper/sections/06_related_literature.tex`.

Changes:
- adds Bryan and Lemus (2017), *The Direction of Innovation*, Journal of Economic Theory;
- states that scarce research-resource allocation and underappropriation-driven innovation direction are established ideas and are not claimed as novel;
- distinguishes AGZ (2012)'s dynamic growth/standardization mechanism from the present static scope/portfolio feedback;
- narrows the contribution to the scope-to-portfolio-to-policy-reversal architecture and exact quadratic threshold.

Bibliography: `references/references.bib` contains the Bryan–Lemus citation and DOI.

### Section 7 — Conclusion

File: `paper/sections/07_conclusion.tex`.

Changes:
- removes first-best language;
- states the general monotonicity result with correct quantifiers;
- restricts policy uniqueness to the quadratic baseline;
- clarifies that the paper does not rank selective scope against complete scope plus omitted appropriation instruments.

### Appendix

File: `paper/sections/appendix.tex`.

Changes:
- completes the global price-continuation argument by excluding separate zero-demand/one-active-product equilibria and nonnegative foreclosure deviations;
- provides the decreasing/increasing-differences proof that covers general-technology corners;
- derives strict comparative statics only at interior optima;
- retains the verified threshold-uniqueness argument;
- explicitly derives the efficient-quantity welfare gap showing why the coordinated benchmark is not an unconstrained first best;
- updates computational provenance from freeze v1 to active freeze v2 and records the exposition generator.

## 3. Figure/Table Architecture Gate

Canonical record: `docs/FIGURE_TABLE_ARCHITECTURE_STAGE10R.md`.

Every headline result has one primary exposition vehicle. Exactly one quantitative figure is required:

- `figures/policy_regime_map.pdf` — generated from the actual threshold equation `H(y,bar_nu(y))=0` over the proven domain.

No quantitative table is required. Additional allocation-path, welfare, sensitivity, and decorative visuals were rejected because they would be redundant or could communicate a stronger generality claim than the freeze supports.

Generator: `scripts/generate_exposition_outputs.py`.

Manifest: `docs/EXPOSITION_OUTPUT_MANIFEST.json`.

Representative checks:
- `bar_nu(0.7)=0.3587285925190902`;
- `bar_nu(0.9)=0.4755546783510237`.

## 4. Build and regression changes

- `requirements.txt` adds Matplotlib for deterministic figure generation.
- `make paper` now depends on `make exposition`.
- `tests/test_stage9r_metadata.py` requires the Stage-10 regime-map manifest, blocks reintroduction of rejected manuscript phrases, and verifies that citation keys and LaTeX cross-references resolve at source level.
- README and figure/table provenance records are synchronized to Stage 10R.

## 5. Theory-change audit

No frozen equation, primitive, timing assumption, parameter restriction, equilibrium concept, or theorem is changed.

The following are exposition/claim-scope repairs only:
- weak versus strict quantifier correction for general `g`;
- constrained-benchmark nomenclature;
- removal of refuted robustness statements;
- explicit proof details already implied by frozen condition `(R)`;
- title/literature positioning;
- reproducible visualization of the already-proved threshold theorem.

No rollback is triggered.

## 6. Verification status

GitHub Actions run `34022633268` on the Stage-10R PR completed successfully before the final source-reference regression was added. It passed:

1. Python dependency installation — **PASS**;
2. `make verify` — **PASS**;
3. `make exposition` — **PASS**;
4. TeX dependency installation — **PASS**;
5. `make paper` — **PASS**.

The subsequent source-reference regression and this final record update are required to pass the same CI workflow on the final PR head before merge. The PR is not to be merged on a failed or incomplete final-head run.

There is no known manuscript-content, theory-scope, bibliography, cross-reference, build, or exposition-architecture blocker.

## 7. Final verdict

`FULL DRAFT READY FOR REFEREE GATE`

This verdict becomes the authoritative main-branch state only after PR #10's final head passes CI and is merged. Stage 11 must attack the completed v2 manuscript and may not silently add new extensions or restore rejected claims.
