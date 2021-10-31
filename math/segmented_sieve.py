# segmented sieve

from __future__ import annotations

import math


def sieve(n: int) -> tuple:
    """
    >>> sieve(2 **3)
    (2, 3, 5, 7)

    >>> sieve(3 ** 3)
    (2, 3, 5, 7, 11, 13, 17, 19, 23)

    >>> sieve(4)
    (2, 3)
    """
    in_prime = []
    start = 2
    end = int(math.sqrt(n))
    temp = [True] * (end + 1)
    prime = []

    while start <= end:
        if temp[start] is True:
            in_prime.append(start)
            for i in range(start * start, end + 1, start):
                if temp[i] is True:
                    temp[i] = False

        start += 1
    prime += in_prime

    low = end + 1
    high = low + end - 1
    if high > n:
        high = n

    while low <= n:
        temp = [True] * (high - low + 1)
        for each in in_prime:
            t = math.floor(low / each) * each
            if t < low:
                t += each

            for j in range(t, high + 1, each):
                temp[j - low] = False

        for j in range(len(temp)):
            if temp[j] is True:
                prime.append(low + j)

        low = high + 1
        high = low + end - 1

        if high > n:
            high = n

    return tuple(prime)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    # print(sieve(4))
