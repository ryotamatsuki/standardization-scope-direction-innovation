import SSDI.Core

/-!
# P4 threshold formalization

This file advances the Lean verification of Proposition P4 for the active
`SSDI-THEORY-FREEZE-2026-09-06-v3` theory freeze.  It proves the existence and
uniqueness of the rivalry threshold `bar_nu(y)` from the paper's threshold
polynomial `H`, without changing the economic model.

The proof deliberately avoids differentiating `H`: strict monotonicity is
obtained from an exact two-point factorization of `H y nu₂ - H y nu₁`.
-/

namespace SSDI

noncomputable section

section ThresholdExistenceUniqueness

/-- Exact secant factorization of the threshold polynomial in its `nu` argument. -/
theorem H_diff_factor (y nu1 nu2 : ℝ) :
    H y nu2 - H y nu1 =
      (nu2 - nu1) *
        (nu1 ^ 2 + nu1 * nu2 + nu2 ^ 2
          + 2 * (nu1 + nu2) * (y ^ 2 - 4 * y + 1)
          + y ^ 2 - 4 * y + 16) := by
  unfold H
  ring

/--
The secant factor is strictly positive on the frozen P4 domain.  This is the
two-point analogue of the lower bound already proved for `Hnu` in `Core.lean`.
-/
theorem H_secant_factor_lower_bound
    {y nu1 nu2 : ℝ}
    (hyhalf : (1 / 2 : ℝ) < y)
    (hy1 : y < 1)
    (hnu10 : 0 ≤ nu1)
    (hnu12 : nu1 < nu2)
    (hnu2y : nu2 ≤ y) :
    5 * (y - 2) ^ 2 <
      nu1 ^ 2 + nu1 * nu2 + nu2 ^ 2
        + 2 * (nu1 + nu2) * (y ^ 2 - 4 * y + 1)
        + y ^ 2 - 4 * y + 16 := by
  have hy0 : 0 < y := by linarith
  have hq : y ^ 2 - 4 * y + 1 < 0 := by
    nlinarith
  have hnu2pos : 0 < nu2 := lt_of_le_of_lt hnu10 hnu12
  have hnu2lt1 : nu2 < 1 := lt_of_le_of_lt hnu2y hy1
  have hnu1lt1 : nu1 < 1 := lt_trans hnu12 hnu2lt1
  have hsum : nu1 + nu2 < 2 := by linarith
  have hcross :
      0 < 2 * ((nu1 + nu2) - 2) * (y ^ 2 - 4 * y + 1) := by
    have hsneg : (nu1 + nu2) - 2 < 0 := by linarith
    have hp : 0 < ((nu1 + nu2) - 2) * (y ^ 2 - 4 * y + 1) :=
      mul_pos_of_neg_of_neg hsneg hq
    nlinarith
  have hsq1 : 0 ≤ nu1 ^ 2 := sq_nonneg nu1
  have hsq2 : 0 ≤ nu2 ^ 2 := sq_nonneg nu2
  have hprod : 0 ≤ nu1 * nu2 :=
    mul_nonneg hnu10 (le_of_lt hnu2pos)
  nlinarith

/-- The secant factor itself is positive in the frozen domain. -/
theorem H_secant_factor_pos
    {y nu1 nu2 : ℝ}
    (hyhalf : (1 / 2 : ℝ) < y)
    (hy1 : y < 1)
    (hnu10 : 0 ≤ nu1)
    (hnu12 : nu1 < nu2)
    (hnu2y : nu2 ≤ y) :
    0 <
      nu1 ^ 2 + nu1 * nu2 + nu2 ^ 2
        + 2 * (nu1 + nu2) * (y ^ 2 - 4 * y + 1)
        + y ^ 2 - 4 * y + 16 := by
  have hlower := H_secant_factor_lower_bound hyhalf hy1 hnu10 hnu12 hnu2y
  have hy2 : y - 2 ≠ 0 := by linarith
  have hbase : 0 < 5 * (y - 2) ^ 2 := by positivity
  exact lt_trans hbase hlower

