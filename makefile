.DEFAULT_GOAL := clean

clean:
	rm -rf ./build
	rm -rf ./dist
	rm -rf ./geovdata.egg-info

build:
	python3 setup.py sdist bdist_wheel

install-local:
	pip install -e .
	
save:
	git add .
	git commit -m "save"
	git push origin master

install: clean build install