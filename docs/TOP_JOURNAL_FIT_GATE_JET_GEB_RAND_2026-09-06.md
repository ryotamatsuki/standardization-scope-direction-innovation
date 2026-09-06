# JET vs GEB vs RAND — Three-Journal Top-Journal Architecture Gate

Date: 2026-09-06

Repository: `ryotamatsuki/standardization-scope-direction-innovation`

Working title at gate entry: *Standardization Scope and the Direction of Innovation*

Entry main SHA: `ba641614eb191928193f443d46d15d40af08b1d9`

Active theory freeze: `SSDI-THEORY-FREEZE-2026-09-06-v2`

Active workflow authority from Stage 9R onward: `ryotamatsuki/research-paper-workflow` v1.3, release commit `3e4e6a3f76d86058024d06f9710f942e21627386`.

This is a one-shot project-specific editorial gate inserted between Stage 9R and Stage 10R. It is not a new canonical workflow stage and has no authority to modify frozen theory. Its purpose is to decide whether the current paper should (i) remain on the v2 architecture and be built for RAND/IJIO/JIE positioning, (ii) reopen theory in order to pursue Journal of Economic Theory, or (iii) reopen theory in order to pursue Games and Economic Behavior.

## 1. Executive verdict

`RAND-DOMINANT — NO THEORY ROLLBACK`

The current SSDI paper should **not** be generalized inside the present project merely to create a plausible JET or GEB submission. The amount and type of generalization required for either journal would cross the v2 theory freeze and would no longer be a bounded top-journal upgrade. In the JET direction, abstraction away from technical standards would also move the paper materially closer to existing general theories of the direction of innovation, especially Bryan and Lemus (2017), thereby reducing rather than expanding the paper's novelty moat unless a genuinely new general theorem is found. In the GEB direction, the current strategic interaction is not itself the main contribution; obtaining a GEB-native contribution would require a materially richer game or a new game-theoretic result.

The current architecture is most naturally an industrial-organization / regulation / innovation-policy paper. RAND Journal of Economics is therefore the correct top-journal stretch architecture to build toward. This verdict does **not** predict acceptance at RAND. It means only that the highest-value next action is to strengthen the frozen v2 paper for a RAND-quality applied-micro theory standard rather than reopen the model to chase a different journal identity.

Authorized route after this gate:

`Stage 9R -> Top-Journal Fit Gate -> Stage 10R (v2 manuscript synchronization + v1.3 Figure/Table Architecture Gate)`

No theory rollback is authorized by this gate.

## 2. Current frozen contribution being evaluated

The active v2 contribution is the whole-game/result combination in which:

1. a regulator chooses continuous standardization scope `b`;
2. firms subsequently allocate fixed R&D capacity between common-layer and proprietary innovation;
3. broader scope raises transferability of common innovation to rivals;
4. the private relative return to common R&D falls because common innovation strengthens the competitor;
5. private common R&D therefore falls with scope in the quadratic baseline, while under general increasing strictly concave technology the private allocation is globally nonincreasing;
6. with fixed positive symmetric R&D, complete standardization is optimal;
7. in a coordinated symmetric-R&D benchmark with decentralized Bertrand pricing, complete standardization is optimal;
8. with decentralized endogenous R&D composition in the quadratic baseline, sufficiently strong rivalry generates a unique interior standardization scope.

The exact global policy theorem is deliberately quadratic-baseline specific. The v2 freeze contains no unconstrained first-best theorem, no generic `C^2` policy-curvature robustness claim, and no policy-persistence theorem with endogenous total R&D.

## 3. Journal scope check

### Journal of Economic Theory (JET)

Current official description checked on 2026-09-06: JET publishes original research on economic theory and describes itself as the most general-interest journal among those specializing in economic theory, emphasizing innovative theoretical work across fields.

Source: https://shop.elsevier.com/journals/journal-of-economic-theory/0022-0531

### Games and Economic Behavior (GEB)

Current official description checked on 2026-09-06: GEB is a general-interest journal devoted to advancing game theory and its applications. Its publication criterion is significant advancement of the frontiers of game theory or its applications; an applied IO paper is relevant when the application contributes to a general game-theoretic understanding.

Source: https://shop.elsevier.com/journals/games-and-economic-behavior/0899-8256

### RAND Journal of Economics (RAND)

Current official description checked on 2026-09-06: RAND publishes theoretical and empirical research in industrial organization and closely related topics, including regulation, organizations, contracts, and applied microeconomics.

Sources:
- https://www.rje.org/
- https://onlinelibrary.wiley.com/page/journal/17562171/homepage/productinformation.html

