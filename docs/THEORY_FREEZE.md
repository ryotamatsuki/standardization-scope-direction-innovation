# Canonical Theory Freeze

Freeze ID: `SSDI-THEORY-FREEZE-2026-09-06-v2`

Freeze date: 2026-09-06

Status: **ACTIVE CANONICAL FREEZE**

Supersedes: `SSDI-THEORY-FREEZE-2026-09-06-v1` (preserved in `docs/THEORY_FREEZE_v1.md`).

Canonical workflow authority: `ryotamatsuki/research-paper-workflow` v1.1, release SHA `488e5ab06c207909296a7564eaf9066f7f94319c`.

Stage 7.5R authorization source: commit `7c7f19094c0151f350e0b256152c34da6ba9f851`.

## 1. Research question

How does the scope of a mandatory common technical standard affect firms' endogenous allocation of a fixed R&D capacity between common-layer and proprietary innovation, and when can this endogenous portfolio response make selective rather than complete standardization welfare-optimal?

## 2. Contribution boundary

The contribution is the whole-game/result combination in which a regulator chooses continuous standardization scope before firms allocate a fixed innovation capacity across common and proprietary layers; greater transferability lowers the private relative return to common innovation because it strengthens rivals; and this endogenous portfolio response changes the policy conclusion from complete scope under fixed positive symmetric R&D to a unique interior scope when rivalry is sufficiently strong in the quadratic baseline.

No broader claim that standards affect innovation, that partial standardization can be optimal, or that innovation portfolios are endogenous is authorized as novel by itself.

## 3. Players, timing, and equilibrium concept

Players: one benevolent regulator, two symmetric firms `i in {1,2}`, and a representative consumer.

Timing:
1. Regulator chooses standardization scope `b in [0,1]`.
2. Firms simultaneously choose common-layer R&D `x_i in [0,E]`; proprietary R&D is `z_i=E-x_i`.
3. Firms simultaneously choose nonnegative prices `p_i >= 0`.

Equilibrium concept: subgame-perfect Nash equilibrium with a valid price continuation at every feasible upstream history.

## 4. Baseline technology and quality

Fixed R&D capacity: `E>0`.

Quadratic innovation technology:
`g(r)=r-kappa*r^2/2`, with `kappa>0`.

Define `y=kappa E` and impose `1/2<y<1`, so `g` is increasing and strictly concave on `[0,E]`.

Quality:
`A_i = a + theta [ g(x_i) + b g(x_j) + g(E-x_i) ]`, `j != i`, with `a>0`, `theta>0`.

The policy `b` changes transferability of the rival's common-layer innovation; it does not directly change product substitutability.

## 5. Consumer side and price competition

Utility:
`U(q_1,q_2)=A_1 q_1+A_2 q_2-(q_1^2+q_2^2)/2-rho q_1 q_2`, with `0<rho<1`.

Production marginal cost is zero.

Interior demand:
`q_i=[A_i-p_i-rho(A_j-p_j)]/(1-rho^2)`.

Define `nu=rho/(2-rho^2)` and impose `0<nu<y`.

All-history regularity condition:
`A_max/A_min < 2/[rho(3-rho^2)]`, where
`A_min=a+theta E(1-y/2)` and
`A_max=a+theta E(2-3y/4)`.

This condition is frozen as a sufficient global-continuation restriction ensuring the intended active-product differentiated-Bertrand equilibrium over all feasible upstream histories.

## 6. Baseline equilibrium objects

Price equilibrium:
`p_i^*=[(2-rho^2)A_i-rho A_j]/(4-rho^2)`.

Private R&D problem:
`max_{x_i in [0,E]} (1-nu b)g(x_i)+g(E-x_i)`.

Under the baseline parameter restrictions the unique private optimum is interior:
`x^F(b)=(y-nu b)/[kappa(2-nu b)]`.

Quadratic coordinated symmetric-R&D benchmark:
`max_{x in [0,E]} (1+b)g(x)+g(E-x)`, yielding
`x^S(b)=(y+b)/[kappa(2+b)]`.

This coordinated benchmark retains decentralized Bertrand pricing and is **not** an unconstrained first best.

## 7. Proposition register

### P1 — Private R&D reallocation
Status: `PROVED`.

In the quadratic baseline,
`dx^F/db=-nu(2-y)/[kappa(2-nu b)^2] < 0`.
Hence broader scope shifts the fixed private R&D portfolio from common-layer toward proprietary innovation.

### P2R — Directional private/coordinated wedge under general concave technology
Status: `PROVED` after repair.

For differentiable increasing strictly concave `g` on `[0,E]`, the private maximizer is globally nonincreasing in `b`, while the coordinated symmetric maximizer is globally nondecreasing in `b`. Strict opposite signs hold only on intervals where the relevant optima are interior.

No unconditional globally strict comparative static is frozen.

### P3R — Fixed symmetric allocation benchmark
Status: `PROVED`.

For a fixed symmetric common-R&D allocation `x_1=x_2=bar{x}>0`, welfare is strictly increasing in scope, so `b=1` is optimal. If `bar{x}=0`, the regulator is indifferent over scope.

No asymmetric fixed-allocation welfare benchmark is frozen.

### P4 — Selective standardization
Status: `PROVED` and headline theorem.

