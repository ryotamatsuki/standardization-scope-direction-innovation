# Provenance

## Active canonical state

- Freeze ID: `SSDI-THEORY-FREEZE-2026-09-06-v2`
- Freeze date: 2026-09-06
- Freeze record: `docs/THEORY_FREEZE.md`
- Stage 8R merge commit: `26d28b84dc3e0649c6c9f40e4fd706e23c0694ed`
- Stage 7.5R authorization commit: `7c7f19094c0151f350e0b256152c34da6ba9f851`

## Workflow authority

- Repository: `ryotamatsuki/research-paper-workflow`
- Version used from Stage 9R onward: `v1.3`
- Release commit: `3e4e6a3f76d86058024d06f9710f942e21627386`
- Stage 9 template: `templates/STAGE_09_REPRODUCIBILITY_SETUP.md` at that release commit
- v1.3 figure/table lifecycle is active; Stage 10 must complete the Figure/Table Architecture Gate before manuscript completion.

Earlier workflow references in repository history (`v1.1` and `v1.2`) remain historical provenance only and are not the active authority for Stage 9R onward.

## Stage 9R start-state record

- Starting remote `main`: `26d28b84dc3e0649c6c9f40e4fd706e23c0694ed`
- Open pull requests at start: none
- Existing non-main branches observed at start: `stage7-5r-freeze-decision`, `stage7r-post-astra-repair`, `stage8r-amended-theory-freeze`, `stage9-reproducibility`, `stage10-paper-build`
- Stage 9R working branch: `stage9r-v13-reproducibility-sync`
- Concurrent-work policy: no reset or overwrite of historical branches; Stage 9R starts from current remote main only.

## Reproducibility scope

Stage 9R changes repository infrastructure, metadata, tests, and exposition-output plumbing only. It does not alter the frozen game, equations, propositions, welfare claims, robustness scope, or novelty boundary.

At Stage 9R there are zero approved quantitative manuscript figures/tables. This is intentional: workflow v1.3 assigns exposition-vehicle selection to the Stage 10 Figure/Table Architecture Gate. The Stage 9R pipeline validates an explicit empty manifest so later outputs cannot appear through undocumented manual steps.

## Pre-Stage-10R one-shot editorial gate

After Stage 9R and before Stage 10R, a project-specific **JET vs GEB Two-Journal Top-Journal Architecture Gate** is active.

RAND Journal of Economics is explicitly excluded from this gate by project instruction and is not part of the active architecture comparison.

- Gate base state after the superseding user instruction: main `094344c2141c4c5e98c22f72c3b2031f8f93b47c`
- Active gate record: `docs/TOP_JOURNAL_FIT_GATE_JET_GEB_2026-09-06.md`
- Gate role: journal-identity / architecture routing only; no theory-change authority
- Gate verdict: `KEEP SSDI v2 — NO JET/GEB THEORY ROLLBACK — PROCEED TO STAGE 10R`
- JET decision: no in-project generalization; a credible JET move requires a new general policy theorem beyond weak allocation monotonicity and must clear the Bryan–Lemus (2017) direction-of-innovation collision test
- GEB decision: no in-project generalization; a credible GEB move requires materially new game-theoretic interaction or a general strategic result
- Preferred separate top-theory fork if pursued later: JET-oriented general theory of policy-controlled spillovers and endogenous allocation
- Authorized current-paper route: `Stage 9R -> JET/GEB Top-Journal Architecture Gate -> Stage 10R`

Historical note: commit `094344c2141c4c5e98c22f72c3b2031f8f93b47c` briefly contained a three-journal JET/GEB/RAND gate created by parallel work. The user then explicitly instructed that RAND should not be considered. That RAND-inclusive gate is therefore superseded and is not active project authority.

The special gate does not alter `SSDI-THEORY-FREEZE-2026-09-06-v2`. Any later desire to pursue a JET/GEB-level general theorem must reopen the earliest affected theory stage or begin a separate project.
