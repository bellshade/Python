from typing import Callable

import numpy as np


def rectangle(
    func: Callable[..., float], a: float, b: float, eps: float = 0.0001, *args, **kwargs
) -> float:

    """
    Metode segi empat adalah metode integrasi paling sederhana.
    Metode ini membagi domain integrasi sebanyak n buah
    dan menjumlahkan seluruh luas segi empat dengan dimensi
    (a + b)/n * f(x), dimana x adalah sudut kiri segiempat

    Parameter:
    func = fungsi input
    a    = batas bawah integrasi
    b    = batas atas integrasi
    eps  = error relatif maksimal

    >>> rectangle(lambda x: x**2, 0, 2)
    2.6992751228325296
    >>> rectangle(lambda x: x**1, 0, 2)
    2.0198019801980194
    """
    try:
        n = 100
        x = np.linspace(a, b, n)
        dx = x[1] - x[0]
        L0 = sum(dx * func(i, *args, **kwargs) for i in x)
        err = 1
        while err > eps:
            n += 1
            x = np.linspace(a, b, n)
            dx = x[1] - x[0]
            L1 = sum(dx * func(i, *args, **kwargs) for i in x)
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
        return x ** 2

    print(rectangle(f, 0, 2))

    import doctest

    doctest.testmod()
