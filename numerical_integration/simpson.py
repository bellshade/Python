# type: ignore[arg-type]
from typing import Callable

import numpy as np


def simpson_13(
    func: Callable[..., float],
    a: float,
    b: float,
    eps: float = 0.0001,
    *args,
    **kwargs
) -> float:

    """
    Metode simpson 1/3 menggunakan
    kurva polinomial ordo 2 untuk melakukan
    approximasi terhadap fungsi yang akan
    diintegrasi

    Parameter:
    f   = fungsi input
    a   = batas bawah integrasi
    b   = batas atas integrasi
    eps = error relatif maksimal

    >>> simpson_13(lambda x: x**2, 0, 2)
    2.6666666666666665
    >>> simpson_13(lambda x: x**5, 0, 1)
    0.16666679687500002
    """
    try:
        # Iterasi pertama
        n = 10
        h = (b - a) / n
        fx = [func(a + i * h, *args, **kwargs) for i in range(n + 1)]
        L0 = h / 3 * (fx[0] + 4 * sum(fx[1:-1:2]) + 2 * sum(fx[2:-2:2]) + fx[-1])

        # Optimasi
        err = 1
        while err > eps:
            n *= 2
            h = (b - a) / n
            fx = [func(a + i * h, *args, **kwargs) for i in range(n + 1)]
            L1 = h / 3 * (fx[0] + 4 * sum(fx[1:-1:2]) + 2 * sum(fx[2:-2:2]) + fx[-1])
            err = np.abs(L1 - L0) / np.abs(L1)
            L0 = L1
    except Exception:
        raise RuntimeError("Integrasi gagal, pastikan fungsi anda benar!")
    return L1


def simpson_38(
    func: Callable[..., float],
    a: float,
    b: float,
    eps: float = 0.0001,
    *args,
    **kwargs
) -> float:

    """
    Metode simpson 3/8 menggunakan
    kurva polinomial ordo 3 untuk melakukan
    approximasi terhadap fungsi yang akan
    diintegrasi

    Parameter:
    f   = fungsi input
    a   = batas bawah integrasi
    b   = batas atas integrasi
    eps = error relatif maksimal

    >>> simpson_38(lambda x: x**2, 0, 2)
    2.666666666666667
    >>> simpson_38(lambda x: x**5, 0, 1)
    0.16666667809785096
    """
    try:
        # Iterasi pertama
        n = 10
        h = (b - a) / n
        fx = [func(a + i * h, *args, **kwargs) for i in range(n + 1)]
        L0 = (
            3
            / 8
            * h
            * (
                fx[0]
                + 3 * sum(fx[1:-2:3])
                + 3 * sum(fx[2:-1:3])
                + 2 * sum(fx[3:-3:3])
                + fx[-1]
            )
        )

        # Optimasi
        err = 1
        while err > eps:
            n *= 3
            h = (b - a) / n
            fx = [func(a + i * h, *args, **kwargs) for i in range(n + 1)]
            L1 = (
                3
                / 8
                * h
                * (
                    fx[0]
                    + 3 * sum(fx[1:-2:3])
                    + 3 * sum(fx[2:-1:3])
                    + 2 * sum(fx[3:-3:3])
                    + fx[-1]
                )
            )
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
        return x ** 4

    print(simpson_13(f, 0, 1))
    print(simpson_38(f, 0, 1))

    import doctest

    doctest.testmod()
