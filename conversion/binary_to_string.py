def binary_to_string(binaryString: str):
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
    if not all(char in "01" for char in binaryString):
        raise ValueError("bukan bilangan biner")

    if type(binaryString) != str:
        raise ValueError("bukan string")

    elif len(binaryString) < 1:
        raise ValueError("tidak ada yang diinputkan")

    return "".join([chr(int(i, 2)) for i in binaryString.split()])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
