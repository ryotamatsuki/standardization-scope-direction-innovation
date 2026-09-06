# Stage 14 — IJIO Submission QA

Date: 2026-09-06

Repository: `ryotamatsuki/standardization-scope-direction-innovation`

Starting `main`: `25a308c07277614a522164d0b52387b550c93a2e`

Stage-14 branch: `stage14-submission-qa`

Active freeze: `SSDI-THEORY-FREEZE-2026-09-06-v3`

Workflow authority: `ryotamatsuki/research-paper-workflow` v1.3, release commit `3e4e6a3f76d86058024d06f9710f942e21627386`.

Canonical Stage-14 template: `templates/STAGE_14_SUBMISSION_QA.md`.

Qualified submission-package source commit: `c5c5f132a051a40339fc3a140c07f91e0920629e`.

Qualification workflow run: `34029839013` (`success`).

Qualified artifact: `stage14-submission-package`, artifact ID `9988256374`, ZIP SHA-256 `df90da9f8cf7e8a485702399f542eef2a232d703afcfe5acf7094377e3f47c64`.

## 1. Executive verdict

`SUBMISSION QA PASS`

The frozen IJIO manuscript and its submission package pass clean-build, mathematical-verification, figure-regeneration, bibliography, anonymity, declaration, PDF-preflight, visual-layout, and package-completeness checks. No theory, theorem, equilibrium, welfare, novelty, or exposition defect requiring rollback was found.

The package is ready for Stage 15 submission freeze and authenticated Editorial Manager entry. Remaining actions are portal-state checks rather than manuscript defects.

## 2. Clean-build verification

GitHub Actions rebuilt the package from a clean Ubuntu runner at the qualified source commit.

Passed steps:

- dependency installation from `requirements.txt`;
- `make verify`;
- `make exposition`;
- `make paper`;
- separate title-page compilation;
- unresolved-reference/citation kill test;
- Stage-14 fail-closed package-QA script;
- PDF metadata/font preflight;
- submission-artifact upload.

The anonymous manuscript builds to 16 pages. The separate title page builds to one page. The policy-regime figure builds as a one-page vector PDF.

## 3. Symbolic, numerical, equilibrium, and regression verification

The qualified run reports:

- `SYMBOLIC_VERIFY: PASS`;
- `NUMERICAL_VERIFY: PASS`, canonical `b* ≈ 0.68775`;
- independent continuation audit: `PASS`, 73 histories, 0 unresolved histories, 0 failures;
- pytest: `11 passed`.

These checks reproduce the already frozen theory rather than introducing a Stage-14 result.

## 4. Figure regeneration and quantitative-output integrity

`make exposition` regenerated the only approved quantitative visual directly from the frozen threshold equation.

Representative checks:

- `bar_nu(0.7) = 0.358728592519`;
- `bar_nu(0.9) = 0.475554678351`.

The figure remains conditional on the global continuation restriction `(R)` and does not extend the policy theorem beyond the quadratic baseline. The Stage-14 package-QA script fails if that scope qualification disappears from the caption.

No quantitative table is required by the Stage-10 exposition architecture.

## 5. Artwork and font preflight

The sole separate artwork file is `figures/policy_regime_map.pdf`.

Stage 14 changed only its export encoding, not its data or appearance: Matplotlib now writes PDF/PS fonts as Type-42/TrueType-compatible embedded fonts. Preflight confirms the figure contains embedded CID TrueType fonts.

The manuscript PDF contains only embedded fonts. The separate title page contains embedded Latin Modern Type-1 fonts. No missing or unembedded font was found.

The standalone figure remains readable without reliance on color alone: the threshold is solid, the domain boundary is dashed, and the two policy regions are explicitly labeled.

## 6. Bibliography and reference audit

The fail-closed package QA reports:

- 12 citation keys used;
- 12 bibliography keys present;
- 0 unresolved citation keys;
- 0 duplicate bibliography keys.

The LaTeX log contains no unresolved citation or cross-reference warning after the final build.

## 7. IJIO format, metadata, and prior-submission reuse

The article type is fixed to `Research Paper`. This is not inferred from a generic Elsevier label: it is the exact article-type label in the author's 5 September 2026 IJIO Editorial Manager submission confirmation for manuscript `IJIO-D-26-00585`.

Author/account information was reused from the author's prior journal submissions rather than reconstructed from the user's current employment profile:

