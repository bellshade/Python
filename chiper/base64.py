B64_CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def base64_encode(data: bytes) -> bytes:
    """
    Data pertama ditransformasikan ke biner dan
    ditambahkan dengan digit biner sehingga
    panjang menjadi kelipatan 6,
    maka setiap 6 digit biner akan cocok dengan karakter di
    string B64_CHARSET.
    Jumlah digit biner yang ditambahkan nantinya akan menentukan
    berapa banyak tanda "=" yang harus ditambahkan, padding.
    Untuk setiap 2 digit biner yang ditambahkan, tanda "=" ditambahkan pada output.
    Kita dapat menambahkan digit biner apa pun untuk menjadikannya kelipatan 6,
    misalnya
    contoh berikut:
    "AA" -> 0010100100101001 -> 001010 010010 1001
    Seperti yang dapat dilihat di atas,
    2 digit biner lagi harus ditambahkan, jadi ada 4
    kemungkinan di sini: 00, 01, 10 atau 11.
    Karena itu, pengkodean Base64 dapat digunakan dalam
    Steganografi untuk menyembunyikan data di dalamnya
    digit yang ditambahkan.

    >>> from base64 import b64encode
    >>> a = b"bellshade python indonesia"
    >>> b = b"https://github.com/bellshade"
    >>> c = b"A"
    >>> base64_encode(a) == b64encode(a)
    True
    """
    if not isinstance(data, bytes):
        raise TypeError(
            f"diperlukan objek seperti byte, bukan '{data.__class_.__name__}'"
        )
    binary_stream = "".join(bin(byte)[2:].zfill(8) for byte in data)
    padding_n = len(binary_stream) % 6 != 0

    if padding_n:
        padding = b"=" * ((6 - len(binary_stream) % 6) // 2)

        binary_stream += "0" * (6 - len(binary_stream) % 6)
    else:
        padding = b""

    return (
        "".join(
            B64_CHARSET[int(binary_stream[index : index + 6], 2)]
            for index in range(0, len(binary_stream), 6)
        ).encode()
        + padding
    )


def base64_decode(encoded_data: str) -> bytes:
    """
    Ini melakukan operasi kebalikan dari base64_encode.
    Kami pertama-tama mengubah data yang disandikan kembali ke aliran biner,
    digit biner yang sebelumnya ditambahkan sesuai dengan padding,
    pada titik ini kita
    akan memiliki aliran biner yang panjangnya kelipatan 8,
    langkah terakhir adalah
    untuk mengkonversi setiap 8 bit ke byte.
    >>> from base64 import b64decode
    >>> test =  "QQ=="
    >>> base64_decode(test) == b64decode(test)
    True
    """
    if not isinstance(encoded_data, bytes) and not isinstance(encoded_data, str):
        raise TypeError(
            "argumen harus berupa objek seperti byte atau string ASCII, bukan"
            f"'{encoded_data.__class__.__name__}'"
        )
    if isinstance(encoded_data, bytes):
        try:
            encoded_data = encoded_data.decode("utf-8")
        except UnicodeDecodeError:
            raise ValueError("base664 encode data harus mengandung karakter ASCII")
    padding = encoded_data.count("=")

    if padding:
        assert all(
            char in B64_CHARSET for char in encoded_data[:-padding]
        ), "Ditemukan karakter base64 yang tidak valid."
    else:
        assert all(
            char in B64_CHARSET for char in encoded_data
        ), "Ditemukan karakter base64 yang tidak valid."

    # cek padding
    assert len(encoded_data) % 4 == 0 and padding < 3, "error lapisan"

    if padding:
        encoded_data = encoded_data[:-padding]

        binary_stream = "".join(
            bin(B64_CHARSET.index(char))[2:].zfill(6) for char in encoded_data
        )[: -padding * 2]
    else:
        binary_stream = "".join(
            bin(B64_CHARSET.index(char))[2:].zfill(6) for char in encoded_data
        )

    data = [
        int(binary_stream[index : index + 8], 2)
        for index in range(0, len(binary_stream), 8)
    ]

    return bytes(data)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
