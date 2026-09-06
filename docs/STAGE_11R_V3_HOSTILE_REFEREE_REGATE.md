# Stage 11R — v3 Hostile Full-Manuscript Referee Re-Gate

Date: 2026-09-06

Repository: `ryotamatsuki/standardization-scope-direction-innovation`

Starting remote `main`: `4d221158ed9d1b3375a8a5e970ea9e6f5cd2afcd`

Active freeze: `SSDI-THEORY-FREEZE-2026-09-06-v3`

Workflow authority: `ryotamatsuki/research-paper-workflow` v1.3, release commit `3e4e6a3f76d86058024d06f9710f942e21627386`.

Templates/checklists applied:

- `templates/STAGE_11_REFEREE_GATE.md`;
- `checklists/REFEREE_ATTACK_CHECKLIST.md`;
- `checklists/EQUILIBRIUM_CONTINUATION_CHECKLIST.md`.

This is the repeated Stage-11 gate required by the Stage-7R2 rollback. It audits the full v3 manuscript rather than merely confirming the repaired sentence.

## 1. Executive referee-gate verdict

`GO TO JOURNAL POSITIONING`

No unresolved fatal or major defect remains. The Stage-11 defect that triggered the v2 rollback is closed: P2R is now an order-comparative-statics theorem, uses no `g''`, and adds no hidden smoothness assumption. Independent re-derivation also leaves P1, P3R, P4, P5R, the welfare formulas, and the global pure-price continuation intact.

The surviving contribution remains **distinct but narrow**. This is a Stage-12 positioning constraint, not a correctness blocker.

## 2. Referee A — novelty and mechanism

### Attack A1 — classic innovation-direction result in new notation

- Severity: `MINOR / SURVIVED`
- Evidence: Bryan and Lemus (2017), *The Direction of Innovation*, JET 172, 247–272, already studies scarce research resources, underappropriation, and distorted innovation direction. Its trade-expansion application holds the aggregate measure of science fixed but changes market size, endogenous entry, and research competition.
- Current response: the manuscript now explicitly concedes that scarce-resource allocation, underappropriation, and endogenous innovation direction are not novel. The present policy object instead changes cross-product transferability inside a fixed two-firm common/proprietary portfolio and then optimizes the standard scope itself.
- Required fix: none before Stage 12.
- Theory reopening: no.
- Resolved: yes.

### Attack A2 — standardization/innovation second-best already exists

- Severity: `MINOR / SURVIVED`
- Evidence: Acemoglu, Gancia, and Zilibotti (2012), *Competing Engines of Growth: Innovation and Standardization*, JET 147, 570–601.e3, already characterizes welfare-maximizing standardization in a dynamic growth model and shows that standardization can both promote and impede growth.
- Current response: the manuscript no longer claims that “second-best restriction of standardization” is novel. Its claimed result is the scope → portfolio → policy-reversal architecture and the exact rivalry threshold in the quadratic differentiated-Bertrand environment.
- Required fix: none.
- Theory reopening: no.
- Resolved: yes.

### Attack A3 — technical standards already affect innovation incentives

- Severity: `MINOR / SURVIVED`
- Evidence: Llanes (2024), *Innovation Incentives in Technical Standards*, IJIO 93, 103046, studies development and inclusion of complementary technologies, patent pools, price caps, and cooperative R&D. Heywood, Wang, and Ye (2022) study R&D rivalry with endogenous compatibility. Da Silva (2024) studies internal/external R&D allocation under spillovers and scarce managerial resources.
- Current response: none contains the same regulator-selected continuous scope followed by a fixed common/proprietary portfolio and the complete-to-selective scope reversal with an exact rivalry threshold.
- Required fix: none.
- Theory reopening: no.
- Resolved: yes.

### Attack A4 — contemporaneous literature gap

- Severity: `MINOR`
- Evidence: Bergeaud, Schmidt, and Zago (2026), *Patents that Match your Standards: Firm-level Evidence on Competition, Innovation and Growth*, provides recent empirical evidence that standardization creates a common technological basis and that R&D responses vary with competition. Nabin (2023) studies an SSO, product quality, and process R&D.
- Current response: these are adjacent empirical/institutional references, not result-level theorem collisions.
- Required fix: consider citation during journal-specific integration if useful; not required for Stage-11 passage.
- Theory reopening: no.
- Resolved: not a gate blocker.

### Novelty verdict

`DISTINCT BUT NARROW`

