# Transformasi 2D secara teratur digunakan dalam Aljabar Linier
# kode untuk matriks refleksi, proyeksi, penskalaan, dan rotasi 2D.

from math import cos, sin
from typing import List


def scaling(scaling_factor: float) -> List[List[float]]:
    """
    >>> scaling(5)
    [[5.0, 0.0], [0.0, 5.0]]
    """
    scaling_factor = float(scaling_factor)
    return [[scaling_factor * int(x == y) for x in range(2)] for y in range(2)]


def rotation(angle: float) -> List[List[float]]:
    """
    >>> rotation(45)  # doctest: +NORMALIZE_WHITESPACE
    [[0.5253219888177297, -0.8509035245341184],
     [0.8509035245341184, 0.5253219888177297]]
    """
    c, s = cos(angle), sin(angle)
    return [[c, -s], [s, c]]


def projection(angle: float) -> List[List[float]]:
    """
    >>> projection(45)  # doctest: +NORMALIZE_WHITESPACE
    [[0.27596319193541496, 0.446998331800279],
     [0.446998331800279, 0.7240368080645851]]
    """
    c, s = cos(angle), sin(angle)
    cs = c * s
    return [[c * c, cs], [cs, s * s]]


def reflection(angle: float) -> List[List[float]]:
    """
    >>> reflection(45)  # doctest: +NORMALIZE_WHITESPACE
    [[0.05064397763545947, 0.893996663600558],
     [0.893996663600558, 0.7018070490682369]]
    """
    c, s = cos(angle), sin(angle)
    cs = c * s
    return [[2 * c - 1, 2 * cs], [2 * cs, 2 * s - 1]]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
