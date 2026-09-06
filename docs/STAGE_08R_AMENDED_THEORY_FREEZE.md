# Stage 8R — Amended Canonical Theory Freeze

Date: 2026-09-06

Repository: `ryotamatsuki/standardization-scope-direction-innovation`

Working title: **Standardization Scope and the Direction of Innovation**

Active freeze ID: `SSDI-THEORY-FREEZE-2026-09-06-v2`

Freeze anchor commit: `9be3ec13169b2a34d7c962994ffcfc259527bcb7`

Superseded freeze: `SSDI-THEORY-FREEZE-2026-09-06-v1`

Stage 7.5R authorization commit: `7c7f19094c0151f350e0b256152c34da6ba9f851`

Canonical workflow: `ryotamatsuki/research-paper-workflow` v1.1, release SHA `488e5ab06c207909296a7564eaf9066f7f94319c`.

Canonical template: `templates/STAGE_08_THEORY_FREEZE.md` at that release SHA.

## 1. Objective

Convert the repaired Stage 7.5R-approved theory into a canonical auditable specification before any downstream manuscript or reproducibility synchronization. No new theory is introduced in Stage 8R.

The v2 freeze exists because the post-Stage-10 hostile audit found three material claim-scope defects in v1: an over-quantified general-technology comparative static, an invalid generic `C^2` curvature-preservation robustness claim, and an object mislabeled as the unconstrained first best. Stage 7R repaired those defects by narrowing claims without changing the quadratic baseline game or the selective-standardization theorem. Stage 7.5R then returned `GO TO FULL PAPER` under the repaired scope.

## 2. Canonical theory specification

### Research question

How does the scope of a mandatory common technical standard affect firms' endogenous allocation of a fixed R&D capacity between common-layer and proprietary innovation, and when can that portfolio response make selective rather than complete standardization welfare-optimal?

### Core mechanism

Broader standardization makes common-layer innovation more transferable to rivals. A firm therefore internalizes a stronger competitive penalty from common-layer R&D and reallocates scarce innovation effort toward proprietary R&D. The regulator values the direct diffusion benefit but also recognizes the induced retreat from common innovation. Under sufficiently strong rivalry, the composition loss can make an interior scope optimal in the quadratic baseline.

### Players and objectives

- Benevolent regulator choosing standardization scope to maximize total surplus evaluated in the modeled differentiated-Bertrand environment.
- Two symmetric firms choosing R&D composition and then prices to maximize profit.
- Representative consumer with quasi-linear differentiated-product utility.

### Timing and information

1. Regulator chooses `b in [0,1]`.
2. Firms simultaneously choose `x_i in [0,E]`, with proprietary R&D `z_i=E-x_i`.
3. Firms simultaneously choose `p_i >= 0`.

All primitives and prior actions are common knowledge. The solution concept is subgame-perfect Nash equilibrium.

### Utility and demand

`U(q_1,q_2)=A_1 q_1+A_2 q_2-(q_1^2+q_2^2)/2-rho q_1 q_2`, with `0<rho<1`.

For both products active,
`q_i=[A_i-p_i-rho(A_j-p_j)]/(1-rho^2)`.

### Technology and costs

Baseline innovation technology:
`g(r)=r-kappa*r^2/2`, `kappa>0`.

Fixed total R&D capacity:
`x_i+z_i=E`, `E>0`.

Quality:
`A_i=a+theta[g(x_i)+b g(x_j)+g(E-x_i)]`, with `a>0`, `theta>0`.

Production marginal cost is zero.

No separate variable R&D resource cost affects policy comparisons in the baseline; if a fixed-capacity resource cost is represented it is policy-invariant and therefore a constant in the relevant comparisons.

### Contracts/transfers

There are no contracts or monetary transfers other than product-market payments. The common-layer spillover is technological usability, not a licensing transfer.

### Parameter restrictions

Define:
`y=kappa E`,
`nu=rho/(2-rho^2)`.

Main region:
`1/2<y<1`,
`0<nu<y`.

All-history price regularity:
`A_max/A_min < 2/[rho(3-rho^2)]`,
where
`A_min=a+theta E(1-y/2)` and
`A_max=a+theta E(2-3y/4)`.

