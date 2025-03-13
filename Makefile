# Windows version


.PHONY: all clean install test

#all: build run-tests
ENVNAME := local_python_environment

install:
		python -m venv $(ENVNAME)
		.\$(ENVNAME)\Scripts\activate
		python -m pip install --upgrade pip
		pip install -r  .\requirements.txt

clean:
	 rmdir /s /q $(ENVNAME)

lint:
		.\$(ENVNAME)\Scripts\activate
	  set PYTHONPATH=modules
		pylint .\scripts .\modules

test:
		.\$(ENVNAME)\Scripts\activate
	  set PYTHONPATH=modules
		python -m unittest discover modules
