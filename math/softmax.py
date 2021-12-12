# demonstrasi darii implementasi fungsi softmax

# Ini adalah fungsi yang mengambil vektor dari K
# bilangan real sebagai input, dan menormalkan
# ke dalam distribusi probabilitas yang terdiri
# dari K probabilitas proporsional
# ke eksponensial dari angka input.
# Setelah softmax, elemen dari
# vektor selalu berjumlah 1.

# referensi
# https://en.wikipedia.org/wiki/Softmax_function

import numpy as np


def softmax(vector):
    """
    Menerapkan fungsi softmax
    Parameter:
        vector (np.array,list,tuple): Array berbentuk numpy (1,n)
        terdiri dari nilai-nilai nyata atau daftar serupa,tuple
    Pengembalian:
        softmax_vec (np.array):
        Input array numpy setelah diterapkan
        softmax.
    Vektor softmax menambahkan hingga satu.
    Kita perlu membatasi untuk
    presisi

    >>> vec = np.array([5, 5])
    >>> softmax(vec)
    array([0.5, 0.5])

    >>> softmax([0])
    array([1.])
    """
    exponent_vector = np.exp(vector)

    # Jumlahkan semua eksponensialnya
    sum_exponent = np.sum(exponent_vector)

    # bagi setiap eksponen dengan jumlah
    # semua eksponen
    softmax_vector = exponent_vector / sum_exponent

    return softmax_vector


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
