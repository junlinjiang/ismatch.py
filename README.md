![python](https://img.shields.io/badge/language-python-blue.svg)[![PyPI](https://img.shields.io/pypi/pyversions/ismatch.svg)](https://pypi.python.org/pypi/ismatch)
[![landscape.io](https://landscape.io/github/russianidiot/ismatch.py/master/landscape.svg?style=flat)](https://landscape.io/github/russianidiot/ismatch.py/master)
[![Code Health](https://scrutinizer-ci.com/g/russianidiot/ismatch.py/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/russianidiot/ismatch.py)

[![Build Status](https://travis-ci.org/russianidiot/ismatch.py.svg?branch=master)](https://travis-ci.org/russianidiot/ismatch.py)[![drone.io](https://drone.io/github.com/russianidiot/ismatch.py/status.png)](https://drone.io/github.com/russianidiot/ismatch.py)[![codeship](https://img.shields.io/codeship/0b248fb0-e323-0133-366f-420e2277e1c8.svg)](https://codeship.com/projects/145865)[![Wercker](https://img.shields.io/wercker/ci/russianidiot/ismatch.py.svg)](https://app.wercker.com/#applications/None/)

[![PyPI](https://img.shields.io/pypi/v/ismatch.svg)](https://pypi.python.org/pypi/ismatch)
[![PyPI](https://img.shields.io/pypi/dm/ismatch.svg)](https://pypi.python.org/pypi/ismatch)
[![PyPI](https://img.shields.io/pypi/dd/ismatch.svg)](https://pypi.python.org/pypi/ismatch)

<p align="center">
	<b>ismatch(string,pattern) function - True if string match pattern(s). pattern types: string, wildcard, regex</b>
</p>

#### Install

pip: 
`[sudo] pip install ismatch`

#### Usage

```python
from ismatch import *

>>> ismatch("string","str*")
True

>>> ismatch("string",["str*","another pattern"]) # 2 patterns
True

>>> ismatch("string","string") # static pattern
```

[Examples/](https://github.com/russianidiot/ismatch.py/tree/master/Examples)

Sources:
*	[py_modules/ismatch.py](https://github.com/russianidiot/ismatch.py/blob/master/py_modules/ismatch.py)

Feedback
[![GitHub issues](https://img.shields.io/github/issues/russianidiot/ismatch.py.svg)](https://github.com/russianidiot/ismatch.py/issues)
[![Join the chat at https://gitter.im/russianidiot/ismatch.py](https://badges.gitter.im/russianidiot/ismatch.py.svg)](https://gitter.im/russianidiot/ismatch.py)
[![GitHub followers](https://img.shields.io/github/followers/russianidiot.svg?style=social&label=Follow)](https://github.com/russianidiot)

* * *

<p align="center">
	Python packages <a href="http://russianidiot.github.io/python/">russianidiot.github.io/python/</a>
	<img src="http://russianidiot.github.io/images/python/16.png" />
</p>
<p align="center">
	cli packages <a href="http://russianidiot.github.io/python/">russianidiot.github.io/cli/</a>
<img src="http://russianidiot.github.io/images/cli/16.png" />
</p>

<p align="center">
	repos list <a href="http://russianidiot.github.io/">russianidiot.github.io</a> <img src="http://russianidiot.github.io/images/star/16.png" />
</p>

<p align="center">
	<a href="https://raw.githubusercontent.com/russianidiot/ismatch.py/master/README.md">README.md</a> generated with <a href="https://github.com/russianidiot/readme-mako.py">readmemako.py</a> (python+<a href="http://www.makotemplates.org/">mako</a> templates) and <a href="https://github.com/russianidiot-dotfiles/.README">.README</a> dotfiles 
<img src="http://russianidiot.github.io/images/book/16.png">
</p>
