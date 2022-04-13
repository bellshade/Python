# metode newton https://en.wikipedia.org/wiki/Newton%27s_metho
from typing import Callable

function_real = Callable[[float], float]


def newton(
    function: function_real, derivative: function_real, starting_int: int
) -> float:
    """
    >>> newton(lambda x: x ** 3 - 2 * x - 5, lambda x: 3 * x ** 2 - 2, 3)
    2.0945514815423474
    >>> newton(lambda x: x ** 3 - 1, lambda x: 3 * x ** 2, -2)
    1.0
    >>> newton(lambda x: x ** 3 - 1, lambda x: 3 * x ** 2, -4)
    1.0000000000000102
    >>> import math
    >>> newton(math.sin, math.cos, 1)
    0.0
    >>> newton(math.sin, math.cos, 2)
    3.141592653589793
    >>> newton(math.cos, lambda x: -math.sin(x), 2)
    1.5707963267948966
    >>> newton(math.cos, lambda x: -math.sin(x), 0)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: tidak dapat menemukan akar
    """
    prev_guess = float(starting_int)
    while True:
        try:
            next_guess = prev_guess - function(prev_guess) / derivative(prev_guess)
        except ZeroDivisionError:
            raise ZeroDivisionError("tidak dapat menemukan akar") from None
        if abs(prev_guess - next_guess) < 10**-5:
            return next_guess
        prev_guess = next_guess


def f(x: float) -> float:
    return (x**3) - (2 * x) - 5


def f1(x: float) -> float:
    return 3 * (x**2) - 2


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    # print(newton(f, f1, 3))
