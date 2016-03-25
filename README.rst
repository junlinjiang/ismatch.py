.. image:: https://img.shields.io/pypi/v/ismatch.svg
   :target: https://pypi.python.org/pypi/ismatch

.. image:: https://img.shields.io/pypi/pyversions/ismatch.svg
   :target: https://pypi.python.org/pypi/ismatch

.. image:: https://img.shields.io/pypi/dm/ismatch.svg
   :target: https://pypi.python.org/pypi/ismatch

	

Install
~~~~~~~

github.com_: :code:`pip install git+git://github.com/russianidiot/ismatch.py.git`

pypi.python.org_: :code:`pip install ismatch`

download_: :code:`[ -e requirements.txt ] && pip install -r requirements.txt; python setup.py install`

.. _github.com: http://github.com/russianidiot/ismatch.py
.. _pypi.python.org: https://pypi.python.org/pypi/ismatch.py
.. _download: https://github.com/russianidiot/ismatch.py/archive/master.zip

	

	

	

Usage
~~~~~

.. code-block:: python

	from ismatch import *

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

`russianidiot.github.io/python/`_  - my Python packages

.. _russianidiot.github.io/python/: http://russianidiot.github.io/python/