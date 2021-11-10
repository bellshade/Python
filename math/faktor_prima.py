from __future__ import annotations


def faktor_prima(n: int) -> list[int]:
    """
    mengembalikan bilangan faktor prima
    dalam list

    >>> faktor_prima(0)
    []
    >>> faktor_prima(100)
    [2, 2, 5, 5]
    >>> faktor_prima(10**-2)
    []
    """
    i = 2
    faktor = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= 1
            faktor.append(i)

    if n > 1:
        faktor.append(n)
    return faktor


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
