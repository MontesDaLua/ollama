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
	 del -r -y $(ENVNAME)