The threshold does conceptual work: the existence of an adverse portfolio response alone does not imply incomplete scope. Low competitive penalty still yields complete standardization, whereas sufficiently strong rivalry crosses a unique threshold into selective scope. The coefficients of `H(y,nu)` are not themselves a general-theory contribution.

## 3. Referee B — assumptions and mathematics

### Attack B1 — repaired P2R still needs hidden C2 smoothness

- Severity: `FATAL IF TRUE / SURVIVED`
- Evidence: v3 Proposition 2 and Appendix.
- Independent result: for `b_2>b_1`,
  - `f_F(x,b_2)-f_F(x,b_1)=-nu(b_2-b_1)g(x)` is nonincreasing in `x`;
  - `f_S(x,b_2)-f_S(x,b_1)=(b_2-b_1)g(x)` is nondecreasing in `x`.
  Strict concavity gives unique maximizers and therefore the global weak order. If two compared interior optima were equal, the two FOCs at distinct `b` values would contradict `g'(x)>0`. Differentiability + monotonicity + strict concavity imply `g'(x)>0` at interior points. No `g''` is needed.
- Kill tests: repository tests include a corner-plateau technology and a differentiable strictly concave technology that is not twice differentiable at an interior point.
- Required fix: none.
- Theory reopening: no.
- Resolved: yes.

### Attack B2 — quadratic P1/P4 changed accidentally during repair

- Severity: `FATAL IF TRUE / SURVIVED`
- Independent re-derivation:
  - `x^F(b)=(y-nu b)/[kappa(2-nu b)]`;
  - `dx^F/db=-nu(2-y)/[kappa(2-nu b)^2]<0`;
  - `F''(b)=-nu(2-y)^2(2b nu^2+b nu+2nu+4)/(2-b nu)^4<0`;
  - `F'(0)=y(4-y)/8>0`;
  - `F'(1)=-H(y,nu)/[2(2-nu)^3]`.
- `H_nu=3nu^2+4nu(y^2-4y+1)+y^2-4y+16>5(y-2)^2>0` on `0<nu<y<1`; together with `H(y,0)<0<H(y,y)` this gives a unique threshold in `(0,y)`.
- A 200-draw independent policy grid/root audit found zero regime-classification failures.
- Required fix: none.
- Theory reopening: no.
- Resolved: yes.

### Attack B3 — result is built into the assumption

- Severity: `MINOR / SURVIVED`
- Evidence: scope enters common-layer transferability directly, so the private relative-return penalty is intentionally primitive. But the policy reversal is not assumed: direct diffusion is positive, fixed symmetric and coordinated-symmetric benchmarks choose `b=1`, and decentralized policy remains `b=1` below the rivalry threshold.
- Required fix: none.
- Resolved: yes.

### Attack B4 — all-history condition (R) is ad hoc

- Severity: `MINOR`
- Evidence: `(R)` bounds feasible quality ratios and is stronger than the conditions needed for positive candidate prices, active demand, and impossibility of nonnegative foreclosure deviations.
- Current response: the paper labels `(R)` as a sufficient global-continuation restriction, not as part of the economic mechanism. Since `a` can be sufficiently large relative to innovation increments, the condition is nonempty and transparent.
- Required fix: none before Stage 12.
- Theory reopening: no.
- Resolved: yes as a correctness issue.

## 4. Referee C — welfare and institution

### Attack C1 — welfare accounting error / transfer relabeling

- Severity: `FATAL IF TRUE / SURVIVED`
- Independent reconstruction at symmetric quality gives
  - `CS=A^2/[(2-rho)^2(1+rho)]`;
  - `PS=2A^2(1-rho)/[(2-rho)^2(1+rho)]`;
  - `W=A^2(3-2rho)/[(2-rho)^2(1+rho)]`.
- The efficient-quantity benchmark exceeds Bertrand welfare by `A^2(1-rho)^2/[(2-rho)^2(1+rho)]>0`.
- Required fix: none.
- Resolved: yes.

### Attack C2 — first-best conflation

- Severity: `MAJOR IF PRESENT / SURVIVED`
- Evidence: the coordinated benchmark retains Bertrand pricing and restricts R&D to the symmetric diagonal. The manuscript explicitly states that it is not an unconstrained first best and separately displays the Bertrand quantity gap.
- Required fix: none.
- Resolved: yes.

### Attack C3 — composition loss sign overstated

- Severity: `MINOR / RESOLVED BY v3`
- Evidence: the endogenous composition term is proportional to `b dx^F/db`; it is zero at `b=0` and strictly negative for `b>0` in the quadratic interior baseline. The manuscript now says exactly this.
- Required fix: none.
- Resolved: yes.

