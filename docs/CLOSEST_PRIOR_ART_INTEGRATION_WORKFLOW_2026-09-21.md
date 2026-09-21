# Closest Prior-Art Integration Workflow

Date recorded: 2026-09-21

Repository: `ryotamatsuki/standardization-scope-direction-innovation`

Active theory freeze: `SSDI-THEORY-FREEZE-2026-09-10-v4`

## Purpose

Record the mandatory workflow created after identifying additional closest prior art on platform sharing, component commonality, product distinctiveness, and R&D spillovers.

This is a **literature/novelty recertification workflow**, not a theory redesign. The frozen model, propositions, proofs, thresholds, welfare formulas, equilibrium concept, and formal certificates must remain unchanged unless the prior-art audit identifies a genuine absorption problem that requires explicit workflow rollback.

## Newly identified prior-art set

### Closest commonality / platform-sharing literature

At minimum, inspect and position:

1. Ghosh and Morita (2006), *Platform Sharing in a Differentiated Duopoly*, JEMS.
2. Ghosh and Morita (2008), *An Economic Analysis of Platform Sharing*, JJIE.
3. Ghosh and Morita (2012), *Competitor Collaboration and Product Distinctiveness*, IJIO.
4. Desai, Kekre, Radhakrishnan, and Srinivasan (2001), *Product Differentiation and Commonality in Design*, Management Science.
5. Krishnan and Gupta (2001), *Appropriateness and Impact of Platform-Based Product Development*, Management Science.
6. Bourreau and Doğan (2010), *Component Sharing Through Licensing*.

Bourreau–Doğan is a mandatory stress test because it already allows the innovator to choose how much of a component set to share. Therefore **continuous scope / “how much to share” is not itself a valid novelty claim**.

### Supporting R&D-spillover lineage

Use as needed to delimit the appropriability mechanism rather than as closest-paper claims:

- Katz (1986), cooperative R&D / sharing.
- Kamien, Muller, and Zang (1992), R&D spillovers and research joint ventures.
- Motta (1992), R&D cooperation and product differentiation.

Do not inflate the bibliography mechanically. Supporting papers should be retained only where they sharpen the contribution boundary.

## Canonical contribution boundary to test

The working contribution is:

```
regulator-chosen standardization scope
    -> cross-product transferability
    -> common/proprietary R&D portfolio reallocation
    -> decentralized appropriability wedge
    -> complete-to-selective policy-ranking reversal
```

The project must **not** claim novelty for any of the following in isolation:

- commonality or platform sharing;
- continuous sharing/scope;
- commonality affecting product differentiation;
- compatibility affecting R&D incentives;
- scarce R&D resources being allocated across activities;
- endogenous direction of innovation;
- partial standardization being optimal.

The key surviving distinction to test is that the manuscript holds product substitutability fixed and studies a policy-induced reallocation of scarce innovative capacity, rather than a direct commonality-to-product-distinctiveness channel.

## Mandatory stage sequence

### Stage 11N — Closest Prior-Art Recertification

Status: **NEXT / NOT STARTED**

Tasks:

1. Build a structured prior-art matrix for the six closest papers above.
2. For each paper record:
   - who chooses commonality/scope;
   - whether the choice is binary or continuous;
   - what is shared;
   - whether product substitutability/distinctiveness changes directly;
   - whether total R&D is endogenous;
   - whether common-vs-proprietary R&D composition is endogenous;
   - whether a regulator chooses scope;
   - whether partial scope/commonality is optimal;
   - the mechanism producing any partial-scope result;
   - whether the current manuscript's complete-to-selective reversal is already present.
3. Re-test the current novelty verdict against this enlarged set.
4. Explicitly test Bourreau–Doğan as a continuous-sharing-scope collision.
5. Produce one of:
   - `ABSORBED — ROLLBACK REQUIRED`;
   - `PARTIALLY ABSORBED — CLAIM REWRITE / POSSIBLE ROLLBACK`;
   - `DISTINCT BUT NARROW — RECERTIFIED`.
