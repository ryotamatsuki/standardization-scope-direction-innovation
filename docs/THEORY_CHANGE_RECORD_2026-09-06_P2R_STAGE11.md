# Theory Change Record — Stage 11 P2R Repair

Date: 2026-09-06

Trigger: Stage 11 hostile referee audit.

From freeze: `SSDI-THEORY-FREEZE-2026-09-06-v2`

To freeze: `SSDI-THEORY-FREEZE-2026-09-06-v3`

## Changed

Only P2R for arbitrary differentiable increasing strictly concave innovation technology.

Withdrawn:

`At interior optima, dx^F/db<0<dx^S/db.`

Replaced by:

For every `b_2>b_1`,

- `x^F(b_2)<=x^F(b_1)`;
- `x^S(b_2)>=x^S(b_1)`.

If both compared optima are interior, the respective order inequality is strict.

No pointwise derivative statement is made for arbitrary general `g`.

## Why

The v2 proof used `g''` although the theorem assumed only differentiability. Strict monotonicity in the order sense does not imply a strictly signed derivative at every point. The repaired proof uses decreasing/increasing differences and first-order conditions only for equality exclusion between two interior optima.

## Assumptions

Unchanged. No additional smoothness or curvature assumption is introduced.

## Unchanged objects

P1, P3R, P4, P5R, all quadratic formulas, price continuation, welfare formulas, threshold polynomial `H`, threshold checkpoints, the policy-regime figure, and the contribution boundary.

## Downstream synchronization

Updated locations include the active freeze, abstract/introduction/equilibrium/robustness/conclusion/appendix, welfare clarification, closest-literature wording, README, provenance, exposition manifest/generator/architecture record, and regression tests.

## Required routing

After CI pass and merge: repeat Stage 11. No direct Stage 12 progression.