### Attack C4 — realized transfer confused with transferability

- Severity: `MINOR / SURVIVED`
- Evidence: the manuscript explicitly denies a theorem that `b g(x^F(b))` is globally increasing.
- Required fix: none.
- Resolved: yes.

### Attack C5 — institutional primitive too literal

- Severity: `MINOR`
- Evidence: `b` is a reduced-form scope/transferability object, not a literal legal disclosure share. API/protocol and modular-interface examples are interpretations only.
- Required fix: maintain this interpretation discipline at Stage 13; no new empirical validation is required for Stage 11.
- Resolved: yes as a gate issue.

## 5. Referee D — journal and exposition

### Attack D1 — contribution insufficient for a broad theory journal

- Severity: `MATERIAL POSITIONING CONSTRAINT, NOT A STAGE-11 FAILURE`
- Evidence: the general-technology result is directional allocation ordering; the exact interior-policy theorem remains quadratic and demand-specific. The earlier JET/GEB architecture gate therefore remains binding: no in-project JET/GEB redesign is authorized.
- Required fix: Stage 12 must select a journal for the contribution that actually survived; it must not generalize the theory merely to fit a preferred outlet.
- Theory reopening: no.
- Resolved: deferred appropriately to Stage 12.

### Attack D2 — Figure 1 overstates domain

- Severity: `MINOR / SURVIVED`
- Evidence: the figure plots only `1/2<y<1`, `0<nu<y`, uses the actual root of `H=0`, and the caption states that the theorem is quadratic-baseline only. The policy theorem remains conditional on `(R)` as stated in the proposition/model.
- Required fix: Stage 13 may add “conditional on (R)” to the caption for maximal self-containment, but this is not a Stage-11 blocker.
- Resolved: yes.

### Attack D3 — price-equilibrium uniqueness wording and mixed strategies

- Severity: `MINOR`
- Evidence: the paper analytically establishes the unique global **pure** active-price equilibrium and rules out pure boundary equilibria. The repeated audit does not independently establish absence of every possible nondegenerate mixed price equilibrium.
- Current response: this does not invalidate the constructed pure-strategy SPNE or the upstream calculations, but the literal phrase “unique global Nash equilibrium” can be read more broadly than the proof supplied.
- Required fix: during journal-specific copy integration, prefer “unique global pure-strategy Nash equilibrium” or explicitly state that the paper works in pure strategies. This is a claim-scope clarification, not a new economic assumption for the results actually used.
- Theory reopening: no.
- Resolved: not a correctness blocker for Stage 12.

## 6. Independent equilibrium / continuation re-audit

Equilibrium concept audited: the manuscript's pure strategy path implementing the stated SPNE.

Full upstream history domain:

- `b in [0,1]`;
- `(x_1,x_2) in [0,E]^2`;
- downstream prices `p_i>=0`;
- consumer quantities reconstructed from the nonnegative-quantity KKT problem rather than the manuscript's deviation evaluator.

### Analytic checks

For every feasible quality pair, `(R)` implies

`A_i/A_j < 2/[rho(3-rho^2)]`

and by reciprocity

`A_i/A_j > rho(3-rho^2)/2 > rho`.

This gives positive candidate prices and makes a zero-demand product able to profitably re-enter at a sufficiently small positive price, excluding separate pure one-active-product equilibria.

Against the candidate rival price, the price needed to foreclose the rival is

`p_i <= A_i-(A_j-p_j^*)/rho`.

Substitution gives a negative right-hand side iff

`A_i/A_j < 2/[rho(3-rho^2)]`,

so `(R)` rules out every nonnegative foreclosure deviation. A sufficiently large own-price deviation makes the deviator inactive and earns zero, while the candidate active profit is positive.

### Independent direct-payoff implementation

Added: `scripts/stage11_independent_continuation_audit.py`.

It reconstructs consumer allocation directly from the KKT active-set conditions and does not call `scripts/numerical_verify.py` or its price-profit evaluator.

Adversarial set:

- all eight combinations of `b in {0,1}`, `x_1 in {0,E}`, `x_2 in {0,E}`;
- the explicit asymmetric history `(b,x_1,x_2)=(1,0,E)`;
- 64 deterministic random feasible histories;
- for each history and each firm, 10,001 nonnegative deviation prices from zero to twice the larger quality intercept.

Explicit off-path history at the canonical parameters:

