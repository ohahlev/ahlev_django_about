package:
	python3 setup.py sdist
uptest: package
	python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
upprod: package
	python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*