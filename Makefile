# Windows version :-(


.PHONY: all clean install test venv lint

SHELL := /bin/bash
VENV_DIR := local_python_environment
PYTHON := python3

venv:
	@if [ ! -d $(VENV_DIR) ]; then \
		$(PYTHON) -m venv $(VENV_DIR); \
	fi

install:
	@source ./$(VENV_DIR)/bin/activate && \
		pip install -r  requirements.txt

clean:
	@rm -rf $(VENV_DIR)

lint: install
		@source ./$(VENV_DIR)/bin/activate && \
	  	PYTHONPATH=modules pylint scripts modules

test:
		@source ./$(VENV_DIR)/bin/activate && \
	  	PYTHONPATH=modules python -m unittest discover modules
		@source ./$(VENV_DIR)/bin/activate && \
	  	PYTHONPATH=modules python -m unittest discover scripts

#all: build run-tests
