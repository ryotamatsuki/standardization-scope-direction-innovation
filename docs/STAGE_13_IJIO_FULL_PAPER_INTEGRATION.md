# Stage 13 — IJIO Full-Paper Integration

Date: 2026-09-06

Repository: `ryotamatsuki/standardization-scope-direction-innovation`

Target journal: **International Journal of Industrial Organization (IJIO)**

Active theory freeze: `SSDI-THEORY-FREEZE-2026-09-06-v3`

Workflow authority: `ryotamatsuki/research-paper-workflow` v1.3, `templates/STAGE_13_FULL_PAPER_INTEGRATION.md`.

Stage-12 input verdict: `PRIMARY JOURNAL SELECTED — GO TO INTEGRATION`.

## 1. Executive integration verdict

`INTEGRATED MANUSCRIPT READY FOR SUBMISSION QA`

The paper has been integrated for IJIO without reopening the frozen theory. The Stage-13 changes are limited to journal-specific exposition, claim-scope clarification, literature emphasis, figure-caption self-containment, disclosure compliance, and submission-package preparation.

No fatal or major substantive inconsistency was discovered during integration.

## 2. Section-role audit

### Abstract

Retained without substantive change. It already states the policy question, private portfolio response, general order result, fixed/coordinated benchmark, quadratic selective-standardization result, and second-best interpretation without claiming a general policy theorem.

Current abstract length: 160 words.

### Introduction

Reordered the contribution boundary around the closest IJIO-relevant comparison.

- `Llanes (2024, IJIO)` is now identified first as the closest technical-standards comparison.
- Compatibility/product-design papers remain separated from the common/proprietary R&D allocation margin.
- `Acemoglu, Gancia, and Zilibotti (2012)` is explicitly credited with a broader constrained-standardization result.
- `Bryan and Lemus (2017)` is explicitly credited with scarce-resource innovation-direction and underappropriation results.
- The manuscript continues to claim only the result-level architecture: regulator-selected scope -> transferability -> common/proprietary portfolio reallocation -> complete-to-selective policy reversal -> exact rivalry threshold in the quadratic baseline.
- `Bergeaud, Schmidt, and Zago (2026, JFE)` is added only as contemporary institutional evidence that standardization, competition, and R&D responses interact; it is not presented as validation of the model's portfolio mechanism.

### Model / equilibrium / welfare / robustness

No theory changes. Parameter restrictions, proposition statements, welfare accounting, and robustness boundaries remain governed by the v3 freeze.

The Stage-11 copy clarification was implemented: the Appendix now calls the downstream object the unique global **pure-strategy** Nash equilibrium, matching what the proof establishes rather than implying a result about all mixed equilibria.

### Conclusion

No change required. It remains aligned with the abstract and does not add a new policy instrument or first-best claim.

## 3. Contribution-claim audit

The manuscript consistently does **not** claim novelty for:

- standards affecting innovation;
- compatibility affecting R&D;
- endogenous direction of innovation;
- underappropriation reallocating scarce research resources;
- endogenous product design responses to compatibility;
- partial/selective standardization being generically optimal.

The surviving contribution remains:

`continuous regulator-chosen standard scope -> cross-product transferability -> fixed-capacity common/proprietary R&D portfolio response -> policy-ranking reversal -> exact rivalry threshold in the quadratic differentiated-Bertrand baseline`.

Verdict: contribution claims are internally consistent and appropriately narrow for the Stage-12 IJIO positioning.

## 4. Related-literature structure audit

The four-literature organization is retained:

1. compatibility and endogenous product design;
2. standards and innovation incentives;
3. direction of innovation;
4. allocation of innovative effort.

The second block now leads with Llanes (2024) because it is the closest technical-standards theory comparison and was published in IJIO. The 2026 Bergeaud-Schmidt-Zago evidence is included as an empirical/institutional bridge, not a theorem comparator.

No closest paper is described as identical, and no citation is used to inflate novelty.

## 5. Results / discussion separation audit

The results sections continue to establish the private allocation response, coordinated allocation ordering, fixed-allocation benchmark, selective-standardization threshold, and welfare decomposition.

Interpretive statements remain bounded:

- scope is a reduced-form transferability object;
- selective standardization is instrument-constrained;
- complete standardization is not declared inferior under a richer policy set;
- empirical examples motivate rather than validate the mechanism.

Verdict: PASS.

## 6. Abstract / introduction / conclusion alignment

All three locations now communicate the same result hierarchy:

1. broader scope lowers private common-layer R&D in the quadratic baseline;
2. the general-technology result is an order comparison, not a derivative theorem;
3. fixed positive symmetric R&D and coordinated symmetric composition imply complete scope;
4. decentralized endogenous composition can imply an interior scope under sufficiently strong rivalry in the quadratic baseline;
5. the policy interpretation is second best and instrument constrained.

No killed v2 general-derivative claim was reintroduced.

## 7. Figure/Table architecture and IJIO-specific integration

The Stage-10 architecture remains binding: one quantitative figure and no quantitative table.

Figure 1 remains the policy-regime map generated from the verified threshold equation. The caption now states explicitly that all plotted policy claims are conditional on the global continuation restriction `(R)` and that the theorem is quadratic-baseline-specific.

Current IJIO articles visibly use Highlights and concise figure/result presentation. A separate four-bullet Highlights file has therefore been added at `submission/ijio_highlights.txt`. Stage-13 character counts are 80, 77, 71, and 78 characters respectively.

