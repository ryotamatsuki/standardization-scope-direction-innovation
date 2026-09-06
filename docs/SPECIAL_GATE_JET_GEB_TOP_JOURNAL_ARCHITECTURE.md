# Special Gate — JET vs GEB Top-Journal Architecture

Date: 2026-09-06

Repository: `ryotamatsuki/standardization-scope-direction-innovation`

Starting `main`: `ba641614eb191928193f443d46d15d40af08b1d9`

Active theory freeze: `SSDI-THEORY-FREEZE-2026-09-06-v2`

Canonical workflow in force: `ryotamatsuki/research-paper-workflow` v1.3, release commit `3e4e6a3f76d86058024d06f9710f942e21627386`.

This is a one-shot special architecture gate inserted after Stage 9R and before Stage 10R. It does not modify the theory freeze or canonical stage numbering.

RAND Journal of Economics is outside this gate by explicit project instruction and is not evaluated.

## 1. Executive verdict

`KEEP SSDI v2 — DO NOT ROLLBACK FOR JET/GEB — PROCEED TO STAGE 10R`

The present SSDI architecture is not a natural Journal of Economic Theory or Games and Economic Behavior paper in its current form. Raising it to either journal would require a substantive architecture change rather than a bounded generalization. Such a change would reopen the mechanism/model stages and would materially alter the identity of the current paper.

Among the two possible top-theory directions, JET is the more plausible sequel architecture. GEB is materially less natural because the current R&D allocation stage has very limited strategic best-response interaction across firms.

The recommended strategy is therefore:

1. preserve `SSDI-THEORY-FREEZE-2026-09-06-v2`;
2. complete Stage 10R and the current SSDI paper without adding a new mechanism;
3. if a top-theory follow-on is pursued, create a separate general-theory project oriented first toward JET;
4. do not retrofit GEB-oriented strategic interaction into SSDI.

## 2. Journal criteria used in the gate

### Journal of Economic Theory

JET describes itself as publishing original research on economic theory and as the most general-interest journal among journals specializing in economic theory. It emphasizes innovative theoretical work across fields rather than a narrow application-specific result.

Official journal page:
`https://shop.elsevier.com/journals/journal-of-economic-theory/0022-0531`

A useful architecture benchmark is Hoppe and Lehmann-Grube, "Innovation timing games: a general framework with applications" (JET, 2005), which contributes a general analytical framework and then applies it to innovation problems rather than presenting only an industry-specific special case.

### Games and Economic Behavior

GEB describes itself as a general-interest journal devoted to advancing game theory and its applications, with the publication criterion that papers significantly advance the frontiers of game theory or its applications. Its own description explicitly notes that an industrial-organization application is suitable only when it contributes to a broader game-theoretic issue.

Official journal page:
`https://shop.elsevier.com/journals/games-and-economic-behavior/0899-8256`

Relevant architecture precedents include:

- Amir and Wooders, "One-Way Spillovers, Endogenous Innovator/Imitator Roles, and Research Joint Ventures" (GEB, 2000), using submodularity to obtain a general R&D-game analysis;
- Amir, Evstigneev, and Wooders, "Noncooperative versus cooperative R&D with endogenous spillover rates" (GEB, 2003), which deliberately generalizes the product-market stage and spillover environment;
- Baye and Hoppe, "The strategic equivalence of rent-seeking, innovation, and patent-race games" (GEB, 2003), whose contribution is a game-theoretic equivalence result rather than the innovation application alone.

These are benchmarks for architecture, not claims about required citation or novelty priority.

## 3. Current SSDI architecture

The current paper studies:

1. regulator chooses standardization scope `b`;
2. two firms allocate fixed capacity `E` between common R&D `x_i` and proprietary R&D `E-x_i`;
3. firms compete in differentiated Bertrand prices.

The baseline private R&D problem reduces to

`max_x (1-nu b) g(x) + g(E-x)`.

In the quadratic baseline,

`x^F(b)=(y-nu b)/[kappa(2-nu b)]`

and

`dx^F/db<0`.

For general increasing strictly concave `g`, the verified general result is only global weak monotonicity of the private allocation in `b`, with strictness conditional on interiority.

The exact selective-standardization theorem — unique interior scope iff rivalry exceeds `bar_nu(y)` — is proved only for the quadratic baseline.

## 4. JET fit audit

### Current-form fit

Verdict: `NO-GO AS CURRENTLY ARCHITECTED`.

The present paper has a clear IO mechanism and a sharp baseline theorem, but its most general result is a standard monotone-comparative-statics statement and its strongest policy characterization relies on the quadratic specification. That is not yet a general economic-theory architecture of the sort normally needed to make the standards application secondary to the theorem.

### What a genuine JET upgrade would require

A credible JET architecture would need to recast the paper around a general object such as:

`policy-controlled externality exposure -> endogenous allocation between transferable and privately appropriable activities`.

At minimum, that architecture would need new general results at the primitive level. Examples of the required theorem class are:

1. a general allocation theorem under decreasing/increasing differences establishing the private/social directional wedge;
2. a general policy theorem identifying primitive sufficient or necessary-and-sufficient conditions under which a policy with a positive direct effect is optimally incomplete because of the endogenous allocation response;
3. a result that does not depend on linear differentiated demand or the quadratic `g` merely to obtain interior policy existence;
4. preferably a characterization in economically interpretable elasticities, cross-partials, or curvature conditions rather than one polynomial threshold tied to the baseline specification;
5. applications such as technical standards presented after, rather than defining, the general theorem.

