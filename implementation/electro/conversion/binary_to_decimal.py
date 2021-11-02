def binary_to_decimal(bin_string: str) -> int:
    """
    >>> binary_to_decimal("101")
    5
    >>> binary_to_decimal(" 1010   ")
    10
    >>> binary_to_decimal("-11101")
    -29
    >>> binary_to_decimal("0")
    0
    >>> binary_to_decimal("a")
    Traceback (most recent call last):
    ...
    ValueError: bukan bilangan biner
    >>> binary_to_decimal("")
    Traceback (most recent call last):
    ...
    ValueError: Tidak ada yang diinputkan
    >>> binary_to_decimal("39")
    Traceback (most recent call last):
    ...
    ValueError: bukan bilangan biner
    """
    bin_string = str(bin_string).strip()
    if not bin_string:
        raise ValueError("Tidak ada yang diinputkan")
    is_negative = bin_string[0] == "-"
    if is_negative:
        bin_string = bin_string[1:]
    if not all(char in "01" for char in bin_string):
        raise ValueError("bukan bilangan biner")
    decimal_number = 0
    for char in bin_string:
        decimal_number = 2 * decimal_number + int(char)
    return -decimal_number if is_negative else decimal_number


if __name__ == "__main__":
    import doctest

    doctest.testmod()
