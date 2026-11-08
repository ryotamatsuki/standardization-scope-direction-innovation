# Gate 1 / Gate 2 Independent Research Audit — 2026-11-08

**Baseline:** main@5a62e9228ef05e25290602c59ca1f560889098d2  
**Theory freeze:** SSDI-THEORY-FREEZE-2026-09-10-v4  
**Status:** exploratory research proposal; **NOT** part of the certified baseline. Main and the frozen paper remain unchanged.

## Gate 1 — Closest prior art

**CONDITIONAL PASS.** An important missing antecedent is Bourreau and Doğan (2010), *Cooperation in Product Development and Process R&D Between Competitors*, **IJIO** 28(2), 176–190, DOI 10.1016/j.ijindorg.2009.07.010. The Harvard author manuscript was inspected, including Propositions 3–5. Proposition 3 already proves that, under partial cooperation, the ratio of R&D in common versus proprietary components decreases with the scope of joint product development. Proposition 4 establishes competition-dependent investment rankings. Hence private R&D portfolio diversion and differentiated joint/in-house R&D are **not** novel in themselves.

The prior decision maker is a joint-profit-maximizing coalition of firms; cooperation scope also changes product differentiation. The SSDI result instead holds product substitutability fixed and asks when a welfare-maximizing scope-only regulator selects partial scope because of firms' endogenous portfolio choices, even though fixed/coordination benchmarks favor full scope. No exact counterpart of this benchmark policy reversal was found in the inspected Bourreau–Doğan (2010) propositions.

Other relevant antecedents: Bourreau–Doğan, *Component Sharing Through Licensing* (Communications & Strategies 2010/11, SSRN 1809722), already studies a continuous extent of component sharing. Ghosh–Morita (2006, 2008, 2012) studies platform commonality, differentiation, competition and welfare; Desai et al. (2001) endogenizes design choices; Llanes (2024, IJIO 93, 103046) studies standards, pools and price caps; Bryan–Lemus (2017, JET) studies distorted innovation direction under scarce researchers; Acemoglu–Gancia–Zilibotti (2012, JET) already finds constrained optimal standardization.

**Remaining material risk:** Kretschmer–Reitzig, *How Much to Integrate? Firms' Profit-Maximizing R&D Allocations in Emerging Standard Settings* (2012/13; DOI 10.2139/ssrn.2166219, AOM Proceedings DOI 10.5465/ambpp.2013.87), explicitly studies the joint-standard versus proprietary R&D allocation and reduced co-specialization when network effects increase. Its **33-page full text was not obtained**, so complete theorem-level non-collision is UNVERIFIED. Do not issue an unconditional novelty certificate.

## Gate 2 — Theorem A: selective standardization with general concave innovation

Let E>0. Assume g:[0,E]→R is continuous, strictly increasing and strictly concave, with **g(0)=0**. For b∈[0,1] and ν∈[0,1), let

- G(x) = g(x)+g(E−x);
- x_ν(b) = argmax_{0≤x≤E} [G(x)−ν b g(x)];
- Q_ν(b) = G(x_ν(b))+b g(x_ν(b)).

Strict concavity guarantees a unique private x_ν(b) and continuity of this policy response.

**Theorem A (candidate, analytic proof completed):** There exists ν₀(g,E)<1 such that for each ν∈(ν₀,1), **every global maximizer** of Q_ν(b) on [0,1] lies strictly between 0 and 1. By contrast, for any fixed positive symmetric common allocation, and in the constrained benchmark coordinating scope with symmetric R&D composition, the unique optimal scope is 1. At ν=0 the decentralized optimal scope is also 1. This asserts **existence of interior optima**, not uniqueness or a unique competition threshold.

**Proof (zero endpoint).** G is strictly concave and symmetric, so x_ν(0)=E/2 and Q_ν(0)=2g(E/2)>0. Write x_b=x_ν(b). Private optimality implies

G(x_b)−ν b g(x_b) ≥ G(E/2)−ν b g(E/2).

Since G(x_b)≤G(E/2), it follows that

ν b[g(x_b)−g(E/2)] ≤ G(x_b)−G(E/2) ≤0.

Add b g(x_b), divide by b>0, and obtain

(1+ν)g(x_b)−ν g(E/2) ≤ [Q_ν(b)−Q_ν(0)]/b ≤ g(x_b).

Continuity of x_ν and x_ν(0)=E/2 imply Q_ν'(0+)=g(E/2)>0. Zero scope is never optimal.

