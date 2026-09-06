PYTHON ?= python

.PHONY: all verify symbolic numerical test exposition figures tables paper clean

all: verify paper

verify: symbolic numerical test

symbolic:
	$(PYTHON) scripts/symbolic_verify.py

numerical:
	$(PYTHON) scripts/numerical_verify.py

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
