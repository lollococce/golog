
init:
	pip install -r requirements.txt

test:
	py.test tests

publish:
	rm -rf dist/* && rm -rf golog.egg-info/* && python3 setup.py sdist && twine upload --skip-existing dist/*