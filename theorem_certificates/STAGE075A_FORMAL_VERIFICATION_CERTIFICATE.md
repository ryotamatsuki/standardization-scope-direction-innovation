# Stage 7.5A Formal Verification Certificate

Date: 2026-09-10

Repository: `ryotamatsuki/standardization-scope-direction-innovation`

Scientific object: `SSDI-THEORY-FREEZE-2026-09-06-v3`

Latest-workflow authority: `ryotamatsuki/research-paper-workflow@f48984013898696f010f0437a8cfed6b5b54bdc2`, especially `templates/STAGE_075A_GENERALITY_QUANTIFIER_RED_TEAM.md` and `checklists/FORMAL_VERIFICATION_CHECKLIST.md`.

## 1. Final state

`FORMAL VERIFICATION PASS`

This certificate covers a selected proof-critical formalization of the current theorem set. It is not a claim that Lean formally proves the complete economic game, the complete SPNE correspondence, or mixed-strategy price equilibrium uniqueness.

The certified formal-source commit is:

`5078719c57495c510405aa0cd33e621f3a7a2ab0`

A subsequent manuscript-only scope clarification at branch commit `30b8cc93adf8d67a67fc64863cef3e089ac1bb5c` narrows the price-equilibrium prose to `pure-strategy`; it does not alter any certified Lean source or broaden any theorem.

## 2. Toolchain and reproducibility

- Proof assistant: Lean 4 `v4.32.1`
- Lean executable reported by clean CI: `Lean (version 4.32.1, x86_64-unknown-linux-gnu, commit f054605aea4b840552cca2e725580bffd1e1b704, Release)`
- mathlib revision: `520045ab14e26149ee970e2e617ca04b09bde5d6`
- Toolchain pin: `formal/lean-toolchain`
- Library pin: `formal/lakefile.toml`
- Formal root: `formal/`
- Canonical build sequence: `lake update`; `lake exe cache get`; `lake build`
- Dedicated CI workflow: `.github/workflows/lean.yml`

Clean CI evidence:

- workflow: `lean-formal`
- run ID: `34469130983`
- source commit: `5078719c57495c510405aa0cd33e621f3a7a2ab0`
- conclusion: `success`
- build result: `Build completed successfully (8664 jobs).`
- escape-hatch audit: `PROJECT_LEAN_ESCAPE_HATCH_AUDIT=PASS`

Companion full verification/package CI:

- workflow run ID: `34469131273`
- source commit: `5078719c57495c510405aa0cd33e621f3a7a2ab0`
- conclusion: `success`
- includes `make verify`, exposition regeneration, LaTeX manuscript build, Stage-14 package QA, PDF/font preflight, and artifact upload.

Post-scope-wording manuscript CI:

- run ID: `34469426862`
- source commit: `30b8cc93adf8d67a67fc64863cef3e089ac1bb5c`
- conclusion: `success`

## 3. Formal source map

The certified source is:

- `formal/SSDI/Core.lean`
- `formal/SSDI/Threshold.lean`
- `formal/SSDI/PolicySigns.lean`
- `formal/SSDI/Generality.lean`
- `formal/SSDI/Continuation.lean`
- `formal/SSDI/WelfareIdentities.lean`
- `formal/SSDI/PolicyObjective.lean`
- `formal/SSDI/Assurance.lean`
- umbrella target: `formal/SSDI.lean`

## 4. Claim-to-formal-theorem map

