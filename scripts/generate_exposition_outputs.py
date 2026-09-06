import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs" / "EXPOSITION_OUTPUT_MANIFEST.json"
EXPECTED_FREEZE = "SSDI-THEORY-FREEZE-2026-09-06-v2"
EXPECTED_WORKFLOW = "v1.3"
EXPECTED_RELEASE = "3e4e6a3f76d86058024d06f9710f942e21627386"

with MANIFEST.open("r", encoding="utf-8") as fh:
    manifest = json.load(fh)

assert manifest["freeze_id"] == EXPECTED_FREEZE
assert manifest["workflow_version"] == EXPECTED_WORKFLOW
assert manifest["workflow_release_commit"] == EXPECTED_RELEASE
assert manifest["approved_quantitative_outputs"] == []

for directory in (ROOT / "figures", ROOT / "tables"):
    assert directory.is_dir(), f"missing exposition directory: {directory}"
    assert (directory / "README.md").is_file(), f"missing provenance README: {directory}"

print("EXPOSITION_OUTPUTS: PASS; Stage 9R has 0 approved quantitative outputs pending the Stage 10 v1.3 architecture gate")
