# penjelasan tentang bit operator
# https://www.tutorialspoint.com/python3/bitwise_operators_example.htm

def binary_or(a: int, b: int) -> str:
    """
    Ambil 2 bilangan integer, 
    ubah menjadi biner, 
    dan kembalikan angka biner yang merupakan hasil biner 
    atau operasi pada bilangan bulat yang disediakan.
    >>> binary_or(1, 1)
    '0b1'
    >>> binary_or(0, 1)
    '0b1'
    >>> binary_or(1, 0)
    '0b1'
    >>> binary_or(0, 0)
    '0b0'
    >>> binary_or(58, 73)
    '0b1111011'
    >>> binary_or(-1, 2)
    Traceback (most recent call last):
    ...
    ValueError: Angka tidak boleh negatif
    >>> binary_or(3, -1)
    Traceback (most recent call last):
    ...
    ValueError: Angka tidak boleh negatif
    """
    if a < 0 or b < 0:
        raise ValueError("Angka tidak boleh negatif")
    a_binary = str(bin(a))[2:]
    b_binary = str(bin(b))[2:]
    max_binary = max(len(a_binary), len(b_binary))
    return "0b" + "".join(
        str(int("1" in (char_a, char_b)))
        for char_a, char_b in zip(a_binary.zfill(max_binary), b_binary.zfill(max_binary))
    )

if __name__ == "__main__":
    import doctest
    print(binary_or(1, 1))
    doctest.testmod()