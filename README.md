<p align="center">
	<b>ismatch(string,pattern) function - True if string match pattern(s). pattern types: string, wildcard, regex</b>
</p>

[![Build Status](https://travis-ci.org/russianidiot/ismatch.py.svg?branch=master)](https://travis-ci.org/russianidiot/ismatch.py)[![PyPI](https://img.shields.io/pypi/v/ismatch.svg)](https://pypi.python.org/pypi/ismatch)
[![PyPI](https://img.shields.io/pypi/pyversions/ismatch.svg)](https://pypi.python.org/pypi/ismatch)[![PyPI](https://img.shields.io/pypi/dm/ismatch.svg)](https://pypi.python.org/pypi/ismatch)[![PyPI](https://img.shields.io/pypi/dw/ismatch.svg)](https://pypi.python.org/pypi/ismatch)[![PyPI](https://img.shields.io/pypi/dd/ismatch.svg)](https://pypi.python.org/pypi/ismatch)

	

### Install

[github.com](http://github.com/russianidiot/ismatch.py):
`pip install git+git://github.com/russianidiot/ismatch.py.git`

[pypi.python.org](https://pypi.python.org/pypi/ismatch/): `pip install ismatch`

[download](https://github.com/russianidiot/ismatch.py/archive/master.zip): `[ -e requirements.txt ] && pip install -r requirements.txt; python setup.py install`

	

	

	

### Usage

```python
from ismatch import *

>>> ismatch("string","str*")
True

>>> ismatch("string",["str*","another pattern"]) # 2 patterns
True

>>> ismatch("string","string") # static pattern
```

* * *

### Feedback

[![GitHub issues](https://img.shields.io/github/issues/russianidiot/ismatch.py.svg)](https://github.com/russianidiot/ismatch.py/issues) - Github Issues

[![Join the chat at https://gitter.im/russianidiot/ismatch.py](https://badges.gitter.im/russianidiot/ismatch.py.svg)](https://gitter.im/russianidiot/ismatch.py) - Chat (english/russian) 

* * *

<p align="center">
my Python packages <a href="http://russianidiot.github.io/python/">russianidiot.github.io/python/</a>
<img src="http://russianidiot.github.io/images/python/16.png" />
</p>

<p align="center">
	all my repos <a href="http://russianidiot.github.io/">russianidiot.github.io</a> <img src="http://russianidiot.github.io/images/star/16.png" />
</p>

<p align="center">
	follow me <a href="http://github.com/russianidiot">github.com/russianidiot</a>
<img src="http://russianidiot.github.io/images/github/16.png" />
</p>

<p align="center">
	<a href="https://raw.githubusercontent.com/russianidiot/ismatch.py/master/README.md">README.md</a> generated with <a href="https://github.com/russianidiot/readme-mako.py">readmemako.py</a> (python+<a href="http://www.makotemplates.org/">mako</a> templates) and <a href="https://github.com/russianidiot-dotfiles/.README">.README</a> dotfiles 
<img src="http://russianidiot.github.io/images/book/16.png">
</p>