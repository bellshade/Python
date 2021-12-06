# Saringan Eratosthenes adalah algoritma yang digunakan
# untuk mencari bilangan prima, kurang dari atau
# sama dengan nilai yang diberikan.
# informasi lebih lanjut
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

from __future__ import annotations

import math


def prime_sieve(angka: int) -> list[int]:
    """
    mengembalikan daftar dengan semua bilangan prima
    hingga ke n
    >>> prime_sieve(25)
    [2, 3, 5, 7, 11, 13, 17, 19, 23]
    >>> prime_sieve(10)
    [2, 3, 5, 7]
    >>> prime_sieve(2)
    [2]
    >>> prime_sieve(1)
    []
    """
    if angka <= 0:
        raise ValueError("angka harus positif atau tidak boleh 0")

    sieve = [True] * (angka + 1)
    prime = []
    start = 2
    end = int(math.sqrt(angka))

    while start <= end:
        if sieve[start] is True:
            prime.append(start)

            # atur kelipatan awal menjadi false
            for i in range(start * start, angka + 1, start):
                if sieve[i] is True:
                    sieve[i] = False

        start += 1

    for j in range(end + 1, angka + 1):
        if sieve[j] is True:
            prime.append(j)

    return prime


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
