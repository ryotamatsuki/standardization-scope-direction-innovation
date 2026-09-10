import SSDI.Core

/-!
# Algebraic core of the global price continuation

This file formalizes the proof-critical inequalities used with condition (R)
in the paper's pure-strategy Bertrand continuation proof.  It does not encode
the full consumer KKT correspondence or exclude mixed-strategy equilibria.
Those model-boundary items are certified separately by the analytic Stage-4A
argument and the independent direct-KKT regression evaluator.
-/

namespace SSDI

noncomputable section

/-- Interior differentiated-Bertrand candidate price. -/
def candidatePrice (Ai Aj rho : ℝ) : ℝ :=
  ((2 - rho ^ 2) * Ai - rho * Aj) / (4 - rho ^ 2)

/-- Price threshold below which firm i would make rival j inactive. -/
def foreclosureThreshold (Ai Aj rho : ℝ) : ℝ :=
  Ai - (Aj - candidatePrice Aj Ai rho) / rho

/-- The active-region candidate solves firm i's linear price FOC. -/
theorem candidatePrice_foc
    {Ai Aj rho : ℝ}
    (hden : 4 - rho ^ 2 ≠ 0) :
    2 * candidatePrice Ai Aj rho - rho * candidatePrice Aj Ai rho =
      Ai - rho * Aj := by
  unfold candidatePrice
  field_simp [hden]
  ring

/-- On 0<rho<1, the common price denominator is strictly positive. -/
theorem price_den_pos
    {rho : ℝ}
    (hrho0 : 0 < rho)
    (hrho1 : rho < 1) :
    0 < 4 - rho ^ 2 := by
  nlinarith [sq_nonneg rho]

/-- Exact algebraic expression for the rival-foreclosure threshold. -/
theorem foreclosureThreshold_eq
    {Ai Aj rho : ℝ}
    (hrho : rho ≠ 0)
    (hden : 4 - rho ^ 2 ≠ 0) :
    foreclosureThreshold Ai Aj rho =
      (rho * (3 - rho ^ 2) * Ai - 2 * Aj) /
        (rho * (4 - rho ^ 2)) := by
  unfold foreclosureThreshold candidatePrice
  field_simp [hrho, hden]
  ring

/--
The upper cross-ratio inequality implied by (R) makes the foreclosure threshold
strictly negative, so no nonnegative own price can enter that regime against
the candidate continuation.
-/
theorem foreclosureThreshold_neg
    {Ai Aj rho : ℝ}
    (hrho0 : 0 < rho)
    (hrho1 : rho < 1)
    (hRupper : rho * (3 - rho ^ 2) * Ai < 2 * Aj) :
    foreclosureThreshold Ai Aj rho < 0 := by
  have hden : 0 < 4 - rho ^ 2 := price_den_pos hrho0 hrho1
  rw [foreclosureThreshold_eq (ne_of_gt hrho0) (ne_of_gt hden)]
  apply div_neg_of_neg_of_pos
  · linarith
  · positivity

/--
The opposite cross-ratio inequality implied by (R), together with positive
quality, implies Ai>rho Aj.  This is the positive re-entry margin used to rule
out pure equilibria with an inactive product.
-/
theorem reentry_margin_pos
    {Ai Aj rho : ℝ}
    (hrho0 : 0 < rho)
    (hrho1 : rho < 1)
    (hAj : 0 < Aj)
    (hRlower : rho * (3 - rho ^ 2) * Aj < 2 * Ai) :
    0 < Ai - rho * Aj := by
  have hrhosq : rho ^ 2 < 1 := by nlinarith
  have hfac : 2 < 3 - rho ^ 2 := by nlinarith
  have hrhoAj : 0 < rho * Aj := mul_pos hrho0 hAj
  have hmiddle : 2 * rho * Aj < rho * (3 - rho ^ 2) * Aj := by
    nlinarith
  nlinarith

/-- The candidate own-price numerator is positive under the re-entry margin. -/
theorem candidatePrice_numerator_pos
    {Ai Aj rho : ℝ}
    (hrho0 : 0 < rho)
    (hrho1 : rho < 1)
    (hAi : 0 < Ai)
    (hreentry : rho * Aj < Ai) :
    0 < (2 - rho ^ 2) * Ai - rho * Aj := by
  have hrhosq : rho ^ 2 < 1 := by nlinarith
  have hcoef : 1 < 2 - rho ^ 2 := by nlinarith
  nlinarith

/-- Hence the active candidate price is strictly positive. -/
theorem candidatePrice_pos
    {Ai Aj rho : ℝ}
    (hrho0 : 0 < rho)
    (hrho1 : rho < 1)
    (hAi : 0 < Ai)
    (hreentry : rho * Aj < Ai) :
    0 < candidatePrice Ai Aj rho := by
  unfold candidatePrice
  have hnum := candidatePrice_numerator_pos hrho0 hrho1 hAi hreentry
  have hden := price_den_pos hrho0 hrho1
  positivity

end

end SSDI
