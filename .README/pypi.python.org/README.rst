.. README generated with readmemako.py (github.com/russianidiot/readme-mako.py) and .README dotfiles (github.com/russianidiot-dotfiles/.README)

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
