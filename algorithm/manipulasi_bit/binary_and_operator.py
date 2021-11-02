# fungsi binary and operator
# https://www.tutorialspoint.com/python3/bitwise_operators_example.htm


def binary_and(a: int, b: int) -> str:
    """
    Ambil 2 bilangan bulat, ubah menjadi biner,
    mengembalikan bilangan biner yaitu
    hasil dari binary_and operasi pada bilangan
    bulat yang disediakan.
    >>> binary_and(25, 32)
    '0b000000'
    >>> binary_and(37, 50)
    '0b100000'
    >>> binary_and(21, 30)
    '0b10100'
    >>> binary_and(58, 73)
    '0b0001000'
    >>> binary_and(0, 255)
    '0b00000000'
    >>> binary_and(256, 256)
    '0b100000000'
    >>> binary_and(0, -1)
    Traceback (most recent call last):
    ...
    ValueError: Kedua bilangan harus positif
    >>> binary_and(-1,  0)
    Traceback (most recent call last):
    ...
    ValueError: Kedua bilangan harus positif
    """

    if a < 0 or b < 0:
        raise ValueError("Kedua bilangan harus positif")

    a_binary = str(bin(a))[2:]
    b_binary = str(bin(b))[2:]

    max_binary = max(len(a_binary), len(b_binary))

    return "0b" + "".join(
        str(int(char_a == "1" and char_b == "1"))
        for char_a, char_b in zip(
            a_binary.zfill(max_binary), b_binary.zfill(max_binary)
        )
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
