# Canonical Theory Freeze

Freeze ID: `SSDI-THEORY-FREEZE-2026-09-10-v4`

Freeze date: 2026-09-10

Status: **ACTIVE CANONICAL FREEZE — CERTIFICATION-ONLY REFREEZE**

Scientific baseline inherited from: `SSDI-THEORY-FREEZE-2026-09-06-v3`, preserved in `docs/THEORY_FREEZE_v3.md`.

Scientific baseline commit entering this refreeze: `main@3648ac2d4917986f1f09873a30bbd5948fceb8b3`.

Latest-workflow authority: `ryotamatsuki/research-paper-workflow@f48984013898696f010f0437a8cfed6b5b54bdc2`.

Historical production workflow: `v1.3@3e4e6a3f76d86058024d06f9710f942e21627386`.

Stage-4A state: `GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS`.

Stage-7.5A state: `GO — GENERALITY / QUANTIFIER CERTIFICATION PASS`.

Formal-verification state: `FORMAL VERIFICATION PASS`.

This v4 freeze is certification-only. It does not alter any primitive, payoff, timing assumption, equilibrium condition, proposition conclusion, parameter restriction, welfare comparison, threshold, numerical result, or contribution claim inherited from v3. It records the current theory under the latest workflow after the retroactive Stage 4A and Stage 7.5A/Formal Verification gates were closed. The only manuscript fidelity changes preceding this freeze were narrower `pure-strategy` uniqueness wording and bounded-domain alignment of the Lean P2R statement; neither changes the scientific result set.

## 1. Research question

How does the scope of a mandatory common technical standard affect firms' endogenous allocation of a fixed R&D capacity between common-layer and proprietary innovation, and when can this endogenous portfolio response make selective rather than complete standardization welfare-optimal?

## 2. Contribution statement

The contribution is the whole-game/result combination in which a regulator chooses continuous standardization scope before firms allocate a fixed innovation capacity across common and proprietary layers; greater transferability lowers the private relative return to common innovation because it strengthens rivals; and this endogenous portfolio response changes the policy conclusion from complete scope under fixed positive symmetric R&D to a unique interior scope when rivalry is sufficiently strong in the quadratic baseline.

No broader claim that standards affect innovation, that partial standardization can be optimal, or that innovation portfolios are endogenous is authorized as novel by itself.

## 3. Players, objectives, timing, and information

Players: one benevolent regulator, two symmetric firms `i in {1,2}`, and a representative consumer.

Timing:

1. The regulator chooses mandatory standardization scope `b in [0,1]`.
2. Firms simultaneously allocate fixed R&D capacity by choosing `x_i in [0,E]`; proprietary R&D is `z_i=E-x_i`.
3. Firms simultaneously choose nonnegative prices `p_i>=0`.
4. The consumer chooses quantities subject to `q_i>=0`.

The model is complete-information and solved by backward induction.

The regulator maximizes total surplus on the equilibrium path. Each firm maximizes operating profit; fixed total R&D capacity is policy-invariant in the baseline.

## 4. Complete strategy and choice sets

- Policy: `b in [0,1]`.
- Firm common-layer R&D: `x_i in [0,E]`.
- Firm proprietary R&D: `z_i=E-x_i in [0,E]`.
- Prices: `p_i in [0,infinity)`.
- Consumer quantities: `(q_1,q_2) in R_+^2`.

No price floor, no loss-exclusion refinement, no tie-breaking equilibrium selection, and no restriction to on-path R&D histories is part of the game.

## 5. Utility, demand, technology, costs, transfers

Consumer utility is

`U(q_1,q_2)=A_1 q_1+A_2 q_2-(q_1^2+q_2^2)/2-rho q_1 q_2`,

with `0<rho<1`.

Production marginal cost is zero.

When both products are active, demand is

`q_i=[A_i-p_i-rho(A_j-p_j)]/(1-rho^2)`.

Fixed R&D capacity satisfies `E>0`. The quadratic baseline innovation technology is

`g(r)=r-kappa*r^2/2`, `kappa>0`.

Quality is

`A_i=a+theta[g(x_i)+b g(x_j)+g(E-x_i)]`, `j!=i`,

with `a>0`, `theta>0`.

