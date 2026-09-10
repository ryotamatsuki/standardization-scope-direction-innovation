import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ACTIVE_FREEZE = "SSDI-THEORY-FREEZE-2026-09-10-v4"
INHERITED_FREEZE = "SSDI-THEORY-FREEZE-2026-09-06-v3"
WORKFLOW_VERSION = "v1.3"
WORKFLOW_RELEASE = "3e4e6a3f76d86058024d06f9710f942e21627386"
LATEST_WORKFLOW = "f48984013898696f010f0437a8cfed6b5b54bdc2"
FORMAL_CERT = "theorem_certificates/STAGE075A_FORMAL_VERIFICATION_CERTIFICATE.md"
MATHLIB_COMMIT = "520045ab14e26149ee970e2e617ca04b09bde5d6"


def _manuscript_text():
    paths = [ROOT / "paper" / "main.tex", *sorted((ROOT / "paper" / "sections").glob("*.tex"))]
    return "\n".join(path.read_text(encoding="utf-8") for path in paths)


def test_active_metadata_is_synchronized_after_stage9_v4_sync():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    provenance = (ROOT / "docs" / "PROVENANCE.md").read_text(encoding="utf-8")
    freeze = (ROOT / "docs" / "THEORY_FREEZE.md").read_text(encoding="utf-8")
    migration = (ROOT / "docs" / "LATEST_WORKFLOW_COMPATIBILITY_MIGRATION.md").read_text(encoding="utf-8")
    formal_readme = (ROOT / "formal" / "README.md").read_text(encoding="utf-8")
    for text in (readme, provenance, freeze, migration, formal_readme):
        assert ACTIVE_FREEZE in text
    assert WORKFLOW_VERSION in readme
    assert WORKFLOW_VERSION in provenance
    assert WORKFLOW_RELEASE in readme
    assert WORKFLOW_RELEASE in provenance
    assert LATEST_WORKFLOW in readme
    assert LATEST_WORKFLOW in provenance
    assert (ROOT / "docs" / "THEORY_FREEZE_v2.md").is_file()
    assert (ROOT / "docs" / "THEORY_FREEZE_v3.md").is_file()
    assert (ROOT / FORMAL_CERT).is_file()
    assert "THEORY FROZEN — GO TO REPRODUCIBILITY SETUP" in freeze
    assert "FORMAL VERIFICATION PASS" in freeze


def test_stage9_exposition_manifest_is_synchronized_to_v4_without_scientific_change():
    manifest = json.loads((ROOT / "docs" / "EXPOSITION_OUTPUT_MANIFEST.json").read_text(encoding="utf-8"))
    assert manifest["freeze_id"] == ACTIVE_FREEZE
    assert manifest["inherited_scientific_freeze_id"] == INHERITED_FREEZE
    assert manifest["certification_only_refreeze"] is True
    assert manifest["workflow_version"] == WORKFLOW_VERSION
    assert manifest["workflow_release_commit"] == WORKFLOW_RELEASE
    assert manifest["latest_workflow_compatibility_commit"] == LATEST_WORKFLOW
    assert manifest["scientific_output_invariance"]["status"] == "PASS"
    assert manifest["scientific_output_invariance"]["scientific_source_delta"] == "NONE"
    outputs = manifest["approved_quantitative_outputs"]
    assert len(outputs) == 1
    figure = outputs[0]
    assert figure["id"] == "policy-regime-map"
    assert figure["output_path"] == "figures/policy_regime_map.pdf"
    assert figure["required_in_final_paper"] is True
    assert figure["v3_to_v4_scientific_change"] == "NONE"
    assert abs(figure["representative_checks"]["bar_nu_at_y_0_7"] - 0.3587285925190902) < 1e-15
    assert abs(figure["representative_checks"]["bar_nu_at_y_0_9"] - 0.4755546783510237) < 1e-15


def test_stage9_reproducibility_manifest_traces_certification_and_formal_sources():
    manifest = json.loads((ROOT / "docs" / "REPRODUCIBILITY_MANIFEST.json").read_text(encoding="utf-8"))
    assert manifest["active_freeze_id"] == ACTIVE_FREEZE
    assert manifest["inherited_scientific_freeze_id"] == INHERITED_FREEZE
    assert manifest["latest_workflow_authority"] == LATEST_WORKFLOW
    assert manifest["formal_verification"]["certificate"] == FORMAL_CERT
    assert manifest["formal_verification"]["mathlib_commit"] == MATHLIB_COMMIT
    assert manifest["formal_verification"]["state"] == "FORMAL VERIFICATION PASS"
    assert manifest["build"]["complete_local_gate"] == "make all"
    assert manifest["scientific_invariance"]["status"] == "PASS"
    assert manifest["scientific_invariance"]["scientific_source_delta"] == "NONE"
    for claim in ("E0", "P1", "P2R", "P3R", "P4", "P5R_W1"):
        assert claim in manifest["headline_claim_traceability"]


def test_formal_readme_points_to_real_v4_certificate_and_pins():
    formal_readme = (ROOT / "formal" / "README.md").read_text(encoding="utf-8")
    lakefile = (ROOT / "formal" / "lakefile.toml").read_text(encoding="utf-8")
    makefile = (ROOT / "Makefile").read_text(encoding="utf-8")
    assert ACTIVE_FREEZE in formal_readme
    assert FORMAL_CERT in formal_readme
    assert "formal/FORMAL_VERIFICATION_CERTIFICATE.md" not in formal_readme
    assert MATHLIB_COMMIT in lakefile
    assert "all: reproducibility" in makefile
    assert "reproducibility: verify exposition paper formal formal-audit" in makefile
    assert "make formal" in formal_readme
    assert "make formal-audit" in formal_readme


def test_v4_inherits_repaired_p2r_order_scope():
    freeze = (ROOT / "docs" / "THEORY_FREEZE.md").read_text(encoding="utf-8")
    equilibrium = (ROOT / "paper" / "sections" / "03_equilibrium.tex").read_text(encoding="utf-8")
    robustness = (ROOT / "paper" / "sections" / "05_robustness.tex").read_text(encoding="utf-8")
    appendix = (ROOT / "paper" / "sections" / "appendix.tex").read_text(encoding="utf-8")

    assert "x^F(b_2)\\leq x^F(b_1)" in equilibrium
    assert "x^S(b_2)\\geq x^S(b_1)" in equilibrium
    assert "x^F(b_2)<x^F(b_1)" in equilibrium
    assert "x^S(b_2)>x^S(b_1)" in equilibrium
    assert "No pointwise sign for $dx^F/db$ or $dx^S/db$" in equilibrium
    assert "No pointwise" in freeze
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


def test_pure_strategy_scope_is_explicit():
    model = (ROOT / "paper" / "sections" / "02_model.tex").read_text(encoding="utf-8")
    equilibrium = (ROOT / "paper" / "sections" / "03_equilibrium.tex").read_text(encoding="utf-8")
    assert "unique pure-strategy Bertrand equilibrium" in model
    assert "unique active-product pure-strategy price equilibrium" in equilibrium


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
