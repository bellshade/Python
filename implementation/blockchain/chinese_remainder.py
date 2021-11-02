# chinese remainder theorem adalah salah satu teori algoritma yang berfungsi
# untuk mempercepat dan meningkatkan efisiensi performa sistem kriptografi RSA
# https://en.wikipedia.org/wiki/Chinese_remainder_theorem

from typing import Tuple


def extended_euclid(a: int, b: int) -> Tuple[int, int]:
    """
    >>> extended_euclid(10, 6)
    (-1, 2)
    """
    if b == 0:
        return (1, 0)
    (x, y) = extended_euclid(b, a % b)
    k = a // b
    return (y, x - k * y)


def chinese_remainder(n1: int, r1: int, n2: int, r2: int) -> int:
    """
    >>> chinese_remainder(5,1,7,3)
    31

    penjelasan : 31 adalah nomor yang paling kecil
    ketika dibagi dengan 5 kita dapat hasil bagi 1
    ketika dibagi dengan 7 kita dapat hasil bagi 3
    """
    (x, y) = extended_euclid(n1, n2)
    m = n1 * n2
    n = r2 * x * n1 + r1 * y * n2
    return (n % m + m) % m


if __name__ == "__main__":
    import doctest

    doctest.testmod()
