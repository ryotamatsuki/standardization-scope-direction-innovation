PYTHON ?= python

.PHONY: all verify symbolic numerical stage4a continuation test exposition figures tables paper clean

all: verify paper

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

clean:
	rm -f paper/*.aux paper/*.bbl paper/*.blg paper/*.log paper/*.out paper/*.pdf
	rm -f figures/policy_regime_map.pdf
