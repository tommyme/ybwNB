del /q /f dist
python setup.py build sdist bdist_wheel
python -m twine upload --repository pypi dist/*