<p align="center">
	<b>ismatch(string,pattern) - True if string match pattern(s). pattern types: string, wildcard, regex</b>
</p>

<p>
	<a href="https://travis-ci.org/b'russianidiot'/ismatch.py" class="reference external">
		<img src="https://travis-ci.org/b'russianidiot'/ismatch.py.svg?branch=master" alt="Build Status">
	</a>
	<!--
	<a href="https://codecov.io/github/b'russianidiot'/ismatch.py/">
		<img src="https://img.shields.io/codecov/c/github/b'russianidiot'/ismatch.py.svg" alt="Codecov">
	</a>
	-->
</p>
<p>
	<a href="http://badge.fury.io/py/ismatch" class="reference external">
		<img src="https://badge.fury.io/py/ismatch.svg" alt="PyPI version">
	</a>
	<a href="https://pypi.python.org/pypi/ismatch">
		<img src="https://img.shields.io/pypi/pyversions/ismatch.svg" alt="PyPI">
	</a>

</p>

	
Install
-------

[github.com](http://github.com/b'russianidiot'/ismatch.py):
`pip install git+git://github.com/b'russianidiot'/ismatch.py.git`

[pypi.python.org](https://pypi.python.org): `pip install ismatch`

[download](https://github.com/b'russianidiot'/ismatch.py/archive/master.zip): `python setup.py install` or `setup/.setup.py develop.command` 

	

	

Usage 
=====
```
from ismatch import *

ismatch("string","str*")
>>> True

ismatch("string",["str*","another pattern"]) # 2 patterns
>>> True

ismatch("string","string") # static pattern
>>> True
```

---

**Tested**: python 2.6, 2.7, 3+

---

<p align="center">
my Python packages 
<a href="http://b'russianidiot'.github.io/python/packages">b'russianidiot'.github.io/python/packages</a> <img src="http://b'russianidiot'.github.io/images/python/16.png" />
</p>
<p align="center">
my Python repos <a href="http://b'russianidiot'.github.io/python/">b'russianidiot'.github.io/python/</a>
<img src="http://b'russianidiot'.github.io/images/python/16.png" />
</p>

<p align="center">
	all repos <a href="http://b'russianidiot'.github.io/">b'russianidiot'.github.io</a> <img src="http://b'russianidiot'.github.io/images/star/16.png" />
</p>

<p align="center">
	README.md generated with <a href="https://github.com/b'russianidiot'/README.mako.py.automation">README.mako.py.automation</a> + <a href="https://github.com/b'russianidiot'/.README.mako">.README.mako</a> 
<img src="http://b'russianidiot'.github.io/images/book/16.png">
</p>

<p align="center">
	follow me <a href="http://github.com/b'russianidiot'">github.com/b'russianidiot'</a>
<img src="http://b'russianidiot'.github.io/images/github/16.png" />
</p>