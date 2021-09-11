from string import ascii_letters
from typing import Optional


def encrypt(input_string: str, key: int, alphabet: Optional[str] = None) -> str:
    """
    Mengkodekan string yang diberikan dengan sandi caesar
    dan mengembalikan kode yang disandikan pesan
    >>> alphabet = 'abcdefghijklmnopqrstuvwxyz'
    >>> encrypt('situasi pantai aman', 5, alphabet)
    'xnyzfxn ufsyfn frfs'
    """
    alpha = alphabet or ascii_letters
    result = ""

    for character in input_string:
        if character not in alpha:
            # Tambahkan tanpa enkripsi jika karakter tidak ada dalam alfabet
            result += character
        else:
            # Dapatkan indeks kunci baru dan pastikan tidak terlalu besar
            new_key = (alpha.index(character) + key) % len(alpha)

            # tambahkan enskripsi karakter ke dalam alfabet
            result += alpha[new_key]

    return result


def decrypt(input_string: str, key: int, alphabet: Optional[str] = None) -> str:
    """
    Mendekode string teks sandi yang diberikan
    dan mengembalikan teks biasa yang didekodekan
    >>> alphabet = 'abcdefghijklmnopqrstuvwxyz'
    >>> decrypt('xnyzfxn ufsyfn frfs', 5, alphabet)
    'situasi pantai aman'
    """
    key *= -1
    return encrypt(input_string, key, alphabet)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
