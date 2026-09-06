# Stage 7R — Post-Astra Welfare / Generality Repair

Date: 2026-09-06

Repository: `ryotamatsuki/standardization-scope-direction-innovation`

Trigger commit: `1fe07b574be9b5f9e47730f3c3ad85ca1fcb5d26`

Theory freeze under review: `SSDI-THEORY-FREEZE-2026-09-06-v1`

Canonical workflow authority for this rollback: `ryotamatsuki/research-paper-workflow`, version `v1.1`, release SHA `488e5ab06c207909296a7564eaf9066f7f94319c`.

## 1. Objective

Resolve the bounded welfare/generality defects found by the independent post-Stage-10 hostile audit without changing the frozen baseline game or adding a new mechanism.

The audit did **not** refute the quadratic baseline equilibrium or the selective-standardization theorem. It did establish that (i) the general-concave-technology claim was over-quantified, (ii) the claimed `C^2` robustness of policy-objective strict concavity was false, and (iii) the object called the first best was in fact a constrained coordinated-R&D benchmark that leaves Bertrand pricing decentralized and restricts planner R&D control to symmetric allocations.

## 2. Frozen facts carried forward

The following baseline objects survive and are not reopened in Stage 7R:

- timing: regulator scope `b`, firm R&D composition `x_i`, then differentiated-Bertrand prices;
- fixed firm R&D capacity `E` in the baseline;
- quadratic technology `g(r)=r-kappa r^2/2`;
- main parameter region `1/2 < y < 1`, `0 < nu < y`, plus all-history price regularity;
- unique interior private allocation in the quadratic baseline;
- `dx^F/db < 0` in the quadratic baseline;
- strict concavity of the quadratic reduced policy objective `F(b)`;
- the threshold theorem for selective standardization, including the necessary-and-sufficient condition `nu > bar_nu(y)` for a unique interior scope within the frozen region;
- the direct diffusion versus endogenous innovation-composition decomposition.

No new strategic mechanism is authorized.

## 3. Repair A — General concave innovation technology

For a differentiable, increasing, strictly concave innovation technology `g`, firm `i` solves

`max_{x in [0,E]} (1-nu*b) g(x) + g(E-x)`.

The objective has decreasing differences in `(x,b)` because the cross effect is `-nu g'(x) < 0`. Hence the unique private maximizer `x^F(b)` is globally **nonincreasing** in `b`.

The coordinated symmetric R&D benchmark solves

`max_{x in [0,E]} (1+b) g(x) + g(E-x)`.

This objective has increasing differences in `(x,b)` because the cross effect is `g'(x) > 0`. Hence the unique coordinated maximizer `x^S(b)` is globally **nondecreasing** in `b`.

Strict comparative statics require that the relevant maximizers remain interior over the interval under consideration. When both allocations are interior, the first-order conditions imply

`(1-nu*b) g'(x^F)=g'(E-x^F)`

and

`(1+b) g'(x^S)=g'(E-x^S)`,

and implicit differentiation yields the strict signs

`dx^F/db < 0 < dx^S/db`.

The original unconditional strict-sign statement is therefore withdrawn. Corner plateaus are admissible under general strictly concave technologies.

### Counterexample check

For `E=0.7`, `nu=0.5`, and `g(r)=10(1-exp(-r/10))`, the private optimum is at `x^F=0` whenever

`b >= 2(1-exp(-0.07)) = 0.135212360188...`,

and the coordinated symmetric optimum is at `x^S=E` whenever

`b >= exp(0.07)-1 = 0.072508181254...`.

Thus for, e.g., `b=0.2`, both comparative statics are flat at corners. This confirms that the repaired global claim must be weak monotonicity plus conditional strictness.

## 4. Repair B — Robustness of the selective-policy theorem

The claim that sufficiently small `C^2` perturbations of `g` preserve strict concavity of the induced policy objective is withdrawn.

The reason is structural: after substituting the endogenous R&D allocation, the second derivative of the policy objective depends on the second derivative of the allocation rule, and the latter depends on `g'''`. Closeness in `C^2` does not control this term.

The hostile audit's perturbation check is valid. Around the quadratic baseline at `E=0.7`, `nu=0.5`, `b=0.5`, the baseline curvature is

`F_0'' = -29744/60025 = -0.4955268638...`,

while an arbitrarily small `C^2` perturbation with a localized third derivative of magnitude `1000` changes the curvature by

`1000 * 158184/14706125 = 10.7563345205...`,

so the perturbed curvature is

`30179344/2941225 = 10.2608076567... > 0`.

Accordingly, Stage 7R retains **no claim of local uniqueness or strict concavity of the policy objective under generic `C^2` perturbations**. The exact selective-standardization theorem remains a quadratic-baseline theorem.

## 5. Repair C — Welfare benchmark taxonomy

The welfare identity evaluated at the symmetric differentiated-Bertrand equilibrium remains

`W(A,rho) = A^2 (3-2 rho) / ((2-rho)^2 (1+rho))`.

This is correctly derived as consumer surplus plus producer surplus for decentralized Bertrand quantities.

However, the benchmark in which the regulator chooses `b` and a common symmetric R&D composition `x` while leaving the price subgame at differentiated-Bertrand equilibrium is **not** the unconstrained first best.

The unconstrained efficient quantity under symmetric quality is

`q^FB = A/(1+rho)`,

with efficient surplus

`W_efficient^FB = A^2/(1+rho)`,

which exceeds the Bertrand-evaluated welfare by

`A^2 (1-rho)^2 / ((2-rho)^2 (1+rho)) > 0`.

In addition, the original planner problem restricted R&D allocation to the symmetric diagonal rather than proving that symmetry is without loss over `[0,E]^2`.