The term `b g(x_j)` is technological transferability/usability inside the common layer. There are no monetary transfers, licenses, subsidies, disclosure payments, or contracting instruments in the baseline game.

## 6. Parameter and function-class restriction register

Baseline quadratic restrictions:

- `E>0`, `kappa>0`, `a>0`, `theta>0`;
- `y=kappa E`;
- `1/2<y<1`;
- `0<rho<1`;
- `nu=rho/(2-rho^2)`;
- `0<nu<y`;
- `b in [0,1]`.

All-history price-continuation restriction:

`A_max/A_min < 2/[rho(3-rho^2)]`, tagged `(R)`, where

`A_min=a+theta E(1-y/2)` and
`A_max=a+theta E(2-3y/4)`.

General-technology P2R function class:

`g` is differentiable, increasing, and strictly concave on `[0,E]`. The general theorem is an order-comparative-static theorem; it does not assume or infer a pointwise derivative of the optimizer with respect to `b`.

## 7. Equilibrium concept and continuation specification

The equilibrium concept is subgame-perfect Nash equilibrium built on the certified global **pure-strategy** downstream price continuation under `(R)` at every feasible upstream history.

The paper does not claim uniqueness among mixed-strategy price equilibria. All global price-uniqueness language is restricted to pure strategies.

Condition `(R)` is a primitive sufficient parameter restriction ensuring the intended continuation. It is not an ex post equilibrium-selection rule.

## 8. Baseline equilibrium objects

Price continuation:

`p_i^*=[(2-rho^2)A_i-rho A_j]/(4-rho^2)`.

Private R&D problem:

`max_{x_i in [0,E]} (1-nu b)g(x_i)+g(E-x_i)`.

Quadratic private allocation:

`x^F(b)=(y-nu b)/[kappa(2-nu b)]`.

Coordinated symmetric-R&D problem:

`max_{x in [0,E]} (1+b)g(x)+g(E-x)`.

Quadratic coordinated allocation:

`x^S(b)=(y+b)/[kappa(2+b)]`.

## 9. Proposition register with proof maturity and formal coverage

### E0 — Global downstream price continuation

Analytic maturity: `PROVED`.

Exact scope: for every feasible `b in [0,1]` and `(x_1,x_2) in [0,E]^2`, under `(R)` the downstream price game has the certified unique global pure-strategy equilibrium with both products active.

Formal coverage: `PROOF-CRITICAL CORE`.

Lean certifies the active FOC identity, positive denominator/candidate-price implications, foreclosure-threshold algebra and sign, and positive re-entry margin. The complete consumer KKT correspondence and full pure-equilibrium exhaustion remain analytic/Stage-4A objects. Mixed-strategy uniqueness is not certified or claimed.

### P1 — Private R&D reallocation

Analytic maturity: `PROVED`.

For every baseline quadratic parameter vector and `b in [0,1]`,

`dx^F/db=-nu(2-y)/[kappa(2-nu b)^2] < 0`.

Broader scope reallocates the fixed private R&D budget from common-layer to proprietary innovation.

Formal coverage: `PROOF-CRITICAL CORE`, including the exact closed-form order/sign result.

### P2R — Directional private/coordinated wedge under general concave technology

Analytic maturity: `PROVED`.

For every differentiable increasing strictly concave `g` on `[0,E]` and every `b_2>b_1`:

- `x^F(b_2)<=x^F(b_1)`;
- `x^S(b_2)>=x^S(b_1)`.

If both compared private optima are interior, the private inequality is strict. If both compared coordinated optima are interior, the coordinated inequality is strict.

No pointwise sign for `dx^F/db` or `dx^S/db` is claimed for arbitrary general `g`.

Formal coverage: `PROOF-CRITICAL CORE`. Lean formalizes the decreasing/increasing-differences revealed-preference order logic on the actual bounded choice set `[0,E]` and the contradiction core for equal interior optima conditional on the relevant FOCs. The analytic regularity-to-unique-argmax and FOC derivations remain outside Lean.

### P3R — Fixed symmetric-allocation benchmark

Analytic maturity: `PROVED`.

For each fixed symmetric common allocation `x_1=x_2=bar{x}>0`, welfare is strictly increasing in `b`, so `b^FIX=1`. If `bar{x}=0`, the regulator is indifferent.

No asymmetric fixed-allocation theorem is frozen.

