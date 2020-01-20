# rom

This is a basic roman numeral parser written in Python.

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
