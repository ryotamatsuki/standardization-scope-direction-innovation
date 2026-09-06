# Standardization Scope and the Direction of Innovation

Active canonical theory freeze: `SSDI-THEORY-FREEZE-2026-09-06-v2`

Canonical workflow: `ryotamatsuki/research-paper-workflow` v1.3  
Workflow release commit: `3e4e6a3f76d86058024d06f9710f942e21627386`

Stage 9R starting remote `main`: `26d28b84dc3e0649c6c9f40e4fd706e23c0694ed`

## Reproducibility

Install Python dependencies and run:

```bash
make verify
make exposition
make paper
```

Or run the complete local-equivalent gate:

```bash
make all
```

- `make verify` runs symbolic identities, numerical checks, and pytest.
- `make exposition` validates the reproducible figure/table output manifest. Under workflow v1.3, Stage 10 must complete the mandatory Figure/Table Architecture Gate before approving any quantitative figure/table for the manuscript; Stage 9R therefore records zero approved quantitative outputs rather than inventing one.
- `make paper` builds `paper/main.pdf` from the modular LaTeX source and bibliography.

## Theory change control

The active theory is defined by `docs/THEORY_FREEZE.md`. The historical v1 freeze is preserved in `docs/THEORY_FREEZE_v1.md`. No theory change is permitted without recording the change and reopening every affected workflow stage.
