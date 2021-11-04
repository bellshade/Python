import math


def radian_to_degree(radian: float) -> float:
    """
    Fungsi ini digunakan untuk mengonversi radian ke derajat.
    Rumus : radian * (180 derajat / pi)

    >>> radian_to_degree(5)
    286.4788975654116
    """
    return radian * (180 / math.pi)


def degree_to_radian(degree: float) -> float:
    """
    Fungsi ini digunakan untuk mengonversi derajat ke radian.
    Rumus : derajat * (pi / 180 derajat)

    >>> degree_to_radian(60)
    1.0471975511965976
    """
    return degree * (math.pi / 180)


def radian_to_gradian(radian: float) -> float:
    """
    Fungsi ini digunakan untuk mengonversi radian ke gradian.
    Rumus : radian * (200 gradian / pi)

    >>> radian_to_gradian(3)
    190.9859317102744
    """
    return radian * (200 / math.pi)


def gradian_to_radian(gradian: float) -> float:
    """
    Fungsi ini digunakan untuk mengonversi radian ke gradian.
    Rumus : gradian * (180 / (200 gradian)

    >>> gradian_to_radian(53)
    0.8325220532012952
    """
    return gradian * (math.pi / 200)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
