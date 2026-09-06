# Stage 10R — Figure/Table Architecture Gate

Date: 2026-09-06

Repository: `ryotamatsuki/standardization-scope-direction-innovation`

Active freeze: `SSDI-THEORY-FREEZE-2026-09-06-v2`

Workflow: `ryotamatsuki/research-paper-workflow` v1.3, release commit `3e4e6a3f76d86058024d06f9710f942e21627386`.

This record implements the mandatory Stage-10 Figure/Table Architecture Gate. The governing rule is that a visual is required only when it materially reduces the reader's cost of understanding a central verified result.

## Exposition map

| Headline result | Economic object | Primary vehicle | Why this vehicle | Verified source / generator | Required in final paper? |
|---|---|---|---|---|---|
| Private R&D reallocation | `dx^F/db<0` in the quadratic baseline | Proposition 1 | Closed-form sign is compact and exact; a graph would add little | `docs/THEORY_FREEZE.md`; `scripts/symbolic_verify.py` | Yes |
| General private/coordinated directional wedge | private `x^F` globally nonincreasing; coordinated `x^S` globally nondecreasing; strict only at interior optima | Proposition 2 | The key content is a quantifier/domain distinction; a calibration plot could obscure corners | `docs/THEORY_FREEZE.md`; Appendix decreasing/increasing-differences proof | Yes |
| Fixed symmetric-allocation benchmark | `b^{FIX}=1` for fixed symmetric common R&D `>0` | Proposition 3 | One-line derivative establishes the benchmark | `docs/THEORY_FREEZE.md`; Section 3 | Yes |
| Selective-standardization threshold | regime boundary `nu=bar_nu(y)` solving `H(y,nu)=0` | **Figure 1: policy regime map** | The theorem is a two-parameter threshold/regime result; seeing the boundary materially reduces reader cost | `scripts/generate_exposition_outputs.py`; `docs/EXPOSITION_OUTPUT_MANIFEST.json` | **Yes** |
| Formal selective-standardization theorem | unique `b*=1` below threshold and unique `0<b*<1` above it in the quadratic baseline | Proposition 4 | Formal theorem is needed for exact scope and proof authority; Figure 1 is the primary intuitive vehicle | `docs/THEORY_FREEZE.md`; symbolic threshold identities | Yes |
| Welfare decomposition | direct diffusion gain plus negative endogenous portfolio term in the quadratic interior baseline | Equation plus concise prose | The decomposition has two signed terms and no non-monotone path requiring a visual | Section 4; `scripts/symbolic_verify.py` | Yes |
| Coordinated symmetric-R&D benchmark | complete scope when regulator chooses symmetric composition but Bertrand pricing remains decentralized | Proposition 5 | Compact benchmark; a table would duplicate Proposition 3/5 | `docs/THEORY_FREEZE.md`; Section 4 | Yes |
| General-technology robustness boundary | weak global monotonicity only; no generic policy-curvature theorem | Concise prose anchored to Proposition 2 | The contribution is the limit on the claim, not a quantitative sensitivity exercise | v2 freeze and Stage 7R repair record | Yes |
| Incomplete transferability | effective transferability `t=lambda b` preserves relative-return wedge | Concise prose | Reparameterization is algebraic; visual is redundant | v2 freeze; Section 5 | Yes |
| Endogenous total R&D | only conditional relative FOC `(1-nu b)g'(x)=g'(z)` | Concise prose | No policy-persistence theorem is authorized, so a quantitative extension plot would overstate evidence | v2 freeze; Section 5 | Yes |
| Canonical calibration | `bar_nu(0.7)≈0.358728593`, `b*≈0.6878` at `nu=0.5` | Numerical illustration in prose | One checkpoint helps scale the theorem without requiring a table | `scripts/numerical_verify.py`; figure generator | No separate object |

## Required quantitative output

Exactly one quantitative figure is approved:

`figures/policy_regime_map.pdf`

It plots the actual economic threshold `bar_nu(y)` defined by `H(y,bar_nu(y))=0` on the proven domain `1/2<y<1`, `0<nu<y`, together with the domain boundary `nu=y`. It labels the complete-standardization and selective-standardization regions.

Representative machine checks:

- `bar_nu(0.7)=0.3587285925190902`;
- `bar_nu(0.9)=0.4755546783510237`;
- every generated threshold lies strictly between `0` and `y`;
- the generated threshold is increasing on the plotting grid.

The figure caption states explicitly that the regime map is a quadratic-baseline theorem and does not generalize the policy result to arbitrary concave innovation technologies.

## Rejected visuals/tables

1. **Private-versus-coordinated allocation-path figure — rejected.** A single calibration would visually suggest globally strict comparative statics, whereas the v2 theorem allows flat corner segments for general `g`. Proposition 2 communicates the correct quantifiers more precisely.
2. **Welfare-decomposition figure — rejected.** The paper does not prove a general non-monotone welfare shape outside the quadratic baseline; the signed decomposition equation is sufficient.
3. **Sensitivity table — rejected.** No multi-parameter robustness theorem beyond the frozen threshold is authorized. A table would risk presenting numerical robustness as theorem-level evidence.
4. **Decorative timing/mechanism diagram — rejected.** The three-stage timing and common/proprietary mechanism are simple enough in prose and equations.

## Reproducibility contract

- Generator: `scripts/generate_exposition_outputs.py`.
- Machine-readable authority: `docs/EXPOSITION_OUTPUT_MANIFEST.json`.
- Python environment: `requirements.txt`.
- Build hooks: `make exposition`; `make paper` depends on exposition regeneration.
- Manuscript label: `fig:regime-map`.
- No hand-entered plotted values are permitted.

## Gate verdict

`FIGURE/TABLE ARCHITECTURE COMPLETE`

Every headline result has a primary exposition vehicle. The only required quantitative visual is reproducibly implemented; no quantitative table is required.
