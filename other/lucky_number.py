# Algoritma untuk mengecek apakah bilangan itu lucky number
# https://en.wikipedia.org/wiki/Lucky_number
def is_lucky_number(number):
    """
    Lucky number adalah angka yang selamat dari persortiran
    angka berdasarkan posisi mirip Sieve.

    >>> is_lucky_number(1)
    'Angka Lucky'
    >>> is_lucky_number(21)
    'Angka Lucky'
    >>> is_lucky_number(1232)
    'Bukan Angka Lucky'
    >>> is_lucky_number(700)
    'Bukan Angka Lucky'

    """
    benar , bukan = "Angka Lucky" , "Bukan Angka Lucky"
    MAX_NUMBER = 10000

    idx = 1
    nbr = []
    for i in range(1 , MAX_NUMBER):
        nbr.append(i)

    while idx < len(nbr):
        step = nbr[idx]
        if step > len(nbr):
            break

        new_numbers = []
        pos = 1
        for val in nbr:
            if pos % step != 0:
                new_numbers.append(val)
            pos += 1
        nbr = new_numbers
        idx += 1

    if number in nbr:
        return benar
    else:
        return bukan


def main(args=None):
    import doctest

    doctest.testmod()

    print(is_lucky_number(1))  # Angka Lucky
    print(is_lucky_number(21))  # Angka Lucky
    print(is_lucky_number(80))  # Bukan Angka Lucky
    print(is_lucky_number(897))  # Bukan Angka Lucky


if __name__ == "__main__":
    main()
