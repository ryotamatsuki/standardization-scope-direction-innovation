import SSDI.Core
import SSDI.PolicySigns

/-!
# Quadratic policy-objective fidelity layer

This file encodes the actual normalized policy objective used in the paper,
not merely its reported derivative expressions, and proves its exact rational
closed form after substituting the private R&D allocation.  The subsequent
formal sign layer still treats the manuscript's derivative formulas as the
analytic input; formal calculus connecting this objective to those derivative
formulas is explicitly outside the selected Stage-7.5A target and is not
claimed here.
-/

namespace SSDI

noncomputable section

/-- Quadratic innovation technology in the baseline. -/
def gQuadratic (kappa r : ℝ) : ℝ := r - kappa * r ^ 2 / 2

/--
The paper's normalized reduced policy objective
`F(b)=kappa[(1+b)g(xF(b))+g(E-xF(b))]`, with `E=y/kappa`.
-/
def policyObjective (kappa y nu b : ℝ) : ℝ :=
  kappa *
    ((1 + b) * gQuadratic kappa (xPrivate kappa y nu b) +
      gQuadratic kappa (y / kappa - xPrivate kappa y nu b))

/-- Exact rational closed form of the normalized reduced policy objective. -/
def policyObjectiveClosed (y nu b : ℝ) : ℝ :=
  (b ^ 3 * nu ^ 2
      - b ^ 2 * nu ^ 2 * y ^ 2
      + 4 * b ^ 2 * nu ^ 2 * y
      - 2 * b ^ 2 * nu ^ 2
      - 4 * b ^ 2 * nu
      + 2 * b * nu * y ^ 2
      - 8 * b * nu * y
      - b * y ^ 2
      + 4 * b * y
      - 2 * y ^ 2
      + 8 * y) /
    (2 * (2 - b * nu) ^ 2)

/--
Exact statement-fidelity bridge from the paper's substituted economic objective
to a rational expression containing only `(y,nu,b)`.
-/
theorem policyObjective_eq_closed
    {kappa y nu b : ℝ}
    (hkappa : kappa ≠ 0)
    (hden : 2 - b * nu ≠ 0) :
    policyObjective kappa y nu b = policyObjectiveClosed y nu b := by
  unfold policyObjective policyObjectiveClosed gQuadratic xPrivate
  field_simp [hkappa, hden] <;> ring

/-- On the frozen policy domain, the private-allocation denominator is positive. -/
theorem policyObjective_den_pos
    {y nu b : ℝ}
    (hy1 : y < 1)
    (hnuy : nu < y)
    (hb0 : 0 ≤ b)
    (hb1 : b ≤ 1) :
    0 < 2 - b * nu := by
  have hnu1 : nu < 1 := lt_trans hnuy hy1
  have hbnu : b * nu ≤ nu := by nlinarith
  linarith

end

end SSDI
