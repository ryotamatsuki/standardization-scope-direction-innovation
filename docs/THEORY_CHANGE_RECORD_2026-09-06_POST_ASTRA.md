# Theory-Change Record — Post-Astra Rollback

Date: 2026-09-06

Trigger manuscript commit: `1fe07b574be9b5f9e47730f3c3ad85ca1fcb5d26`

Affected freeze: `SSDI-THEORY-FREEZE-2026-09-06-v1`

Canonical workflow: `ryotamatsuki/research-paper-workflow` v1.1, release SHA `488e5ab06c207909296a7564eaf9066f7f94319c`.

## Trigger

An independent hostile full-manuscript audit conducted after Stage 10 found that the quadratic baseline model and selective-standardization theorem survive, but three frozen/manuscript claims were not supportable as stated:

1. unconditional strict comparative statics for every increasing strictly concave innovation technology;
2. preservation of policy-objective strict concavity under sufficiently small `C^2` perturbations of the technology;
3. use of the term `first best` for a benchmark that retains decentralized Bertrand pricing and restricts the regulator to symmetric R&D allocation.

The audit also identified an unsupported convergence statement in the endogenous-total-R&D robustness discussion and minor proof/exposition gaps.

## Classification

This is a **bounded claim-scope repair**, not a change in the baseline game.

The following are unchanged:

- players and timing;
- baseline quadratic innovation technology;
- fixed R&D capacity;
- differentiated-Bertrand demand and pricing game;
- parameter region;
- private R&D equilibrium;
- selective-standardization threshold theorem.

The following freeze components require amendment before downstream production can again be canonical:

- robustness scope;
- welfare benchmark nomenclature and feasible set;
- contribution wording that contrasts decentralized selective scope with a purported unconstrained first best.

## Authorized rollback

Earliest affected canonical stage: **Stage 7 — Welfare / Generality / Institutional Validation**.

Authorized route:

`Stage 7R -> Stage 7.5R -> Stage 8R -> Stage 9R -> Stage 10R -> Stage 11`

No Stage 4/5 model reconstruction is authorized because the baseline equilibrium and headline selective-standardization theorem were independently re-derived and survived the hostile audit.

## Stage 7R repair scope

Authorized changes are limited to:

- replace general-technology strict global signs with global weak monotonicity plus strict interior comparative statics;
- withdraw generic `C^2` strict-concavity/uniqueness robustness of the policy problem;
- relabel the existing `first best` object as a coordinated symmetric-R&D benchmark with decentralized Bertrand pricing;
- withdraw the unproved steep-capacity-cost convergence/persistence claim for endogenous total R&D;
- restrict the fixed-allocation benchmark to symmetric fixed allocation;
- record minor downstream proof and provenance corrections.

## Prohibited changes

Until a new freeze is issued:

- no new strategic mechanism;
- no new demand system;
- no new policy instrument;
- no attempt to rescue the `first best` label by silently expanding the planner problem;
- no new robustness theorem inserted to replace the withdrawn claims;
- no alteration of the quadratic selective-standardization theorem.

## Freeze status

`SSDI-THEORY-FREEZE-2026-09-06-v1` remains an immutable historical record but is **not sufficient for further Stage 11 progression** because its headline wording includes the disputed `first best` claim.

A successor freeze must receive a new freeze ID at Stage 8R if Stage 7.5R authorizes continued full-paper investment.
