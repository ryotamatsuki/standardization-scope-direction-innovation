import SSDI.Threshold

/-!
# Policy-sign layer for P4

This file formalizes the sign claims used by the quadratic selective-
standardization argument: positive initial slope, negative curvature expression,
and the sign of the complete-standardization endpoint slope relative to the
unique rivalry threshold.

The expressions here are exactly those reported in equations (Fpp), (Fp0), and
(Fp1) of the manuscript.  A later layer will connect them to a full formal
argmax theorem for the regulator's policy problem.
-/

namespace SSDI

noncomputable section

/-- Paper expression for `F'(0)`. -/
def Fp0Expr (y : ℝ) : ℝ := y * (4 - y) / 8

/-- Paper expression for `F''(b)` in the quadratic interior baseline. -/
def FppExpr (y nu b : ℝ) : ℝ :=
  -(nu * (2 - y) ^ 2 * (2 * b * nu ^ 2 + b * nu + 2 * nu + 4)) /
    (2 - b * nu) ^ 4

/-- Paper expression for `F'(1)`, written with the threshold polynomial. -/
def Fp1Expr (y nu : ℝ) : ℝ :=
  -H y nu / (2 * (2 - nu) ^ 3)

section PolicySigns

/-- The regulator's initial-scope slope expression is strictly positive. -/
theorem Fp0Expr_pos
    {y : ℝ}
    (hyhalf : (1 / 2 : ℝ) < y)
    (hy1 : y < 1) :
    0 < Fp0Expr y := by
  unfold Fp0Expr
  have hy0 : 0 < y := by linarith
  have hy4 : 0 < 4 - y := by linarith
  positivity

/-- The reported second-derivative expression is strictly negative on `b∈[0,1]`. -/
theorem FppExpr_neg
    {y nu b : ℝ}
    (hyhalf : (1 / 2 : ℝ) < y)
    (hy1 : y < 1)
    (hnu0 : 0 < nu)
    (hnuy : nu < y)
    (hb0 : 0 ≤ b)
    (hb1 : b ≤ 1) :
    FppExpr y nu b < 0 := by
  unfold FppExpr
  have hy0 : 0 < y := by linarith
  have hy2 : 0 < 2 - y := by linarith
  have hnu1 : nu < 1 := lt_trans hnuy hy1
  have hbnu_le : b * nu ≤ nu := by
    nlinarith
  have hdenbase : 0 < 2 - b * nu := by linarith
  have hsum : 0 < 2 * b * nu ^ 2 + b * nu + 2 * nu + 4 := by
    have hbnunonneg : 0 ≤ b * nu := mul_nonneg hb0 (le_of_lt hnu0)
    have hbnu2nonneg : 0 ≤ b * nu ^ 2 := mul_nonneg hb0 (sq_nonneg nu)
    nlinarith
  rw [neg_div]
  apply neg_lt_zero.mpr
  positivity

/-- On the frozen domain the denominator in the complete-scope slope is positive. -/
theorem Fp1_den_pos
    {y nu : ℝ}
    (hy1 : y < 1)
    (hnuy : nu ≤ y) :
    0 < 2 * (2 - nu) ^ 3 := by
  have hnu2 : 0 < 2 - nu := by linarith
  positivity

/-- Nonpositive `H` implies a nonnegative complete-scope endpoint slope. -/
theorem Fp1Expr_nonneg_of_H_nonpos
    {y nu : ℝ}
    (hy1 : y < 1)
    (hnuy : nu ≤ y)
    (hH : H y nu ≤ 0) :
    0 ≤ Fp1Expr y nu := by
  unfold Fp1Expr
  have hden := Fp1_den_pos hy1 hnuy
  exact div_nonneg (neg_nonneg.mpr hH) (le_of_lt hden)

