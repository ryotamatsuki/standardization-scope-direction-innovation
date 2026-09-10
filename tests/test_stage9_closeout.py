from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLOSEOUT = ROOT / "docs" / "STAGE_09_FINAL_CLOSEOUT.md"


def test_stage9_is_formally_closed_on_merged_main():
    text = CLOSEOUT.read_text(encoding="utf-8")
    assert "SSDI-THEORY-FREEZE-2026-09-10-v4" in text
    assert "707b9688dfb8afd4624f006795b91f5f2ef83b79" in text
    assert "34479910733" in text
    assert "34479910711" in text
    assert "REPRODUCIBILITY BASELINE READY" in text
    assert "Stage 9 is **CLOSED**" in text
    assert "Remaining Stage-9 blockers\n\n`NONE`" in text


def test_stage9_closeout_preserves_next_gate():
    text = CLOSEOUT.read_text(encoding="utf-8")
    assert "Stage 11 — certification-regression recheck" in text
    assert "Journal Requirements Ledger" in text
    assert "new Stage 15 submission freeze" in text
