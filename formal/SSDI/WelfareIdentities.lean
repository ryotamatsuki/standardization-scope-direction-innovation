import SSDI.Core

/-!
# Exact welfare identities

This file connects the paper's symmetric Bertrand price and quantity objects
directly to consumer surplus, producer surplus, total surplus, and the efficient
quantity benchmark. It protects the benchmark taxonomy used in P3R/P5R.
-/

namespace SSDI

noncomputable section

/-- Symmetric Bertrand price at common quality A. -/
def symmetricPrice (A rho : ℝ) : ℝ := A * (1 - rho) / (2 - rho)

/-- Symmetric Bertrand quantity at common quality A. -/
def symmetricQuantity (A rho : ℝ) : ℝ := A / ((2 - rho) * (1 + rho))

/-- Consumer surplus reconstructed from utility net of expenditure. -/
def consumerSurplusDirect (A rho : ℝ) : ℝ :=
  let p := symmetricPrice A rho
  let q := symmetricQuantity A rho
  2 * A * q - (1 + rho) * q ^ 2 - 2 * p * q

/-- Aggregate producer surplus at the symmetric zero-cost Bertrand outcome. -/
def producerSurplusDirect (A rho : ℝ) : ℝ :=
  2 * symmetricPrice A rho * symmetricQuantity A rho

/-- Total surplus reconstructed as CS+PS. -/
def welfareDirect (A rho : ℝ) : ℝ :=
  consumerSurplusDirect A rho + producerSurplusDirect A rho

/-- Efficient symmetric quantity when a planner controls quantities at fixed A. -/
def efficientQuantity (A rho : ℝ) : ℝ := A / (1 + rho)

/-- Efficient gross surplus at the symmetric efficient quantity. -/
def efficientWelfareDirect (A rho : ℝ) : ℝ :=
  let q := efficientQuantity A rho
  2 * A * q - (1 + rho) * q ^ 2

/-- Exact consumer-surplus identity in the manuscript. -/
theorem consumerSurplus_identity
    {A rho : ℝ}
    (hrho0 : 0 < rho)
    (hrho1 : rho < 1) :
    consumerSurplusDirect A rho =
      A ^ 2 / ((2 - rho) ^ 2 * (1 + rho)) := by
  have h2 : 2 - rho ≠ 0 := ne_of_gt (by linarith)
  have h1p : 1 + rho ≠ 0 := ne_of_gt (by linarith)
  unfold consumerSurplusDirect symmetricPrice symmetricQuantity
  dsimp
  field_simp [h2, h1p] <;> ring

/-- Exact aggregate producer-surplus identity in the manuscript. -/
theorem producerSurplus_identity
    {A rho : ℝ}
    (hrho0 : 0 < rho)
    (hrho1 : rho < 1) :
    producerSurplusDirect A rho =
      2 * A ^ 2 * (1 - rho) / ((2 - rho) ^ 2 * (1 + rho)) := by
  have h2 : 2 - rho ≠ 0 := ne_of_gt (by linarith)
  have h1p : 1 + rho ≠ 0 := ne_of_gt (by linarith)
  unfold producerSurplusDirect symmetricPrice symmetricQuantity
  field_simp [h2, h1p] <;> ring

/-- Exact total-surplus identity in the manuscript. -/
theorem welfare_identity
    {A rho : ℝ}
    (hrho0 : 0 < rho)
    (hrho1 : rho < 1) :
    welfareDirect A rho =
      A ^ 2 * (3 - 2 * rho) / ((2 - rho) ^ 2 * (1 + rho)) := by
  unfold welfareDirect
  rw [consumerSurplus_identity hrho0 hrho1, producerSurplus_identity hrho0 hrho1]
  have h2 : 2 - rho ≠ 0 := ne_of_gt (by linarith)
  have h1p : 1 + rho ≠ 0 := ne_of_gt (by linarith)
  field_simp [h2, h1p] <;> ring

/-- Exact efficient fixed-quality welfare identity. -/
theorem efficientWelfare_identity
    {A rho : ℝ}
    (hrho0 : 0 < rho)
    (hrho1 : rho < 1) :
    efficientWelfareDirect A rho = A ^ 2 / (1 + rho) := by
  have h1p : 1 + rho ≠ 0 := ne_of_gt (by linarith)
  unfold efficientWelfareDirect efficientQuantity
  dsimp
  field_simp [h1p] <;> ring

/-- The exact Bertrand quantity-control gap equals the Core expression. -/
theorem efficient_minus_bertrand_identity
    {A rho : ℝ}
    (hrho0 : 0 < rho)
    (hrho1 : rho < 1) :
    efficientWelfareDirect A rho - welfareDirect A rho = bertrandGap A rho := by
  rw [efficientWelfare_identity hrho0 hrho1, welfare_identity hrho0 hrho1]
  unfold bertrandGap
  have h2 : 2 - rho ≠ 0 := ne_of_gt (by linarith)
  have h1p : 1 + rho ≠ 0 := ne_of_gt (by linarith)
  field_simp [h2, h1p] <;> ring

end

end SSDI
