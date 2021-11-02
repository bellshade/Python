from math import log2


def binary_count_trailing_zero(a: int) -> int:
    """
    Ambil 1 integer,
    kembalikan angka yang merupakan jumlah nol trailing
    dalam representasi biner dari angka itu.
    contoh
    angka 25 = 11001 angka 0 akhir dari 1 tidak ada 0
    angka 36 = 100100 angka dari akhir 1 ada 0 mulai dibaca
    100 < 1 100 < 2 = 2
    angka 16 = 10000 angka 0 akhir dari 1 ada 5
    1 0 < 1 0 < 2 0 < 3 0 < 4 maka jumlah 4
    >>> binary_count_trailing_zero(25)
    0
    >>> binary_count_trailing_zero(36)
    2
    >>> binary_count_trailing_zero(16)
    4
    >>> binary_count_trailing_zero(-10)
    Traceback (most recent call last):
    ...
    ValueError: Angka harus positif.
    >>> binary_count_trailing_zero(2.3)
    Traceback (most recent call last):
    ...
    TypeError: Angka harus integer.
    """
    if a < 0:
        raise ValueError("Angka harus positif.")
    elif isinstance(a, float):
        raise TypeError("Angka harus integer.")
    return 0 if (a == 0) else int(log2(a & -a))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
