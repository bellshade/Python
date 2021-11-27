def hex_to_rgb(hex_color):
    """
    Fungsi ini menerima inputan berupa string hexadecimal
    dan mengembalikan hasilnya dalam bentuk tuple (r, g, b).

    Contoh:
    >>> hex_to_rgb('#000000')
    (0, 0, 0)
    >>> hex_to_rgb('#FFFFFF')
    (255, 255, 255)
    >>> hex_to_rgb('#0ef')
    (0, 238, 255)
    >>> hex_to_rgb('800040')
    (128, 0, 64)
    >>> hex_to_rgb('#aabbccdd')
    Traceback (most recent call last):
        ...
    ValueError: Hexadecimal tidak valid
    """
    hex_string = hex_color.lstrip("#")

    if len(hex_string) == 3:
        hex_string = "".join(x * 2 for x in hex_string)

    if len(hex_string) != 6:
        raise ValueError("Hexadecimal tidak valid")

    return tuple(int(hex_string[i:i + 2], 16) for i in (0, 2, 4))


def main(args=None):
    import doctest

    doctest.testmod()

    # basic tests
    print(hex_to_rgb('#000000'))    # (0, 0, 0)
    print(hex_to_rgb('#FFFFFF'))    # (255, 255, 255)
    print(hex_to_rgb('#0ef'))       # (0, 238, 255)
    print(hex_to_rgb('800040'))     # (128, 0, 64)
    # print(hex_to_rgb('#aabbccdd'))  # ValueError: Hexadecimal tidak valid

    # custom test
    # aktifkan baris berikutnya untuk menjalankan custom test
    # print(hex_to_rgb(input("Masukkan warna hex:")))


if __name__ == '__main__':
    main()
