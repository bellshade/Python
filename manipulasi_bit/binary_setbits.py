def binary_count(a: int) -> int:
    """
    ambil 1 bilangan integer
    dan kemudian mengambil angka
    yaitu jumlah bit yang berisi 1
    dalam representasi biner
    dari nomor itu
    contoh bilangan biner dari 25
    25 = 11001
    yang berarti 3 angka 1 dari 25
    >>> binary_count(25)
    3
    >>> binary_count(36)
    2
    >>> binary_count(16)
    1
    >>> binary_count(58)
    4
    >>> binary_count(4294967295)
    32
    >>> binary_count(0)
    0
    >>> binary_count(-10)
    Traceback (most recent call last):
    ...
    ValueError: Angka harus positif
    >>> binary_count(0.3)
    Traceback (most recent call last):
    ...
    TypeError: Input harus berupa tipe 'int'
    """
    if a < 0:
        raise ValueError("Angka harus positif")
    elif isinstance(a, float):
        raise TypeError("Input harus berupa tipe 'int'")
    return bin(a).count("1")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
