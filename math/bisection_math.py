# informasi tentang bisection
# https://en.wikipedia.org/wiki/Bisection_method

from __future__ import annotations


def equation(x: float) -> float:
    """
    hasil dari pengurangan dan perkalian
    dari x
    parameter dan tipe:
        x: float
    return:
        hasil dari 10 - x * x
    tipe:
        float
    >>> equation(5)
    -15
    >>> equation(0.1)
    9.99
    """
    return 10 - x * x


def bisection(a: float, b: float) -> float:
    """
    Diberikan fungsi pada bilangan mengambang f(x) dan dua bilangan
    float 'a' dan 'b' sedemikian sehingga
    f(a) * f(b) < 0 dan f(x) kontinu di [a, b]self.
    Di sini f(x) mewakili persamaan aljabar atau transendentalself.
    Cari akar fungsi dalam interval [a, b]
    (Atau cari nilai x sehingga f(x) adalah 0)

    >>> bisection(-2, 5)
    3.1611328125
    >>> bisection(0, 6)
    3.158203125
    """

    # menggunakan teori bolzano
    if equation(a) * equation(b) >= 0:
        print("0")

    c = a
    while (b - a) >= 0.01:
        # mencari nilai tengahnya
        c = (a + b) / 2
        if equation(c) == 0.0:
            break
        if equation(c) * equation(a) < 0:
            b = c
        else:
            a = c

    return c


if __name__ == "__main__":
    import doctest

    doctest.testmod()