Formal coverage: `PARTIAL / SUPPORTING IDENTITIES`; the policy monotonicity argument remains analytic.

### P4 — Selective standardization

Analytic maturity: `PROVED` and headline theorem.

Let

`H(y,nu)=nu^3+2nu^2 y^2-8nu^2 y+2nu^2+nu y^2-4nu y+16nu+2y^2-8y`.

For every `y in (1/2,1)` there exists a unique `bar_nu(y) in (0,y)` with `H(y,bar_nu(y))=0`.

Within the frozen quadratic domain:

- `nu<=bar_nu(y) => b*=1`;
- `bar_nu(y)<nu<y =>` a unique `b*` satisfies `0<b*<1`.

Formal coverage: `PROOF-CRITICAL CORE`. Lean certifies threshold existence/uniqueness/sign partition, positivity of `F'(0)` expression, negativity of the displayed `F''` expression, the `F'(1)` threshold-sign equivalence, and exact equality between the substituted quadratic policy objective and its rational closed form. Formal differentiation from the objective to all derivative formulas and the complete argmax theorem remain analytic.

### P5R — Coordinated symmetric-R&D benchmark

Analytic maturity: `PROVED` as a constrained benchmark.

When the regulator chooses `b` and the symmetric R&D composition while differentiated Bertrand pricing remains decentralized, `b^COORD=1`.

This is not an unconstrained first best.

Formal coverage: `SUPPORTING WELFARE CORE`; the complete coordinated argmax proof remains analytic.

No headline result is `NUMERICALLY SUPPORTED ONLY`, `CONJECTURE`, or unresolved.

## 10. Welfare and benchmark register

At the symmetric Bertrand equilibrium with common quality `A`,

`CS(A,rho)=A^2/[(2-rho)^2(1+rho)]`,

`PS(A,rho)=2A^2(1-rho)/[(2-rho)^2(1+rho)]`,

`W(A,rho)=A^2(3-2rho)/[(2-rho)^2(1+rho)]`.

Hence symmetric welfare ranks `A` monotonically.

Along the decentralized quadratic R&D equilibrium,

`A(b)=a+theta[(1+b)g(x^F(b))+g(E-x^F(b))]`.

The policy derivative separates a positive direct diffusion term from a negative endogenous portfolio-response term for positive scope in the quadratic interior baseline.

Benchmark definitions:

- `FIX`: R&D composition fixed symmetrically; prices decentralized.
- `COORD`: regulator chooses scope and symmetric R&D composition; prices decentralized.
- `EFF`: fixed-quality quantity-control benchmark only.
- unrestricted first best: not solved and not claimed.

At fixed symmetric quality,

`W^EFF=A^2/(1+rho)` and

`W^EFF-W=A^2(1-rho)^2/[(2-rho)^2(1+rho)]>0`.

Lean formalizes the exact CS/PS/W identities and fixed-quality quantity-control gap.

## 11. Approved robustness scope

Only the following robustness statements are authorized:

1. General differentiable increasing strictly concave `g`: private common-layer R&D is globally nonincreasing in scope and coordinated symmetric common-layer R&D globally nondecreasing; strict order only when both compared optima are interior.
2. Incomplete transferability `t=lambda b`: approved as a reparameterization of the relative-return wedge only.
3. Endogenous total R&D: only the conditional relative interior FOC `(1-nu b)g'(x)=g'(z)` under a common marginal total-capacity cost is authorized. No global total-R&D or optimal-scope result follows.
4. Institutional applications are interpretations, not causal validation.

## 12. Empirical and institutional interpretation

`b` is the mandatory scope of a common technological layer/interface. It is not a generic compatibility index and not a legal disclosure share.

Permitted application families include digital protocols/APIs/interfaces and modular industrial interfaces. Empirical implications concern innovation composition rather than total R&D expenditure.

Outside the quadratic/interior baseline, wording must use the certified order statements rather than pointwise derivative language.

## 13. Closest-paper distinction

The closest-literature boundary remains narrow and result-level. Existing work already covers compatibility and endogenous product design, standards and innovation incentives, partial/constrained standardization, and scarce-research-resource allocation. Bryan and Lemus (2017) are close on innovation direction with scarce research resources and underappropriation, while Acemoglu, Gancia, and Zilibotti (2012) already show constrained optimal standardization in a dynamic growth setting. The frozen distinction is the specific architecture:

