# python-learning
Learning Python

## Decimal speed
```python
from timeit import Timer
import platform


def run(val, the_class):
    test = the_class(29.074)
    for c in range(10000):
        d = the_class(val)
        d + test
        d - test
        d * test
        d / test
        d ** 2
        #str(d)
        abs(d)


if __name__ == '__main__':
    print('Python', platform.python_version(), 'running on', platform.system(), platform.release(), f'({platform.machine()})')
    a = Timer("run(123.345, float)", "from decimal_speed import run")
    print('FLOAT', a.timeit(1))
    b = Timer("run('123.345', Decimal)", "from decimal_speed import run; from decimal import Decimal")
    print('DECIMAL', b.timeit(1))
    print('DECIMAL / FLOAT', b.timeit(1) / a.timeit(1))
    c = Timer("run('123.345', np.float64)", "from decimal_speed import run; import numpy as np")
    print('np.float64', b.timeit(1))
    print('np.float64 / FLOAT', c.timeit(1) / a.timeit(1))

```
Output:
```shell
Python 3.8.5 running on Windows 10 (AMD64)
FLOAT 0.002470800000000002
DECIMAL 0.010187999999999996
DECIMAL / FLOAT 4.114297188755033
np.float64 0.010377499999999998
np.float64 / FLOAT 1.8912895338116917
```

## Decimal precision
```shell
-- Precision
<class 'float'>
0.3333333333333333
-----------------------
<class 'decimal.Decimal'>
0.3333333333333333333333333333

-- Calculation
with x = 0.1 + 0.1 + 0.1:
  x == 0.3 is False
  x = 0.30000000000000004
----------------------
with x = Decimal('0.1') + Decimal('0.1') + Decimal('0.1'):
  x == Decimal('0.3') is True
  float(x) == 0.3 is True
  x = 0.3
```
The Decimal has a default precision of 28 places, while the float has 18 places.

Read more at https://zetcode.com/python/decimal/
