# Lean formal verification

This directory contains the Lean 4 + mathlib proof-assurance layer for the active scientific theory `SSDI-THEORY-FREEZE-2026-09-06-v3`.

The formal layer is complementary to the analytic proof, Stage-4A independent adversarial certification, Python/SymPy checks, and direct-KKT continuation audit. It is **not** a claim that the complete economic model or complete SPNE correspondence has been machine formalized.

## Toolchain and clean build

- Lean: `v4.32.1`, pinned by `formal/lean-toolchain`.
- mathlib: `v4.32.1`, pinned in `formal/lakefile.toml`; clean CI records the resolved mathlib commit.
- project root: `formal/`.
- build command:

```bash
lake update
lake exe cache get
lake build
```

`.github/workflows/lean.yml` executes this build from a clean Ubuntu runner and fails if project Lean source contains `sorry`, `admit`, or a project-specific `axiom` declaration. `SSDI/Assurance.lean` emits `#print axioms` dependency reports for the principal certified theorems.

## Selected Stage-7.5A proof-critical targets

The Formal Verification Gate intentionally selects a high-value core rather than the entire game.

### P1 — quadratic private R&D

`SSDI/Core.lean` certifies:

- `0<rho<1 -> 0<nu(rho)<1`;
- exact two-policy identity for `xPrivate`;
- strict decrease of the closed-form private allocation on its stated denominator domain;
- negativity of the reported quadratic derivative expression;
- the coordinated quadratic allocation identity and strict increase.

### P2R — general-technology direction

`SSDI/Generality.lean` certifies on the actual choice domain `[0,E]`:

- exact decreasing-differences and increasing-differences identities;
- the revealed-preference implication that unique private maximizers are nonincreasing in scope when `g` is monotone on `[0,E]`;
- the corresponding nondecreasing result for coordinated maximizers;
- the algebraic contradiction used to obtain strict order when equal interior optima would satisfy two FOCs and `g'(x)>0`.

Existence/uniqueness of maximizers from differentiability and strict concavity is supplied as a hypothesis to the abstract Lean order lemmas and remains analytically proved in the paper. Lean does not claim a pointwise derivative theorem for arbitrary `g`.

### E0 — price-continuation algebraic core

`SSDI/Continuation.lean` certifies:

- the active candidate solves the linear Bertrand FOC system;
- positivity of `4-rho^2` for `0<rho<1`;
- the exact rival-foreclosure threshold formula;
- the `(R)` cross-ratio inequality implies a negative foreclosure threshold;
- the opposite cross-ratio inequality plus positive quality implies `A_i>rho A_j`, the profitable re-entry margin used to eliminate inactive-product pure equilibria;
- the resulting candidate-price numerator and candidate price are positive.

The full consumer KKT correspondence and complete pure-price equilibrium-set exhaustion remain analytic/independent-computational objects, not Lean objects. Mixed-strategy equilibria are not claimed by the paper or formal layer.

### P4 — threshold and policy-sign core

`SSDI/Threshold.lean` and `SSDI/PolicySigns.lean` certify:

- `H(y,0)` and `H(y,y)` identities and signs;
- strict monotonicity of `H` on the frozen rivalry interval;
- existence and uniqueness of `bar_nu(y)` in `(0,y)`;
- sign classification of `H` relative to that root;
- positivity of the reported `F'(0)` expression;
- negativity of the reported `F''(b)` expression on `b in [0,1]`;
- the exact sign/threshold classification of the reported `F'(1)` expression.

`SSDI/PolicyObjective.lean` additionally encodes the actual normalized reduced policy objective from the paper and proves its exact rational closed form after substitution of `xPrivate`. This prevents the formal layer from treating an unrelated policy object as the paper's `F`.

Formal differentiation connecting that objective to the displayed `F'` and `F''` formulas, and the final calculus theorem turning strict curvature plus endpoint slopes into the complete regulator argmax theorem, are **not** claimed as Lean-certified. Those steps remain analytic and are independently SymPy/regression checked. The selected formal target certifies the fragile threshold, sign, domain, and objective-algebra core rather than claiming a complete P4 machine proof.

### W1 / P5R — welfare and benchmark identities

`SSDI/WelfareIdentities.lean` and `SSDI/Core.lean` certify:

- symmetric Bertrand price and quantity substitutions;
- exact consumer-surplus, producer-surplus, and total-welfare identities;
- the efficient fixed-quality quantity/welfare identity;
- the exact Bertrand quantity-control welfare gap and its positivity.

These facts protect the statement that the coordinated symmetric-R&D exercise is a constrained benchmark with decentralized Bertrand pricing, not an unconstrained first best.

## Explicit non-formalized model boundary

The Stage-7.5A certificate does **not** claim Lean formalization of:

- the representative consumer's complete KKT demand correspondence across all price regimes;
- the full Nash-equilibrium definition and exhaustive pure-price best-response correspondence;
- any absence theorem for mixed-strategy price equilibria;
- the complete three-stage SPNE construction;
- the derivation that price-equilibrium profit maximization reduces to the private R&D index from the full game primitives;
- existence/uniqueness of general-`g` maximizers from strict concavity as an internal Lean theorem;
- formal differentiation of the complete reduced policy objective or a full machine-checked regulator argmax theorem;
- institutional interpretations, literature novelty, or empirical claims.

Those components are covered, where claimed, by the analytic manuscript, Stage-4A theorem/equilibrium-set certificates, symbolic verification, and independent numerical/global-deviation artifacts.

## Formal gate status

The canonical Stage-7.5A formal certificate is `formal/FORMAL_VERIFICATION_CERTIFICATE.md`. Its final `FORMAL VERIFICATION PASS` state applies only to the selected proof-critical core documented above and must be invalidated if the corresponding paper theorem, assumptions, parameter domain, or formal source changes materially.
