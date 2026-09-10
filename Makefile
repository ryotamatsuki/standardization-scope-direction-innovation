PYTHON ?= python

.PHONY: all reproducibility verify symbolic numerical stage4a continuation test exposition figures tables paper formal formal-audit clean

all: reproducibility

reproducibility: verify exposition paper formal formal-audit

verify: symbolic numerical stage4a continuation test

symbolic:
	$(PYTHON) scripts/symbolic_verify.py

numerical:
	$(PYTHON) scripts/numerical_verify.py

stage4a:
	$(PYTHON) scripts/stage4a_independent_equilibrium_set_audit.py

continuation:
	$(PYTHON) scripts/stage11_independent_continuation_audit.py

test:
	pytest -q

exposition:
	$(PYTHON) scripts/generate_exposition_outputs.py

figures: exposition

tables: exposition

paper: exposition
	cd paper && pdflatex -interaction=nonstopmode -halt-on-error main.tex >/dev/null
	cd paper && bibtex main >/dev/null
	cd paper && pdflatex -interaction=nonstopmode -halt-on-error main.tex >/dev/null
	cd paper && pdflatex -interaction=nonstopmode -halt-on-error main.tex >/dev/null

formal:
	cd formal && elan default "$$(cat lean-toolchain)" >/dev/null && lake update && lake exe cache get && lean --version && echo "MATHLIB_COMMIT=$$(git -C .lake/packages/mathlib rev-parse HEAD)" && lake build

formal-audit:
	@if grep -RInE '(^|[^A-Za-z])(sorry|admit)([^A-Za-z]|$$)|^[[:space:]]*axiom[[:space:]]' formal/SSDI formal/SSDI.lean --include='*.lean'; then \
		echo "Lean proof escape hatch or project-specific axiom detected"; \
		exit 1; \
	fi
	@echo "PROJECT_LEAN_ESCAPE_HATCH_AUDIT=PASS"

clean:
	rm -f paper/*.aux paper/*.bbl paper/*.blg paper/*.log paper/*.out paper/*.pdf
	rm -f figures/policy_regime_map.pdf
