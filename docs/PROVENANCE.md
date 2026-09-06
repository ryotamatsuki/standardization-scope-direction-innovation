# Provenance

## Active canonical state

- Freeze ID: `SSDI-THEORY-FREEZE-2026-09-06-v2`
- Freeze date: 2026-09-06
- Freeze record: `docs/THEORY_FREEZE.md`
- Stage 8R merge commit: `26d28b84dc3e0649c6c9f40e4fd706e23c0694ed`
- Stage 7.5R authorization commit: `7c7f19094c0151f350e0b256152c34da6ba9f851`

## Workflow authority

- Repository: `ryotamatsuki/research-paper-workflow`
- Active version from Stage 9R onward: `v1.3`
- Release commit: `3e4e6a3f76d86058024d06f9710f942e21627386`
- Stage 10 template: `templates/STAGE_10_PAPER_BUILD.md` at that release commit
- Figure/table checklist: `checklists/FIGURE_TABLE_CHECKLIST.md` at that release commit

Earlier workflow references in repository history (`v1.1` and `v1.2`) remain historical provenance only.

## Stage 9R

- Starting remote `main`: `26d28b84dc3e0649c6c9f40e4fd706e23c0694ed`
- Stage 9R branch: `stage9r-v13-reproducibility-sync`
- Stage 9R merge commit: `ba641614eb191928193f443d46d15d40af08b1d9`
- Verdict: `REPRODUCIBILITY BASELINE READY`

Stage 9R established the v2 reproducibility baseline and v1.3 exposition-output plumbing without changing theory or manuscript claims.

## Pre-Stage-10R JET/GEB architecture gate

A project-specific **JET vs GEB Two-Journal Top-Journal Architecture Gate** was inserted after Stage 9R. RAND Journal of Economics was explicitly excluded from the active comparison by project instruction.

- Active gate record: `docs/TOP_JOURNAL_FIT_GATE_JET_GEB_2026-09-06.md`
- Gate verdict: `KEEP SSDI v2 — NO JET/GEB THEORY ROLLBACK — PROCEED TO STAGE 10R`
- JET: no in-project generalization; a credible move requires a new general policy theorem and a distinct novelty position relative to Bryan–Lemus (2017)
- GEB: no in-project redesign; a credible move requires materially new game-theoretic interaction or a general strategic result
- Current-paper route: preserve v2 and complete Stage 10R

Historical note: commit `094344c2141c4c5e98c22f72c3b2031f8f93b47c` briefly contained a RAND-inclusive three-journal gate created by parallel work. It is superseded and not active authority.

## Stage 10R

- Starting remote `main`: `b975e42e4cba97ee6aa2cb177efa34df3f1c85d0`
- Open pull requests at Stage 10R start: none
- Working branch: `stage10r-v2-manuscript-sync`
- Active manuscript title after exposition-only retitling: *Standardization Scope and Endogenous Innovation Portfolios*
- Theory authority remains `SSDI-THEORY-FREEZE-2026-09-06-v2`; no theory change is authorized or made
- Figure/Table Architecture record: `docs/FIGURE_TABLE_ARCHITECTURE_STAGE10R.md`
- Quantitative-output authority: `docs/EXPOSITION_OUTPUT_MANIFEST.json`
- Required quantitative outputs: one verified policy-regime figure; no quantitative tables

Stage 10R manuscript repairs include:

1. removal of unconstrained first-best claims;
2. replacement of globally strict general-technology comparative statics by global weak monotonicity with strictness only under interiority;
3. explicit restriction of the fixed-allocation benchmark to symmetric allocations;
4. deletion of the rejected generic `C^2` policy-curvature robustness claim;
5. deletion of the rejected steep-capacity-cost policy-persistence claim;
6. retention of endogenous-total-R&D only through the conditional relative-return FOC;
7. completion of boundary-price-equilibrium and KKT/corner exposition;
8. explicit closest-literature positioning against Bryan–Lemus (2017) and Acemoglu–Gancia–Zilibotti (2012);
9. implementation of the v1.3 Figure/Table Architecture Gate and reproducible threshold regime map.

The title change is an exposition/positioning change only and does not modify the frozen research question, game, assumptions, propositions, or welfare concept.
