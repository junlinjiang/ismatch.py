<!--
README generated with readmemako.py (github.com/russianidiot/readme-mako.py) and .README dotfiles (github.com/russianidiot-dotfiles/.README)
-->

![python](https://img.shields.io/badge/language-python-blue.svg)
[![PyPI](https://img.shields.io/pypi/pyversions/ismatch.svg)](https://pypi.python.org/pypi/ismatch)[![PyPI](https://img.shields.io/pypi/v/ismatch.svg)](https://pypi.python.org/pypi/ismatch)

[![codacy.com](https://api.codacy.com/project/badge/Grade/e58b4e41a8944871be85cd35f1626102)](https://www.codacy.com/app/russianidiot-github/ismatch-py/dashboard)
[![landscape.io](https://landscape.io/github/russianidiot/ismatch.py/master/landscape.svg?style=flat)](https://landscape.io/github/russianidiot/ismatch.py)
[![codeclimate.com](https://codeclimate.com/github/russianidiot/ismatch.py/badges/gpa.svg)](https://codeclimate.com/github/russianidiot/ismatch.py)
[![scrutinizer-ci.com](https://scrutinizer-ci.com/g/russianidiot/ismatch.py/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/russianidiot/ismatch.py/)

[![codecov.io](https://codecov.io/github/russianidiot/ismatch.py/coverage.svg?branch=master)](https://codecov.io/github/russianidiot/ismatch.py?branch=master)
[![drone.io](https://drone.io/github.com/russianidiot/ismatch.py/status.png)](https://drone.io/github.com/russianidiot/ismatch.py)
[![scrutinizer-ci.com](https://scrutinizer-ci.com/g/russianidiot/ismatch.py/badges/build.png?b=master)](https://scrutinizer-ci.com/g/russianidiot/ismatch.py/)
[![semaphoreci.com](https://semaphoreci.com/api/v1/russianidiot/ismatch-py/branches/master/shields_badge.svg)](https://semaphoreci.com/russianidiot/ismatch-py)
[![shippable.com](https://api.shippable.com/projects/57068cbb2a8192902e1bbbc0/badge?branch=master)](https://app.shippable.com/projects/57068cbb2a8192902e1bbbc0/status/)
[![travis-ci.org](https://api.travis-ci.org/russianidiot/ismatch.py.svg)](https://travis-ci.org/russianidiot/ismatch.py)
[![wercker.com](https://app.wercker.com/status/49064affcb33a7cfaf6cc64a8b06c27a/s/master)](https://app.wercker.com/#applications/570bf0fb3f1a8913740466d7)

<p align="center">
    <b>ismatch(string,pattern) function - True if string match pattern(s). pattern types: string, wildcard, regex</b>
</p>

#### Install

`[sudo] pip install ismatch`

#### Usage

```python
>>> from ismatch import ismatch

>>> ismatch(string,pattern)
```

#### Example

```python
>>> ismatch("string","str*")
True

>>> ismatch("string",["str*","another pattern"]) # 2 patterns
True

>>> ismatch("string","string") # static pattern
True
```

[Examples/](https://github.com/russianidiot/ismatch.py/tree/master/Examples)

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
	cli packages <a href="http://russianidiot.github.io/cli/">russianidiot.github.io/cli/</a>
<img src="http://russianidiot.github.io/images/cli/16.png" />
</p>

<p align="center">
	repos list <a href="http://russianidiot.github.io/">russianidiot.github.io</a> <img src="http://russianidiot.github.io/images/star/16.png" />
</p>
