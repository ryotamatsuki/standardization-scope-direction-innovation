# Stage 9R — Repository / Reproducibility Synchronization

Date: 2026-09-06

Repository: `ryotamatsuki/standardization-scope-direction-innovation`

Active freeze: `SSDI-THEORY-FREEZE-2026-09-06-v2`

Canonical workflow: `ryotamatsuki/research-paper-workflow` **v1.3**, release commit `3e4e6a3f76d86058024d06f9710f942e21627386`.

Canonical template: `templates/STAGE_09_REPRODUCIBILITY_SETUP.md` at the same release commit.

## 1. Starting remote state

- Starting remote `main`: `26d28b84dc3e0649c6c9f40e4fd706e23c0694ed`.
- Open pull requests at work start: none.
- Existing non-main branches observed: `stage7-5r-freeze-decision`, `stage7r-post-astra-repair`, `stage8r-amended-theory-freeze`, `stage9-reproducibility`, `stage10-paper-build`.
- Stage 9R branch: `stage9r-v13-reproducibility-sync`.
- No historical branch was reset, overwritten, or used as the work base.

The v1.3 release is backward compatible and does not alter stage numbering, theory-freeze meaning, or normal routing. Its new figure/table lifecycle is adopted from Stage 9R onward.

## 2. Repository tree after Stage 9R infrastructure sync

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
- `make numerical` — numerical/global-deviation checkpoints already in the repository;
- `make test` — pytest regression suite;
- `make verify` — symbolic + numerical + tests;
- `make exposition` — validate/regenerate the currently approved exposition-output set;
- `make paper` — LaTeX/BibTeX manuscript build;
- `make all` — complete local-equivalent gate: verification + exposition + paper.

The manuscript is modular LaTeX with bibliography in `references/references.bib`.

## 4. Verification scripts and tests

Existing verified model infrastructure is retained without theory edits:

- `scripts/symbolic_verify.py` checks the quadratic private allocation FOC, `dx^F/db`, the coordinated symmetric allocation, `F''`, endpoint derivative identities, threshold polynomial identities, and Bertrand price/profit formulas.
- `scripts/numerical_verify.py` checks the canonical interior policy example, private allocation against grid optimization, and unilateral price deviations at representative histories.
- `tests/test_freeze_regressions.py` checks threshold endpoint signs, canonical interiority, and the `rho -> nu` mapping.
- `tests/test_stage9r_metadata.py` prevents drift in active freeze/workflow metadata and verifies the Stage-9R exposition manifest.

Stage 9R does not claim that these implementation tests substitute for analytic proofs. The proposition register remains governed by `docs/THEORY_FREEZE.md`.

## 5. Environment / dependencies

CI uses Python 3.12. Python dependencies are documented in `requirements.txt`:

- `sympy>=1.13,<2`;
- `pytest>=8,<9`;
- `numpy>=2,<3`.

The CI manuscript build installs TeX Live LaTeX base/recommended/extra and BibTeX-extra packages. No external data download is required for the current baseline verification or manuscript build.

## 6. Figure / table pipeline under workflow v1.3

Workflow v1.3 requires a Figure/Table Architecture Gate in Stage 10. Stage 9R therefore does not pre-commit the paper to a decorative or unverified visual.

`docs/EXPOSITION_OUTPUT_MANIFEST.json` records exactly zero approved quantitative outputs at Stage 9R. `scripts/generate_exposition_outputs.py` validates the active freeze/workflow identifiers, the explicit empty output set, and the presence of provenance locations in `figures/` and `tables/`.

`make exposition` is the deterministic regeneration gate. At Stage 10R, every figure/table accepted by the architecture gate must be added to the manifest, generated from verified model objects or authoritative data, and incorporated into this target and CI.

## 7. CI / local-equivalent gate

The GitHub Actions workflow runs:

1. install Python dependencies;
2. `make verify`;
3. `make exposition`;
4. install TeX dependencies;
5. `make paper`.

Final Stage 9R status is to be recorded only after the branch CI completes successfully.

## 8. Provenance locations

- Active theory: `docs/THEORY_FREEZE.md`.
- Historical v1 theory: `docs/THEORY_FREEZE_v1.md`.
- Theory repair record: `docs/THEORY_CHANGE_RECORD_2026-09-06_POST_ASTRA.md`.
- Stage 7R / 7.5R / 8R decisions: corresponding files under `docs/`.
- Active workflow and remote-start metadata: `docs/PROVENANCE.md`.
- Figure/table output authority: `docs/EXPOSITION_OUTPUT_MANIFEST.json`.

The active workflow authority is v1.3 / `3e4e6a3...`; earlier v1.1/v1.2 references are historical only.

## 9. Remaining blockers / stale state

There is no reproducibility-infrastructure blocker.

However, the current manuscript text was produced before the v2 repair and remains **substantively stale** in places. A successful `make paper` at Stage 9R proves only that the source builds; it does not certify manuscript-to-freeze consistency. In particular, Stage 10R must remove the old unconstrained-`first best` language, repair general-technology quantifiers, remove refuted `C^2` policy-curvature robustness, narrow endogenous-total-R&D claims, and close the documented appendix exposition gaps.

That stale manuscript state is intentionally not repaired in Stage 9R because section synchronization belongs to Stage 10R.

## 10. Exact Stage 10R writing contract under workflow v1.3

Stage 10R must use only `SSDI-THEORY-FREEZE-2026-09-06-v2` and must re-fetch current remote state before substantial implementation cycles.

Required manuscript synchronization:

1. update abstract, introduction, welfare, robustness, related-literature contribution boundary, conclusion, proposition statements, and appendix to v2;
2. prohibit any claim of an unconstrained first best;
3. state the general concave result as global weak monotonicity, with strict signs only under interiority;
4. restrict fixed-allocation welfare claims to fixed symmetric allocation;
5. retain the exact selective-standardization uniqueness/threshold theorem only for the quadratic baseline;
6. retain endogenous-total-R&D only for the conditional relative-return FOC;
7. close the omitted price-boundary-equilibrium uniqueness exposition and add KKT/corner language where required;
8. complete the **mandatory v1.3 Figure/Table Architecture Gate before finalizing the Introduction**;
9. assign every headline result one primary exposition vehicle;
10. implement every required quantitative figure/table reproducibly, update `docs/EXPOSITION_OUTPUT_MANIFEST.json`, and make `make exposition` regenerate/check it;
11. run `make all` and CI before declaring the repaired manuscript complete.

No new theorem, extension, assumption, or broader novelty claim is authorized.

## 11. Provisional Stage 9R verdict

`REPRODUCIBILITY BASELINE READY` **conditional only on the branch CI gate succeeding**.

If CI succeeds, no further Stage 9R repair is required and the project proceeds to Stage 10R. If CI fails, the failure must be repaired at Stage 9R unless it reveals a substantive theory mismatch, in which case the affected earlier stage must be reopened.
