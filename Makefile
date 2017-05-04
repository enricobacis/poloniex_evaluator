.PHONY: clean run

MAIN := src/markets.py
VENV := venv

PIP := $(VENV)/bin/pip
PYTHON := $(VENV)/bin/python

run: $(VENV) $(MAIN)
	@ $(PYTHON) $(MAIN)

clean:
	@ rm -rf $(VENV)

$(VENV): requirements.txt
	@ virtualenv -p python2 $@
	@ $(PIP) install -r $<
