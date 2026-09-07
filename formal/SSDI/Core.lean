import Mathlib

/-!
# Formal verification kernel for
`Standardization Scope and Endogenous Innovation Portfolios`

This file formalizes algebraic claims from the active theory freeze
`SSDI-THEORY-FREEZE-2026-09-06-v3`.

The purpose is verification, not theory extension. In particular, this initial
kernel does not yet formalize the full subgame-perfect equilibrium construction
or the existence/uniqueness theorem for the endogenous policy threshold.
-/

namespace SSDI

noncomputable section

/-- Competitive-harm parameter, equation (nu). -/
def nu (rho : ℝ) : ℝ := rho / (2 - rho ^ 2)

/-- Closed-form private common-layer R&D allocation, equation (xprivate). -/
def xPrivate (kappa y nu b : ℝ) : ℝ :=
  (y - nu * b) / (kappa * (2 - nu * b))

/-- Closed-form coordinated symmetric common-layer allocation, equation (xsocial). -/
def xSocial (kappa y b : ℝ) : ℝ :=
  (y + b) / (kappa * (2 + b))

/-- The derivative expression reported for the quadratic private allocation. -/
def dxPrivate (kappa y nu b : ℝ) : ℝ :=
  -(nu * (2 - y)) / (kappa * (2 - nu * b) ^ 2)

/-- Threshold polynomial H(y, nu), equation (H). -/
def H (y nu : ℝ) : ℝ :=
  nu ^ 3
    + 2 * nu ^ 2 * y ^ 2
    - 8 * nu ^ 2 * y
    + 2 * nu ^ 2
    + nu * y ^ 2
    - 4 * nu * y
    + 16 * nu
    + 2 * y ^ 2
    - 8 * y

/-- Polynomial expression for the partial derivative H_nu. -/
def Hnu (y nu : ℝ) : ℝ :=
  3 * nu ^ 2 + 4 * nu * (y ^ 2 - 4 * y + 1) + y ^ 2 - 4 * y + 16

/-- Symmetric-Bertrand welfare multiplier K(rho). -/
def welfareK (rho : ℝ) : ℝ :=
  (3 - 2 * rho) / ((2 - rho) ^ 2 * (1 + rho))

/-- Bertrand quantity-control welfare gap at fixed symmetric quality. -/
def bertrandGap (A rho : ℝ) : ℝ :=
  A ^ 2 * (1 - rho) ^ 2 / ((2 - rho) ^ 2 * (1 + rho))

section ParameterBounds

/-- In the model region 0 < rho < 1, nu is positive. -/
theorem nu_pos {rho : ℝ} (hrho0 : 0 < rho) (hrho1 : rho < 1) :
    0 < nu rho := by
  unfold nu
  have hprod : 0 < (1 - rho) * (1 + rho) := by positivity
  have hsq : rho ^ 2 < 1 := by nlinarith
  have hden : 0 < 2 - rho ^ 2 := by nlinarith
  exact div_pos hrho0 hden

/-- In the model region 0 < rho < 1, nu is strictly below one. -/
theorem nu_lt_one {rho : ℝ} (hrho0 : 0 < rho) (hrho1 : rho < 1) :
    nu rho < 1 := by
  unfold nu
  have hprod : 0 < (1 - rho) * (1 + rho) := by positivity
  have hsq : rho ^ 2 < 1 := by nlinarith
  have hden : 0 < 2 - rho ^ 2 := by nlinarith
  rw [div_lt_iff₀ hden]
  nlinarith

/-- Compact version of the parameter restriction 0 < nu < 1. -/
theorem nu_mem_unit {rho : ℝ} (hrho0 : 0 < rho) (hrho1 : rho < 1) :
    0 < nu rho ∧ nu rho < 1 := by
  exact ⟨nu_pos hrho0 hrho1, nu_lt_one hrho0 hrho1⟩

end ParameterBounds

section QuadraticAllocation

/-- Exact two-policy difference identity for private common-layer R&D. -/
theorem xPrivate_diff
    (kappa y nu b1 b2 : ℝ)
    (hkappa : kappa ≠ 0)
    (hd1 : 2 - nu * b1 ≠ 0)
    (hd2 : 2 - nu * b2 ≠ 0) :
    xPrivate kappa y nu b1 - xPrivate kappa y nu b2 =
      nu * (2 - y) * (b2 - b1) /
        (kappa * (2 - nu * b1) * (2 - nu * b2)) := by
  unfold xPrivate
  field_simp [hkappa, hd1, hd2] <;> ring

/-- P1 in order form: broader scope strictly lowers private common-layer R&D. -/
theorem xPrivate_strict_decrease
    {kappa y nu b1 b2 : ℝ}
    (hkappa : 0 < kappa)
    (hy : y < 2)
    (hnu : 0 < nu)
    (hb : b1 < b2)
    (hd1 : 0 < 2 - nu * b1)
    (hd2 : 0 < 2 - nu * b2) :
    xPrivate kappa y nu b2 < xPrivate kappa y nu b1 := by
  have hdiff := xPrivate_diff kappa y nu b1 b2
    (ne_of_gt hkappa) (ne_of_gt hd1) (ne_of_gt hd2)
  have hratio :
      0 < nu * (2 - y) * (b2 - b1) /
        (kappa * (2 - nu * b1) * (2 - nu * b2)) := by
    positivity
  linarith

