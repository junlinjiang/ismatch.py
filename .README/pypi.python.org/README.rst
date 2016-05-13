.. image:: https://img.shields.io/badge/language-python-blue.svg

.. image:: https://img.shields.io/pypi/pyversions/ismatch.svg
   :target: https://pypi.python.org/pypi/ismatch

|codacy| |landscape| |codeclimate| |scrutinizer|

.. |scrutinizer| image:: https://scrutinizer-ci.com/g/russianidiot/ismatch.py/badges/quality-score.png?b=master
   :target: https://scrutinizer-ci.com/g/russianidiot/ismatch.py/master
   :alt: scrutinizer-ci.com

.. |codacy| image:: https://img.shields.io/codacy/e58b4e41a8944871be85cd35f1626102.svg
   :target: https://www.codacy.com/app/russianidiot-github/ismatch-py/dashboard
   :alt: codacy.com

.. |codeclimate| image:: https://img.shields.io/codeclimate/github/russianidiot/ismatch.py.svg
   :target: https://codeclimate.com/github/russianidiot/ismatch.py
   :alt: codeclimate.com

.. |landscape| image:: https://landscape.io/github/russianidiot/ismatch.py/master/landscape.svg?style=flat
   :target: https://landscape.io/github/russianidiot/ismatch.py/master
   :alt: landscape.io

Install
```````

:code:`[sudo] pip install ismatch`

Usage
`````

.. code:: python
	
	>>> from ismatch import ismatch
	
	>>> ismatch(string,pattern)

Example
```````

.. code:: python
	
	>>> ismatch("string","str*")
	True
	
	>>> ismatch("string",["str*","another pattern"]) # 2 patterns
	True
	
	>>> ismatch("string","string") # static pattern
	True

`Examples/`_

.. _Examples/: https://github.com/russianidiot/ismatch.py/tree/master/Examples

Sources:

*	`py_modules/ismatch.py`_

.. _`py_modules/ismatch.py`: https://github.com/russianidiot/ismatch.py/blob/master/py_modules/ismatch.py

Feedback |github_issues| |gitter| |github_follow|

.. |github_issues| image:: https://img.shields.io/github/issues/russianidiot/ismatch.py.svg
	:target: https://github.com/russianidiot/ismatch.py/issues

.. |github_follow| image:: https://img.shields.io/github/followers/russianidiot.svg?style=social&label=Follow
	:target: https://github.com/russianidiot

.. |gitter| image:: https://badges.gitter.im/russianidiot/ismatch.py.svg
	:target: https://gitter.im/russianidiot/ismatch.py

----

`russianidiot.github.io/python/`_  - Python packages

.. _russianidiot.github.io/python/: http://russianidiot.github.io/python/

`russianidiot.github.io/cli/`_  - command line scripts

.. _russianidiot.github.io/cli/: http://russianidiot.github.io/cli/

`README.rst`_  - generated with `readmemako.py`_ (python+ `mako`_ templates) and `.README`_ dotfiles

.. _README.rst: https://github.com/russianidiot/ismatch.py/blob/master/.README/pypi.python.org/README.rst
.. _readmemako.py: http://github.com/russianidiot/readmemako.py/
.. _mako: http://www.makotemplates.org/
.. _.README: https://github.com/russianidiot-dotfiles/.README
