import SSDI.Core

/-!
# General-technology order core for P2R

This file formalizes the revealed-preference / decreasing-differences logic
behind the repaired general-technology Proposition P2R on the paper's actual
choice domain `[0,E]`. It deliberately does not encode the complete theorem
that differentiability plus strict concavity implies existence/uniqueness of
the one-dimensional maximizers; those facts are supplied here as explicit
hypotheses and proved analytically in the paper.
-/

namespace SSDI

noncomputable section

/-- Private allocation objective for an arbitrary innovation technology. -/
def privateObjective (g : ℝ → ℝ) (E nu b x : ℝ) : ℝ :=
  (1 - nu * b) * g x + g (E - x)

/-- Coordinated symmetric allocation objective for an arbitrary innovation technology. -/
def coordinatedObjective (g : ℝ → ℝ) (E b x : ℝ) : ℝ :=
  (1 + b) * g x + g (E - x)

/-- Exact decreasing-differences identity used in the private P2R argument. -/
theorem privateObjective_scope_diff
    (g : ℝ → ℝ) (E nu b1 b2 x : ℝ) :
    privateObjective g E nu b2 x - privateObjective g E nu b1 x =
      (-nu * (b2 - b1)) * g x := by
  unfold privateObjective
  ring

/-- Exact increasing-differences identity used in the coordinated P2R argument. -/
theorem coordinatedObjective_scope_diff
    (g : ℝ → ℝ) (E b1 b2 x : ℝ) :
    coordinatedObjective g E b2 x - coordinatedObjective g E b1 x =
      (b2 - b1) * g x := by
  unfold coordinatedObjective
  ring

/--
Abstract revealed-preference core of the private global order theorem on
`[0,E]`. If `x1` and `x2` are unique maximizers at `b1<b2` and `g` is monotone
on the feasible R&D interval, the higher-scope private maximizer cannot lie to
the right.
-/
theorem private_argmax_nonincreasing
    {g : ℝ → ℝ} {E nu b1 b2 x1 x2 : ℝ}
    (hnu : 0 < nu)
    (hb : b1 < b2)
    (hx1 : x1 ∈ Set.Icc (0 : ℝ) E)
    (hx2 : x2 ∈ Set.Icc (0 : ℝ) E)
    (hg : MonotoneOn g (Set.Icc (0 : ℝ) E))
    (hmax1 : ∀ x ∈ Set.Icc (0 : ℝ) E,
      privateObjective g E nu b1 x ≤ privateObjective g E nu b1 x1)
    (hmax2 : ∀ x ∈ Set.Icc (0 : ℝ) E,
      privateObjective g E nu b2 x ≤ privateObjective g E nu b2 x2)
    (huniq1 : ∀ x ∈ Set.Icc (0 : ℝ) E,
      privateObjective g E nu b1 x = privateObjective g E nu b1 x1 → x = x1) :
    x2 ≤ x1 := by
  by_contra hnot
  have hx : x1 < x2 := lt_of_not_ge hnot
  have h1 := hmax1 x2 hx2
  have h2 := hmax2 x1 hx1
  have hg12 : g x1 ≤ g x2 := hg hx1 hx2 (le_of_lt hx)
  have hc : -nu * (b2 - b1) ≤ 0 := by nlinarith
  have hdelta :
      privateObjective g E nu b2 x2 - privateObjective g E nu b1 x2 ≤
        privateObjective g E nu b2 x1 - privateObjective g E nu b1 x1 := by
    rw [privateObjective_scope_diff, privateObjective_scope_diff]
    exact mul_le_mul_of_nonpos_left hg12 hc
  have hreverse :
      privateObjective g E nu b2 x1 - privateObjective g E nu b1 x1 ≤
        privateObjective g E nu b2 x2 - privateObjective g E nu b1 x2 := by
    linarith
  have _heq := le_antisymm hdelta hreverse
  have hf1eq :
      privateObjective g E nu b1 x2 = privateObjective g E nu b1 x1 := by
    linarith
  have hxeq := huniq1 x2 hx2 hf1eq
  linarith

/--
Abstract revealed-preference core of the coordinated global order theorem on
`[0,E]`. If `x1` and `x2` are unique maximizers at `b1<b2` and `g` is monotone
on the feasible R&D interval, the higher-scope coordinated maximizer cannot lie
to the left.
-/
theorem coordinated_argmax_nondecreasing
    {g : ℝ → ℝ} {E b1 b2 x1 x2 : ℝ}
    (hb : b1 < b2)
    (hx1 : x1 ∈ Set.Icc (0 : ℝ) E)
    (hx2 : x2 ∈ Set.Icc (0 : ℝ) E)
    (hg : MonotoneOn g (Set.Icc (0 : ℝ) E))
    (hmax1 : ∀ x ∈ Set.Icc (0 : ℝ) E,
      coordinatedObjective g E b1 x ≤ coordinatedObjective g E b1 x1)
    (hmax2 : ∀ x ∈ Set.Icc (0 : ℝ) E,
      coordinatedObjective g E b2 x ≤ coordinatedObjective g E b2 x2)
    (huniq1 : ∀ x ∈ Set.Icc (0 : ℝ) E,
      coordinatedObjective g E b1 x = coordinatedObjective g E b1 x1 → x = x1) :
    x1 ≤ x2 := by
  by_contra hnot
  have hx : x2 < x1 := lt_of_not_ge hnot
  have h1 := hmax1 x2 hx2
  have h2 := hmax2 x1 hx1
  have hg21 : g x2 ≤ g x1 := hg hx2 hx1 (le_of_lt hx)
  have hc : 0 ≤ b2 - b1 := by linarith
  have hdelta :
      coordinatedObjective g E b2 x2 - coordinatedObjective g E b1 x2 ≤
        coordinatedObjective g E b2 x1 - coordinatedObjective g E b1 x1 := by
    rw [coordinatedObjective_scope_diff, coordinatedObjective_scope_diff]
    exact mul_le_mul_of_nonneg_left hg21 hc
  have hreverse :
      coordinatedObjective g E b2 x1 - coordinatedObjective g E b1 x1 ≤
        coordinatedObjective g E b2 x2 - coordinatedObjective g E b1 x2 := by
    linarith
  have _heq := le_antisymm hdelta hreverse
  have hf1eq :
      coordinatedObjective g E b1 x2 = coordinatedObjective g E b1 x1 := by
    linarith
  have hxeq := huniq1 x2 hx2 hf1eq
  linarith

/--
FOC contradiction used for strict private ordering when two compared interior
optima coincide at the same `x`; positivity of the derivative is passed in
explicitly rather than smuggled into the conclusion.
-/
theorem private_same_interior_foc_impossible
    {gp : ℝ → ℝ} {nu b1 b2 x rhs : ℝ}
    (hnu : 0 < nu)
    (hb : b1 < b2)
    (hgp : 0 < gp x)
    (hfoc1 : (1 - nu * b1) * gp x = rhs)
    (hfoc2 : (1 - nu * b2) * gp x = rhs) :
    False := by
  have hpos : 0 < nu * (b2 - b1) * gp x := by positivity
  nlinarith

/-- Coordinated analogue of the interior-FOC contradiction. -/
theorem coordinated_same_interior_foc_impossible
    {gp : ℝ → ℝ} {b1 b2 x rhs : ℝ}
    (hb : b1 < b2)
    (hgp : 0 < gp x)
    (hfoc1 : (1 + b1) * gp x = rhs)
    (hfoc2 : (1 + b2) * gp x = rhs) :
    False := by
  have hpos : 0 < (b2 - b1) * gp x := by positivity
  nlinarith

end

end SSDI
