import SSDI.Core
import SSDI.Threshold
import SSDI.PolicySigns
import SSDI.Generality
import SSDI.Continuation
import SSDI.WelfareIdentities
import SSDI.PolicyObjective

/-!
# Kernel-dependency report

These commands make the proof dependencies of the main certified Lean targets
visible in clean CI logs. Any listed dependencies are standard Lean/mathlib
logical foundations; the project source declares no project-specific axioms.
-/

#print axioms SSDI.xPrivate_strict_decrease
#print axioms SSDI.private_argmax_nonincreasing
#print axioms SSDI.coordinated_argmax_nondecreasing
#print axioms SSDI.exists_unique_threshold_root
#print axioms SSDI.FppExpr_neg
#print axioms SSDI.Fp1Expr_nonneg_iff_le_threshold
#print axioms SSDI.policyObjective_eq_closed
#print axioms SSDI.foreclosureThreshold_neg
#print axioms SSDI.reentry_margin_pos
#print axioms SSDI.welfare_identity
#print axioms SSDI.efficient_minus_bertrand_identity