| Paper claim / object | Formal theorem(s) | Encoded assumptions | Certified component | Explicitly not certified by this theorem |
|---|---|---|---|---|
| Mapping `0<rho<1 => 0<nu<1` | Core mapping lemmas | real-valued parameters, `nu=rho/(2-rho^2)` | exact sign/range algebra | economic interpretation of `nu` |
| P1 quadratic private reallocation | `xPrivate_strict_decrease` and Core identities | frozen quadratic parameter region | exact closed-form order/sign result | derivation of the profit maximization problem from all game primitives |
| P2R private weak global ordering | `privateObjective_scope_diff`, `private_argmax_nonincreasing` | maximizers on `Set.Icc 0 E`, monotonicity of `g`, `nu>0`, `b1<b2`, uniqueness where invoked | decreasing-differences/revealed-preference order core on the actual bounded R&D domain | proof inside Lean that differentiability + strict concavity imply the required unique maximizers |
| P2R coordinated weak global ordering | `coordinatedObjective_scope_diff`, `coordinated_argmax_nondecreasing` | maximizers on `Set.Icc 0 E`, monotonicity of `g`, `b1<b2`, uniqueness where invoked | increasing-differences/revealed-preference order core on the bounded domain | construction of the coordinated planner problem from primitive welfare inside Lean |
| P2R strict interior ordering | `private_same_interior_foc_impossible`, `coordinated_same_interior_foc_impossible` | positive marginal technology, two distinct policy values, both FOCs supplied | contradiction if identical interior optimum satisfied both policy FOCs | derivation of FOCs from differentiability/interior optimality inside Lean |
| Global pure-price continuation under `(R)` | `candidatePrice_foc`, `foreclosureThreshold_eq`, `foreclosureThreshold_neg`, `reentry_margin_pos`, `candidatePrice_pos` | pointwise ratio inequalities implied analytically by `(R)`, positive quality, `0<rho<1` | fragile algebraic implications excluding nonnegative foreclosure region and supporting re-entry/positive candidate prices | full consumer KKT correspondence, full global best-response proof, complete pure-equilibrium uniqueness, mixed strategies |
| P4 threshold existence and uniqueness | `exists_unique_threshold_root` plus Threshold sign/monotonicity lemmas | frozen `1/2<y<1`, threshold domain `[0,y]` | exact existence, uniqueness, and sign classification of the polynomial root | derivation of threshold polynomial from primitive policy objective |
| P4 initial slope / curvature / endpoint regime | `Fp0Expr_pos`, `FppExpr_neg`, `Fp1Expr_nonneg_iff_le_threshold`, `Fp1Expr_neg_iff_threshold_lt` | frozen quadratic parameter restrictions | signs of the exact manuscript expressions and threshold equivalence | formal differentiation of the policy objective and full argmax theorem |
| P4 policy-objective fidelity bridge | `policyObjective_eq_closed`, `policyObjective_den_pos` | quadratic technology, nonzero `kappa`, denominator/domain restrictions | exact equality between the paper's substituted economic objective and its rational closed form | formal proof that the reported `F'` and `F''` expressions are derivatives of that closed form |
| Welfare identities | `consumerSurplus_identity`, `producerSurplus_identity`, `welfare_identity` | symmetric Bertrand objects, `0<rho<1` | exact CS, PS and W formulas | equilibrium derivation of the symmetric price from the complete game |
| Constrained benchmark / quantity-control gap | `efficientWelfare_identity`, `efficient_minus_bertrand_identity` plus Core gap positivity | symmetric fixed-quality comparison, `0<rho<1` | efficient-quantity welfare identity and exact positive Bertrand gap | unrestricted first-best R&D/policy problem |

## 5. Statement-fidelity audit

### P2R

The manuscript states the general-technology result for differentiable, increasing, strictly concave `g` on `[0,E]`: private common-layer R&D is globally nonincreasing in scope, coordinated symmetric common-layer R&D is globally nondecreasing, and the comparisons are strict when both compared optima are interior. It explicitly rejects a pointwise `dx/db` statement for arbitrary `g`.

The Lean order theorem is intentionally modular. It formalizes the revealed-preference order argument on `Set.Icc 0 E`; unique maximization is supplied as a hypothesis rather than rederived from strict concavity. The strict-interior layer formalizes the FOC incompatibility conditional on the two FOCs. Therefore the Lean statement does not silently replace the bounded R&D domain with all of `R`, and it is not presented as a complete formal proof of every analytic prerequisite.

### P4

The Lean threshold layer proves existence and uniqueness of the rivalry threshold and the exact sign partition. `PolicySigns.lean` proves the signs of the exact displayed slope/curvature expressions. `PolicyObjective.lean` additionally connects the paper's substituted quadratic economic objective to an exact rational closed form. Formal differentiation and the complete regulator argmax theorem remain outside the selected Lean target and continue to rely on the analytic derivation plus independent symbolic/numerical regression evidence. This boundary is explicit and therefore is not conclusion smuggling.

### Price continuation

The analytic Stage-4A certificate establishes the global pure-strategy continuation claim. Lean formalizes high-risk algebraic implications of `(R)`, not the entire KKT/equilibrium correspondence. The manuscript was narrowed where necessary so that it says `unique ... pure-strategy` rather than an unqualified uniqueness claim. Mixed-strategy uniqueness is not asserted.

### Welfare and benchmarks

Lean derives the welfare identities directly from the symmetric price/quantity objects and formally proves the fixed-quality efficient quantity-control welfare gap. The paper calls the coordinated R&D comparison a constrained benchmark and explicitly states that it is not an unconstrained first best. The formal layer makes no stronger benchmark claim.

## 6. Axiom and escape-hatch audit

`formal/SSDI/Assurance.lean` applies `#print axioms` to the main certified targets.

