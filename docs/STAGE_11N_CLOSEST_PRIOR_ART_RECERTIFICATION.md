# Stage 11N — Closest Prior-Art Recertification

Date: 2026-09-21

Repository: `ryotamatsuki/standardization-scope-direction-innovation`

Branch: `stage11n-closest-prior-art-recertification`

Active theory freeze: `SSDI-THEORY-FREEZE-2026-09-10-v4`

Input workflow: `docs/CLOSEST_PRIOR_ART_INTEGRATION_WORKFLOW_2026-09-21.md`

## 1. Executive verdict

**DISTINCT BUT NARROW — RECERTIFIED**

The enlarged closest-prior-art set materially narrows the admissible novelty claim but does not absorb the paper's surviving result-level contribution.

The following claims are **not novel and must not be used as standalone contribution claims**:

- component commonality or platform sharing;
- a continuous or multi-component “how much to share” choice;
- commonality reducing product distinctiveness;
- standards/compatibility changing innovation incentives;
- scarce innovative resources being allocated across activities;
- endogenous direction of innovation;
- partial/selective standardization being optimal in some environment.

The surviving contribution boundary is:

```
regulator-chosen standardization scope
    -> cross-product transferability of common-layer innovation
    -> private common/proprietary R&D portfolio reallocation
    -> private/coordinated allocation wedge
    -> complete-to-selective policy-ranking reversal
```

More precisely, the distinctive result is the conjunction that:

1. product substitutability is held fixed while scope changes transferability of common-layer innovation;
2. firms allocate a fixed innovative capacity between common and proprietary activities after scope is chosen;
3. broader scope weakly decreases private common-layer R&D but weakly increases the coordinated symmetric common-layer allocation under general increasing strictly concave innovation technology;
4. complete scope is optimal for every fixed positive symmetric common-R&D allocation and under the coordinated symmetric-R&D benchmark;
5. nevertheless, with decentralized endogenous portfolio choice, the quadratic baseline yields an exact rivalry threshold above which the regulator chooses an interior selective scope.

No inspected closest paper contains this full architecture or the benchmark reversal in items 3–5.

## 2. Source hierarchy and audit standard

Priority was given to publisher pages, author/NBER versions, and bibliographic records tied to the published article.

Key source records inspected:

- Ghosh & Morita (2006), JEMS, DOI `10.1111/j.1530-9134.2006.00105.x`.
- Ghosh & Morita (2008), JJIE, DOI `10.1016/j.jjie.2007.05.001`; NBER Working Paper 13058 / author-conference version inspected for model details.
- Ghosh & Morita (2012), IJIO, DOI `10.1016/j.ijindorg.2011.07.003`.
- Desai et al. (2001), Management Science, DOI `10.1287/mnsc.47.1.37.10672`.
- Krishnan & Gupta (2001), Management Science, DOI `10.1287/mnsc.47.1.52.10665`.
- Bourreau & Doğan (2010/2011), *Component Sharing Through Licensing*, Communications & Strategies 77, 113–132; SSRN/public author metadata inspected.

Where full published text was not openly available, the audit does **not** claim a line-by-line published-version reconstruction. The novelty decision is bounded to the choice variables, mechanisms, and headline results established by the accessible publisher/author records.

## 3. Structured closest-prior-art matrix

| Paper | Who chooses commonality / collaboration? | Binary or continuous? | What changes directly? | Endogenous R&D / innovation composition? | Regulator chooses scope? | Partial scope/commonality result? | Collision with current contribution |
|---|---|---|---|---|---|---|---|
| Ghosh & Morita (2006) | competing manufacturers | platform-sharing choice | procurement cost and horizontal product differentiation | No fixed common/proprietary R&D portfolio | No | sharing may or may not be chosen depending on cost/competition conditions | **Adjacent, not absorbing** |
| Ghosh & Morita (2008) | firm(s), monopoly/duopoly | common platform choice | fixed platform-development cost and horizontal/vertical differentiation | No common/proprietary R&D allocation | No | platform sharing choice differs across market structures | **Adjacent, not absorbing** |
| Ghosh & Morita (2012) | subset of competitors | collaboration participation / structure | product distinctiveness, prices, cost saving, welfare | Collaboration can concern technology development in interpretation, but no fixed common/proprietary R&D portfolio mechanism in the reported model | No | partial collaboration among a subset of firms is central | **Important IJIO neighbor, not absorbing** |
| Desai et al. (2001) | multiproduct manufacturer | discrete design configurations (unique / premium-common / basic-common) | manufacturing cost, component quality/design, price premium/product differentiation | Design effort is endogenous, but not a two-firm fixed common-vs-proprietary R&D portfolio under spillover/transferability | No | optimizes among commonality configurations | **Closer than a background citation, not absorbing** |
| Krishnan & Gupta (2001) | multiproduct firm | platform adoption / product-planning choice | product positioning, over/underdesign, introduction sequence | No interfirm common/proprietary R&D portfolio under standard scope | No | platform appropriateness depends on market/product conditions | **Adjacent product-platform design literature** |
| Bourreau & Doğan (2010) | innovator/licensor | **multi-component / “how much to license”** | component commonality -> product differentiation -> post-licensing competition; entry and licensing terms in extensions | No fixed common/proprietary R&D portfolio reallocation after scope | No regulator; scope is chosen strategically by innovator/licensor | yes, smaller component sets can be strategically chosen | **Strongest collision on continuous scope; does not absorb portfolio-mediated policy reversal** |