6. No manuscript integration until the verdict is recorded.

Completion condition: a written, source-grounded novelty verdict with no unresolved closest-paper collision.

### Stage 12R — Journal Positioning Recertification

Status: **BLOCKED ON STAGE 11N**

Tasks:

1. Reassess IJIO as primary target using the Stage-11N contribution boundary.
2. Treat Ghosh–Morita (2012) being an IJIO paper as both:
   - positive audience-fit evidence; and
   - a higher novelty-scrutiny risk.
3. Reconfirm or revise the ladder:
   `IJIO -> RIO -> JICT`
   with JIE only as an optional stretch.
4. Do not change theory merely to improve journal positioning.

Completion condition: primary target and fallback ladder recertified for the surviving contribution.

### Stage 13R — Literature Integration

Status: **BLOCKED ON STAGE 12R**

Authorized manuscript changes only:

- `references/references.bib`;
- `paper/sections/01_introduction.tex`;
- a bounded clarification in `paper/sections/02_model.tex`;
- `paper/sections/06_related_literature.tex`;
- at most a bounded contribution-boundary sentence in `paper/sections/07_conclusion.tex`;
- journal-facing cover letter / metadata if needed.

Required integration architecture:

1. compatibility / endogenous product design: Boom, Ruiz;
2. platform/component commonality and product distinctiveness:
   Ghosh–Morita, Desai et al., Krishnan–Gupta, Bourreau–Doğan;
3. standards and innovation incentives: Llanes, Bond-Smith, Maruyama–Zennyo, Heywood–Wang–Ye, AGZ;
4. innovation direction / scarce research resources: Bryan–Lemus;
5. R&D allocation / spillover lineage as needed;
6. exact current contribution boundary.

Required model clarification:

> standardization scope changes transferability of common innovation but does not directly alter product substitutability; this isolates the innovation-portfolio channel from the product-distinctiveness channel in platform/commonality models.

The wording may be polished, but the economic content must remain exactly this.

Abstract: no change by default.

Theory source, theorem statements, proofs, threshold formulas, Lean files, and theorem certificates: **no change permitted** absent explicit rollback.

Completion condition: literature-integrated IJIO manuscript with no novelty overclaim and no scientific-theory delta.

### Stage 14 — Refreshed Submission QA

Status: **BLOCKED ON STAGE 13R**

Tasks:

- rerun full manuscript/reproducibility/package checks;
- verify citations and bibliography;
- verify no theorem/formal-source drift;
- check contribution wording against Stage 11N;
- inspect compiled PDF;
- reconcile current IJIO portal/Guide requirements.

Any theory-file delta must fail this gate and trigger investigation.

Completion condition: refreshed submission QA pass or portal-only conditional pass.

### Stage 15 — Submission Freeze

Status: **BLOCKED ON STAGE 14**

Tasks:

- freeze exact source/PDF/package provenance;
- close authenticated portal-specific requirements;
- record the immutable submission object;
- submit only after all mandatory Stage-14 conditions pass.

## Change-control rule

The workflow order is mandatory:

`Stage 11N -> Stage 12R -> Stage 13R -> Stage 14 -> Stage 15`

Do not jump directly from the current state to portal submission.

If Stage 11N identifies a true result-level absorption, stop the sequence and roll back to the earliest scientific stage affected. Do not solve an absorption problem by cosmetic rewriting.

## Expected final novelty statement if Stage 11N passes

The safe contribution should be centered on:

> Standardization scope changes cross-product transferability and therefore the relative private return to common-layer innovation. Firms reallocate a fixed R&D capacity toward proprietary activity as scope expands, whereas the coordinated symmetric allocation moves weakly in the opposite direction. This endogenous portfolio response can make selective standardization optimal even though complete standardization is optimal when the portfolio is fixed or symmetrically coordinated.

This statement is a working boundary, not a substitute for the Stage-11N source audit.