- sole/corresponding author: Ryota Matsuki;
- affiliation: `Independent Researcher`;
- ORCID and contact fields: prior-submission values;
- funding: no external funding;
- competing interests: none;
- originality/simultaneous-submission statement: manuscript original and not under consideration elsewhere;
- CRediT statement: sole-author conceptualization, methodology, formal analysis, validation, visualization, original drafting, and review/editing.

The public repository stores only the repository-safe postal form `790-0853, Matsuyama, Ehime, Japan`. The private street address is deliberately excluded from GitHub and is to be entered only in authenticated Editorial Manager if the portal makes it mandatory.

The Stage-14 package-QA tokenizer counts the abstract at 167 words. The four Highlights contain 80, 77, 71, and 78 characters respectively.

## 8. Anonymity and disclosure QA

The review manuscript remains anonymous: `paper/main.tex` contains an empty `\author{}` and no title-page author block.

Author-identifying material is isolated in the separate `submission/ijio_title_page.tex` / generated PDF and authenticated submission fields.

The manuscript includes, immediately before the references:

- Funding;
- Declaration of competing interest;
- Data availability;
- Declaration of generative AI and AI-assisted technologies in manuscript preparation.

The Appendix separately discloses the AI-assisted computational-verification workflow. This preserves the distinction between manuscript-preparation assistance and research-process assistance.

## 9. PDF visual QA

The exact qualified CI artifact was downloaded and rendered page by page at 180 dpi.

Inspection result:

- manuscript: all 16 pages inspected;
- title page: inspected;
- standalone Figure 1: inspected;
- clipped text: none;
- text/figure overlap: none;
- broken glyphs or black boxes: none;
- illegible equations: none;
- missing figure/caption: none;
- page-order anomaly: none.

Two bounded cosmetic defects found during Stage 14 were repaired before qualification:

1. default `hyperref` citation/equation rectangles were removed with `hidelinks`;
2. an internal operational note was removed from the submitted title page.

The post-repair qualified artifact is visually clean.

## 10. Submission package inventory

Qualified CI artifact contains exactly the submission-facing set:

1. `paper/main.pdf` — anonymous review manuscript;
2. `submission/ijio_title_page.pdf` — separate author title page;
3. `figures/policy_regime_map.pdf` — vector artwork;
4. `submission/ijio_highlights.txt`;
5. `submission/ijio_cover_letter.md`;
6. `submission/ijio_submission_metadata.md`;
7. `submission/ijio_declarations.md`.

Editable LaTeX sources and bibliography remain in the repository and can be uploaded if the live submission system requests source files.

## 11. Live fee / submission-system boundary

Current public IJIO/Elsevier information does not state a mandatory IJIO submission fee. Optional open-access APCs are publication-route charges, not a submission fee. The author's immediately preceding IJIO submission was completed without a recorded payment step.

Stage 14 therefore does not encode `mandatory submission fee = 0` as an immutable fact. Stage 15 must verify the authenticated Editorial Manager flow immediately before final submission and stop if a new mandatory payment condition appears.

Likewise, subject-area dropdown labels, optional/required reviewer nominations, file-role labels, and any portal-specific declarations must be taken from the live authenticated fields rather than guessed in advance.

## 12. Warnings and residual items

No manuscript blocker remains.

The following are Stage-15 operational checks only:

- authenticate to IJIO Editorial Manager;
- confirm live article type remains `Research Paper`;
- enter the private street address only if required by a protected field;
- select only actual live subject classifications;
- supply reviewer nominations only if the portal requires them and verify current affiliations/contact details at that time;
- confirm file-role assignment for anonymous manuscript, title page, figure, Highlights, and cover letter;
- re-check declarations generated by the portal;
- inspect the Editorial Manager-generated combined PDF before approval;
- verify no mandatory fee/payment screen has appeared;
- click final Submit only after those checks pass.

## 13. Stage-14 verdict and Stage-15 contract

Final verdict:

`SUBMISSION QA PASS`

Theory freeze remains `SSDI-THEORY-FREEZE-2026-09-06-v3`. No rollback is triggered.

Stage 15 must freeze the exact submission objects and authenticated Editorial Manager entries. It may repair portal/file-role/metadata defects, but it may not rewrite the theory, contribution, or substantive manuscript without rollback to the earliest affected stage.

Authorized forward route:

`Stage 14 complete -> Stage 15 submission freeze / Editorial Manager finalization`.