/-- Positive `H` implies a strictly negative complete-scope endpoint slope. -/
theorem Fp1Expr_neg_of_H_pos
    {y nu : ℝ}
    (hy1 : y < 1)
    (hnuy : nu ≤ y)
    (hH : 0 < H y nu) :
    Fp1Expr y nu < 0 := by
  unfold Fp1Expr
  have hden := Fp1_den_pos hy1 hnuy
  exact div_neg_of_neg_of_pos (neg_neg_of_pos hH) hden

/-- At or below the unique rivalry threshold, the endpoint slope is nonnegative. -/
theorem Fp1Expr_nonneg_of_le_threshold
    {y nuBar nu : ℝ}
    (hyhalf : (1 / 2 : ℝ) < y)
    (hy1 : y < 1)
    (hbar0 : 0 < nuBar)
    (hbary : nuBar < y)
    (hroot : H y nuBar = 0)
    (hnu0 : 0 ≤ nu)
    (hnule : nu ≤ nuBar) :
    0 ≤ Fp1Expr y nu := by
  have hH := H_nonpos_of_le_root hyhalf hy1 hbar0 hbary hroot hnu0 hnule
  have hnuy : nu ≤ y := le_trans hnule (le_of_lt hbary)
  exact Fp1Expr_nonneg_of_H_nonpos hy1 hnuy hH

/-- Above the unique rivalry threshold, the endpoint slope is strictly negative. -/
theorem Fp1Expr_neg_of_threshold_lt
    {y nuBar nu : ℝ}
    (hyhalf : (1 / 2 : ℝ) < y)
    (hy1 : y < 1)
    (hbar0 : 0 < nuBar)
    (hbary : nuBar < y)
    (hroot : H y nuBar = 0)
    (hbarlt : nuBar < nu)
    (hnuy : nu ≤ y) :
    Fp1Expr y nu < 0 := by
  have hH := H_pos_of_root_lt hyhalf hy1 hbar0 hbary hroot hbarlt hnuy
  exact Fp1Expr_neg_of_H_pos hy1 hnuy hH

/-- Exact endpoint-slope regime characterization at the unique threshold. -/
theorem Fp1Expr_nonneg_iff_le_threshold
    {y nuBar nu : ℝ}
    (hyhalf : (1 / 2 : ℝ) < y)
    (hy1 : y < 1)
    (hbar0 : 0 < nuBar)
    (hbary : nuBar < y)
    (hroot : H y nuBar = 0)
    (hnu0 : 0 ≤ nu)
    (hnuy : nu ≤ y) :
    0 ≤ Fp1Expr y nu ↔ nu ≤ nuBar := by
  constructor
  · intro hslope
    by_contra hnot
    have hbarlt : nuBar < nu := lt_of_not_ge hnot
    have hneg := Fp1Expr_neg_of_threshold_lt
      hyhalf hy1 hbar0 hbary hroot hbarlt hnuy
    linarith
  · intro hnule
    exact Fp1Expr_nonneg_of_le_threshold
      hyhalf hy1 hbar0 hbary hroot hnu0 hnule

/-- Strictly negative endpoint slope occurs exactly above the rivalry threshold. -/
theorem Fp1Expr_neg_iff_threshold_lt
    {y nuBar nu : ℝ}
    (hyhalf : (1 / 2 : ℝ) < y)
    (hy1 : y < 1)
    (hbar0 : 0 < nuBar)
    (hbary : nuBar < y)
    (hroot : H y nuBar = 0)
    (hnu0 : 0 ≤ nu)
    (hnuy : nu ≤ y) :
    Fp1Expr y nu < 0 ↔ nuBar < nu := by
  constructor
  · intro hneg
    by_contra hnot
    have hnule : nu ≤ nuBar := le_of_not_gt hnot
    have hnonneg := Fp1Expr_nonneg_of_le_threshold
      hyhalf hy1 hbar0 hbary hroot hnu0 hnule
    linarith
  · intro hbarlt
    exact Fp1Expr_neg_of_threshold_lt
      hyhalf hy1 hbar0 hbary hroot hbarlt hnuy

end PolicySigns

end

end SSDI
