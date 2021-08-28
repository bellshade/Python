def binary_to_octal(msg: str) -> str:
    """
    implementasi biner ke oktal
    >>> binary_to_octal("1111")
    '17'
    """
    if not all(char in "01" for char in msg):
        raise ValueError("Nilai non-biner diteruskan ke fungsi")
    if not msg:
        raise ValueError("String kosong diteruskan ke fungsi")

    oct_string = ""
    while len(msg) % 3 != 0:
        msg = "0" + msg

    msg_string = [msg[index : index + 3] for index in range(len(msg)) if index % 3 == 0]
    for bin_group in msg_string:
        oct_val = 0
        for index, val in enumerate(bin_group):
            oct_val += int(2 ** (2 - index) * int(val))
        oct_string += str(oct_val)
    return oct_string


if __name__ == "__main__":
    import doctest

    # print(binary_to_octal("1111"))
    doctest.testmod()
