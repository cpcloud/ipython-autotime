# ipython-autotime
Time everything in IPython

## Installation:

```console
$ pip install ipython-autotime
```

## Examples

```python
In [1]: %load_ext autotime
time: 295 µs

In [2]: x = 1
time: 519 µs

In [3]: x / 0
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-3-034eb0c6102b> in <module>
----> 1 x/0

ZeroDivisionError: division by zero
time: 79.7 ms
```

## Want to turn it off?

```python
In [4]: %unload_ext autotime
```
