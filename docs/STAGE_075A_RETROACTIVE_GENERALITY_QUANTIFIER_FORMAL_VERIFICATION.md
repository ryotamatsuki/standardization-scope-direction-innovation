# Retroactive Stage 7.5A — Generality / Quantifier Red-Team Gate + Formal Verification Gate

Date: 2026-09-10

Repository: `ryotamatsuki/standardization-scope-direction-innovation`

Scientific object: `SSDI-THEORY-FREEZE-2026-09-06-v3`

Compatibility branch: `retro-stage075a-formal-verification`

Latest-workflow authority: `ryotamatsuki/research-paper-workflow@f48984013898696f010f0437a8cfed6b5b54bdc2`.

Historical production workflow remains `v1.3@3e4e6a3f76d86058024d06f9710f942e21627386`; this record is a retroactive compatibility certification and does not rewrite historical Stage chronology.

## 1. Executive scope-certification verdict

`GO — GENERALITY / QUANTIFIER CERTIFICATION PASS`

Embedded Formal Verification Gate:

`FORMAL VERIFICATION PASS`

No theorem failure, omitted equilibrium class within the claimed pure-strategy scope, benchmark mislabeling, or unsupported generality claim survives the audit. No substantive theory rollback is required.

Two certification-only repairs were made during the gate:

1. the new Lean P2R order theorem was corrected from an unnecessarily all-real maximizer/monotonicity formulation to assumptions explicitly restricted to the actual R&D choice set `[0,E]`;
2. two manuscript sentences were narrowed from unqualified `unique Bertrand equilibrium` / `unique active-product price equilibrium` to `unique ... pure-strategy ... equilibrium`, matching the Stage-4A equilibrium-set certificate.

Neither repair changes the v3 mathematical result set.

## 2. Formal quantifier table

| Claim | Certified quantifiers/domain | Classification | Status |
|---|---|---|---|
| P1 private R&D reallocation | for every frozen quadratic parameter vector satisfying `1/2<y<1`, `0<nu<y`, `(R)`, and every `b in [0,1]`, the unique interior private allocation satisfies `dxF/db<0` | baseline closed-form theorem | PASS |
| P2R private order | for every differentiable increasing strictly concave `g` on `[0,E]` and every `b2>b1`, `xF(b2)<=xF(b1)`; strict if both compared private optima are interior | general function-class theorem | PASS |
| P2R coordinated order | same function class and policy comparison, `xS(b2)>=xS(b1)`; strict if both compared coordinated optima are interior | general function-class theorem | PASS |
| P3R fixed symmetric allocation | for every fixed symmetric common allocation `xbar>0`, welfare is strictly increasing in `b`, hence `bFIX=1`; if `xbar=0`, regulator is indifferent | constrained benchmark theorem | PASS |
| P4 selective standardization | for every `y in (1/2,1)` there exists a unique `bar nu(y) in (0,y)`; at/below threshold `b*=1`; above threshold and below `y`, unique interior `b*` | quadratic-specific global policy theorem | PASS |
| P5R coordinated symmetric R&D | under frozen restrictions, regulator choosing `b` and symmetric R&D composition while Bertrand pricing remains decentralized chooses `bCOORD=1` | constrained benchmark theorem | PASS |
| Price continuation | under `(R)`, for every feasible `b in [0,1]`, `(x1,x2) in [0,E]^2`, the downstream game has the certified unique global pure-strategy price continuation with both products active | all-history pure-strategy equilibrium-set theorem | PASS |
| Endogenous total-R&D extension | only the relative interior FOC `(1-nu b)g'(x)=g'(z)`; no claim on total R&D, global common effort, or optimal scope | local comparative mechanism statement | PASS |
| Incomplete transferability | `t=lambda b` reparameterizes the relative-return wedge; no new global policy theorem | reparameterization robustness | PASS |

The paper explicitly does not claim a pointwise `dx/db` sign for arbitrary general `g`, generic persistence of P4 under small `C^2` perturbations, or a general selective-standardization theorem outside the quadratic baseline.