**Proof (full endpoint).** At b=1, the private objective (1−ν)g(x)+g(E−x) converges uniformly as ν↑1 to g(E−x), which has the unique maximizer x=0. Therefore x_ν(1)→0 and Q_ν(1)→2g(0)+g(E)=g(E). Strict concavity and g(0)=0 imply 2g(E/2)>g(E). Hence Q_ν(0)>Q_ν(1) for every sufficiently large ν<1. Complete scope is not optimal.

**Proof (conclusion).** Q_ν is continuous on a compact domain, so it attains a maximum; both endpoints have been excluded. Every maximizer is interior. For fixed positive x, [(1+b)g(x)+g(E−x)] strictly increases in b. The coordinated value max_x[(1+b)g(x)+g(E−x)] is likewise strictly increasing in b. At ν=0, x_0(b)=E/2 and Q_0(b)=(2+b)g(E/2), also strictly increasing. QED.

### Embedding in the differentiated-Bertrand game

Let ν=ρ/(2−ρ²), 0<ρ<1, and A_i=a+θ[g(x_i)+b g(x_j)+g(E−x_i)], with a,θ>0. Concavity and g(0)=0 give the conservative *all-history* bounds

a+θg(E) ≤ A_i ≤ a+θ[2g(E/2)+g(E)].

The paper's pure-strategy all-history continuation condition (R) is Amax/Amin < 2/[ρ(3−ρ²)]. Its RHS is >1 for each fixed ρ<1. The ratio of these conservative bounds approaches 1 as θ/a→0, so there are feasible positive a,θ for any fixed ρ sufficiently close to 1. This establishes a nonempty set of full-game parameters in which Theorem A's welfare ranking is implementable, **not** uniform (R)-feasibility with fixed a,θ as ρ→1. The original quadratic restricted domain ν<κE is not carried over automatically to this new general-technology extension.

### Theorem B — Local C² sufficient condition (secondary)

If g∈C², g'>0, x_1=x_ν(1) is interior and D(1)>0 with D(b)=−(1−ν b)g''(x_ν(b))−g''(E−x_ν(b)), implicit differentiation yields

x_ν'(b)=−ν g'(x_ν(b))/D(b)

and

Q_ν'(b)=g(x_ν(b))−bν(1+ν)[g'(x_ν(b))]²/D(b).

Thus **ν(1+ν)[g'(x_1)]² > g(x_1)D(1)** implies Q_ν'(1)<0. Together with Q_ν'(0+)>0 it excludes both endpoints and ensures all global policy optima are interior. This condition is sufficient, not necessary: corner allocations may make Q_ν'(1)=0 while complete scope is globally dominated.

### Numeric/symbolic test case, not a full Gate 3

With g(r)=log(1+3r)/3, E=1, private allocation is x_ν(b)=(3−4νb)/[3(2−νb)] in the all-interior region ν<3/4. Symbolic differentiation yields

Q''_ν(b)=ν[b²ν³+3bν−2ν−4]/[3(2−bν)²(1−bν)²] < 0.

The unique sign-switch of Q'_ν(1) in this region occurs at ν*=0.410410971694386. At ν=.7, numerical optimization gives b*=0.544863935215696, Q*=0.709431597548, Q(0)=0.610860487916, Q(1)=0.544425111749. The same parameter ν corresponds to ρ≈0.870076644; a=10 and θ=.2 satisfy a conservative all-history (R) test (bound ratio 1.012105333 < required threshold 1.024824907). These outputs support, but do not replace, the analytic results.

### Limits and publication significance

- g(0)=0 is **essential**, not an innocent additive normalization. Adding a large positive constant to g can restore optimal full scope at high ν.
- Theorem A does **not** prove uniqueness of the policy optimum, a single global rivalry threshold, endogenous total-R&D robustness, or arbitrary-market-structure generality.
- Theorem A is structurally stronger than frozen quadratic P4, but it remains specific to the present scope → spillover → R&D composition → welfare game. Reviewer-level prior-art examination and policy-significance assessment are still required before an IJIO novelty claim.
- No main, paper source, theory freeze, Lean certificates, or baseline stage records have been modified by this branch note.

References: https://dash.harvard.edu/bitstreams/7312037c-898f-6bd4-e053-0100007fdf3b/download ; https://doi.org/10.1016/j.ijindorg.2009.07.010 ; https://doi.org/10.2139/ssrn.2166219 ; https://doi.org/10.1016/j.ijindorg.2024.103046 ; https://doi.org/10.1016/j.jet.2010.09.001 .
