# menghitung volume dari semua ukuran
# referensi
# https://en.wikipedia.org/wiki/volume

from __future__ import annotations

from math import pi, pow


def volume_kubus(panjang_sisi: int | float) -> float:
    """
    menghitung volume kubus

    >>> volume_kubus(1)
    1.0
    >>> volume_kubus(3)
    27.0
    """
    return pow(panjang_sisi, 3)


def volume_berbentuk_kubus(lebar: float, tinggi: float, panjang: float) -> float:
    """
    kalkulasi volume kuboid

    >>> volume_berbentuk_kubus(1, 1, 1)
    1.0
    >>> volume_berbentuk_kubus(1, 2, 3)
    6.0
    """
    return float(lebar * tinggi * panjang)


def volume_kerucut(area_dasar: float, tinggi: float) -> float:
    """
    kalkulasi dari volume kerucut
    referensi wikipedia
    https://en.wikipedia.org/wiki/Cone

    >>> volume_kerucut(10, 3)
    10.0
    >>> volume_kerucut(1, 1)
    0.3333333333333333
    """
    return area_dasar * tinggi / 3.0


def volume_kerucut_melingkar(radius: float, tinggi: float) -> float:
    """
    referensi dari kerucut melingkar
    https://en.wikipedia.org/wiki/Cone

    >>> volume_kerucut_melingkar(2, 3)
    12.566370614359172
    """
    return pi * pow(radius, 2) * tinggi / 3.0


def volume_prisma(area_dasar: float, tinggi: float) -> float:
    """
    kalkulasi dari volume prisma
    referensi
    https://en.wikipedia.org/wiki/Prism_(geometry)
    >>> volume_prisma(10, 2)
    20.0
    >>> volume_prisma(11, 1)
    11.0
    """
    return float(area_dasar * tinggi)


def volume_pyramid(area_dasar: float, tinggi: float) -> float:
    """
    kalkulasi dari volume pyramid
    referensi
    https://en.wikipedia.org/wiki/Pyramid_(geometry)
    >>> volume_pyramid(10, 3)
    10.0
    >>> volume_pyramid(1.5, 3)
    1.5
    """
    return area_dasar * tinggi / 3.0


def volume_bola(radius: float) -> float:
    """
    kalkulasi dari volume bola
    referensi
    https://en.wikipedia.org/wiki/Sphere
    >>> volume_bola(2)
    33.510321638291124
    """
    return 4 / 3 * pi * pow(radius, 3)


def volume_silinder_melingar(radius: float, tinggi: float) -> float:
    """
    kalkulasi dari volume silinder melingkar
    referensi
    https://en.wikipedia.org/wiki/Cylinder
    >>> volume_silinder_melingar(2, 3)
    37.69911184307752
    """
    return pi * pow(radius, 2) * tinggi


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(
        f"nilai volume kubus adalah {3} maka hasilnya adalah" f" {volume_kubus(3)} m3"
    )
