# Bilangan Taxicab adalah bilangan yang dapat dinyatakan sebagai jumlah
# dua kubus bilangan bulat positif dengan lebih dari satu cara berbeda.
# https://en.wikipedia.org/wiki/Taxicab_number
from array import array


def taxi_cab(x):
    """
    Fungsi ini akan menghitung nilai kubus dari 0 sampai x-1 untuk menciptakan pasangan
    angka (a, b), lalu dihitung a^3 + b^3. Jika hasil penjumlahan muncul sekali, maka
    akan disimpan sebagai bilangan Taxicab.

    >>> taxi_cab(10)
    []
    >>> taxi_cab(20)
    [1729, 4104]
    >>> taxi_cab(30)
    [1729, 4104, 13832, 20683]
    >>> taxi_cab(40)
    [1729, 4104, 13832, 20683, 32832, 39312, 40033, 46683, 64232]
    """
    cubes = array('i', [i**3 for i in range(0, x)])
    dict_sum_pairs = {}
    raman = set()

    for a in range(0, x):
        for b in range(a + 1, x):
            a3, b3 = cubes[a], cubes[b]

            sum_pairs = a3 + b3

            if sum_pairs not in dict_sum_pairs:
                dict_sum_pairs[sum_pairs] = (a, b)
            else:
                raman.add(sum_pairs)
    return sorted(raman)


def main(args=None):
    import doctest

    doctest.testmod()
    # base case
    print(taxi_cab(10))
    # output = []
    print(taxi_cab(20))
    # output = [1729, 4104]
    print(taxi_cab(30))
    # output = [1729, 4104, 13832, 20683]
    print(taxi_cab(40))
    # output = [1729, 4104, 13832, 20683, 32832, 39312, 40033, 46683, 64232]


if __name__ == "__main__":
    main()
