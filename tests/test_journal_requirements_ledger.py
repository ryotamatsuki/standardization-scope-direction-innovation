from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
LEDGER_MD = ROOT / "docs" / "JOURNAL_REQUIREMENTS_LEDGER.md"
LEDGER_JSON = ROOT / "docs" / "JOURNAL_REQUIREMENTS_LEDGER.json"
ACTIVE_FREEZE = "SSDI-THEORY-FREEZE-2026-09-10-v4"
BASELINE = "24f6f357277a8721ff95b12382891c7b69454863"
WORKFLOW = "f48984013898696f010f0437a8cfed6b5b54bdc2"


def load_json():
    return json.loads(LEDGER_JSON.read_text(encoding="utf-8"))


def test_current_ledger_is_fail_closed_until_material_rules_are_verified():
    data = load_json()
    assert data["overall_state"] == "OPEN — MATERIAL UNVERIFIED ITEMS REMAIN"
    assert data["stage14_full_pass_allowed"] is False
    assert data["conflicts"] == []
    assert data["active_theory_freeze"] == ACTIVE_FREEZE
    assert data["canonical_baseline_entering_ledger"] == BASELINE
    assert data["workflow_authority"] == WORKFLOW


def test_high_risk_initial_submission_and_portal_rules_remain_explicit():
    data = load_json()
    unresolved = set(data["material_unverified"])
    for requirement in ("F01", "F02", "R01", "D06", "D10", "C03", "AP11", "AP12"):
        assert requirement in unresolved
    assert "PDF-only" in data["highest_priority_blockers"]["F01"]
    assert "editable" in data["highest_priority_blockers"]["F02"]
    assert data["next_gate"] == "AUTHENTICATED IJIO GUIDE / EDITORIAL MANAGER PREFLIGHT"


def test_ledger_preserves_source_hierarchy_and_current_guide_boundary():
    data = load_json()
    md = LEDGER_MD.read_text(encoding="utf-8")
    assert data["sources"]["S2"]["level"] == 3
    assert data["sources"]["S2"]["status"] == "IDENTIFIED_BUT_BODY_NOT_RETRIEVABLE"
    assert data["sources"]["S3"]["level"] == 2
    assert data["sources"]["S3"]["status"] == "AUTHENTICATED_FIELDS_NOT_YET_INSPECTED"
    assert "OPEN — MATERIAL UNVERIFIED ITEMS REMAIN" in md
    assert "SUBMISSION QA PASS" in md
    assert "prohibited" in md.lower() or "blocks" in md.lower()
    assert "https://www.sciencedirect.com/journal/international-journal-of-industrial-organization/publish/guide-for-authors" in md


def test_general_elsevier_pdf_rule_cannot_be_promoted_to_ijio_specific_pass():
    data = load_json()
    md = LEDGER_MD.read_text(encoding="utf-8")
    assert "F01" in data["material_unverified"]
    assert "F02" in data["material_unverified"]
    assert "Most journals" not in data["highest_priority_blockers"]["F01"]
    assert "most journals" in md.lower()
    assert "target-journal exceptions control" in md


def test_current_package_strengths_do_not_close_portal_requirements():
    data = load_json()
    strengths = set(data["verified_package_strengths"])
    assert "anonymous review manuscript already prepared" in strengths
    assert "separate author title page already prepared" in strengths
    assert "four Highlights prepared and each below 85 characters" in strengths
    assert data["stage14_full_pass_allowed"] is False
