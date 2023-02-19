# python-learning
Learning Python

## Decimal speed
```python
from timeit import Timer

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


if __name__ == "__main__":
    a = Timer("run(123.345, float)", "from decimal_speed import run")
    print("FLOAT", a.timeit(1))
    b = Timer("run('123.345', Decimal)", "from decimal_speed import run; from decimal import Decimal")
    print("DECIMAL", b.timeit(1))
    print("DECIMAL / FLOAT", b.timeit(1) / a.timeit(1))
    c = Timer("run('123.345', np.float64)", "from decimal_speed import run; import numpy as np")
    print("np.float64", b.timeit(1))
    print("np.float64 / FLOAT", c.timeit(1) / a.timeit(1))
```
Output:
```shell
FLOAT 0.002489199999999997
DECIMAL 0.010443099999999997
DECIMAL / FLOAT 3.7357072494436063
np.float64 0.010137199999999999
np.float64 / FLOAT 1.8826756534346936
```