`regulator-chosen continuous scope -> cross-product transferability -> endogenous common/proprietary fixed-capacity portfolio response -> differentiated Bertrand rivalry -> exact complete-to-selective policy reversal and rivalry threshold in the quadratic baseline`.

No generic second-best-standardization claim is frozen as novel.

## 14. Explicit exclusions and prohibited stronger claims

The following are not authorized:

- unrestricted first-best claims;
- mixed-strategy price-equilibrium uniqueness;
- a generic policy-uniqueness theorem for arbitrary concave `g`;
- pointwise `dx/db` signs for arbitrary differentiable concave `g`;
- generic small-`C^2` perturbation persistence of P4;
- selective-standardization persistence with endogenous total R&D;
- asymmetric fixed-allocation welfare theorem;
- global monotonicity of realized transferred innovation `b g(x^F(b))`;
- causal validation from the cited empirical examples;
- a claim that Lean certifies the complete economic game or full SPNE correspondence;
- use of numerical verification as a substitute for analytic proof.

## 15. Stage-4A theorem-certificate register

Canonical Stage-4A record:

`docs/STAGE_04A_RETROACTIVE_MATH_ADVERSARIAL_CERTIFICATION.md`.

Canonical theorem-certificate bundle:

`theorem_certificates/STAGE4A_RETROACTIVE_CERTIFICATES.md`.

Verdict:

`GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS`.

Certified Stage-4A scope includes E0 price continuation, P1, P2R, P3R, P4, P5R/W1, with D1 candidate-deviation, D2 multiplicity/alternative-equilibrium, and D3 indifference/zero-payoff audits separated where relevant.

Permanent independent evaluator:

`scripts/stage4a_independent_equilibrium_set_audit.py`.

Recorded audit summary:

`parameter_sets=126; histories=2142; player_histories=4284; unresolved=0; profitable_price_deviations=0; alternative_pure_price_equilibria=0; rd_corner_failures=0; policy_regime_failures=0; welfare_failures=0`.

## 16. Stage-7.5A claim-scope / quantifier register

Canonical record:

`docs/STAGE_075A_RETROACTIVE_GENERALITY_QUANTIFIER_FORMAL_VERIFICATION.md`.

Verdict:

`GO — GENERALITY / QUANTIFIER CERTIFICATION PASS`.

The maximum defensible wording is exactly the proposition and exclusion scope stated in Sections 9–14 of this freeze. In particular, P2R is a global order theorem with strictness only for two compared interior optima; P4 is quadratic-specific; price uniqueness is pure-strategy only; and P5R is constrained rather than first best.

## 17. Formal-verification applicability, certificate, and toolchain

Applicability: `FORMALIZATION APPLICABLE`.

Final state: `FORMAL VERIFICATION PASS`.

Canonical certificate:

`theorem_certificates/STAGE075A_FORMAL_VERIFICATION_CERTIFICATE.md`.

Certified formal-source commit: `5078719c57495c510405aa0cd33e621f3a7a2ab0`.

Formal source paths:

- `formal/SSDI/Core.lean`
- `formal/SSDI/Generality.lean`
- `formal/SSDI/Continuation.lean`
- `formal/SSDI/Threshold.lean`
- `formal/SSDI/PolicySigns.lean`
- `formal/SSDI/PolicyObjective.lean`
- `formal/SSDI/WelfareIdentities.lean`
- `formal/SSDI/Assurance.lean`
- umbrella `formal/SSDI.lean`

Toolchain/build provenance:

- Lean 4 `v4.32.1`;
- Lean executable commit `f054605aea4b840552cca2e725580bffd1e1b704`;
- mathlib exact commit `520045ab14e26149ee970e2e617ca04b09bde5d6`;
- build sequence: `lake update`; `lake exe cache get`; `lake build`;
- clean Lean CI run `34469130983`: success, 8664 build jobs;
- PR-head Lean CI `34471931934`: success;
- merged-main Lean CI `34472224655`: success.

Axiom/placeholder state:

- no project `sorry`;
- no project `admit`;
- no project-specific axiom;
- certified theorem dependency reports contain only standard Lean/mathlib foundations `propext`, `Classical.choice`, and `Quot.sound`.

