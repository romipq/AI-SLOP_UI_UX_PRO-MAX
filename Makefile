# AI-SLOP PRO-MAX — convenience targets
# Usage: make demo | make lint | make gate | make score

PY ?= python3
TEMPLATES := templates/landing.html templates/dashboard.html templates/components.html

.PHONY: help demo lint gate score json clean

help:
	@echo "make demo    — serve the repo at http://localhost:8000"
	@echo "make lint    — verbose slop report for every template"
	@echo "make gate    — CI gate: fail below 90/100"
	@echo "make score   — one number per template"
	@echo "make json    — machine-readable report"

demo:
	@echo "→ http://localhost:8000/templates/landing.html"
	$(PY) -m http.server 8000 --bind 0.0.0.0

lint:
	$(PY) scripts/slop_lint.py $(TEMPLATES) --verbose

gate:
	$(PY) scripts/slop_lint.py $(TEMPLATES) --min-score 90 --quiet > /dev/null && echo "✓ slop gate passed"

score:
	@for f in $(TEMPLATES); do printf "%-32s " $$f; $(PY) scripts/slop_lint.py $$f --quiet; done

json:
	$(PY) scripts/slop_lint.py $(TEMPLATES) --json

clean:
	rm -rf __pycache__ scripts/__pycache__ .DS_Store