Let
`H(y,nu)=nu^3+2nu^2 y^2-8nu^2 y+2nu^2+nu y^2-4nu y+16nu+2y^2-8y`.

For each `y in (1/2,1)` there is a unique `bar_nu(y) in (0,y)` satisfying `H(y,bar_nu(y))=0`. In the frozen region:
- if `nu <= bar_nu(y)`, the unique optimum is `b*=1`;
- if `bar_nu(y) < nu < y`, the unique optimum satisfies `0<b*<1`.

Equivalently, within the frozen region, a unique interior scope occurs iff `nu>bar_nu(y)`.

The global uniqueness result is frozen only for the quadratic baseline.

### P5R — Coordinated symmetric-R&D benchmark
Status: `PROVED` as a constrained benchmark.

When the regulator directly chooses `b` and the symmetric R&D composition `x` while decentralized Bertrand pricing remains in place, complete standardization `b=1` is optimal.

This result must not be labeled `first best`.

## 8. Welfare register

At a symmetric Bertrand equilibrium with common quality `A`,
`W(A,rho)=A^2(3-2rho)/[(2-rho)^2(1+rho)]`.

Along the decentralized R&D equilibrium,
`A(b)=a+theta[(1+b)g(x^F(b))+g(E-x^F(b))]`.

The quality/welfare derivative decomposes into:
- a positive direct diffusion term from broader transferability; and
- a negative endogenous innovation-composition term caused by `dx^F/db<0`.

The selective-standardization theorem is therefore a policy result generated by an endogenous innovation-composition distortion inside the differentiated-Bertrand environment.

Fixed R&D-capacity resource cost, if represented, is policy-invariant in the baseline and may be omitted from policy comparisons only as a constant.

## 9. Approved robustness scope

Only the following robustness statements are authorized:

1. General increasing strictly concave `g`: weak directional monotonicity globally, strict opposite signs conditional on interior optima.
2. Incomplete transferability: effective transferability may be written as `t=lambda b` to the extent already algebraically established.
3. Endogenous total R&D: only the conditional relative-return FOC `(1-nu b)g'(x)=g'(z)` may be stated; no policy persistence theorem is authorized.
4. Institutional applications may illustrate the common/proprietary-layer interpretation but do not establish causal validation.

## 10. Explicit exclusions / nonclaims

The following are explicitly outside the v2 freeze:

- no unconstrained first-best result;
- no generic `C^2` perturbation result preserving policy-objective strict concavity or uniqueness;
- no general policy-uniqueness theorem for arbitrary concave innovation technologies;
- no proof that selective standardization persists under endogenous total R&D;
- no asymmetric fixed-allocation welfare theorem;
- no novelty claim broader than the scope → endogenous R&D portfolio → selective-policy threshold architecture;
- no claim that realized transferred innovation `b g(x^F(b))` is globally increasing in scope;
- no use of numerical verification as a substitute for analytic proof.

## 11. Verification status

Analytic/symbolic verification covers the private allocation formula and derivative, coordinated symmetric allocation formula and derivative, reduced policy curvature, endpoint derivative, threshold polynomial identities, price equilibrium, and profit formula.

Independent numerical verification checks the canonical selective-standardization example, private R&D global maximization on a grid, and unilateral price deviations. Regression tests check threshold endpoint signs, interior private allocation in the canonical example, and the `rho`-to-`nu` mapping.

The post-Stage-10 hostile audit independently re-derived the quadratic baseline and found the selective-standardization theorem intact while identifying the claim-scope defects repaired in Stage 7R.

## 12. Closest-literature distinction

Existing literature already covers compatibility/product-design responses, standards and innovation incentives, partial standardization, and allocation of innovative effort. The frozen distinction is the strategic architecture and result-level reversal: continuous scope changes the private composition of a fixed R&D portfolio between common and proprietary innovation, and that portfolio feedback can overturn the complete-standardization conclusion of the fixed symmetric-allocation benchmark and generate a unique rivalry threshold for selective scope.

## 13. Institutional and empirical interpretation

`b` is the mandatory scope of a common technical layer/interface, not a generic compatibility index and not a legal disclosure share.

Permitted application families include digital protocols/APIs/interfaces and modular manufacturing interfaces, provided they are presented as interpretations.

Baseline empirical implications may include a lower private share of common-layer innovation after scope expansion and a stronger composition response under greater downstream substitutability. Outside the quadratic/interior baseline, general-language claims must respect weak rather than everywhere-strict monotonicity.

## 14. Change control

Any theoretical change after this freeze must record:
1. what changed;
2. why it changed;
3. affected equations/propositions;
4. affected verification artifacts;
5. affected literature/contribution claims;
6. earliest workflow stage that must be reopened.

No silent theory drift is permitted.

## 15. Downstream contract

Stage 9R must synchronize repository provenance, verification metadata, regression coverage, and all references to the active freeze with v2.

Stage 10R must synchronize the manuscript to v2, including Proposition 2, the fixed-allocation benchmark, welfare benchmark nomenclature, robustness claims, appendix KKT/boundary language, abstract, introduction, related literature, and conclusion.

Stage 11 is prohibited until Stage 9R and Stage 10R are completed against this v2 freeze.

## Final verdict

`THEORY FROZEN — GO TO REPRODUCIBILITY SETUP`