## 4. Paper-by-paper adversarial findings

### 4.1 Ghosh & Morita (2006)

The paper explicitly studies the trade-off between component commonality/procurement savings and reduced horizontal product differentiation. Platform sharing is therefore an antecedent for the proposition that commonality can intensify downstream competition.

**What it kills:** any claim that this paper is the first to connect commonality/platform sharing to product-market competition or to welfare consequences.

**What remains distinct:** the current manuscript fixes product substitutability and changes the transferability/appropriability of innovation instead. The strategic margin is innovation composition, not product distinctiveness.

Verdict: `ADJACENT — NONABSORBING`.

### 4.2 Ghosh & Morita (2008)

The horizontal model makes the distinction especially clear: platform sharing saves fixed development cost while directly increasing the demand-system substitutability parameter. The vertical model similarly restricts quality differentiation. The authors also explicitly connect the platform-sharing literature to cooperative R&D/RJV work, while emphasizing product-differentiation restrictions as their own added channel.

**What it kills:** novelty claims based on “platform/common component sharing affects competition,” “platform sharing can help consumers,” or “commonality and R&D cooperation are related.”

**What remains distinct:** in the current manuscript `rho` is not changed by scope. Scope changes cross-product usability of common-layer innovation and therefore the relative return to common vs proprietary innovative effort.

Verdict: `CLOSE ADJACENT — NONABSORBING`.

### 4.3 Ghosh & Morita (2012)

This IJIO paper broadens competitor collaboration to shared value-creating activities such as technology development, product design, and distribution. Its reported mechanism is product distinctiveness: collaboration reduces distinctiveness among collaborators, can increase their distinctiveness relative to a non-collaborator, and changes pricing/welfare.

**What it kills:** any broad claim that collaboration in technology development and product design affecting competitive positioning is new.

**What remains distinct:** the current paper has a regulator-selected standard scope and an explicit common/proprietary innovation allocation after that policy choice. The current theorem compares private and coordinated portfolio responses and derives a scope-policy reversal, rather than a collaboration/distinctiveness welfare comparison.

Because this is an IJIO article, it is both strong audience-fit evidence and a reason to state the distinction explicitly in the IJIO manuscript.

Verdict: `IMPORTANT IJIO NEIGHBOR — NONABSORBING`.

### 4.4 Desai et al. (2001)

This paper is closer than a generic product-platform citation. A manufacturer first selects among commonality configurations and then chooses component design effort before pricing. It therefore combines commonality with endogenous design effort and market outcomes.

**What it kills:** any assertion that commonality has not previously been studied jointly with endogenous design choices.

**Why it still does not absorb:** the choice is a multiproduct design/commonality problem internal to a manufacturer. It does not contain a regulator choosing standard scope, rival-benefiting common-layer R&D transferability, a fixed common/proprietary R&D capacity allocation across competing firms, or the private-vs-coordinated portfolio reversal.

Verdict: `CLOSE DESIGN-CHOICE NEIGHBOR — NONABSORBING`.

### 4.5 Krishnan & Gupta (2001)

The paper studies platform-based product development within a product family and shows that platform use affects product positioning, over/underdesign, and introduction strategy.

**What it kills:** broad novelty claims about product platforms changing optimal product positioning or design decisions.

**What remains distinct:** there is no scope-induced appropriability wedge between common and proprietary R&D across downstream rivals and no regulator policy problem matching the current manuscript.

Verdict: `ADJACENT — NONABSORBING`.

### 4.6 Bourreau & Doğan (2010)

This is the strongest newly identified collision. The innovator chooses the set of components licensed to a rival — explicitly “how much to license.” The chosen set determines product commonality and thereby post-licensing product differentiation and competition. Extensions add entry timing and licensing-contract structure.

**Material consequence for the current manuscript:** continuous or graded sharing scope is **not** novel. The manuscript must not contrast itself with prior work merely by saying that its scope variable is continuous.

