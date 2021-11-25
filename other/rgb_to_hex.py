def rgb_to_hex(r: int, g: int, b: int) -> str:
    """
    Fungsi untuk mengubah tipe value warna RGB ke Hex.

    Alur proses:
    * Inisialisasi variabel `result` dengan string kosong
    * Looping `x` untuk ketiga value dari input
    * Cek apakah nilai x < 0
          * Jika benar, maka nilai x = 0
          * Jika salah, maka lanjutkan
    * Cek apakah nilai x > 255
          * Jika benar, maka nilai x = 255
          * Jika salah, maka lanjutkan
    * x > 0 dan x < 255
          * maka x diformat menjadi 2 digit hex
    * Tambahkan semua nilai x ke variabel `result`
    * Kembalikan nilai `result`

    Referensi format string:
    * [f-strings](\
        https://docs.python.org/3/reference/lexical_analysis.html#f-strings)
    * [format string syntax](\
        https://docs.python.org/3/library/string.html#format-string-syntax)
    * [format specifier](\
        https://docs.python.org/3/library/string.html#format-specification-mini-language)

    >>> rgb_to_hex(0, 0, 0)
    '000000'
    >>> rgb_to_hex(1, 2, 3)
    '010203'
    >>> rgb_to_hex(255, 255, 255)
    'FFFFFF'
    >>> rgb_to_hex(-10, 255, 300)
    '00FFFF'
    >>> rgb_to_hex(150, 0, 180)
    '9600B4'
    """
    result = ""

    for x in (r, g, b):
        if x < 0:
            x = 0
        elif x > 255:
            x = 255

        # f-string specifier yang digunakan:
        # '0' : padding '0' di depan string yang dihasilkan sesuai dengan width
        # '2' : width atau panjang string yang dihasilkan
        # 'X' : format int x menjadi hex yang telah di upper case
        result += f"{x:02X}"

    return result


def rgb_to_hex_v2(r: int, g: int, b: int) -> str:
    """
    Dengan menggunakan:

    * [list comprehension](\
        https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
    * [conditional expressions](\
        https://docs.python.org/3/reference/expressions.html#conditional-expressions)

    Kita bisa menuliskan fungsi ini dalam beberapa baris Python.

    >>> rgb_to_hex_v2(0, 0, 0)
    '000000'
    >>> rgb_to_hex_v2(1, 2, 3)
    '010203'
    >>> rgb_to_hex_v2(255, 255, 255)
    'FFFFFF'
    >>> rgb_to_hex_v2(-10, 255, 300)
    '00FFFF'
    >>> rgb_to_hex_v2(150, 0, 180)
    '9600B4'
    """
    return "".join([
        "00" if x <= 0
        else "FF" if x >= 255
        else f"{x:02X}"
        for x in (r, g, b)
    ])


def main(args=None):
    import doctest

    doctest.testmod()

    # basic test
    print(rgb_to_hex(0, 0, 0))        # returns 000000
    print(rgb_to_hex(1, 2, 3))        # returns 010203
    print(rgb_to_hex(255, 255, 255))  # returns FFFFFF
    print(rgb_to_hex(-10, 255, 300))  # returns 00FFFF
    print(rgb_to_hex(150, 0, 180))    # returns 9600B4

    # custom test
    # aktifkan baris berikutnya untuk menjalankan custom test
    # print(rgb_to_hex(*[int(input()) for _ in range(3)]))


if __name__ == '__main__':
    main()