### Why this is not a bounded SSDI repair

The Astra audit already established that generic `C^2` perturbations do not preserve the strict concavity/uniqueness property used by P4 and that general concave technology only supports weak global monotonicity. Therefore a JET upgrade cannot be obtained by simply replacing quadratic notation by a generic `g`.

It would require discovering a new set of primitive restrictions and proving a new policy theorem. That changes the theoretical contribution and would require rollback to at least the mechanism/minimal-model/hardening sequence, a new novelty audit, and a new theory freeze.

Classification: `SEPARATE GENERAL-THEORY ARCHITECTURE`, not Stage-10 exposition repair.

### JET sequel potential

Verdict: `PROMISING`.

The most promising new-paper architecture is a general theory of policy-controlled spillovers and endogenous resource allocation. The standards model can then serve as one application or implementation.

This route should be pursued only as a separate project unless a later proof discovery shows that the general policy theorem can be added without changing SSDI's central primitives and contribution identity.

## 5. GEB fit audit

### Current-form fit

Verdict: `NO-GO AS CURRENTLY ARCHITECTED`.

The current model is a sequential game, but the core R&D allocation problem has very weak strategic interaction at the allocation stage. Firm `i`'s private objective for `x_i` reduces to a problem whose marginal condition does not require the rival's chosen R&D allocation as a strategic state variable. The central result is therefore primarily an IO policy/incentive result rather than a contribution to the theory of strategic interaction.

### What a genuine GEB upgrade would require

A credible GEB architecture would likely require at least one new strategic object, for example:

- R&D best responses that genuinely depend on rivals' R&D choices;
- endogenous spillover/compatibility choices by firms;
- heterogeneous players with endogenous specialization roles;
- network or coalition formation over common technological layers;
- a strategic-equivalence, supermodularity/submodularity, potential-game, or equilibrium-selection theorem of independent game-theoretic interest;
- an `n`-player characterization in which strategic structure, not the standards application, drives the main theorem.

These additions are not innocuous robustness checks. They create a different game.

Classification: `NEW MECHANISM / NEW PAPER`.

### GEB sequel potential

Verdict: `LOWER THAN JET ROUTE`.

A GEB sequel is possible, but it would require deliberately redesigning the R&D stage around strategic interaction. That would move substantially away from the current paper's clean policy-controlled appropriability mechanism.

## 6. Comparative architecture verdict

| Dimension | JET route | GEB route |
|---|---|---|
| Current v2 fit | low | very low |
| Can current P4 carry the paper? | no | no |
| Required upgrade | general economic-theory theorem | new strategic game structure |
| Small/bounded extension? | no | no |
| Earliest likely rollback | Stage 3/4 or earlier | Stage 3/4 or earlier |
| Risk of destroying current SSDI identity | high | very high |
| Value as separate sequel | high | moderate |
| Preferred top-theory direction | **first** | second |

## 7. Kill tests

### Test A — Can the journal upgrade be achieved only by generalizing `g`?

`FAIL` for both journals.

The repaired general-technology result is economically useful but too weak to turn the paper into a top general-theory contribution.

### Test B — Can the policy theorem be made general without new substantive restrictions or theorems?

`FAIL` on current evidence.

The post-Astra audit showed that policy curvature/uniqueness is not generically stable under the previously claimed perturbation class.

### Test C — Is the R&D subgame itself a sufficiently rich strategic game for GEB?

`FAIL`.

The core allocation response is driven by the policy-dependent private appropriability coefficient rather than a rich cross-player best-response system.

### Test D — Would the required upgrade remain recognizably the same paper?

`FAIL` for GEB; `AT BEST UNCERTAIN` for JET.

A successful JET architecture would likely make standards an application of a broader theorem. A successful GEB architecture would require changing the game itself.

### Test E — Does delaying Stage 10R create positive option value?

`NO` after this gate.

The gate has identified no bounded high-return theory upgrade worth inserting before manuscript synchronization.

## 8. Routing decision

`NO THEORY ROLLBACK`.

Proceed with the existing SSDI paper under:

- active freeze `SSDI-THEORY-FREEZE-2026-09-06-v2`;
- workflow v1.3;
- Stage 10R manuscript synchronization and Figure/Table Architecture Gate.

Do not add a JET/GEB-motivated theorem, strategic interaction, endogenous spillover choice, heterogeneity, or multi-player extension inside Stage 10R.

If a general-theory project is opened, it should be a separate repository and start at Stage 0. Preferred candidate architecture:

`Policy-Controlled Spillovers and the Endogenous Allocation of Scarce Innovative Effort`.

The first target to test for that separate architecture is JET, not GEB.

## 9. Status of current paper after gate

The special gate does not weaken or amend v2. It only answers whether the current project should be reopened before Stage 10R for the purpose of targeting JET or GEB.

Final answer: **no**.

## 10. Final verdict

`KEEP SSDI v2 — PROCEED TO STAGE 10R`

JET-oriented generalization: `SEPARATE-PAPER CANDIDATE`.

GEB-oriented redesign: `DO NOT PURSUE INSIDE SSDI`.