/-- `H(y,nu)` is strictly increasing in `nu` on the frozen interval `[0,y]`. -/
theorem H_strict_increase_on_frozen
    {y nu1 nu2 : ℝ}
    (hyhalf : (1 / 2 : ℝ) < y)
    (hy1 : y < 1)
    (hnu10 : 0 ≤ nu1)
    (hnu12 : nu1 < nu2)
    (hnu2y : nu2 ≤ y) :
    H y nu1 < H y nu2 := by
  have hfactor := H_secant_factor_pos hyhalf hy1 hnu10 hnu12 hnu2y
  have hdelta : 0 < nu2 - nu1 := sub_pos.mpr hnu12
  have hprod :
      0 < (nu2 - nu1) *
        (nu1 ^ 2 + nu1 * nu2 + nu2 ^ 2
          + 2 * (nu1 + nu2) * (y ^ 2 - 4 * y + 1)
          + y ^ 2 - 4 * y + 16) :=
    mul_pos hdelta hfactor
  have hdiff := H_diff_factor y nu1 nu2
  nlinarith

/-- A root of `H(y,·)` exists strictly between `0` and `y`. -/
theorem exists_threshold_root
    {y : ℝ}
    (hyhalf : (1 / 2 : ℝ) < y)
    (hy1 : y < 1) :
    ∃ nuBar : ℝ, 0 < nuBar ∧ nuBar < y ∧ H y nuBar = 0 := by
  have hy0 : 0 < y := by linarith
  have hcont : Continuous (fun t : ℝ => H y t) := by
    unfold H
    fun_prop
  have himage :
      (0 : ℝ) ∈ (fun t : ℝ => H y t) '' Set.Icc 0 y := by
    apply intermediate_value_Icc (le_of_lt hy0) hcont.continuousOn
    exact ⟨le_of_lt (H_at_zero_neg hy0 hy1), le_of_lt (H_at_diag_pos hy0 hy1)⟩
  rcases himage with ⟨nuBar, hmem, hroot⟩
  rcases hmem with ⟨hbar0, hbary⟩
  have hbarpos : 0 < nuBar := by
    by_contra hnot
    have hbarle0 : nuBar ≤ 0 := le_of_not_gt hnot
    have hbareq : nuBar = 0 := le_antisymm hbarle0 hbar0
    subst nuBar
    have hneg := H_at_zero_neg hy0 hy1
    linarith
  have hbarlty : nuBar < y := by
    by_contra hnot
    have hybar : y ≤ nuBar := le_of_not_gt hnot
    have hbareq : nuBar = y := le_antisymm hbary hybar
    subst nuBar
    have hpos := H_at_diag_pos hy0 hy1
    linarith
  exact ⟨nuBar, hbarpos, hbarlty, hroot⟩

/-- Any two roots in `[0,y]` coincide. -/
theorem threshold_root_unique
    {y nu1 nu2 : ℝ}
    (hyhalf : (1 / 2 : ℝ) < y)
    (hy1 : y < 1)
    (hnu10 : 0 ≤ nu1)
    (hnu1y : nu1 ≤ y)
    (hroot1 : H y nu1 = 0)
    (hnu20 : 0 ≤ nu2)
    (hnu2y : nu2 ≤ y)
    (hroot2 : H y nu2 = 0) :
    nu1 = nu2 := by
  rcases lt_trichotomy nu1 nu2 with hlt | heq | hgt
  · have hinc := H_strict_increase_on_frozen hyhalf hy1 hnu10 hlt hnu2y
    rw [hroot1, hroot2] at hinc
    linarith
  · exact heq
  · have hinc := H_strict_increase_on_frozen hyhalf hy1 hnu20 hgt hnu1y
    rw [hroot2, hroot1] at hinc
    linarith

