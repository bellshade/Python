# informasi tentang two complemen
# https://en.wikipedia.org/wiki/Two%27s_complement


def two_complement(num: int) -> str:
    """
    ambil angka integer negatif
    kemudian mengembalikan
    representasi complement dari 'num'
    >>> two_complement(0)
    '0b0'
    >>> two_complement(-1)
    '0b11'
    >>> two_complement(-5)
    '0b1011'
    >>> two_complement(-17)
    '0b101111'
    >>> two_complement(-207)
    '0b100110001'
    >>> two_complement(1)
    Traceback (most recent call last):
        ...
    ValueError: Angka harus negatif
    """
    if num > 0:
        raise ValueError("Angka harus negatif")
    binary_num_len = len(bin(num)[3:])
    two_complement_num = bin(abs(num) - (1 << binary_num_len))[3:]
    two_complement_num = (
        ("1" + "0" * (binary_num_len - len(two_complement_num)) + two_complement_num)
        if num < 0
        else "0"
    )
    return "0b" + two_complement_num


if __name__ == "__main__":
    import doctest

    doctest.testmod()
