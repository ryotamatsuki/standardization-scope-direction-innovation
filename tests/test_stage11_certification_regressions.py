from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
ACTIVE_FREEZE = "SSDI-THEORY-FREEZE-2026-09-10-v4"
OLD_FREEZE = "SSDI-THEORY-FREEZE-2026-09-06-v3"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def manuscript() -> str:
    paths = [ROOT / "paper" / "main.tex", *sorted((ROOT / "paper" / "sections").glob("*.tex"))]
    return "\n".join(p.read_text(encoding="utf-8") for p in paths)


def test_p2r_historical_scope_regression_is_permanently_blocked():
    eq = read("paper/sections/03_equilibrium.tex")
    app = read("paper/sections/appendix.tex")
    regression = read("docs/CERTIFICATION_REGRESSION_P2R.md")

    assert "x^F(b_2)\\leq x^F(b_1)" in eq
    assert "x^S(b_2)\\geq x^S(b_1)" in eq
    assert "No pointwise sign for $dx^F/db$ or $dx^S/db$ is asserted for arbitrary general $g$." in eq
    assert "No pointwise derivative sign for $x^F(b)$ or $x^S(b)$ is asserted for a general technology." in app
    assert "g''" not in app
    assert "CERTIFICATION REGRESSION — HISTORICAL, REPAIRED, PERMANENTLY GUARDED" in regression
    assert "formal/SSDI/Generality.lean" in regression
    assert "tests/test_p2r_order_monotonicity.py" in regression


def test_equilibrium_uniqueness_scope_cannot_drift_beyond_pure_strategies():
    model = read("paper/sections/02_model.tex")
    eq = read("paper/sections/03_equilibrium.tex")
    app = read("paper/sections/appendix.tex")
    stage4a = read("docs/STAGE_04A_RETROACTIVE_MATH_ADVERSARIAL_CERTIFICATION.md")
    stage75a = read("docs/STAGE_075A_RETROACTIVE_GENERALITY_QUANTIFIER_FORMAL_VERIFICATION.md")

    assert "unique pure-strategy Bertrand equilibrium" in model
    assert "unique active-product pure-strategy price equilibrium" in eq
    assert "unique global pure-strategy Nash equilibrium" in app
    assert "D1 candidate-deviation" in stage4a
    assert "D2 alternative-equilibrium" in stage4a
    assert "Indifference / zero-payoff trigger audit (D3)" in stage4a
    assert "mixed-strategy uniqueness" in stage75a
    assert "unique global Nash equilibrium" not in manuscript()


def test_benchmark_and_policy_scope_cannot_inflate():
    welfare = read("paper/sections/04_welfare.tex")
    eq = read("paper/sections/03_equilibrium.tex")
    stage75a = read("docs/STAGE_075A_RETROACTIVE_GENERALITY_QUANTIFIER_FORMAL_VERIFICATION.md")

    assert "This proposition is not an unconstrained first-best result." in welfare
    assert "The paper therefore makes no claim about the unconstrained social-planner optimum." in welfare
    assert "This global uniqueness and threshold characterization are claims about the quadratic baseline only." in eq
    assert "P4: quadratic baseline policy theorem only" in stage75a
    assert "unrestricted first best" in stage75a


def test_stage9_active_freeze_provenance_is_not_stale_in_manuscript():
    app = read("paper/sections/appendix.tex")
    assert ACTIVE_FREEZE in app
    assert "active certification-only theory freeze" in app
    assert f"active frozen theory record \\texttt{{{OLD_FREEZE}}}" not in app


def test_formal_verification_boundary_and_traceability_remain_explicit():
    cert = read("theorem_certificates/STAGE075A_FORMAL_VERIFICATION_CERTIFICATE.md")
    manifest = json.loads(read("docs/REPRODUCIBILITY_MANIFEST.json"))
    makefile = read("Makefile")

    assert "FORMAL VERIFICATION PASS" in cert
    assert "mixed-strategy" in cert.lower()
    assert "full" in cert.lower() and "spne" in cert.lower()
    assert manifest["active_freeze_id"] == ACTIVE_FREEZE
    assert manifest["status"] == "REPRODUCIBILITY BASELINE READY"
    for claim in ("E0", "P1", "P2R", "P3R", "P4", "P5R_W1"):
        assert claim in manifest["headline_claim_traceability"]
    assert "stage4a:" in makefile
    assert "continuation:" in makefile
    assert "formal-audit:" in makefile


def test_stage11_regression_assets_are_present():
    assert (ROOT / "docs" / "CERTIFICATION_REGRESSION_P2R.md").is_file()
    assert (ROOT / "scripts" / "stage4a_independent_equilibrium_set_audit.py").is_file()
    assert (ROOT / "scripts" / "stage11_independent_continuation_audit.py").is_file()
    assert (ROOT / "tests" / "test_p2r_order_monotonicity.py").is_file()
