import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs" / "EXPOSITION_OUTPUT_MANIFEST.json"
EXPECTED_FREEZE = "SSDI-THEORY-FREEZE-2026-09-06-v2"
EXPECTED_WORKFLOW = "v1.3"
EXPECTED_RELEASE = "3e4e6a3f76d86058024d06f9710f942e21627386"


def H(y: float, nu: float) -> float:
    return (
        nu**3
        + 2 * nu**2 * y**2
        - 8 * nu**2 * y
        + 2 * nu**2
        + nu * y**2
        - 4 * nu * y
        + 16 * nu
        + 2 * y**2
        - 8 * y
    )


def threshold(y: float) -> float:
    if not (0.5 < y < 1.0):
        raise ValueError("threshold is only defined here on 1/2 < y < 1")
    lo, hi = 0.0, y
    assert H(y, lo) < 0.0
    assert H(y, hi) > 0.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if H(y, mid) > 0.0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


with MANIFEST.open("r", encoding="utf-8") as fh:
    manifest = json.load(fh)

assert manifest["freeze_id"] == EXPECTED_FREEZE
assert manifest["workflow_version"] == EXPECTED_WORKFLOW
assert manifest["workflow_release_commit"] == EXPECTED_RELEASE
assert manifest["stage"] == "10R"
outputs = manifest["approved_quantitative_outputs"]
assert len(outputs) == 1
spec = outputs[0]
assert spec["id"] == "policy-regime-map"
assert spec["type"] == "figure"
assert spec["required_in_final_paper"] is True

check_07 = threshold(0.7)
check_09 = threshold(0.9)
assert abs(check_07 - spec["representative_checks"]["bar_nu_at_y_0_7"]) < 1e-12
assert abs(check_09 - spec["representative_checks"]["bar_nu_at_y_0_9"]) < 1e-12

ys = np.linspace(0.5005, 0.9995, 400)
thresholds = np.array([threshold(float(y)) for y in ys])
assert np.all(thresholds > 0.0)
assert np.all(thresholds < ys)
assert np.all(np.diff(thresholds) > 0.0)

fig, ax = plt.subplots(figsize=(6.4, 4.6))
ax.fill_between(ys, 0.0, thresholds, alpha=0.18, label="Complete standardization")
ax.fill_between(ys, thresholds, ys, alpha=0.18, label="Selective standardization")
ax.plot(ys, thresholds, linewidth=2.0, label=r"Threshold $\bar{\nu}(y)$")
ax.plot(ys, ys, linestyle="--", linewidth=1.4, label=r"Domain boundary $\nu=y$")
ax.set_xlim(0.5, 1.0)
ax.set_ylim(0.0, 1.0)
ax.set_xlabel(r"R&D curvature-capacity index $y=\kappa E$")
ax.set_ylabel(r"Competitive penalty $\nu$")
ax.text(0.62, 0.13, "Complete\nstandardization", ha="center", va="center")
ax.text(0.82, 0.64, "Selective\nstandardization", ha="center", va="center")
ax.legend(frameon=False, loc="upper left")
ax.grid(alpha=0.2)

output = ROOT / spec["output_path"]
output.parent.mkdir(parents=True, exist_ok=True)
fig.tight_layout()
fig.savefig(output, bbox_inches="tight")
plt.close(fig)

assert output.is_file() and output.stat().st_size > 0
print(
    "EXPOSITION_OUTPUTS: PASS; generated policy regime map; "
    f"bar_nu(0.7)={check_07:.12f}, bar_nu(0.9)={check_09:.12f}"
)
