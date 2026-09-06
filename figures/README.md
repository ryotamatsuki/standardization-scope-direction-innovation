# Figures

Stage 10R approves exactly one required quantitative manuscript figure under `research-paper-workflow` v1.3:

- `policy_regime_map.pdf` — the complete-versus-selective standardization regime map generated from the unique root `bar_nu(y)` of `H(y,nu)=0` on the frozen quadratic domain `1/2 < y < 1`, `0 < nu < y`.

Provenance:

- active freeze: `SSDI-THEORY-FREEZE-2026-09-06-v3`;
- generator: `scripts/generate_exposition_outputs.py`;
- manifest: `docs/EXPOSITION_OUTPUT_MANIFEST.json`;
- manuscript hook: `fig:regime-map`;
- representative check: `bar_nu(0.7)=0.3587285925190902`;
- regeneration target: `make exposition` or `make paper`.

The Stage-7R2 P2R repair does not alter Proposition 4, `H(y,nu)`, the threshold, or the figure. The PDF is generated rather than hand edited and must not be interpreted outside the quadratic baseline or frozen parameter domain.
