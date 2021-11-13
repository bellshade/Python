def recursion_power(number: int, exp: int, result: int = 1) -> int:
    """
    Perpangkatan dengan metode rekursif
    rumus matematika: number^exp
    >>> recursion_power(2, 5)
    32
    >>> recursion_power(100, 0)
    1
    >>> recursion_power(0, 100)
    0
    >>> recursion_power(1, 100)
    1
    """
    if exp < 1:
        return result
    else:
        return recursion_power(number, exp - 1, result * number)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Pangkat lebih dari 1
    print(recursion_power(number=2, exp=5))

    # Pangkat sama dengan 0
    print(recursion_power(number=100, exp=0))

    # Angka 0 dengan pangkat lebih dari 1
    print(recursion_power(number=0, exp=100))

    # Angka 1 dengan pangkat lebih dari 1
    print(recursion_power(number=1, exp=100))