**Why the current contribution survives:** Bourreau–Doğan's scope is a strategic licensing/component-sharing decision by an innovator, and the mechanism runs through product commonality/differentiation and licensing/entry incentives. It does not establish the current sequence of regulator scope -> transferability -> fixed common/proprietary R&D portfolio -> private/coordinated wedge -> complete-to-selective policy reversal.

Verdict: `STRONGEST COLLISION — PARTIAL CLAIM ABSORPTION, CORE RESULT NONABSORBING`.

## 5. Supporting R&D-spillover lineage

Ghosh & Morita (2008) themselves place platform sharing next to the cooperative-R&D/RJV literature, including Katz (1986), d'Aspremont–Jacquemin, Kamien–Muller–Zang (1992), Suzumura, Motta (1992), and Choi.

This means the current manuscript must not present the general idea

`spillovers / sharing -> weaker private R&D incentives`

as novel.

The safe distinction is the policy architecture and **directional portfolio wedge** between a common layer and a proprietary layer under regulator-chosen scope.

For manuscript integration, one or two canonical R&D-spillover citations are sufficient; there is no need to turn the paper into a survey.

## 6. Result-level collision tests

### Test N1 — continuous scope

**FAIL as novelty claim.**

Bourreau–Doğan already model “how much to license” through the set of shared components.

Action: remove/avoid any statement implying continuous scope by itself is novel.

### Test N2 — commonality changes differentiation and competition

**FAIL as novelty claim.**

Ghosh–Morita and Desai et al. clearly establish this family of mechanisms.

Action: treat as prior literature, not contribution.

### Test N3 — commonality plus endogenous design effort

**FAIL as broad novelty claim.**

Desai et al. endogenize component design effort after a commonality-configuration choice.

Action: contribution cannot be “commonality changes what firms invest/design.”

### Test N4 — regulator-selected scope changes common/proprietary innovation portfolio

**PASS against inspected set.**

No inspected closest paper combines regulator-selected scope with a post-policy fixed-capacity allocation between rival-benefiting common innovation and proprietary innovation.

### Test N5 — private and coordinated allocations move in opposite directions with scope

**PASS against inspected set.**

No inspected paper establishes the current global order comparison for the common/proprietary portfolio.

### Test N6 — complete-to-selective policy-ranking reversal

**PASS against inspected set.**

No inspected paper contains the current benchmark structure:

`b_FIX = b_COORD = 1` but `b_DEC < 1` above an exact rivalry threshold because of endogenous portfolio reallocation.

### Test N7 — exact rivalry threshold in the quadratic differentiated-Bertrand baseline

**PASS against inspected set, conditional on current bounded claim.**

The threshold remains a model-specific characterization, not a general-theory contribution.

## 7. Required manuscript changes for Stage 13R

If Stage 12R keeps IJIO as the target, Stage 13R must:

1. add the six closest papers to the bibliography where publication metadata is verified;
2. create a platform/component-commonality paragraph in Related Literature;
3. explicitly concede that continuous sharing scope is not new;
4. distinguish:
   - prior literature: commonality -> cost/product distinctiveness/product positioning;
   - current paper: standard scope -> transferability/appropriability -> innovation portfolio;
5. preserve the model sentence that scope does not directly alter product substitutability and add one bounded sentence explaining that this isolates the portfolio channel from the product-distinctiveness channel;
6. preserve the abstract by default;
7. center the contribution paragraph on the private/coordinated portfolio wedge and complete-to-selective policy reversal;
8. add at most a bounded conclusion sentence clarifying the distinction.

No theory, theorem, proof, threshold, welfare formula, Lean source, or theorem certificate change is authorized by this Stage 11N result.

## 8. Change-control determination

Scientific theory delta from `SSDI-THEORY-FREEZE-2026-09-10-v4`: **NONE**.

Novelty-positioning delta: **MATERIAL BUT BOUNDED**.

The old phrase-level contribution boundary is narrowed because continuous scope and commonality/design interactions are more clearly pre-existing than the manuscript's current bibliography indicates.

No rollback to Stage 4/7.5/8 is required.

The correct next step is **Stage 12R — Journal Positioning Recertification**.

## 9. Final Stage 11N verdict

`DISTINCT BUT NARROW — RECERTIFIED`

Unresolved fatal prior-art collision: **0**.

Unresolved major result-level absorption: **0**.

Material claim narrowing required: **YES**.

Strongest collision: **Bourreau & Doğan (2010)** on graded/component-set sharing scope.

Most important IJIO-neighbor citation: **Ghosh & Morita (2012)**.

Next mandatory stage: **Stage 12R — Journal Positioning Recertification**.
