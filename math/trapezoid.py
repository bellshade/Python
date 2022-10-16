from typing import Callable

import numpy as np


def trapezoid(
    func: Callable[..., float], a: float, b: float, eps: float = 0.0001, *args, **kwargs
) -> float:

    """
    Metode integrasi trapesium mengganti bentuk segiempat
    yang sebelumnya digunakan untuk mengintegrasi menjadi
    bentuk trapesium. Maka dari itu, pada trapesium, nilai
    f(x) dievaluasi pada masing2 sisi trapesium.

    Parameter:
    f   = fungsi input
    a   = batas bawah integrasi
    b   = batas atas integrasi
    eps = error relatif maksimal

    >>> trapezoid(lambda x: x**5, 0, 1)
    0.16670751153457503
    >>> trapezoid(lambda x: x**2, 0, 2)
    2.6667973728065877
    """
    try:
        # Iterasi pertama
        n = 100
        h = (b - a) / n
        fx = [func(a + i * h, *args, **kwargs) for i in range(n + 1)]
        L0 = h / 2 * (fx[0] + fx[-1]) + h * sum(fx[1:-1])

        # Optimasi
        err = 1
        while err > eps:
            n += 1
            h = (b - a) / n
            fx = [func(a + i * h, *args, **kwargs) for i in range(n + 1)]
            L1 = h / 2 * (fx[0] + fx[-1]) + h * sum(fx[1:-1])
            err = np.abs(L1 - L0) / np.abs(L1)
            L0 = L1
    except Exception:
        raise RuntimeError("Integrasi gagal, pastikan fungsi anda benar!")
    return L1


if __name__ == "__main__":

    def f(x: float) -> float:
        """
        Test Function
        """
        return x**4

    import doctest

    doctest.testmod()
