from typing import Callable


def bisection(function: Callable[[float], float], a: float, b: float) -> float:
    """
    menemukan di mana fungsi menjadi 0 dalam [a,b] menggunakan bolzano
    >>> bisection(lambda x: x ** 3 - 1, -5, 5)
    1.0000000149011612
    >>> bisection(lambda x: x ** 3 - 1, 2, 1000)
    Traceback (most recent call last):
    ...
    ValueError: tidak dapat menemukan root dalam interval yang diberikan.
    >>> bisection(lambda x: x ** 2 - 4 * x + 3, 0, 2)
    1.0
    >>> bisection(lambda x: x ** 2 - 4 * x + 3, 2, 4)
    3.0
    >>> bisection(lambda x: x ** 2 - 4 * x + 3, 4, 1000)
    Traceback (most recent call last):
    ...
    ValueError: tidak dapat menemukan root dalam interval yang diberikan.
    """

    start: float = a
    end: float = b
    if function(a) == 0:
        return a
    elif function(b) == 0:
        return b
    elif function(a) * function(b) > 0:
        # jika tidak ada yang root dan keduanya positif atau negatif
        # maka algoritma ini tidak dapat menemukan root
        raise ValueError("tidak dapat menemukan root dalam interval yang diberikan.")
    else:
        mid: float = start + (end - start) / 2.0
        while abs(start - mid) > 10**-7:
            if function(mid) == 0:
                return mid
            elif function(mid) * function(start) < 0:
                end = mid
            else:
                start = mid
            mid = start + (end - start) / 2.0
        return mid


def float_float(x: float) -> float:
    return x**3 - 2 * x - 5


if __name__ == "__main__":
    print(bisection(float_float, 1, 1000))
    import doctest

    doctest.testmod()
