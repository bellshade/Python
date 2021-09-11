def get_set_bits(number: int) -> int:
    """
    hitung jumlah bit angka 1
    >>> get_set_bits(25)
    3
    >>> get_set_bits(52132)
    8
    >>> get_set_bits(-2)
    Traceback (most recent call last):
    ...
    ValueError: Angka tidak boleh negatif
    """
    if number < 0:
        raise ValueError("Angka tidak boleh negatif")
    result = 0

    while number:
        if number % 2 == 1:
            result += 1
        number = number >> 1
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
