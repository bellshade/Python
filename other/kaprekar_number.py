# mengecek apakah bilangan apakah bilangan itu masuk kaprekar
# https://en.wikipedia.org/wiki/Kaprekar_number
import math


def kaprekar_number(number: int) -> str:
    """
    Angka kaprekar adalah angka yang yang di kuadratkan,
    dan di pisahmenjadi dua bagian dan di jumlahkan lagi
    maka akat menjadi angka itu kembali.

    >>> kaprekar_number(45)
    'Angka Kaprekar'
    >>> kaprekar_number(9)
    'Angka Kaprekar'
    >>> kaprekar_number(5)
    'Bukan Angka Kaprekar'
    >>> kaprekar_number(10)
    'Bukan Angka Kaprekar'

    """
    benar , bukan = "Angka Kaprekar" , "Bukan Angka Kaprekar"
    if number == 1:
        return benar

    square_number = number * number

    cout_d = 0
    while not square_number == 0:
        cout_d += 1
        square_number = square_number // 10

    square_number = number * number

    r_digits = 0
    while r_digits < cout_d:
        r_digits += 1
        eq_parts = math.pow(10 , r_digits)

        if eq_parts == number:
            continue

        jumlah = square_number // eq_parts + square_number % eq_parts
        if jumlah == number:
            return benar

    return bukan


def main(args=None):
    import doctest

    doctest.testmod()

    # sampel case
    print(kaprekar_number(45))  # Angka Kaprekar
    print(kaprekar_number(9))  # Angka Kaprekar
    print(kaprekar_number(5))  # Bukan Angka Kaprekar
    print(kaprekar_number(10))  # Bukan Angka Kaprekar


if __name__ == "__main__":
    main()