Current RAND content also confirms that parsimonious theory papers on competition and innovation remain journal-native. Examples checked for this gate include:
- Marc Bourreau, Bruno Jullien, and Yassine Lefouili, “Horizontal Mergers and Incremental Innovation,” RAND Journal of Economics, 2026.
- Alexandre de Corniere and Greg Taylor, “Data and Competition: A Simple Framework,” RAND Journal of Economics, 2025.

## 4. The critical JET collision test

The strongest reason **not** to generalize SSDI mechanically toward JET is the existence of Kevin A. Bryan and Jorge Lemus (2017), “The Direction of Innovation,” *Journal of Economic Theory*, 172, 247–272, DOI `10.1016/j.jet.2017.09.005`.

That paper already studies a general theory in which firms have a fixed number of researchers allocated across research projects and innovation direction is distorted by racing and underappropriation. It explicitly asks how innovation policy changes the direction of research and emphasizes that underappropriation can lead private innovative effort toward socially distorted research directions.

The current SSDI paper is distinct because its policy variable is the mandatory scope of a common technical standard, its common/proprietary R&D portfolio is embedded in a differentiated-product continuation game, and its key policy result is a reversal from complete scope under fixed symmetric R&D to selective scope under decentralized endogenous R&D composition.

However, if SSDI is abstracted into a generic statement of the form

`policy-controlled spillover exposure -> fixed research resource allocation -> underappropriation -> distorted innovation direction`,

then the distance from Bryan-Lemus becomes materially smaller. Therefore **generality is not monotone in novelty for this project**. A JET upgrade is worthwhile only if it produces a new general theorem that cannot be reduced to a special case or close reformulation of the Bryan-Lemus underappropriation/direction architecture.

A second JET benchmark is Acemoglu, Gancia, and Zilibotti (2012), “Competing Engines of Growth: Innovation and Standardization,” *Journal of Economic Theory*, 147, 570–601.e3, DOI `10.1016/j.jet.2010.09.001`. That paper has a very different dynamic-growth mechanism, but it means that “standardization and innovation” is itself already a JET-level theoretical topic. SSDI's novelty must therefore remain in its specific endogenous portfolio and selective-scope result, not in the broad pairing of standardization and innovation.

## 5. JET architecture test

### Current fit

`LOW`

The v2 paper has a clear mechanism, but the headline policy theorem relies on the quadratic baseline for global strict concavity and policy uniqueness. The general concave result is directional monotonicity only. This is not enough, by itself, to turn the paper into a general-interest economic theory contribution.

### What a credible JET transformation would require

A JET-native version would need a genuinely general theoretical object, for example a theorem characterizing policy-controlled spillover exposure and endogenous resource allocation under primitive conditions that do not depend on differentiated Bertrand demand or the quadratic innovation technology.

At minimum, such a transformation would have to deliver most of the following:

1. a general class of private allocation problems with policy-dependent spillover exposure;
2. a clean strategic or welfare wedge stated in primitives;
3. a nontrivial general policy theorem — not merely weak monotonicity of the private allocation;
4. conditions for interior versus corner policy, multiplicity, or uniqueness that survive beyond the quadratic example;
5. a precise novelty distinction from Bryan-Lemus (2017) and related innovation-direction theory;
6. standards as an application of the general theorem rather than the theorem itself.

The Astra audit already showed that the most natural generic strict-comparative-static and `C^2` policy-curvature claims fail. Therefore the JET transformation is not a minor extension of v2; it requires a new theorem architecture.

### Upgrade-cost classification

`MAJOR THEORY REDESIGN / POTENTIALLY SEPARATE PAPER`

### Gate decision for JET

`NO-GO AS AN IN-PROJECT GENERALIZATION`

If a future project discovers a genuinely new general theorem meeting the conditions above, it should begin as a separate theory architecture or an explicit rollback to the earliest affected stage, not as a silent extension of SSDI v2.

## 6. GEB architecture test

### Current fit

`LOW`

The current paper is a sequential policy game, but the game-theoretic structure is a vehicle for the IO mechanism rather than the source of the contribution. In the frozen private R&D problem, the key allocation distortion can be represented by a reduced objective in which policy changes the relative return to common innovation. The paper does not introduce a new equilibrium concept, game class, strategic-information problem, coalition structure, network game, or general result about strategic interaction.

Recent GEB papers confirm the relevant standard. For example, innovation-related papers in GEB are typically contributions to contest design, coordination, network formation, or another identifiable game-theoretic problem. The journal's own scope explicitly states that an IO application belongs when it advances general game-theoretic understanding.