No graphical abstract is added and no generative-AI image is used.

## 8. Notation / citation / cross-reference audit

Changes introduced at Stage 13:

- new citation key `BergeaudSchmidtZago2026`;
- no new mathematical notation;
- no proposition or equation renumbering by hand;
- Figure 1 retains its existing label and generator;
- `pure-strategy` qualification added to the Appendix price-equilibrium claim;
- declarations inserted immediately before the references.

The new Bergeaud-Schmidt-Zago reference is:

Antonin Bergeaud, Julia Schmidt, and Riccardo Zago (2026), “Patents that Match your Standards: Firm-level Evidence on Competition, Innovation and Growth,” *Journal of Financial Economics* 180, 104281, DOI `10.1016/j.jfineco.2026.104281`.

## 9. IJIO live requirement / fee / format check

### Journal scope

Official Elsevier material accessed on 2026-09-06 describes IJIO as the official journal of EARIE and states that it aims at full coverage of theoretical and empirical industrial organization, including strategic behavior, market structure, technological change, regulation, antitrust, and productivity, and explicitly encourages theoretical work.

Controlling journal page:
`https://shop.elsevier.com/journals/international-journal-of-industrial-organization/0167-7187`

### Submission system

A current 2025-2026 IJIO special-issue instruction page confirms that the journal uses Editorial Manager at:
`https://www.editorialmanager.com/ijio/`

The regular paper must use the normal regular-article option rather than a special-issue article type.

### Current Guide for Authors

Controlling Guide URL:
`https://www.sciencedirect.com/journal/international-journal-of-industrial-organization/publish/guide-for-authors`

The full Guide text was not machine-accessible during this Stage-13 run. Stage 13 therefore does not invent an IJIO-specific page limit, anonymization rule, or exact upload-file requirement that could not be verified directly.

Current IJIO production pages do confirm that contemporary articles may display Highlights, abstracts, keywords/JEL classifications, data statements, and generative-AI declarations. The manuscript/package has been prepared to supply those items without changing theory.

### Generative AI policy

Elsevier's journal AI policy, updated June 2026, requires substantive generative-AI use in manuscript preparation to be disclosed in a separate declaration immediately before the references, including the tool, purpose, and author oversight. It further states that AI-assisted code used as part of research should be described in the research methods/process with reproducible detail.

Official policy:
`https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals`

Implemented:

- `paper/sections/08_declarations.tex`: manuscript-preparation declaration;
- Appendix: AI-assisted verification-workflow disclosure, including OpenAI ChatGPT and the documented model configurations used in the project workflow;
- explicit author responsibility for sources, derivations, code, outputs, and final text.

### Submission and publication fees

IJIO is currently presented by Elsevier as supporting open access; the journal therefore has an optional OA publication route in addition to the subscription route.

Elsevier's official pricing page provides a current APC spreadsheet and states that APC prices are subject to change and should be checked on the journal homepage. The official pricing page was last updated July 26, 2026:
`https://www.elsevier.com/about/policies-and-standards/pricing/journals`

The exact IJIO APC was not imported into the repository because the official spreadsheet could not be machine-read in this run and third-party copied fee tables are not treated as authoritative.

No mandatory IJIO **submission fee** was located in accessible official IJIO/Elsevier public material. This absence is not encoded as `fee = 0` or treated as conclusive proof. Stage 14 must inspect the authenticated Editorial Manager payment/fee screens before submission. If open access is later selected, the exact current APC and any institutional/funder discount must be checked again at that time.

## 10. Submission-package changes made

Added:

- `submission/ijio_highlights.txt`;
- `submission/ijio_cover_letter.md`;
- `submission/ijio_submission_metadata.md`;
- `paper/sections/08_declarations.tex`;
- this Stage-13 integration record.

Modified:

- `paper/sections/01_introduction.tex`;
- `paper/sections/03_equilibrium.tex`;
- `paper/sections/06_related_literature.tex`;
- `paper/sections/appendix.tex`;
- `paper/main.tex`;
- `references/references.bib`.

## 11. Remaining blockers

No manuscript-theory blocker remains.

The following are deliberately deferred to Stage 14 because they require authenticated account state, author declarations, or a live journal screen rather than manuscript inference:

1. exact author names/order, corresponding-author status, affiliation, email, ORCID, and address;
2. competing-interest and funding declarations;
3. originality / no-simultaneous-submission confirmation;
4. exact regular-article label in Editorial Manager;
5. live title-page/anonymization requirement;
6. exact required upload file types and any live field limits;
7. live mandatory submission-fee confirmation;
8. exact optional OA APC only if the OA route is chosen.

These are operational Stage-14 items, not reasons to reopen the theory or Stage 13.

## 12. Verdict and Stage 14 contract

`INTEGRATED MANUSCRIPT READY FOR SUBMISSION QA`

Stage 14 must:

- run the full repository verification/build gate on the integrated branch;
- inspect the generated PDF for declaration placement, Figure 1 caption, references, and pagination;
- reconcile the live IJIO Guide for Authors with the package;
- use authenticated Editorial Manager to verify article type, anonymization/title-page requirements, required metadata fields, and any mandatory submission fee;
- obtain the author's current-paper declarations for authorship, funding, competing interests, and simultaneous submission;
- prepare the final upload set without changing the frozen theory or widening novelty claims.