This is a sufficient continuation/globality restriction, not the economic mechanism.

### Price subgame

The intended active-product differentiated-Bertrand equilibrium is
`p_i^*=[(2-rho^2)A_i-rho A_j]/(4-rho^2)`.

The hostile audit rechecked profitable foreclosure deviations and found no counterexample under the frozen regularity condition. Stage 10R must nevertheless write the omitted boundary-equilibrium exclusion explicitly in the proof appendix.

### Private R&D equilibrium

Firm `i` solves
`max_{x_i in [0,E]} (1-nu b)g(x_i)+g(E-x_i)`.

In the quadratic baseline:
`x^F(b)=(y-nu b)/[kappa(2-nu b)]`,
which is interior throughout the frozen region.

The best response is independent of the rival's allocation, so the R&D subgame has a unique symmetric equilibrium and no asymmetric R&D equilibrium in the frozen baseline region.

### Coordinated symmetric-R&D benchmark

Conditional on scope, the benchmark chooses a common symmetric allocation `x` to maximize symmetric quality/welfare while leaving the differentiated-Bertrand price subgame decentralized:
`max_{x in [0,E]} (1+b)g(x)+g(E-x)`.

In the quadratic baseline:
`x^S(b)=(y+b)/[kappa(2+b)]`.

This is explicitly a **coordinated symmetric-R&D benchmark with decentralized Bertrand pricing**, not an unconstrained first best.

## 3. Proposition register

| ID | Statement | Exact scope | Status |
| --- | --- | --- | --- |
| P1 | Private common R&D strictly falls with scope | quadratic baseline, frozen region | `PROVED` |
| P2R-a | Private common R&D is nonincreasing in scope | differentiable increasing strictly concave `g` | `PROVED` |
| P2R-b | Coordinated symmetric common R&D is nondecreasing in scope | differentiable increasing strictly concave `g` | `PROVED` |
| P2R-c | Strict opposite comparative statics | only intervals where relevant general-`g` optima are interior | `PROVED` |
| P3R | Complete scope under fixed positive symmetric common-R&D allocation | `x_1=x_2=bar{x}>0` | `PROVED` |
| P4 | Unique interior scope iff `nu>bar_nu(y)` | quadratic baseline, frozen region | `PROVED` |
| P5R | Complete scope under coordinated symmetric-R&D benchmark with Bertrand pricing | constrained benchmark only | `PROVED` |
| Old P2 strict-general statement | globally strict signs for every increasing strictly concave `g` | over-broad claim | `REJECTED` |
| Generic `C^2` policy-curvature robustness | small `C^2` perturbations preserve strict concavity/uniqueness | false | `REJECTED` |
| Unconstrained first-best theorem | planner controls all welfare-relevant choices | never solved | `REJECTED` as a manuscript claim |
| Endogenous-total-R&D policy persistence | selective scope persists with endogenous total R&D | not proved | `REJECTED` as a theorem claim |

No headline result is `NUMERICALLY SUPPORTED ONLY`.

## 4. Exact baseline proposition formulas

### P1

`dx^F/db=-nu(2-y)/[kappa(2-nu b)^2]<0`.

Thus proprietary R&D `E-x^F` strictly rises with scope in the quadratic baseline.

### P2R

For general differentiable increasing strictly concave `g`, the private objective has decreasing differences in `(x,b)`, so the unique maximizer is globally nonincreasing in `b`. The coordinated symmetric objective has increasing differences in `(x,b)`, so its unique maximizer is globally nondecreasing in `b`.

When interior, the FOCs are
`(1-nu b)g'(x^F)=g'(E-x^F)` and
`(1+b)g'(x^S)=g'(E-x^S)`,
and implicit differentiation yields strict opposite signs.

### P3R

For fixed symmetric `bar{x}>0`, symmetric quality is
`A^{BT}(b)=a+theta[(1+b)g(bar{x})+g(E-bar{x})]`,
so `dA^{BT}/db=theta g(bar{x})>0` and `b=1` is uniquely optimal. If `bar{x}=0`, scope is payoff-irrelevant.

