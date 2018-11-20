PYTHON := venv/bin/python
PIP := venv/bin/pip

all: install

$(PYTHON):
	rm -rf venv
	virtualenv -p python3.6 venv

$(PIP): $(PYTHON)

install: $(PIP)
	$(PIP) install -r requirements.txt

notebook: $(PYTHON)
	venv/bin/jupyter notebook
