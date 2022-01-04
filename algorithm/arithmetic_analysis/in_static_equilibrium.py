"""
Memeriksa apakah sistem gaya berada dalam kesetimbangan statis.
"""
from typing import List

from numpy import array, cos, cross, ndarray, radians, sin


def polar_force(
    magnitude: float, angle: float, radian_mode: bool = False
) -> List[float]:
    # Menghitung force pada suatu sistem dengan menggunakan matriks
    # rotasi dan magnitudenya.
    # polar 10, 45 = 7.0710678118654755, 7.071067811865475
    # polar 10, 3.14, True = -9.999987317275394, 0.01592652916486828
    if radian_mode:
        return [magnitude * cos(angle), magnitude * sin(angle)]
    return [magnitude * cos(radians(angle)), magnitude * sin(radians(angle))]


def in_static_equilibrium(
    forces: ndarray, location: ndarray, eps: float = 10 ** -1
) -> bool:
    """
    Menentukan apakah sistem berada dalam kesetimbangan statis.
    Periksa apakah suatu sistem dalam keadaan setimbang.
    Dibutuhkan dua objek numpy.array.
    >>> force = array([[1, 1], [-1, 2]])
    >>> location = array([[1, 0], [10, 0]])
    >>> in_static_equilibrium(force, location)
    False
    """
    moments: ndarray = cross(location, forces)
    sum_moments: float = sum(moments)
    return abs(sum_moments) < eps


if __name__ == "__main__":
    forces = array(
        [polar_force(718.4, 180 - 30), polar_force(879.54, 45), polar_force(100, -90)]
    )

    location = array([[0, 0], [0, 0], [0, 0]])
    assert in_static_equilibrium(forces, location)
    forces = array(
        [
            polar_force(30 * 9.81, 15),
            polar_force(215, 180 - 45),
            polar_force(264, 90 - 30),
        ]
    )
    location = array([[0, 0], [0, 0], [0, 0]])
    assert in_static_equilibrium(forces, location)
    forces = array([[0, -2000], [0, -1200], [0, 15600], [0, -12400]])
    location = array([[0, 0], [6, 0], [10, 0], [12, 0]])
    assert in_static_equilibrium(forces, location)

    import doctest

    doctest.testmod()
