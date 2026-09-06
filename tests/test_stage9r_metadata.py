import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FREEZE = "SSDI-THEORY-FREEZE-2026-09-06-v2"
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


def test_stage10r_exposition_manifest_has_required_regime_map():
    manifest = json.loads((ROOT / "docs" / "EXPOSITION_OUTPUT_MANIFEST.json").read_text(encoding="utf-8"))
    assert manifest["freeze_id"] == FREEZE
    assert manifest["workflow_version"] == WORKFLOW_VERSION
    assert manifest["workflow_release_commit"] == WORKFLOW_RELEASE
    assert manifest["stage"] == "10R"
    outputs = manifest["approved_quantitative_outputs"]
    assert len(outputs) == 1
    figure = outputs[0]
    assert figure["id"] == "policy-regime-map"
    assert figure["output_path"] == "figures/policy_regime_map.pdf"
    assert figure["required_in_final_paper"] is True
    assert abs(figure["representative_checks"]["bar_nu_at_y_0_7"] - 0.3587285925190902) < 1e-15


def test_v2_manuscript_does_not_restore_rejected_claims():
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
    assert "globally nonincreasing" in manuscript
    assert "globally nondecreasing" in manuscript
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
