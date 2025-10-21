# Algoritma untuk mengecek apakah bilangan itu lucky number
# https://en.wikipedia.org/wiki/Lucky_number
def is_lucky_number(number):
    """
    Lucky number adalah angka yang selamat dari persortiran
    angka berdasarkan posisi mirip Sieve.

    >>> is_lucky_number(897)
    'Angka Lucky'
    >>> is_lucky_number(80)
    'Angka Lucky'
    >>> is_lucky_number(1232)
    'Bukan Angka Lucky'
    >>> is_lucky_number(700)
    'Bukan Angka Lucky'

    """
    benar , bukan = "Angka Lucky" , "Bukan Angka Lucky"
    ar = set()

    while number != 0:
        digit = number % 10

        if digit in ar:
            return bukan

        ar.add(digit)
        number //= 10

    return benar


def main(args=None):
    import doctest

    doctest.testmod()

    print(is_lucky_number(897))  # Angka Lucky
    print(is_lucky_number(80))  # Angka Lucky
    print(is_lucky_number(1232))  # Bukan Angka Lucky
    print(is_lucky_number(700))  # Bukan Angka Lucky


if __name__ == "__main__":
    main()
