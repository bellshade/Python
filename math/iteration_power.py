def iteration_power(number: int, exp: int) -> int:
    """
    Perpangkatan dengan metode iteratif atau perulangan
    rumus matematika: number^exp
    >>> iteration_power(2, 5)
    32
    >>> iteration_power(100, 0)
    1
    >>> iteration_power(0, 100)
    0
    >>> iteration_power(1, 100)
    1
    """
    result = 1
    for i in range(exp):
        result *= number
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Pangkat lebih dari 1
    print(iteration_power(number=2, exp=5))

    # Pangkat sama dengan 0
    print(iteration_power(number=100, exp=0))

    # Angka 0 dengan pangkat lebih dari 1
    print(iteration_power(number=0, exp=100))

    # Angka 1 dengan pangkat lebih dari 1
    print(iteration_power(number=1, exp=100))