### P4

The reduced quadratic policy objective has
`F''(b)=-nu(2-y)^2(2b nu^2+b nu+2nu+4)/(2-b nu)^4<0`
and
`F'(0)=y(4-y)/8>0`.

Define
`H(y,nu)=nu^3+2nu^2 y^2-8nu^2 y+2nu^2+nu y^2-4nu y+16nu+2y^2-8y`.

At `b=1`, `F'(1)<0` iff `H(y,nu)>0`. Moreover,
`H(y,0)=2y(y-4)<0` and
`H(y,y)=2y(y-2)^2(y+1)>0`,
with the verified monotonicity in `nu` on the frozen `1/2<y<1` region. Hence a unique threshold `bar_nu(y)` exists in `(0,y)`.

Therefore:
- `nu <= bar_nu(y)` implies unique optimum `b*=1`;
- `bar_nu(y)<nu<y` implies unique optimum `0<b*<1`.

### P5R

Within the coordinated symmetric-R&D benchmark, the envelope derivative with respect to scope is positive whenever common R&D is positive; the frozen quadratic solution is interior, hence `b=1`.

The symbol `FB` is not authorized for this object in Stage 10R manuscript text unless explicitly defined as something other than `first best`; the preferred label is the benchmark name above.

## 5. Welfare register

At a symmetric differentiated-Bertrand equilibrium:
`CS(A,rho)=A^2/[(2-rho)^2(1+rho)]`,
`PS(A,rho)=2A^2(1-rho)/[(2-rho)^2(1+rho)]`,
so
`W(A,rho)=A^2(3-2rho)/[(2-rho)^2(1+rho)]`.

Since the coefficient on `A^2` is positive, symmetric welfare rankings coincide with symmetric quality rankings inside the modeled price environment.

Along decentralized private R&D,
`A(b)=a+theta[(1+b)g(x^F(b))+g(E-x^F(b))]`.

The derivative decomposes into a positive direct diffusion term and a negative composition-response term. This decomposition is the welfare mechanism behind P4.

No welfare statement in v2 is an unconstrained social-planner result.

## 6. Verification status table

| Object | Analytic | Symbolic code | Numerical/regression | Hostile re-audit |
| --- | --- | --- | --- | --- |
| Price FOCs / closed form | yes | PASS | deviation check PASS on canonical example | PASS under frozen regularity |
| Private R&D closed form | yes | PASS | grid global check PASS | PASS |
| `dx^F/db` sign | yes | PASS | consistent | PASS |
| Coordinated symmetric R&D closed form | yes | PASS | not needed for proof | PASS as constrained benchmark |
| P4 curvature / endpoint formulas | yes | PASS | canonical interior solution PASS | PASS |
| Threshold endpoint identities | yes | PASS | regression PASS | PASS |
| General-`g` weak monotonicity | monotone-comparative-statics argument | not encoded in current baseline script | counterexample validates need for weak formulation | PASS after repair |
| Generic `C^2` curvature preservation | refuted | not applicable | explicit perturbation counterexample | FAIL / excluded |
| Unconstrained first best | not solved | not applicable | not applicable | excluded |

Current verification files include `scripts/symbolic_verify.py`, `scripts/numerical_verify.py`, and `tests/test_freeze_regressions.py`. Stage 9R must decide whether additional regression tests are needed to prevent reintroduction of v1 claim-scope errors.

## 7. Approved robustness list

Only the following may appear as robustness claims:

1. General concave technology: global weak directional allocation response; strict response conditional on interiority.
2. Incomplete transferability: effective transferability `t=lambda b` where the already-derived algebra applies.
3. Endogenous total R&D: conditional relative-return FOC only.
4. Institutional applications: interpretation/illustration only.

The exact P4 threshold and global policy uniqueness remain quadratic-baseline results.

## 8. Contribution / closest-paper statement

The paper does not claim novelty for compatibility affecting innovation, partial standardization, endogenous product design, or R&D allocation separately. Its frozen result-level contribution is that a continuous scope instrument changes the private composition of a fixed innovation portfolio because common-layer R&D increasingly benefits rivals; this creates a verified direct-diffusion versus composition-loss trade-off and a unique rivalry threshold at which the optimal policy changes from complete to selective scope in the quadratic baseline.

