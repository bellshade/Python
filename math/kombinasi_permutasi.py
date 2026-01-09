# https://en.wikipedia.org/wiki/Combination
# https://en.wikipedia.org/wiki/Permutation

def faktorial(n : int) -> int:
    """
    Fungsi untuk menghitung faktorial

    >>> faktorial(5)
    120
    """
    if n <= 0:
        return ValueError("Nilai tidak boleh kurang dari nol")
    else:
        f = 1
        for i in range(1, n + 1):
            f *= i
        return f


def kombinasi(n : int, r : int) -> int:
    """
    Fungsi untuk kalkulasi kombinasi

    >>> kombinasi(5, 2)
    10.0
    """
    if n <= 0 or r <= 0:
        return ValueError("Nilai tidak boleh kurang dari nol")
    else:
        penyebut = faktorial(n)
        pembilang = faktorial(r) * faktorial(n - r)
        return penyebut / pembilang


def permutasi(n : int, r : int) -> int:
    """
    Fungsi untuk kalkulasi permutasi

    >>> permutasi(6, 2)
    30.0
    """
    if n <= 0 or r <= 0:
        return ValueError("Nilai tidak boleh kurang dari nol")
    else:
        penyebut = faktorial(n)
        pembilang = faktorial(n - r)
        return penyebut / pembilang


def main(args=None):
    import doctest

    doctest.testmod()


if __name__ == "__main__":
    main()
