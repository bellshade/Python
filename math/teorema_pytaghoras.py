# menghitung 2 point menggunakan teorema pythagoras
# https://www.statmat.net/teorema-pythagoras/

import math


class Poin:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        return f"Poin({self.x}, {self.y}, {self.z})"


def jarak(a: Poin, b: Poin) -> float:
    return math.sqrt(abs((b.x - a.x) ** 2 + (b.y - a.y) ** 2 + (b.z - a.z) ** 2))


def tes_hitung() -> None:
    """
    >>> poin1 = Poin(2, -1, 7)
    >>> poin2 = Poin(1, -3, 5)
    >>> print(f"jarak dari {poin1} ke {poin2} adalah {jarak(poin1, poin2)}")
    jarak dari Poin(2, -1, 7) ke Poin(1, -3, 5) adalah 3.0
    """
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
