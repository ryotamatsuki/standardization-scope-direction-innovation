from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "docs" / "IJIO_AUTHENTICATED_PORTAL_PREFLIGHT.json"
RECORD = ROOT / "docs" / "IJIO_AUTHENTICATED_PORTAL_PREFLIGHT.md"


def load_state():
    return json.loads(STATE.read_text(encoding="utf-8"))


def test_preflight_fails_closed_without_current_authenticated_observation():
    data = load_state()
    assert data["authenticated_current_submission_observed"] is False
    assert data["stage14_full_pass_allowed"] is False
    assert data["verdict"] == "CONDITIONAL PASS — AUTHENTICATED PORTAL OBSERVATION REQUIRED"
    assert data["next_action"] == "AUTHENTICATED_CURRENT_IJIO_PORTAL_OBSERVATION"


def test_all_current_portal_items_remain_unverified_until_observed():
    data = load_state()
    expected = {f"AP{i:02d}" for i in range(1, 14)}
    assert set(data["portal_items"]) == expected
    assert all(value == "UNVERIFIED" for value in data["portal_items"].values())


def test_historical_account_evidence_cannot_close_current_portal_requirements():
    data = load_state()
    hist = data["historical_supporting_evidence"]
    assert hist["article_type"]["value"] == "Research Paper"
    assert hist["article_type"]["closes_current_requirement"] is False
    assert hist["generated_pdf_approval"]["closes_current_requirement"] is False


def test_record_prohibits_secret_capture_and_premature_source_archive_freeze():
    text = RECORD.read_text(encoding="utf-8")
    assert "Do not record passwords" in text
    assert "No source archive should be frozen until AP05/AP06" in text
    assert "Full `SUBMISSION QA PASS` is not authorized" in text


def test_scientific_object_is_unchanged():
    data = load_state()
    assert data["scientific_delta"] == "NONE"
    assert data["active_theory_freeze"] == "SSDI-THEORY-FREEZE-2026-09-10-v4"
