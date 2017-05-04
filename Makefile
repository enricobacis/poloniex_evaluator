.PHONY: run

MAIN := src/markets.py
VENV := venv

PIP := $(VENV)/bin/pip
PYTHON := $(VENV)/bin/python

run: $(VENV) $(MAIN)
	$(PYTHON) $(MAIN)

$(VENV): requirements.txt
	@ virtualenv $@
	@ $(PIP) install -r $<