## 3. Equilibrium-set / uniqueness / selection-scope table

| Object | Scope certified | Selection/refinement | What is not claimed |
|---|---|---|---|
| Downstream price game | unique global pure-strategy continuation under `(R)` at every feasible upstream history | none beyond the original game plus sufficient global-continuation condition `(R)` | mixed-strategy uniqueness |
| Quadratic R&D subgame | unique symmetric equilibrium because each best response is independent of rival allocation and strictly concave/interior | none | asymmetric multiplicity outside frozen assumptions |
| General-`g` R&D choice | unique one-dimensional maximizer from strict concavity for each firm/coordinated problem | no equilibrium refinement | differentiability of optimizer in `b` |
| Regulator P4 | unique complete-scope optimum at/below threshold; unique interior optimum above threshold | no equilibrium selection because downstream/upstream pure path is unique in claimed domain | robustness of policy uniqueness to arbitrary nonquadratic `g` |

No welfare theorem is written as equilibrium-selection invariant over mixed equilibria. The relevant welfare path uses the certified pure-strategy continuation.

## 4. Assumption-dependence table

| Result | Economic assumptions | Mathematical/shape restrictions | Tractability/scope restrictions |
|---|---|---|---|
| P1 | fixed R&D capacity; scope changes common-layer transferability; differentiated Bertrand rivalry | quadratic `g`; `1/2<y<1`; `0<nu<y` | `(R)` for all-history price continuation |
| P2R | same allocation objective induced by the model | `g` differentiable, increasing, strictly concave on `[0,E]` | policy theorem not generalized |
| P3R | fixed symmetric R&D composition; decentralized Bertrand pricing | positive fixed common allocation for strictness | constrained comparison only |
| P4 | decentralized endogenous composition, scope-only policy instrument | quadratic `g`; frozen parameter domain; strict concavity of reduced objective | not generic in function space |
| P5R | regulator coordinates only symmetric R&D composition while prices remain decentralized | strict concavity/monotonicity inherited from frozen model | not unrestricted first best |
| Price continuation | nonnegative prices and primitive demand/KKT structure | `0<rho<1`, positive quality bounds | sufficient condition `(R)` |

## 5. Selection/refinement provenance and symmetry audit

Condition `(R)` is a disclosed sufficient regularity condition belonging to the frozen model's global-continuation specification. It is not an ex post equilibrium refinement and is applied symmetrically to both firms and all feasible upstream histories.

Stage-4A separately audited candidate deviations, alternative pure equilibria, zero-demand/zero-profit indifference triggers, and consumer KKT regimes. No weak-dominance elimination or asymmetric refinement is used to retain the preferred equilibrium while deleting inconvenient equilibria.

The Stage-7.5A wording repair makes the manuscript's uniqueness language match the actual equilibrium-set certificate: `pure-strategy` is now explicit where uniqueness is claimed.

## 6. Function-class counterexample audit

The gate re-tested the main ways the manuscript could overstate generality.

### Arbitrary differentiable increasing strictly concave `g`

Potential failure attacked: infer `dxF/db<0` and `dxS/db>0` pointwise from differentiability of `g` alone.

Result: rejected as an invalid stronger claim. The v3 manuscript already uses the correct global order result. Corners may create flat ranges, and differentiability of `g` does not by itself imply differentiability of the argmax correspondence. The paper explicitly says so.

### Small `C^2` perturbations of the quadratic technology

Potential failure attacked: claim P4's strict policy concavity/unique threshold is generically robust.

Result: not licensed. Higher-order features of `g` can alter induced policy curvature. The manuscript explicitly declines this claim and labels P4 quadratic-specific.

### Endogenous total R&D

Potential failure attacked: infer that a steep total-capacity cost preserves selective standardization or signs the total R&D response.

Result: not licensed. Only the relative interior FOC survives. The manuscript states this limitation.

### Corner cases

P2R's weak ordering is global and includes corners; strictness is claimed only when both compared optima are interior. This is the maximum defensible wording.

