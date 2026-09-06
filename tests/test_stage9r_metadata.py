import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FREEZE = "SSDI-THEORY-FREEZE-2026-09-06-v3"
WORKFLOW_VERSION = "v1.3"
WORKFLOW_RELEASE = "3e4e6a3f76d86058024d06f9710f942e21627386"


def _manuscript_text():
    paths = [ROOT / "paper" / "main.tex", *sorted((ROOT / "paper" / "sections").glob("*.tex"))]
    return "\n".join(path.read_text(encoding="utf-8") for path in paths)


def test_active_metadata_is_synchronized():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    provenance = (ROOT / "docs" / "PROVENANCE.md").read_text(encoding="utf-8")
    freeze = (ROOT / "docs" / "THEORY_FREEZE.md").read_text(encoding="utf-8")
    for text in (readme, provenance, freeze):
        assert FREEZE in text
    assert WORKFLOW_VERSION in readme
    assert WORKFLOW_VERSION in provenance
    assert WORKFLOW_RELEASE in readme
    assert WORKFLOW_RELEASE in provenance
    assert (ROOT / "docs" / "THEORY_FREEZE_v2.md").is_file()


def test_stage10r_exposition_manifest_has_required_regime_map_under_v3():
    manifest = json.loads((ROOT / "docs" / "EXPOSITION_OUTPUT_MANIFEST.json").read_text(encoding="utf-8"))
    assert manifest["freeze_id"] == FREEZE
    assert manifest["workflow_version"] == WORKFLOW_VERSION
    assert manifest["workflow_release_commit"] == WORKFLOW_RELEASE
    outputs = manifest["approved_quantitative_outputs"]
    assert len(outputs) == 1
    figure = outputs[0]
    assert figure["id"] == "policy-regime-map"
    assert figure["output_path"] == "figures/policy_regime_map.pdf"
    assert figure["required_in_final_paper"] is True
    assert abs(figure["representative_checks"]["bar_nu_at_y_0_7"] - 0.3587285925190902) < 1e-15
    assert abs(figure["representative_checks"]["bar_nu_at_y_0_9"] - 0.4755546783510237) < 1e-15


def test_v3_p2r_is_order_comparative_statics_only():
    freeze = (ROOT / "docs" / "THEORY_FREEZE.md").read_text(encoding="utf-8")
    equilibrium = (ROOT / "paper" / "sections" / "03_equilibrium.tex").read_text(encoding="utf-8")
    robustness = (ROOT / "paper" / "sections" / "05_robustness.tex").read_text(encoding="utf-8")
    appendix = (ROOT / "paper" / "sections" / "appendix.tex").read_text(encoding="utf-8")

    assert "x^F(b_2)\\leq x^F(b_1)" in equilibrium
    assert "x^S(b_2)\\geq x^S(b_1)" in equilibrium
    assert "x^F(b_2)<x^F(b_1)" in equilibrium
    assert "x^S(b_2)>x^S(b_1)" in equilibrium
    assert "No pointwise sign for $dx^F/db$ or $dx^S/db$" in equilibrium
    assert "No pointwise derivative statement" in freeze
    assert "We do not assert a pointwise sign" in robustness

    assert "g''" not in appendix
    assert "Phi_{F,x}" not in appendix
    assert "frac{dx^F}{db}" not in robustness
    assert "frac{dx^S}{db}" not in robustness


def test_quadratic_p1_and_p4_are_unchanged():
    equilibrium = (ROOT / "paper" / "sections" / "03_equilibrium.tex").read_text(encoding="utf-8")
    symbolic = (ROOT / "scripts" / "symbolic_verify.py").read_text(encoding="utf-8")
    assert "-\\frac{\\nu(2-y)}{\\kappa(2-\\nu b)^2}<0" in equilibrium
    assert "F''(b)" in equilibrium
    assert "F'(1)=-\\frac{H(y,\\nu)}{2(2-\\nu)^3}" in equilibrium.replace("\n", "")
    assert "Fpp_expected = -nu*(y-2)**2" in symbolic
    assert "Fp1" in symbolic


def test_rejected_claims_do_not_reenter_manuscript():
    manuscript = _manuscript_text()
    lower = manuscript.lower()
    forbidden = [
        "under the first best",
        "first-best standardization",
        "persist for sufficiently small $c^2$ perturbations",
        "when the total-capacity cost is sufficiently steep",
        "complete standardization is also first-best",
    ]
    for phrase in forbidden:
        assert phrase not in lower
    assert "not an unconstrained first best" in lower
    assert "BryanLemus2017" in manuscript
    assert "fig:regime-map" in manuscript


def test_citation_keys_and_cross_references_resolve_in_source():
    manuscript = _manuscript_text()
    bib = (ROOT / "references" / "references.bib").read_text(encoding="utf-8")

    cited = set()
    for group in re.findall(r"\\cite[tp]?\{([^}]+)\}", manuscript):
        cited.update(key.strip() for key in group.split(",") if key.strip())
    bib_keys = set(re.findall(r"@\w+\{([^,]+),", bib))
    assert cited <= bib_keys, f"missing bibliography keys: {sorted(cited - bib_keys)}"

    labels = set(re.findall(r"\\label\{([^}]+)\}", manuscript))
    refs = set(re.findall(r"\\(?:ref|eqref)\{([^}]+)\}", manuscript))
    assert refs <= labels, f"missing labels: {sorted(refs - labels)}"
