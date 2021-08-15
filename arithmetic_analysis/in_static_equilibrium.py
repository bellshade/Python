"""
Memeriksa apakah sistem gaya berada dalam kesetimbangan statis.
"""
from typing import List
import numpy as np


def polar_force(
    magnitude: float, angle: float, radian_mode: bool = False
) -> List[float]:
    """
    Menghitung force pada suatu sistem dengan menggunakan matriks
    rotasi dan magnitudenya.
    >>> polar_force(10, 45)
    [7.0710678118654755, 7.071067811865475]
    >>> polar_force(10, 3.14, radian_mode=True)
    [-9.999987317275394, 0.01592652916486828]
    """
    if radian_mode:
        return [magnitude * np.cos(angle), magnitude * np.sin(angle)]
    return [
        magnitude * np.cos(np.radians(angle)),
        magnitude * np.sin(np.radians(angle)),
    ]


def in_static_equilibrium(
    forces: np.ndarray, location: np.ndarray, eps: float = 10 ** -1
) -> bool:
    """
    Menentukan apakah sistem berada dalam kesetimbangan statis.
    Periksa apakah suatu sistem dalam keadaan setimbang.
    Dibutuhkan dua objek numpy.array.
    >>> force = np.array([[1, 1], [-1, 2]])
    >>> location = np.array([[1, 0], [10, 0]])
    >>> in_static_equilibrium(force, location)
    False
    """
    moments: np.ndarray = np.cross(location, forces)
    sum_moments: float = np.sum(moments)
    return abs(sum_moments) < eps


if __name__ == "__main__":
    forces = np.array(
        [polar_force(718.4, 180 - 30), polar_force(879.54, 45), polar_force(100, -90)]
    )

    location = np.array([[0, 0], [0, 0], [0, 0]])
    assert in_static_equilibrium(forces, location)
    forces = np.array(
        [
            polar_force(30 * 9.81, 15),
            polar_force(215, 180 - 45),
            polar_force(264, 90 - 30),
        ]
    )
    location = np.array([[0, 0], [0, 0], [0, 0]])
    assert in_static_equilibrium(forces, location)
    forces = np.array([[0, -2000], [0, -1200], [0, 15600], [0, -12400]])
    location = np.array([[0, 0], [6, 0], [10, 0], [12, 0]])
    assert in_static_equilibrium(forces, location)

    import doctest

    doctest.testmod()