No admissible counterexample was found to the actual v3 headline claims after these scope restrictions.

## 7. Baseline vs robustness vs general-theorem classification

- P1: quadratic baseline theorem.
- P2R: genuine general function-class order theorem; strict only under compared-interior optima.
- P3R: fixed-allocation constrained benchmark theorem.
- P4: quadratic baseline policy theorem only.
- P5R: coordinated-symmetric constrained benchmark theorem.
- incomplete transferability: reparameterization robustness only.
- endogenous total R&D: local relative-FOC robustness only.
- institutional examples: interpretation, not validation.
- empirical cited evidence: suggestive consistency, not causal validation.

The abstract and Introduction respect these distinctions.

## 8. Welfare-selection robustness audit

The welfare analysis is evaluated on the certified symmetric pure-strategy equilibrium path. The exact formulas for `CS`, `PS`, `W`, efficient fixed-quality welfare, and the Bertrand quantity-control gap are machine checked in `formal/SSDI/WelfareIdentities.lean`.

The central welfare comparison is instrument constrained:

`bFIX = bCOORD = 1`, while decentralized endogenous R&D may yield `0<b*<1` above the rivalry threshold.

The manuscript does not state that selective standardization dominates complete standardization combined with unmodeled subsidies, licensing, disclosure, or other appropriation instruments.

## 9. Benchmark-definition audit

PASS.

The coordinated benchmark's feasible set is: regulator chooses standard scope and a common symmetric R&D composition, while differentiated Bertrand pricing remains decentralized. This is correctly called a constrained coordinated-symmetric benchmark.

The paper expressly demonstrates that decentralized Bertrand welfare is below the fixed-quality quantity-control benchmark and states that P5R is not an unconstrained first best. It also notes that R&D is restricted to the symmetric diagonal. No surviving manuscript sentence relabels this object as first best.

## 10. Claim-scope ledger

| Manuscript claim | Evidence | Maximum defensible wording | Prohibited stronger wording | Status |
|---|---|---|---|---|
| broader scope redirects private R&D toward proprietary innovation | P1 analytic proof; `Core.lean`; symbolic regression | strict derivative in quadratic interior baseline | strict derivative for every concave technology | PASS |
| general directional wedge | P2R analytic proof; `Generality.lean` | globally nonincreasing/nondecreasing; strict at two interior optima | globally strict including corners; pointwise derivative for arbitrary `g` | PASS |
| fixed positive symmetric allocation favors full scope | P3R welfare argument | complete scope under fixed symmetric positive common R&D | unrestricted first best | PASS |
| selective standardization threshold | P4 analytic proof; `Threshold.lean`; `PolicySigns.lean`; `PolicyObjective.lean`; symbolic/numerical checks | exact quadratic threshold and unique interior policy above threshold | generic policy theorem for arbitrary concave `g` | PASS |
| coordinated symmetric R&D favors full scope | P5R; welfare identities | constrained coordinated-symmetric benchmark | first best / unconstrained planner optimum | PASS |
| global price continuation | Stage-4A D1/D2/D3; KKT regression; `Continuation.lean` proof-critical inequalities | unique global pure-strategy price continuation under `(R)` | unique equilibrium including mixed strategies | PASS |
| empirical relevance | cited case/firm evidence | motivation / suggestive institutional consistency | causal validation of portfolio mechanism | PASS |

## 11. Evidence ledger

