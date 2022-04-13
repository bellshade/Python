import math


def intersection(function: Callable[[float], float], num1: float, num2: float) -> float:
    """
    fungsinya adalah f kita ingin mencari akarnya
    x0 dan x1, adalah 2 random starting point
    >>> intersection(lambda x: x** 3 - 1, -5, 5)
    0.9999999999954654
    >>> intersection(lambda x: x** 3 - 1, 5, 5)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: tidak bisa dibagikan dengan 0, tidak menemukan akar
    >>> intersection(lambda x: x ** 3 - 1, 100, 200)
    1.0000000000003888
    >>> intersection(lambda x: x ** 2 - 4 * x + 3, 0, 2)
    0.9999999998088019
    >>> intersection(lambda x: x ** 2 - 4 * x + 3, 2, 4)
    2.9999999998088023
    >>> intersection(lambda x: x ** 2 - 4 * x + 3, 4, 1000)
    3.0000000001786042
    >>> intersection(math.sin, -math.pi, math.pi)
    0.0
    >>> intersection(math.cos, -math.pi, math.pi)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: tidak bisa dibagikan dengan 0, tidak menemukan akar
    """
    x_number1: float = num1
    x_number2: float = num2

    while True:
        if x_number1 == x_number2 or function(x_number2) == function(x_number1):
            raise ZeroDivisionError(
                "tidak bisa dibagikan dengan 0, tidak menemukan akar"
            )
        x_number3: float = x_number2 - (
            function(x_number2)
            / ((function(x_number2) - function(x_number1)) / (x_number2 - x_number1))
        )
        if abs(x_number3 - x_number2) < 10**-5:
            return x_number3
        x_number1 = x_number2
        x_number2 = x_number3


def f(x: float) -> float:
    return math.pow(x, 3) - (2 * x) - 5


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    # print(intersection(f, 3, 3.5))