- `(b,x_1,x_2)=(1,0,E)`;
- `(A_1,A_2)=(10.182000,10.091000)`;
- `(p_1^*,p_2^*)=(2.170940,2.113249)`;
- direct KKT quantities `(q_1^*,q_2^*)=(4.677726,4.553418)`.

The search deliberately enters the deviator-inactive regime at high prices. No nonnegative foreclosure regime is reachable against the candidate continuation under `(R)`.

Continuation audit result:

- histories audited: 73;
- player-history deviation problems: 146;
- unresolved continuations: 0;
- numerical failures: 0;
- profitable finite deviations found: 0;
- pure boundary-equilibrium counterexamples found: 0;
- continuation-selection assumption needed: no for the pure continuation used by the paper.

Final continuation verdict: `PASS`.

## 7. Solver-failure / unresolved-continuation ledger

| Outcome class | Count |
|---|---:|
| `SOLVED_EQUILIBRIUM` / audited player-history cases | 146 |
| `SOLVED_NO_EQUILIBRIUM` | 0 |
| `MULTIPLE_EQUILIBRIA` | 0 in the audited pure-price problem |
| `UNRESOLVED` | 0 |
| `NUMERICAL_FAILURE` | 0 |

No `None`, NaN, exception, invalid branch, or failed convergence is converted into an “unprofitable deviation.” The independent audit fails closed if a KKT regime cannot be classified.

## 8. Consolidated severity table

| Attack | Severity after re-audit | Status |
|---|---|---|
| P2R hidden smoothness / derivative overclaim | FATAL if unresolved | **RESOLVED** |
| P1/P4 algebra or threshold failure | FATAL if present | **PASS** |
| Global pure price continuation | FATAL if unresolved | **PASS** |
| Welfare / first-best conflation | MAJOR if present | **PASS** |
| Bryan–Lemus result-level collision | MAJOR if identical | **SURVIVED — DISTINCT BUT NARROW** |
| AGZ generic second-best collision | MAJOR if contribution stated generically | **SURVIVED** |
| Functional-form dependence of P4 | MATERIAL limitation | **DISCLOSED** |
| `(R)` technical restriction | MINOR | **DISCLOSED** |
| Mixed-strategy uniqueness wording | MINOR | **OPEN COPY CLARIFICATION** |
| `(R)` in figure caption | MINOR | **OPTIONAL COPY CLARIFICATION** |
| 2026 adjacent empirical literature | MINOR | **STAGE-13 CANDIDATE CITATION** |

## 9. Required fixes

No theory or manuscript fix is required to begin Stage 12.

The following minor copy/positioning items are carried forward rather than used to block the gate:

1. clarify “unique global Nash equilibrium” as pure-strategy uniqueness unless a separate mixed-equilibrium proof is added;
2. optionally add “conditional on (R)” to the Figure-1 caption;
3. consider the 2026 Bergeaud–Schmidt–Zago evidence and Nabin (2023) during journal-specific literature integration.

None changes P1–P5R, the game, the welfare concept, or the contribution boundary.

## 10. Theory-change implications

`NO THEORY CHANGE AUTHORIZED OR REQUIRED.`

The active freeze remains `SSDI-THEORY-FREEZE-2026-09-06-v3`.

The repeated Stage-11 audit does not reopen Stage 7R2, Stage 8R, or Stage 10R.

## 11. Resolved vs unresolved attacks

Resolved:

- v2 P2R pointwise derivative overclaim;
- hidden `g''` use;
- corner/KKT concern for general `g`;
- P4 algebra/threshold/global optimum;
- fixed/coordinated benchmark nomenclature;
- welfare decomposition sign at `b=0`;
- endogenous-total-R&D claim scope;
- global pure price continuation;
- Bryan–Lemus and AGZ contribution boundary;
- figure mathematics.

Unresolved fatal attacks: `NONE`.

Unresolved major attacks: `NONE`.

Open minor copy/positioning items: three, listed in Section 9.

## 12. Verdict and Stage-12 contract

Final verdict:

`GO TO JOURNAL POSITIONING`

Stage 12 must position the paper that actually survived:

- a standards/IO policy paper with a fixed common/proprietary R&D portfolio;
- a general order-comparative-statics mechanism but a quadratic-baseline exact policy threshold;
- a result-level novelty claim, not a general theory of innovation direction or a generic theorem that partial standardization is optimal.

Stage 12 must not add new primitives, new strategic stages, generic policy-curvature claims, endogenous-total-R&D persistence, or a JET/GEB-motivated redesign. Journal selection should be based on the current contribution and its narrowness.