Therefore the surviving benchmark is renamed:

**coordinated symmetric-R&D benchmark with decentralized Bertrand pricing**.

Within that constrained benchmark, the existing calculation that complete standardization is optimal survives. Stage 7R makes **no claim about the unconstrained first-best policy**.

## 6. Repair D — Fixed-allocation benchmark

The surviving fixed-allocation result is explicitly restricted to a fixed **symmetric** common-R&D allocation `x_1=x_2=bar{x}`.

For `bar{x}>0`, symmetric quality is strictly increasing in `b`, so complete standardization is optimal. For `bar{x}=0`, scope is payoff-irrelevant.

No asymmetric fixed-allocation benchmark is claimed.

## 7. Repair E — Endogenous total R&D robustness

The only retained result is the conditional relative first-order condition

`(1-nu*b) g'(x) = g'(z)`

when firms can choose common and proprietary effort separately and the relevant optimum is interior.

This supports the interpretation that broader scope lowers the private relative return to common innovation. It does **not** by itself imply that an endogenous-capacity model converges to the fixed-`E` baseline when a capacity cost becomes steep, nor does it establish persistence or uniqueness of the selective-policy optimum.

The previous continuity/convergence claim is withdrawn pending a separately specified model and proof. No such extension is added in this repair.

## 8. Private versus social decision map after repair

| Object | Surviving result |
| --- | --- |
| Quadratic baseline private R&D | `dx^F/db < 0` globally in the frozen region |
| Quadratic coordinated symmetric R&D | `dx^S/db > 0` globally in the frozen region |
| General increasing strictly concave `g` | private allocation nonincreasing; coordinated symmetric allocation nondecreasing |
| General `g`, interior segment | strict opposite signs hold |
| Fixed positive symmetric R&D | complete standardization |
| Coordinated symmetric-R&D benchmark with Bertrand pricing | complete standardization |
| Decentralized endogenous R&D, quadratic baseline | unique interior scope iff `nu > bar_nu(y)` within the frozen region |
| Unconstrained first best | not solved; no claim |
| Generic `C^2` perturbations | no strict-concavity/uniqueness robustness claim |
| Endogenous total R&D | relative-return wedge only; no policy persistence claim |

## 9. Policy scope after repair

The central second-best statement is narrowed to the modeled instrument comparison:

- complete scope is optimal when the R&D composition is held fixed at a positive symmetric allocation;
- complete scope is also optimal when the regulator can directly coordinate the symmetric R&D composition but product-market pricing remains decentralized;
- when the regulator controls only scope and firms subsequently choose R&D composition privately, strong enough rivalry can make a unique selective scope optimal in the quadratic baseline.

This is a comparison of policy regimes inside the modeled differentiated-Bertrand environment. It is not a comparison with an unconstrained social planner that also controls quantities/prices and arbitrary asymmetric R&D allocations.

## 10. Institutional and empirical interpretation

No institutional primitive is changed in Stage 7R. Existing application language may be carried forward only as interpretation, not validation of the removed robustness claims.

The empirical prediction that broader scope shifts private innovation composition away from the common layer remains a **baseline-model** prediction. Outside the quadratic/interior region, the general-theory statement is weak monotonicity rather than an everywhere-strict response.

## 11. Remaining downstream repairs

The following are not new theory and must be synchronized after a new freeze is authorized:

1. Proposition 2 and surrounding prose must use weak global monotonicity plus conditional strictness for general `g`.
2. The robustness section must delete the generic `C^2` strict-concavity preservation claim.
3. The endogenous-total-R&D section must delete the unproved steep-cost convergence/policy-persistence claim.
4. The welfare section, abstract, introduction, conclusion, and any literature-positioning language must replace `first best` with the constrained benchmark name unless a true first-best problem is separately solved and verified.
5. Proposition 3 must say `fixed symmetric R&D allocation`.
6. The appendix must add KKT/corner language for the general technology and close the omitted price-boundary uniqueness argument.
7. The fixed R&D capacity cost should be identified as a policy-invariant constant if resource costs are discussed.
8. Provenance must be corrected to the user-designated workflow `v1.1` / release SHA `488e5ab06c207909296a7564eaf9066f7f94319c` during the reproducibility re-sync; the existing `v1.2` / `944e6ba...` entry is inconsistent with the designated canonical workflow.

## 12. Kill tests

- Welfare wedge disappears after correct accounting: **PASS** — it does not.
- Baseline selective-standardization theorem fails: **PASS** — it survives.
- Generality requires an invalid strict comparative static: **REPAIRED** — replaced by weak monotonicity plus interior strictness.
- Robustness requires unproved `C^2` curvature preservation: **REPAIRED** — claim withdrawn.
- Policy conclusion relies on a mislabeled first best: **REPAIRED AT THEORY-SCOPE LEVEL** — benchmark reclassified; manuscript synchronization remains downstream.
- Fixed-capacity interpretation requires an unproved endogenous-capacity theorem: **REPAIRED** — only the relative-return condition is retained.

## 13. Stage 7R verdict

`GO TO STAGE 7.5R`

The quadratic baseline mechanism, exact welfare accounting, and selective-standardization theorem survive. The required repair is a contraction of generality and benchmark claims, not a change to the baseline game.

## 14. Stage 7.5R contract

Stage 7.5R must decide whether the paper still supports full-paper investment under the narrower, accurate contribution statement. No new mechanism, new robustness extension, or new first-best theorem may be added there.

If Stage 7.5R returns `GO`, Stage 8R must issue an explicit amended freeze (new freeze ID) before Stage 9/10 are re-synchronized. The existing `SSDI-THEORY-FREEZE-2026-09-06-v1` must not be silently rewritten.