## 18. Paper-claim ↔ formal-theorem map

The detailed mapping is authoritative in `theorem_certificates/STAGE075A_FORMAL_VERIFICATION_CERTIFICATE.md`.

Frozen summary:

- P1 -> `xPrivate_strict_decrease` and supporting Core identities;
- P2R private weak order -> `privateObjective_scope_diff`, `private_argmax_nonincreasing`;
- P2R coordinated weak order -> `coordinatedObjective_scope_diff`, `coordinated_argmax_nondecreasing`;
- P2R strict interior contradiction core -> `private_same_interior_foc_impossible`, `coordinated_same_interior_foc_impossible`;
- E0 algebraic continuation core -> `candidatePrice_foc`, `foreclosureThreshold_eq`, `foreclosureThreshold_neg`, `reentry_margin_pos`, `candidatePrice_pos`;
- P4 threshold -> `exists_unique_threshold_root` and threshold sign/monotonicity lemmas;
- P4 policy signs -> `Fp0Expr_pos`, `FppExpr_neg`, `Fp1Expr_nonneg_iff_le_threshold`, `Fp1Expr_neg_iff_threshold_lt`;
- P4 policy-objective fidelity -> `policyObjective_eq_closed`, `policyObjective_den_pos`;
- welfare -> `consumerSurplus_identity`, `producerSurplus_identity`, `welfare_identity`, `efficientWelfare_identity`, `efficient_minus_bertrand_identity`.

## 19. Assumptions encoded but not proved inside Lean

The formal layer intentionally receives or leaves outside the kernel proof the following economic/analytic bridges where indicated:

- primitive interpretation of utility, quality, and policy objects;
- complete consumer KKT allocation correspondence;
- full derivation of the price best-response correspondence from primitive consumer optimization;
- analytic implication from global `(R)` to every pointwise continuation inequality supplied to selected Lean lemmas;
- complete global pure-strategy equilibrium exhaustion;
- differentiability/strict-concavity regularity steps establishing unique general-`g` maximizers;
- derivation of interior FOCs from the optimization problem;
- formal differentiation connecting the policy objective to every displayed derivative formula;
- complete regulator argmax theorem;
- unrestricted planner optimization.

These supplied/excluded components are not described in the manuscript as machine-proved.

## 20. Continuation-completeness register

Relevant off-path history class:

all `b in [0,1]` and `(x_1,x_2) in [0,E]^2`.

Continuation status under `(R)`:

`CERTIFIED UNIQUE GLOBAL PURE-STRATEGY PRICE EQUILIBRIUM WITH BOTH PRODUCTS ACTIVE`.

The Stage-4A proof separately establishes inactive-product profitable re-entry, excludes active zero-price equilibria, derives the unique active FOC candidate, and establishes globality by foreclosure-threshold sign and strict concavity on the active region.

Independent direct-payoff/allocation verification is supplied by:

- `scripts/stage4a_independent_equilibrium_set_audit.py`;
- `scripts/stage11_independent_continuation_audit.py`.

## 21. Active-set, corner, participation, and solver taxonomy

Consumer allocation regimes explicitly audited:

- active-active;
- product 1 only;
- product 2 only;
- both inactive / zero-demand behavior.

Upstream corners explicitly audited:

- `b=0`, `b=1`, near-boundary scope;
- `x_i=0`, `x_i=E`, symmetric and asymmetric R&D corners;
- near `y=1/2`, `y=1`, `nu=0`, `nu=y`;
- policy-threshold neighborhood `H=0`.

Solver/evaluator taxonomy is fail-closed: an unclassified KKT regime is `UNRESOLVED`, not an unprofitable deviation.

Stage-4A permanent evaluator result:

- unresolved: `0`;
- profitable price deviations: `0`;
- alternative pure price equilibria: `0`;
- R&D corner failures: `0`;
- policy regime failures: `0`;
- welfare failures: `0`.

Stage-11 independent continuation result:

- upstream histories: `73`;
- player-history deviation problems: `146`;
- tested nonnegative deviation prices per player-history: `10001`;
- `UNRESOLVED=0`;
- numerical failures `=0`;
- profitable finite deviations `=0`;
- pure boundary-equilibrium counterexamples `=0`.

## 22. Multiplicity, nonexistence, and selection assumptions

