.. image:: https://img.shields.io/pypi/v/ismatch.svg
   :target: https://pypi.python.org/pypi/ismatch

.. image:: https://img.shields.io/pypi/pyversions/ismatch.svg
   :target: https://pypi.python.org/pypi/ismatch

.. image:: https://img.shields.io/pypi/dm/ismatch.svg
   :target: https://pypi.python.org/pypi/ismatch

	

Install
~~~~~~~

:code:`pip install ismatch`

	

	

	

Usage
~~~~~

**ismatch(string,pattern)** function

.. code-block:: python

	>>> from ismatch import *

	>>> ismatch("string","str*")
	True

	>>> ismatch("string",["str*","another pattern"]) # 2 patterns
	True

	>>> ismatch("string","string") # static pattern

----

Feedback
~~~~~~~~

|github_issues| - Github Issues

.. |github_issues| image:: https://img.shields.io/github/issues/russianidiot/ismatch.py.svg
	:target: https://github.com/russianidiot/ismatch.py/issues

|gitter| - **Chat** with me (english/russian) 

.. |gitter| image:: https://badges.gitter.im/russianidiot/ismatch.py.svg
	:target: https://gitter.im/russianidiot/ismatch.py

----

`russianidiot.github.io/python/`_  - Python packages

`russianidiot.github.io/cli/`_  - command line scripts

.. _russianidiot.github.io/python/: http://russianidiot.github.io/python/

.. _russianidiot.github.io/cli/: http://russianidiot.github.io/cli/

`README.rst`_  - generated with `readmemako.py`_ (python+ `mako`_ templates) and `.README`_ dotfiles

.. _README.rst: https://github.com/russianidiot/ismatch.py/blob/master/README.rst
.. _readmemako.py: http://github.com/russianidiot/readmemako.py/
.. _mako: http://www.makotemplates.org/
.. _.README: https://github.com/russianidiot-dotfiles/.README