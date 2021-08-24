def get_reverse_bit(number: int) -> str:
    """
    return bit string dari integer
    >>> get_reverse_bit(9)
    '10010000000000000000000000000000'
    >>> get_reverse_bit(43)
    '11010100000000000000000000000000'
    >>> get_reverse_bit(2873)
    '10011100110100000000000000000000'
    >>> get_reverse_bit(9)
    '10010000000000000000000000000000'
    >>> get_reverse_bit(43)
    '11010100000000000000000000000000'
    >>> get_reverse_bit(2873)
    '10011100110100000000000000000000'
    """
    if not isinstance(number, int):
        raise TypeError("number harus integer")
    bit_string = ""
    for _ in range(0, 32):
        bit_string += str(number % 2)
        number = number >> 1
    return bit_string


def reverse_bit(number: int) -> str:
    """
    return string bit dari angka integer 32 bit
    >>> reverse_bit(25)
    '00000000000000000000000000011001'
    >>> reverse_bit(37)
    '00000000000000000000000000100101'
    >>> reverse_bit(21)
    '00000000000000000000000000010101'
    >>> reverse_bit(58)
    '00000000000000000000000000111010'
    >>> reverse_bit(0)
    '00000000000000000000000000000000'
    >>> reverse_bit(256)
    '00000000000000000000000100000000'
    >>> reverse_bit(-23)
    Traceback (most recent call last):
    ...
    ValueError: Angka harus positif
    >>> reverse_bit(23.5)
    Traceback (most recent call last):
    ...
    ValueError: Angka harus integer
    """
    if number < 0:
        raise ValueError("Angka harus positif")
    elif isinstance(number, float):
        raise ValueError("Angka harus integer")
    elif isinstance(number, str):
        raise TypeError("'<' tidak support antara 'str' dan 'int'")
    result = 0

    for _ in range(1, 33):
        result = result << 1
        end_bit = number % 2
        number = number >> 1
        result = result | end_bit

    return get_reverse_bit(result)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