Illustrative sources checked:
- Protopappas and Rietzke (2025), “Incentivizing variety in innovation contests with specialized suppliers,” GEB.
- Ballard and Boosey (2026), “Dynamic coordination with switching costs,” GEB.
- Mandel, Nguyen, and Dong-Xuan (2026), “Strategic formation of production networks,” GEB.

### What a credible GEB transformation would require

A GEB-native version would likely need at least one of:

1. a general strategic-allocation game in which firms' R&D choices interact directly and the equilibrium structure itself is novel;
2. endogenous network/coalition/compatibility formation with a new equilibrium or stability result;
3. incomplete information or dynamic strategic learning that creates a general game-theoretic phenomenon;
4. a new policy-as-game-design result that is useful outside technical standards.

These are not bounded robustness checks. They alter the strategic architecture and risk moving the paper into the territory of the author's separate standards-coalition projects.

### Upgrade-cost classification

`MAJOR GAME REDESIGN / DIFFERENT PAPER IDENTITY`

### Gate decision for GEB

`NO-GO AS AN IN-PROJECT GENERALIZATION`

## 7. RAND architecture test

### Current fit

`HIGH RELATIVE FIT / STRETCH QUALITY BAR`

RAND is the natural top-journal architecture because the paper's primitives and welfare question are intrinsically IO/regulation questions:

- a regulator chooses the scope of a technical standard;
- firms respond through endogenous innovation composition;
- product-market rivalry changes private appropriability;
- the policy instrument has a direct diffusion benefit and an indirect strategic innovation cost;
- optimal regulation can be selectively incomplete because the regulator controls scope but not private R&D composition.

This architecture does not need to be stripped of its institutional content to become more valuable. The opposite is likely true: standards scope, interoperability, appropriability, and innovation composition give the paper a concrete applied-micro identity that protects it from direct collision with more abstract innovation-direction theory.

### What RAND-quality strengthening requires

The next upgrade should be **expositional, proof-disciplined, and literature-disciplined**, not a new model architecture.

Stage 10R must therefore:

1. synchronize every manuscript claim to v2 and eliminate all stale first-best language;
2. explicitly add Bryan and Lemus (2017) to the innovation-direction literature boundary and explain why SSDI's policy-feedback theorem is different;
3. sharpen the distinction from Acemoglu, Gancia, and Zilibotti (2012), Llanes (2024), and compatibility/product-design papers;
4. state the broad mechanism in journal-neutral language — policy raises spillover exposure of one innovation margin and firms reallocate scarce inventive capacity — while making clear that only the weaker monotonicity result is general;
5. preserve the exact selective-scope uniqueness theorem as a quadratic-baseline result rather than overselling robustness;
6. close the remaining price-boundary and KKT exposition gaps;
7. use the workflow-v1.3 Figure/Table Architecture Gate to decide whether the rivalry-threshold region `nu > bar_nu(y)` requires a reproducible regime map and whether the private-versus-coordinated allocation wedge requires a second visual;
8. improve institutional motivation around scope choices in APIs/protocols/modular interfaces without treating examples as causal validation;
9. consider a title that foregrounds the novel portfolio mechanism and avoids sounding derivative of Bryan-Lemus's title. A strong candidate for Stage 10R consideration is **“Standardization Scope and Endogenous Innovation Portfolios.”** This is an exposition recommendation, not a frozen title change.

### Upgrade-cost classification

`BOUNDED STAGE-10R RECONSTRUCTION — NO THEORY ROLLBACK`

### Gate decision for RAND

`CONDITIONAL TOP-TARGET FIT`

RAND should remain a stretch target pending a clean Stage 11 hostile referee gate and Stage 12 journal positioning. If Stage 11 finds the quadratic/fixed-capacity dependence too narrow for RAND, the natural fallback remains an IO field-journal ladder rather than a JET/GEB redesign.

## 8. Three-journal comparison

| Criterion | JET | GEB | RAND |
|---|---|---|---|
| Journal-native question under current v2 | Low | Low | High |
| Current headline theorem meets journal identity | Low | Low | Medium/High for IO field, stretch for RAND |
| Generality needed beyond v2 | Very high | High | Moderate |
| New game-theoretic content needed | Not primary | Very high | Low |
| Novelty risk created by further abstraction | High | Medium | Low/Medium |
| Bounded upgrade possible inside Stage 10R | No | No | Yes |
| Theory rollback required if pursued | Yes | Yes | No |
| Recommended current-paper route | No | No | Yes, conditional |

## 9. Kill tests

### Kill test A — Can the current selective-policy theorem be stated as a general JET theorem without quadratic structure?