/-- The reported derivative expression is strictly negative in its interior domain. -/
theorem dxPrivate_neg
    {kappa y nu b : ℝ}
    (hkappa : 0 < kappa)
    (hy : y < 2)
    (hnu : 0 < nu)
    (hden : 0 < 2 - nu * b) :
    dxPrivate kappa y nu b < 0 := by
  unfold dxPrivate
  rw [neg_div]
  apply neg_lt_zero.mpr
  positivity

/-- Exact two-policy difference identity for the coordinated allocation. -/
theorem xSocial_diff
    (kappa y b1 b2 : ℝ)
    (hkappa : kappa ≠ 0)
    (hd1 : 2 + b1 ≠ 0)
    (hd2 : 2 + b2 ≠ 0) :
    xSocial kappa y b2 - xSocial kappa y b1 =
      (2 - y) * (b2 - b1) /
        (kappa * (2 + b1) * (2 + b2)) := by
  unfold xSocial
  field_simp [hkappa, hd1, hd2] <;> ring

/-- Quadratic coordinated benchmark moves in the opposite direction. -/
theorem xSocial_strict_increase
    {kappa y b1 b2 : ℝ}
    (hkappa : 0 < kappa)
    (hy : y < 2)
    (hb : b1 < b2)
    (hd1 : 0 < 2 + b1)
    (hd2 : 0 < 2 + b2) :
    xSocial kappa y b1 < xSocial kappa y b2 := by
  have hdiff := xSocial_diff kappa y b1 b2
    (ne_of_gt hkappa) (ne_of_gt hd1) (ne_of_gt hd2)
  have hratio :
      0 < (2 - y) * (b2 - b1) /
        (kappa * (2 + b1) * (2 + b2)) := by
    positivity
  linarith

end QuadraticAllocation

section ThresholdPolynomial

/-- Endpoint identity H(y,0)=2y(y-4). -/
theorem H_at_zero (y : ℝ) : H y 0 = 2 * y * (y - 4) := by
  unfold H
  ring

/-- Diagonal endpoint identity H(y,y)=2y(y-2)^2(y+1). -/
theorem H_at_diag (y : ℝ) : H y y = 2 * y * (y - 2) ^ 2 * (y + 1) := by
  unfold H
  ring

/-- Lower endpoint has the sign used in the P4 threshold argument. -/
theorem H_at_zero_neg {y : ℝ} (hy0 : 0 < y) (hy1 : y < 1) :
    H y 0 < 0 := by
  rw [H_at_zero]
  have hy4 : y - 4 < 0 := by linarith
  have h2y : 0 < 2 * y := by positivity
  exact mul_neg_of_pos_of_neg h2y hy4

/-- Upper endpoint has the sign used in the P4 threshold argument. -/
theorem H_at_diag_pos {y : ℝ} (hy0 : 0 < y) (hy1 : y < 1) :
    0 < H y y := by
  rw [H_at_diag]
  have hy2 : y - 2 ≠ 0 := by linarith
  positivity

/--
Core algebraic inequality behind H_nu > 0 on 0 < nu < y < 1,
with the paper's frozen range y > 1/2.
-/
theorem Hnu_lower_bound
    {y nu : ℝ}
    (hyhalf : (1 / 2 : ℝ) < y)
    (hy1 : y < 1)
    (_hnu0 : 0 < nu)
    (hnuy : nu < y) :
    5 * (y - 2) ^ 2 < Hnu y nu := by
  have hy0 : 0 < y := by linarith
  have hyprod : 0 < y * (1 - y) := by positivity
  have hq : y ^ 2 - 4 * y + 1 < 0 := by
    nlinarith
  have hnu1 : nu < 1 := lt_trans hnuy hy1
  have hprod : 0 < (nu - 1) * (y ^ 2 - 4 * y + 1) := by
    exact mul_pos_of_neg_of_neg (sub_neg.mpr hnu1) hq
  unfold Hnu
  nlinarith [sq_nonneg nu]

/-- H_nu is strictly positive throughout the frozen P4 parameter region. -/
theorem Hnu_pos
    {y nu : ℝ}
    (hyhalf : (1 / 2 : ℝ) < y)
    (hy1 : y < 1)
    (hnu0 : 0 < nu)
    (hnuy : nu < y) :
    0 < Hnu y nu := by
  have hlower := Hnu_lower_bound hyhalf hy1 hnu0 hnuy
  nlinarith [sq_nonneg (y - 2)]

end ThresholdPolynomial

section Welfare

/-- The symmetric-Bertrand welfare multiplier is positive for 0 < rho < 1. -/
theorem welfareK_pos {rho : ℝ} (hrho0 : 0 < rho) (hrho1 : rho < 1) :
    0 < welfareK rho := by
  unfold welfareK
  have h2 : 0 < 2 - rho := by linarith
  have h1p : 0 < 1 + rho := by linarith
  have hnum : 0 < 3 - 2 * rho := by linarith
  positivity

/-- Decentralized Bertrand welfare is strictly below efficient quantity choice at A != 0. -/
theorem bertrandGap_pos
    {A rho : ℝ}
    (hA : A ≠ 0)
    (hrho0 : 0 < rho)
    (hrho1 : rho < 1) :
    0 < bertrandGap A rho := by
  unfold bertrandGap
  have h2 : 0 < 2 - rho := by linarith
  have h1m : 0 < 1 - rho := by linarith
  have h1p : 0 < 1 + rho := by linarith
  positivity

end Welfare

end

end SSDI