Within the paper's claimed pure-strategy scope under `(R)`:

- downstream price equilibrium: unique;
- quadratic private R&D equilibrium: unique;
- P4 regulator optimum: unique in the stated threshold regimes.

No continuation-selection assumption is needed within that scope.

No claim is made about mixed-strategy equilibrium uniqueness. No mixed-equilibrium selection is used for welfare.

## 23. Counterexample and regression-test register

Permanent regression evidence includes:

- `scripts/stage4a_independent_equilibrium_set_audit.py`;
- `scripts/stage11_independent_continuation_audit.py`;
- `scripts/symbolic_verify.py`;
- `scripts/numerical_verify.py`;
- `tests/test_p2r_order_monotonicity.py`;
- `tests/test_freeze_regressions.py`;
- `tests/test_stage9r_metadata.py`.

Historical counterexample discipline is part of the freeze: the former pointwise derivative formulation of general-`g` P2R was rejected and replaced by the current order theorem. Regression tests include corner plateaus and a differentiable strictly concave technology that is not twice differentiable at an interior point.

## 24. Verification status

Analytic proof status: PASS for all claims actually presented as theorems/propositions.

Stage-4A independent adversarial certification: PASS.

Stage-7.5A generality/quantifier certification: PASS.

Formal Verification Gate: PASS for the explicitly bounded proof-critical core.

Symbolic/numerical/regression verification: PASS on the current certified object.

Latest merged-main evidence before refreeze:

- normal verify/package run `34472224636`: success;
- formal-verification run `34472224655`: success.

No material unresolved continuation, solver failure, theorem mismatch, benchmark mismatch, proof escape hatch, or stale formal certificate remains at entry to v4.

## 25. Certification-only change record from v3 to v4

Scientific changes: `NONE`.

Administrative/certification changes:

1. v3 preserved as `docs/THEORY_FREEZE_v3.md`;
2. current latest-workflow authority recorded;
3. Stage-4A theorem certificate inheritance recorded;
4. Stage-7.5A claim-scope certificate inheritance recorded;
5. Formal Verification PASS, theorem mapping, toolchain, assumptions, and model boundary recorded;
6. continuation/multiplicity/solver/counterexample registers expanded to current Stage-8 requirements;
7. pre-existing manuscript wording is frozen at the narrower `pure-strategy` uniqueness scope certified in Stage 7.5A.

The formal P2R bounded-domain correction and manuscript pure-strategy wording repair occurred before the v4 refreeze and were classified at Stage 7.5A as statement-fidelity/certification repairs, not changes to theorem conclusions.

## 26. Downstream synchronization contract

The active theory identifier is now `SSDI-THEORY-FREEZE-2026-09-10-v4`.

Historical Stage-9/10 artifacts that still identify v3 remain historical until the next authorized step, **Stage 9 formal-artifact reproducibility synchronization**. They must not be silently rewritten as if they were produced under v4. Stage 9 must explicitly record inherited scientific identity and update active reproducibility metadata to v4 without changing quantitative outputs.

After Stage 9 sync, the project must run the latest-workflow Stage-11 certification-regression recheck before relying on the migrated certificates for refreshed submission QA.

## 27. Theory change control

Any substantive post-v4 theoretical change must record what changed, why, affected equations/propositions/quantifiers/benchmarks/formal theorems/verifications/literature claims, and the earliest workflow stage to reopen.

- equilibrium/globality change -> reopen Stage 4/4A and all affected downstream gates;
- function-class, quantifier, benchmark, or claim-scope change -> reopen Stage 7.5A and earlier affected analytic stages;
- material change to a formally certified theorem, encoded hypothesis, policy objective, continuation inequality, or welfare identity -> mark Formal Verification Certificate stale and rerun the Formal Verification Gate before refreeze;
- substantive theory changes after freeze require a new versioned freeze; no silent edits to v4 are permitted.

Certification-only metadata synchronization that does not change the scientific object may proceed at the appropriate downstream stage with explicit provenance.

## Final verdict

`THEORY FROZEN — GO TO REPRODUCIBILITY SETUP`

Authorized next step under the latest-workflow migration:

`Stage 9 — formal-artifact reproducibility synchronization on SSDI-THEORY-FREEZE-2026-09-10-v4`.
