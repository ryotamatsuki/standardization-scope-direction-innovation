PYTHON ?= python

.PHONY: verify symbolic numerical test paper clean

verify: symbolic numerical test

symbolic:
	$(PYTHON) scripts/symbolic_verify.py

numerical:
	$(PYTHON) scripts/numerical_verify.py

test:
	pytest -q

paper:
	cd paper && pdflatex -interaction=nonstopmode -halt-on-error main.tex >/dev/null
	cd paper && bibtex main >/dev/null
	cd paper && pdflatex -interaction=nonstopmode -halt-on-error main.tex >/dev/null
	cd paper && pdflatex -interaction=nonstopmode -halt-on-error main.tex >/dev/null

clean:
	rm -f paper/*.aux paper/*.bbl paper/*.blg paper/*.log paper/*.out paper/*.pdf
