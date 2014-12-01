PYTHON=/Users/kim/Plone/Python-2.4/bin/python

all:
	cat Makefile
	@echo ""
	@echo "Don't forget to change the version number in setup.py, profiles/default/metadata.xml, and version.txt"

clean:
	rm -rf build dist

egg:
	$(PYTHON) setup.py sdist upload -r http://plone2.webcluster.uwosh.edu:9082/sites1/ploneprojects/software/

dist4:
	/usr/local/bin/python2.6 setup.py sdist  upload -r ourbasket
