# Mengecek apakah krisnamurty atau bukan
from math import factorial


def krisnamurty(number : int) -> int | str:
    """
    Angka Krisnamurty adalah angka factorial yang setiap digitnya
    sama dengan factorial nya.

    contoh :
    145! = 1! + 4! + 5! -> Angka Krisnamurty

    >>> krisnamurty(145)
    'Angka Krisnamurty'
    >>> krisnamurty(1)
    'Angka Krisnamurty'
    >>> krisnamurty(123)
    'Bukan Angka Krisnamuty'

    """
    error = "Masukkan Angka dengan benar"
    benar , bukan = "Angka Krisnamurty" , "Bukan Angka Krisnamuty"
    if not isinstance(number,int) or number < 0:
        return error
    else :
        total = sum(factorial(int(d)) for d in str(number))
        return benar if total == number else bukan


def main(args=None):
    import doctest

    doctest.testmod()

    # sample case
    print(krisnamurty(145))  # Angka Krisnamurty
    print(krisnamurty(1))  # Angka Krisnamurty
    print(krisnamurty(123))  # Bukan Angka Krisnamuty


if __name__ == "__main__":
    main()