| Attack | Evidence artifact | Result | Surviving limitation |
|---|---|---|---|
| overbroad P2R quantifier | `formal/SSDI/Generality.lean` and manuscript P2R | bounded-domain formal statement repaired; PASS | unique-maximizer regularity step remains analytic |
| derivative-overclaim under general `g` | P2R/robustness text and prior Stage-7R2 repair | PASS | no pointwise derivative claim |
| unqualified equilibrium uniqueness | Stage-4A certificate + manuscript Model/Equilibrium wording | repaired to `pure-strategy`; PASS | mixed equilibrium not certified |
| P4 threshold algebra | `formal/SSDI/Threshold.lean` | existence/uniqueness/sign partition PASS | P4 remains quadratic |
| P4 sign architecture | `formal/SSDI/PolicySigns.lean` | initial slope/curvature/endpoint regime PASS | full formal calculus/argmax outside selected target |
| policy-objective statement fidelity | `formal/SSDI/PolicyObjective.lean` | exact substituted-objective closed form PASS | derivative link remains analytic |
| global continuation inequalities | `formal/SSDI/Continuation.lean` | foreclosure/re-entry/candidate-price core PASS | full KKT/global correspondence stays Stage-4A evidence |
| welfare identity/benchmark taxonomy | `formal/SSDI/WelfareIdentities.lean` | PASS | unrestricted first best not analyzed |
| proof escape hatch / axioms | `formal/SSDI/Assurance.lean`, clean CI | only standard logical axioms; no project axiom; no sorry/admit | none |

## 12. Formal-verification applicability decision

`FORMALIZATION APPLICABLE`

Reason: the paper's headline results depend on exact threshold logic, quantified inequality signs, global-continuation inequalities, welfare identities, and comparative-static order arguments. A targeted formal proof layer materially improves assurance even though full game formalization would be disproportionate.

## 13. Formal-verification certificate

Canonical certificate:

`theorem_certificates/STAGE075A_FORMAL_VERIFICATION_CERTIFICATE.md`

Final state:

`FORMAL VERIFICATION PASS`

Certified formal source commit: `5078719c57495c510405aa0cd33e621f3a7a2ab0`.

Dedicated clean Lean CI:

- run `34469130983`: SUCCESS;
- Lean `v4.32.1`;
- mathlib `520045ab14e26149ee970e2e617ca04b09bde5d6`;
- `lake build`: 8664 jobs successful;
- `PROJECT_LEAN_ESCAPE_HATCH_AUDIT=PASS`;
- `#print axioms`: only `propext`, `Classical.choice`, `Quot.sound` for listed certified targets.

Companion full verification CI run `34469131273`: SUCCESS.

Post-manuscript-scope clarification verify run `34469426862`: SUCCESS.

## 14. Paper-claim ↔ formal-theorem mapping and non-formalized scope

The detailed mapping is in `theorem_certificates/STAGE075A_FORMAL_VERIFICATION_CERTIFICATE.md`.

The principal excluded objects are explicit: complete consumer KKT correspondence inside Lean, complete pure-price equilibrium uniqueness proof from primitive utility, all mixed strategies, full SPNE construction, analytic derivation of P2R unique argmax/FOCs, formal differentiation connecting P4's reduced objective to all displayed derivative formulas, the complete regulator argmax theorem, and unrestricted first-best optimization.

These exclusions do not create a scope defect because the manuscript does not represent them as machine-certified and the relevant economic/globality claims remain independently covered by Stage 4A and analytic verification.

## 15. Required wording downgrades

Completed inside this gate:

- `unique Bertrand equilibrium` -> `unique pure-strategy Bertrand equilibrium` in the Model section;
- `unique active-product price equilibrium` -> `unique active-product pure-strategy price equilibrium` in the Equilibrium section.

No further wording downgrade is required.

## 16. Earliest-stage rollback requirement

None.

The issues found were certification-scope/fidelity issues and were repaired within Stage 7.5A. No primitive, payoff, equilibrium condition, theorem conclusion, threshold, or welfare comparison changed.

## 17. Canonical stage verdict and routing

Stage 7.5A verdict:

`GO — GENERALITY / QUANTIFIER CERTIFICATION PASS`

Formal Verification Gate:

`FORMAL VERIFICATION PASS`

Authorized route under the latest-workflow compatibility migration:

`Retroactive Stage 7.5A complete -> certification-only Stage 8 refreeze`

The current scientific theory remains `SSDI-THEORY-FREEZE-2026-09-06-v3` until that certification-only Stage-8 migration step formally records the latest-workflow inheritance. No substantive refreeze is implied by this Stage-7.5A pass.
