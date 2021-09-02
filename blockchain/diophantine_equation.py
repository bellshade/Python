# https://en.wikipedia.org/wiki/Diophantine_equation

from typing import Tuple


def diophantine(a: int, b: int, c: int) -> Tuple[float, float]:
    """
    Persamaan Diophantine : Diberikan bilangan bulat a,b,c
    ( setidaknya satu dari a dan b != 0),
    persamaan diophantine a*x + b*y = c
    memiliki solusi (di mana x dan y adalah bilangan bulat)
    jika gcd(a,b) membagi c.
    >>> diophantine(10,6,14)
    (-7.0, 14.0)
    >>> diophantine(391,299,-69)
    (9.0, -12.0)
    """
    assert c % greatest_common_divisor(a, b) == 0
    (d, x, y) = extended_gcd(a, b)
    r = c / d
    return (r * x, r * y)


def diophantine_all_soln(a: int, b: int, c: int, n: int = 2) -> None:
    """
    Menemukan Semua solusi Persamaan Diophantine:

    Teorema : Misalkan gcd(a,b) = d, a = d*p, b = d*q.
    Jika (x0,y0) adalah solusi dari
    Persamaan Diophantine a*x + b*y = c. a*x0 + b*y0 = c, maka semua
    solusi memiliki bentuk a(x0 + t*q) + b(y0 - t*p) = c,
    di mana t adalah bilangan bulat arbitrer.
    >>> diophantine_all_soln(10, 6, 14)
    -7.0 14.0
    -4.0 9.0
    >>> diophantine_all_soln(10, 6, 14, 4)
    -7.0 14.0
    -4.0 9.0
    -1.0 4.0
    2.0 -1.0
    >>> diophantine_all_soln(391, 299, -69, n = 4)
    9.0 -12.0
    22.0 -29.0
    35.0 -46.0
    48.0 -63.0
    """
    (x0, y0) = diophantine(a, b, c)
    d = greatest_common_divisor(a, b)
    p = a // d
    q = b // d

    for i in range(n):
        x = x0 + i * q
        y = y0 - i * p
        print(x, y)


def greatest_common_divisor(a: int, b: int) -> int:
    """
    >>> greatest_common_divisor(7, 5)
    1
    """
    if a < b:
        a, b = b, a

    while a % b != 0:
        a, b = b, a % b

    return b


def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """
    Extended Euclid's Algorithm :
    Jika d membagi a dan b dan d = a*x + b*y untuk bilangan bulat
    x dan y, maka d = gcd(a,b)
    >>> extended_gcd(10, 6)
    (2, -1, 2)
    """
    assert a >= 0 and b >= 0

    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)

    assert a % d == 0 and b % d == 0
    assert d == a * x + b * y

    return (d, x, y)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
