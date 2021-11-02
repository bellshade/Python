# informasi tentang binary xor
# https://www.tutorialspoint.com/python3/bitwise_operators_example.htm


def binary_xor(a: int, b: int) -> str:
    """
    ambil 2 bilangan integer
    return bilangan biner
    yang merupakan hasil dari binary xor
    pada bilangan bulat yang sudah
    disediakan
    >>> binary_xor(25, 32)
    '0b111001'
    >>> binary_xor(37, 50)
    '0b010111'
    >>> binary_xor(21, 30)
    '0b01011'
    >>> binary_xor(58, 73)
    '0b1110011'
    >>> binary_xor(0, 255)
    '0b11111111'
    >>> binary_xor(256, 256)
    '0b000000000'
    >>> binary_xor(0, -1)
    Traceback (most recent call last):
    ...
    ValueError: Nilai keduanya harus bilangan positif
    """
    if a < 0 or b < 0:
        raise ValueError("Nilai keduanya harus bilangan positif")

    a_binary = str(bin(a))[2:]
    b_binary = str(bin(b))[2:]

    max_len = max(len(a_binary), len(b_binary))

    return "0b" + "".join(
        str(int(char_a != char_b))
        for char_a, char_b in zip(a_binary.zfill(max_len), b_binary.zfill(max_len))
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
