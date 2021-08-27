import random
import sys

from . import cryptomath_module as cryptomath

SIMBOL = (
    r""" !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`"""
    r"""abcdefghijklmnopqrstuvwxyz{|}~"""
)


def check_keys(keyA: int, keyB: int, mode: str) -> None:
    if mode == "enkripsi":
        if keyA == 1:
            sys.exit(
                "sandi affine menjadi lemah saat enkripsi "
                "A set ke 1. masukkan kunci lain."
            )
        if keyB == 0:
            sys.exit(
                "sandi affine menjadi lemah saat enkripsi "
                "B set ke 0. masukkan kunci lain."
            )
    if keyA < 0 or keyB < 0 or keyB > len(SIMBOL) - 1:
        sys.exit(
            "kunci A harus lebih besar dari 0 dan kunci B "
            f"Antara 0 dan {len(SIMBOL) - 1}."
        )
    if cryptomath.gcd(keyA, len(SIMBOL)) != 1:
        sys.exit(
            f"Kunci A {keyA} and simbol set {len(SIMBOL)} "
            "tidak relatif prima. Pilih kunci yang berbeda."
        )


def encrypt_msg(key: int, message: str) -> str:
    """
    >>> encrypt_msg(4545, 'bellshade python indonesia')
    'O}JJvL N}pHsFLxIp{INxI}v{ '
    """
    keyA, keyB = divmod(key, len(SIMBOL))
    check_keys(keyA, keyB, "enkripsi")
    cipherText = ""
    for symbol in message:
        if symbol in SIMBOL:
            symIndex = SIMBOL.find(symbol)
            cipherText += SIMBOL[(symIndex * keyA + keyB) % len(SIMBOL)]
        else:
            cipherText += symbol
    return cipherText


def decrypt_msg(key: int, message: str) -> str:
    """
    >>> decrypt_msg(4545, 'O}JJvL N}pHsFLxIp{INxI}v{ ')
    'bellshade python indonesia'
    """
    keyA, keyB = divmod(key, len(SIMBOL))
    check_keys(keyA, keyB, "dekripsi")
    plainText = ""
    modInverseOfkeyA = cryptomath.find_mod_inverse(keyA, len(SIMBOL))
    for symbol in message:
        if symbol in SIMBOL:
            symIndex = SIMBOL.find(symbol)
            plainText += SIMBOL[(symIndex - keyB) * modInverseOfkeyA % len(SIMBOL)]
        else:
            plainText += symbol
    return plainText


def get_random_key() -> int:
    while True:
        keyA = random.randint(2, len(SIMBOL))
        keyB = random.randint(2, len(SIMBOL))
        if cryptomath.gcd(keyA, len(SIMBOL)) == 1 and keyB % len(SIMBOL) != 0:
            return keyA * len(SIMBOL) + keyB


def testing() -> None:
    """
    >>> key = get_random_key()
    >>> message = 'bellshade python indonesia'
    >>> decrypt_msg(key, encrypt_msg(key, message)) == message
    True
    """
    # message = input("masukkan pesan").strip()
    # key = int(input("masukkan kunci [2000 - 9000]").strip())
    # mode = input("enskripsi / deskripsi ['E' / 'D']").strip().lower()
    message = "jonas jadi badut"
    key = 2500
    mode = "e"

    if mode.startswith("e"):
        mode = "enskripsi"
        trans = encrypt_msg(key, message)
    elif mode.startswith("d"):
        mode = "enskripsi"
        trans = decrypt_msg(key, message)

    print(f"\n{mode.title()}\nText: {trans}")


if __name__ == "__main__":
    import doctest

    # testing()
    doctest.testmod()
