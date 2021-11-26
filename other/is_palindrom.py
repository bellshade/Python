def is_palindrom(x: str) -> bool:
    """
    Palindrom merupakan kata yang dapat dibaca dengan sama baik dari depan
    maupun belakang.

    Fungsi ini mengecek apakah `x` merupakan sebuah palindrom. Fungsi ini
    akan mengembalikan `True` jika `x` merupakan palindrom, dan `False`
    jika tidak.

    >>> is_palindrom("katak")
    True
    >>> is_palindrom("label")
    False
    >>> is_palindrom("Kasur ini rusak")
    True
    """
    # Mengubah string `x` menjadi lowercase dan menghilangkan spasi
    normalized = x.lower().replace(" ", "")

    # Membandingkan string `normalized` dengan `normalized` yang telah dibalik
    return normalized == normalized[::-1]


def main(args=None):
    import doctest

    doctest.testmod()

    # basic tests
    print(is_palindrom("katak"))            # output "True"
    print(is_palindrom("label"))            # output "False"
    print(is_palindrom("Kasur ini rusak"))  # output "True"

    # custom tests
    # aktifkan baris berikutnya untuk menjalankan custom test
    # print(is_palindrom(input('Masukkan kata: ')))


if __name__ == '__main__':
    main()
