import numpy as np


def r2_score(y_predict, y_actual):
    """
    R2_score adalah ukuran yang digunakan dalam statistik untuk mengukur••
    seberapa baik model regresi cocok dengan data yang diamati••
    R2_score memberikan informasi seberapa dekat••
    titik data dengan garis regresi yang dihasilkan oleh model.

    >>> r2_score(np.array([12,34,12,23]),np.array([11,2,11,22]))
    -4.109452736318408
    >>> r2_score(np.array([12,34,12,23]),np.array([12,30,11,23]))
    0.9319999999999999
    """

    sse = sum((y_actual - y_predict) ** 2)
    sst = sum((y_actual - np.mean(y_actual)) ** 2)

    return 1 - (sse / sst)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
