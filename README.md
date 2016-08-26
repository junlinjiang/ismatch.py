<!--
README generated with readmemako.py (github.com/russianidiot/readme-mako.py) and .README dotfiles (github.com/russianidiot-dotfiles/.README)
-->

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
