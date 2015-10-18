	
Install
'''''''

github.com_: :code:`pip install git+git://github.com/russianidiot/ismatch.py.git`

pypi.python.org_: :code:`pip install ismatch`

download_: :code:`python setup.py install` or :code:`setup.py/.setup.py develop.command`

.. _github.com: http://github.com/russianidiot/ismatch.py
.. _pypi.python.org: https://pypi.python.org/pypi/ismatch
.. _download: https://github.com/russianidiot/ismatch.py/archive/master.zip

	

	

	

Usage 
'''''
.. code-block::

	from ismatch import *

	ismatch("string","str*")
	>>> True

	ismatch("string",["str*","another pattern"]) # 2 patterns
	>>> True

	ismatch("string","string") # static pattern

------------

**Tested**: python 2.6, 2.7, 3+

**Bug Tracker**: `github.com/russianidiot/ismatch.py/issues`__

__ https://github.com/russianidiot/ismatch.py/issues