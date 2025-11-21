# Composite number adalah angka yang bukan prima
# https://en.wikipedia.org/wiki/Composite_number
import math


def compositer_number(number: int) -> int | str:
    """
    Fungsi ini membuat daftar compositer number sesuai range
    tertentu.

    >>> compositer_number(2)
    'Bukan angka compositer'
    >>> compositer_number(10)
    [4, 6, 8, 9, 10]
    """
    bukan = "Bukan angka compositer"
    if number < 4:
        return bukan

    list_number = [False] * (number + 1)
    p = 2

    while p * p <= number:
        if not list_number[p]:

            for i in range(p * p, number + 1, p):
                list_number[i] = True

        p += 1

    result = []

    for p in range(4, number + 1):
        if list_number[p]:
            result.append(p)

    return result


def is_compositor(number: int) -> str:
    """
    Fungsi ini mengecek apakah bilangan ini termasuk compositor
    atau tidak.

    >>> is_compositor(8)
    'Angka compositor'
    >>> is_compositor(6)
    'Angka compositor'
    >>> is_compositor(5)
    'Bukan Angka Compositor'
    >>> is_compositor(7)
    'Bukan Angka Compositor'

    """
    benar, bukan = "Angka compositor", "Bukan Angka Compositor"
    if number < 4:
        return bukan

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return benar

    return bukan


def main(args=None):
    import doctest

    doctest.testmod()

    # sample test
    print(compositer_number(2))  # Bukan angka compositer
    print(compositer_number(10))  # [4, 6, 8, 9, 10]
    print("\n")
    print(is_compositor(8))  # Angka Compositor
    print(is_compositor(6))  # Angka Compositor
    print(is_compositor(5))  # Bukan Angka Compositor
    print(is_compositor(7))  # Bukan Angka Compositor


if __name__ == "__main__":
    main()
