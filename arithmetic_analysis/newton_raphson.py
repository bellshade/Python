# Metode Newton-Raphson adalah metode pencarian akar suatu fungsi
# f(x) dengan pendekatan satu titik,
# dimana fungsi f(x) mempunyai turunan.
# Metode ini dianggap lebih mudah dari Metode Bagi-Dua (Bisection Method),
# karena metode ini menggunakan pendekatan satu titik sebagai titik awal.

from __future__ import annotations
from decimal import Decimal
from math import *  # noqa: F401, F403
from sympy import diff


def newton_raphson(func: str, a: float | Decimal, pres: float = 10 ** -10) -> float:
    """
    Menemukan akar dari titik 'a' dan seterusnya dengan metode Newton-Raphson
    >>> newton_raphson("sin(x)", 2)
    3.1415926536808043
    >>> newton_raphson("x**2 - 5*x +2", 0.4)
    0.4384471871911695
    >>> newton_raphson("x**2 - 5", 0.1)
    2.23606797749979
    >>> newton_raphson("log(x)- 1", 2)
    2.718281828458938
    """
    x = a
    while True:
        x = Decimal(x) - (Decimal(eval(func)) / Decimal(eval(str(diff(func)))))
        if abs(eval(func)) < pres:
            return float(x)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
