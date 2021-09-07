def binary_to_string(bin_string: str):
    """
    >>> binary_to_string("01100001")
    'a'
    >>> binary_to_string("a")
    Traceback (most recent call last):
    ...
    ValueError: bukan bilangan biner
    >>> binary_to_string("")
    Traceback (most recent call last):
    ...
    ValueError: tidak ada yang diinputkan
    >>> binary_to_string("39")
    Traceback (most recent call last):
    ...
    ValueError: bukan bilangan biner
    """
    if not all(char in "01" for char in bin_string):
        raise ValueError("bukan bilangan biner")

    if type(bin_string) != str:
        raise ValueError("bukan string")

    elif len(bin_string) < 1:
        raise ValueError("tidak ada yang diinputkan")

    return "".join([chr(int(i, 2)) for i in bin_string.split()])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
