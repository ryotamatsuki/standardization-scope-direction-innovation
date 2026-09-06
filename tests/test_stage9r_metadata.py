import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FREEZE = "SSDI-THEORY-FREEZE-2026-09-06-v2"
WORKFLOW_VERSION = "v1.3"
WORKFLOW_RELEASE = "3e4e6a3f76d86058024d06f9710f942e21627386"


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


def test_stage9r_exposition_manifest_is_explicitly_empty():
    manifest = json.loads((ROOT / "docs" / "EXPOSITION_OUTPUT_MANIFEST.json").read_text(encoding="utf-8"))
    assert manifest["freeze_id"] == FREEZE
    assert manifest["workflow_version"] == WORKFLOW_VERSION
    assert manifest["workflow_release_commit"] == WORKFLOW_RELEASE
    assert manifest["approved_quantitative_outputs"] == []
    assert manifest["stage"] == "9R"