This contribution boundary must be preserved verbatim in substance during Stage 10R positioning.

## 9. Empirical / institutional interpretation

Permitted interpretation:
- digital protocols, APIs, common interfaces versus proprietary implementation/service innovation;
- modular manufacturing external interfaces versus internal/proprietary modules.

The parameter `b` is a scope/transferability object, not a generic compatibility index and not a disclosure/legal-sharing rate.

Predictions may be stated as baseline-model implications. General-language predictions must respect the repaired weak-monotonicity boundary outside the interior quadratic baseline.

## 10. Explicit exclusions

Stage 8R freezes the following nonclaims:

1. No unconstrained first-best result.
2. No claim that generic small `C^2` technology perturbations preserve strict concavity or uniqueness of the reduced policy problem.
3. No general selective-standardization uniqueness theorem for arbitrary concave technology.
4. No proof that the selective policy persists when total R&D is endogenous.
5. No asymmetric fixed-allocation welfare theorem.
6. No theorem that realized transfer `b g(x^F(b))` is globally increasing.
7. No broad novelty claim about standards and innovation generally.
8. No use of institutional examples as causal validation.
9. No silent restoration of v1 wording.

## 11. Historical freeze handling

The original v1 freeze is preserved in `docs/THEORY_FREEZE_v1.md` and is explicitly superseded. `docs/THEORY_FREEZE.md` now identifies v2 as the active canonical freeze.

The post-Astra change history is preserved in:
- `docs/THEORY_CHANGE_RECORD_2026-09-06_POST_ASTRA.md`;
- `docs/STAGE_07R_POST_ASTRA_REPAIR.md`;
- `docs/STAGE_075R_POST_ASTRA_FREEZE_DECISION.md`.

## 12. Downstream mandatory synchronization

### Stage 9R

Must synchronize:
- `docs/PROVENANCE.md` to workflow v1.1 / release SHA `488e5ab...`;
- README/current-freeze references;
- verification metadata and tests with v2;
- any CI/reproducibility references that still identify v1 as active.

Stage 9R must not change theory.

### Stage 10R

Must repair manuscript text and proofs so no v1 overclaim remains, including:
- Proposition 2 general-technology statement and KKT/corner treatment;
- fixed-allocation benchmark symmetry qualifier;
- replacement of `first best` with the constrained benchmark label;
- deletion of generic `C^2` curvature robustness;
- deletion of endogenous-total-R&D policy persistence claim;
- price-boundary uniqueness exposition;
- abstract, introduction, welfare, robustness, related literature, conclusion;
- any notation or cross-reference implying the rejected claims.

### Stage 11

Stage 11 is blocked until Stage 9R and Stage 10R are complete and CI passes against v2.

## 13. Theory-change control

Any post-v2 theoretical change requires an explicit theory-change record stating:
- changed primitive/assumption/result;
- reason;
- affected equations and propositions;
- affected verification;
- affected novelty/literature claims;
- earliest workflow stage to reopen.

No silent theory drift is permitted.

## 14. Kill tests

- Model differs from verified baseline equations: **PASS** — no change.
- Headline theorem only numerically supported: **PASS** — P4 remains analytic and symbolically verified.
- Closest-paper positioning unresolved: **PASS subject to frozen Stage 6 boundary** — contribution remains narrow and explicit.
- Theory changed after Stage 7.5R: **PASS** — Stage 8R only restates the authorized repair.
- Rejected first-best claim reintroduced: **PASS** — explicitly excluded.
- Invalid `C^2` robustness reintroduced: **PASS** — explicitly excluded.

## 15. Final verdict

`THEORY FROZEN — GO TO REPRODUCIBILITY SETUP`

Routing status: **GO TO STAGE 9R — Reproducibility / Provenance Synchronization**.

No Stage 11 work is authorized before Stage 9R and Stage 10R complete against `SSDI-THEORY-FREEZE-2026-09-06-v2`.
