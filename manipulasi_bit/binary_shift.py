# informasi tentang binary shift
# https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types


def logic_left_shift(a: int, b: int) -> str:
    """
    Ambil 2 bilangan integer positif.
    'a' adalah bilangan integer yang secara logis dibiarkan bergeser
    sebanyak 'shift_amount' kali.
    Yaitu (a << b) Kembalikan representasi biner yang bergeser.
    >>> logic_left_shift(0, 1)
    '0b00'
    >>> logic_left_shift(1, 1)
    '0b10'
    >>> logic_left_shift(1, -5)
    Traceback (most recent call last):
    ...
    ValueError: Bilangan harus positif
    """
    if a < 0 or b < 0:
        raise ValueError("Bilangan harus positif")
    binary_number = str(bin(a))
    binary_number += "0" * b
    return binary_number


def logic_right_shift(a: int, b: int) -> str:
    """
    Ambil 2 bilangan integer positif.
    'a' adalah bilangan integer yang secara logis dibiarkan bergeser
    sebanyak 'shift_amount' kali.
    Yaitu (a >>> b) Kembalikan representasi biner yang bergeser.
    >>> logic_right_shift(0, 1)
    '0b0'
    >>> logic_right_shift(1, 1)
    '0b0'
    >>> logic_right_shift(1, 5)
    '0b0'
    >>> logic_right_shift(17, 2)
    '0b100'
    >>> logic_right_shift(1, -1)
    Traceback (most recent call last):
    ...
    ValueError: Bilangan harus positif
    """
    if a < 0 or b < 0:
        raise ValueError("Bilangan harus positif")
    binary_number = str(bin(a))[2:]
    if b >= len(binary_number):
        return "0b0"
    shifted_bin_number = binary_number[: len(binary_number) - b]
    return "0b" + shifted_bin_number


def arithmetic_right_shift(a: int, b: int) -> str:
    """
    Ambil dalam 2 bilangan bulat.
    'angka' adalah bilangan bulat
    yang secara aritmatika benar bergeser 'shift_amount' kali.
    Yaitu (nomor >> shift_amount)
    Kembalikan representasi biner yang bergeser.
    >>> arithmetic_right_shift(0, 1)
    '0b00'
    >>> arithmetic_right_shift(1, 1)
    '0b00'
    >>> arithmetic_right_shift(-1, 1)
    '0b11'
    >>> arithmetic_right_shift(17, 2)
    '0b000100'
    >>> arithmetic_right_shift(-17, 2)
    '0b111011'
    >>> arithmetic_right_shift(-1983, 4)
    '0b111110000100'
    """
    if a >= 0:
        binary_number = "0" + str(bin(a).strip("-"))[2:]
    else:
        binary_number_len = len(bin(a)[3:])
        binary_number = bin(abs(a) - (1 << binary_number_len))[3:]
        binary_number = (
            "1" + "0" * (binary_number_len - len(binary_number)) + binary_number
        )
    if b >= len(binary_number):
        return "0b" + binary_number[0] * len(binary_number)
    return "0b" + binary_number[0] * b + binary_number[: len(binary_number) - b]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
