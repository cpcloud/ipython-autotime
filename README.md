# ipython-autotime
Time everything in IPython

## Installation:

```
$ pip install ipython-autotime
```

## Examples

```python
In [1]: %load_ext autotime
time: 1433692.87 s

In [2]: x = 1
time: 730.99 us

In [3]: x + 2
Out[3]: 3
time: 2.50 ms

In [4]: x + ''
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-5-bde712cacec5> in <module>()
----> 1 x + ''

TypeError: unsupported operand type(s) for +: 'int' and 'str'
time: 156.05 ms
```

## Want to turn it off?

```python
In [5]: %unload_ext autotime
```
