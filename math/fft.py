import cmath
import numpy as np


def fft(A):
    """
    Fungsi untuk kalkulasi Fast Fourier Transform

    >>> y = [i for i in range(1, 10)]
    >>> fft(y)
    array([45.        -0.j        ,  3.27090469+9.43955428j,
            4.30540729+3.93923101j,  4.77196636+1.65987555j,
            5.        +0.j        ,  4.25695936-1.83110215j,
            5.69459271-3.93923101j,  7.70016959-9.26832768j,
            0.        +0.j        ])
    """
    N = len(A)
    if N == 1:
        return A
    odd = fft(A[1::2])
    even = fft(A[::2])
    res = [0] * N
    for i in range(N // 2):
        W = cmath.exp(-1j * 2 * cmath.pi * i / N)
        res[i] = even[i] + W * odd[i]
        res[i + N // 2] = even[i] - W * odd[i]
    return np.array(res)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