`FAIL`.

The general concave model currently proves directional monotonicity, not the global interior-policy threshold/uniqueness theorem.

### Kill test B — Does the current model yield a general game-theoretic result that is independently interesting outside the standards application?

`FAIL`.

The strategic game supports the IO mechanism but is not itself a new game-theoretic object.

### Kill test C — Would abstraction toward a generic innovation-direction model enlarge the novelty moat?

`FAIL`.

Bryan-Lemus (2017) makes the opposite risk salient: abstraction moves SSDI closer to established direction-of-innovation theory.

### Kill test D — Is the frozen standards/R&D portfolio mechanism naturally inside RAND's domain?

`PASS`.

The topic is directly industrial organization, innovation incentives, interoperability/standards, regulation, and applied microeconomics.

### Kill test E — Can the highest-value RAND upgrade be completed without theory drift?

`PASS`.

The major remaining work is v2 manuscript synchronization, literature positioning, proof exposition, and v1.3 exposition architecture.

## 10. Separate-paper fork condition

A JET or GEB project should be forked from SSDI only if a future result satisfies a high bar before manuscript work begins.

### JET fork trigger

A theorem can be stated in primitives without technical standards, differentiated Bertrand demand, or quadratic innovation, and it yields a nontrivial policy result beyond weak allocation monotonicity while remaining clearly distinct from Bryan-Lemus (2017).

### GEB fork trigger

A new strategic interaction, equilibrium structure, or design theorem is found that remains interesting after the technical-standard application is removed.

Until one of these triggers is satisfied, **do not mutate SSDI v2 to chase JET or GEB**.

## 11. Stage 10R contract created by this gate

This gate modifies the editorial contract, not the theory freeze.

Stage 10R proceeds under `SSDI-THEORY-FREEZE-2026-09-06-v2` and workflow v1.3, with these additional requirements:

1. include Bryan and Lemus (2017) in the closest-literature boundary;
2. explicitly distinguish AGZ (2012) dynamic standardization/growth from the present scope/portfolio mechanism;
3. preserve standards as the economically meaningful application rather than abstracting the paper into generic direction-of-innovation language;
4. frame the mechanism generally in prose but never imply a general policy theorem beyond the freeze;
5. consider retitling toward “Endogenous Innovation Portfolios” to sharpen distinctiveness;
6. complete the v1.3 Figure/Table Architecture Gate before finalizing the Introduction;
7. do not add new primitives, strategic stages, heterogeneous-player structure, dynamic R&D, endogenous total capacity, or new policy instruments;
8. route any desire to prove a JET/GEB-level general theorem back to the earliest affected theory stage or to a new repository.

## 12. Submission-strategy implication

The next question is **not** whether to submit to JET or GEB before RAND simply because they are financially cheaper to try. Journal order should follow contribution identity.

For the current SSDI paper, the rational top route after manuscript completion is:

`RAND stretch evaluation at Stage 12 -> if not justified, IO field-journal ladder`

JET and GEB are not recommended as cost-saving shots for the current architecture because the fit problem is substantive, not administrative.

## 13. Sources checked for this one-shot gate

1. Journal of Economic Theory official journal description, Elsevier, checked 2026-09-06.
2. Games and Economic Behavior official journal description, Elsevier, checked 2026-09-06.
3. RAND Journal of Economics official overview and submissions pages, checked 2026-09-06.
4. Bryan, Kevin A., and Jorge Lemus (2017), “The Direction of Innovation,” Journal of Economic Theory 172: 247–272.
5. Acemoglu, Daron, Gino Gancia, and Fabrizio Zilibotti (2012), “Competing Engines of Growth: Innovation and Standardization,” Journal of Economic Theory 147: 570–601.e3.
6. Bourreau, Marc, Bruno Jullien, and Yassine Lefouili (2026), “Horizontal Mergers and Incremental Innovation,” RAND Journal of Economics 57(1): 122–139.
7. de Corniere, Alexandre, and Greg Taylor (2025), “Data and Competition: A Simple Framework,” RAND Journal of Economics 56(4): 494–510.
8. Protopappas, Konstantinos, and David Rietzke (2025), “Incentivizing variety in innovation contests with specialized suppliers,” Games and Economic Behavior 153: 586–621.

## 14. Final routing verdict

`RAND-DOMINANT — NO THEORY ROLLBACK`

Proceed to **Stage 10R — v2 Manuscript Synchronization + workflow-v1.3 Figure/Table Architecture Gate**.

Do not reopen theory for JET or GEB inside the present SSDI project unless a new result independently satisfies the separate-paper fork conditions above.