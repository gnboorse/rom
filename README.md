# rom

[![PyPI](https://img.shields.io/pypi/v/gnboorse-rom)](https://pypi.org/project/gnboorse-rom/)

This is a basic Roman numeral manipulation library written in Python.

It is capable of parsing Arabic numerals into Roman numerals, as well as generating Roman numerals from Arabic numerals.

## Installation

```sh
pip3 install gnboorse-rom
```

## Usage

```python
>>> from rom import rom
>>> rom(12)
XII
>>> int(rom(12))
12
>>> int(rom('xlvi'))
46
>>> rom('XLVI', caps=False)
xlvi
```