/--
For every frozen `y`, the threshold polynomial has exactly one root in `(0,y)`.
This is the formal version of the threshold-existence/uniqueness statement in P4.
-/
theorem exists_unique_threshold_root
    {y : ℝ}
    (hyhalf : (1 / 2 : ℝ) < y)
    (hy1 : y < 1) :
    ∃! nuBar : ℝ, 0 < nuBar ∧ nuBar < y ∧ H y nuBar = 0 := by
  rcases exists_threshold_root hyhalf hy1 with ⟨nuBar, hbar0, hbary, hroot⟩
  refine ⟨nuBar, ⟨hbar0, hbary, hroot⟩, ?_⟩
  intro nu hnu
  rcases hnu with ⟨hnu0, hnuy, hnuroot⟩
  exact threshold_root_unique hyhalf hy1
    (le_of_lt hnu0) (le_of_lt hnuy) hnuroot
    (le_of_lt hbar0) (le_of_lt hbary) hroot

/-- Below (or at) the unique root, the threshold polynomial is nonpositive. -/
theorem H_nonpos_of_le_root
    {y nuBar nu : ℝ}
    (hyhalf : (1 / 2 : ℝ) < y)
    (hy1 : y < 1)
    (hbar0 : 0 < nuBar)
    (hbary : nuBar < y)
    (hroot : H y nuBar = 0)
    (hnu0 : 0 ≤ nu)
    (hnu : nu ≤ nuBar) :
    H y nu ≤ 0 := by
  rcases lt_or_eq_of_le hnu with hlt | heq
  · have hinc := H_strict_increase_on_frozen hyhalf hy1 hnu0 hlt (le_of_lt hbary)
    rw [hroot] at hinc
    linarith
  · subst nu
    linarith

/-- Above the unique root, the threshold polynomial is strictly positive. -/
theorem H_pos_of_root_lt
    {y nuBar nu : ℝ}
    (hyhalf : (1 / 2 : ℝ) < y)
    (hy1 : y < 1)
    (hbar0 : 0 < nuBar)
    (hbary : nuBar < y)
    (hroot : H y nuBar = 0)
    (hbarlt : nuBar < nu)
    (hnuy : nu ≤ y) :
    0 < H y nu := by
  have hinc := H_strict_increase_on_frozen hyhalf hy1 (le_of_lt hbar0) hbarlt hnuy
  rw [hroot] at hinc
  exact hinc

/-- Sign characterization of `H` relative to the unique threshold. -/
theorem H_nonpos_iff_le_root
    {y nuBar nu : ℝ}
    (hyhalf : (1 / 2 : ℝ) < y)
    (hy1 : y < 1)
    (hbar0 : 0 < nuBar)
    (hbary : nuBar < y)
    (hroot : H y nuBar = 0)
    (hnu0 : 0 ≤ nu)
    (hnuy : nu ≤ y) :
    H y nu ≤ 0 ↔ nu ≤ nuBar := by
  constructor
  · intro hH
    by_contra hnot
    have hbarlt : nuBar < nu := lt_of_not_ge hnot
    have hpos := H_pos_of_root_lt hyhalf hy1 hbar0 hbary hroot hbarlt hnuy
    linarith
  · intro hle
    exact H_nonpos_of_le_root hyhalf hy1 hbar0 hbary hroot hnu0 hle

/-- Strict sign characterization above the threshold. -/
theorem H_pos_iff_root_lt
    {y nuBar nu : ℝ}
    (hyhalf : (1 / 2 : ℝ) < y)
    (hy1 : y < 1)
    (hbar0 : 0 < nuBar)
    (hbary : nuBar < y)
    (hroot : H y nuBar = 0)
    (hnu0 : 0 ≤ nu)
    (hnuy : nu ≤ y) :
    0 < H y nu ↔ nuBar < nu := by
  constructor
  · intro hH
    by_contra hnot
    have hnule : nu ≤ nuBar := le_of_not_gt hnot
    have hnonpos := H_nonpos_of_le_root hyhalf hy1 hbar0 hbary hroot hnu0 hnule
    linarith
  · intro hlt
    exact H_pos_of_root_lt hyhalf hy1 hbar0 hbary hroot hlt hnuy

end ThresholdExistenceUniqueness

end

end SSDI