Clean CI reports only standard Lean/mathlib logical foundations:

- `propext`
- `Classical.choice`
- `Quot.sound`

No project-specific axiom is used by the certified targets.

The dedicated workflow recursively fails on:

- `sorry`
- `admit`
- a project-defined `axiom` declaration

and the clean certified run reports `PROJECT_LEAN_ESCAPE_HATCH_AUDIT=PASS`.

No helper definition is treated as proof of economic equivalence merely because it encodes a condition. In particular, pointwise `(R)` consequences supplied to `Continuation.lean` are distinguished from the separate analytic proof that the primitive global condition implies those consequences.

## 7. Model-boundary certificate

Derived inside Lean:

- exact algebraic identities used in P1, P4 and welfare accounting;
- monotone comparative-statics order core for P2R on `[0,E]`;
- threshold existence/uniqueness and sign partition;
- selected price-continuation inequalities;
- welfare and efficient-quantity identities;
- exact substituted quadratic policy-objective closed form.

Supplied or certified outside Lean:

- interpretation of primitive utility and quality equations;
- complete consumer KKT correspondence;
- derivation of the entire price best-response correspondence from primitive consumer optimization;
- complete global pure-strategy price-equilibrium uniqueness proof under `(R)`;
- any mixed-strategy price-equilibrium statement;
- full SPNE construction;
- analytic implication from differentiable increasing strict concavity to all unique maximizers used in P2R;
- derivation of the interior FOCs from the optimization problem;
- formal calculus connecting the policy objective to the displayed `F'` and `F''` expressions;
- full regulator argmax theorem;
- unrestricted social-planner/first-best problem.

These exclusions are intentional. They remain covered by the Stage-4A mathematical certification, manuscript analytic proofs, symbolic verification, numerical regression, or are outside the paper's claim set.

## 8. Surviving risks

No unresolved formal-verification blocker remains for the current theorem scope. The residual risks are scope boundaries rather than failed proofs:

1. formal verification does not certify mixed-strategy price equilibrium uniqueness;
2. formal verification does not replace the Stage-4A all-history KKT/global-deviation audit;
3. P4 is not a complete machine-checked calculus/argmax proof from primitive model to `b*`;
4. P2R's analytic regularity-to-unique-argmax step remains outside Lean;
5. any future theorem or assumption change touching these interfaces makes this certificate stale.

## 9. Rollback rule

Any substantive change to the v3 theorem statements, admissible function class, policy domain, equilibrium concept, condition `(R)`, welfare benchmark, or quadratic policy objective invalidates the affected rows above and requires the earliest affected analytic stage plus Stage 7.5A formal recertification.

Pure wording changes that only narrow a claim and leave the formal source/theorem unchanged may be certified by a statement-fidelity recheck without rebuilding Lean, provided the exact certified source remains unchanged.

## 10. Certification verdict

All requirements of the current `FORMAL_VERIFICATION_CHECKLIST.md` are met for the selected high-value proof-critical core:

- applicability decision: closed as applicable;
- target map: complete;
- statement fidelity: audited;
- model boundary: explicit;
- no unexplained placeholder or project axiom: confirmed;
- toolchain and mathlib: pinned;
- clean CI build: successful;
- axiom/dependency report: retained;
- limitations: explicit.

Final formal-verification state:

`FORMAL VERIFICATION PASS`
