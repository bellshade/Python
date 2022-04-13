# Masalah lambung cembung adalah masalah menemukan semua simpul poligon cembung, P dari
# himpunan titik-titik pada bidang sedemikian rupa sehingga
# semua titik berada pada simpul-simpul P atau
# di dalam P. TH masalah convex hull memiliki beberapa aplikasi dalam masalah geometris,
# grafis komputer dan pengembangan game.

# Dua algoritma telah diterapkan untuk masalah lambung cembung di sini.
# 1. Algoritma brute-force yang berjalan di O(n^3)
# 2. Algoritma bagi-dan-taklukkan yang berjalan di O(n log(n))

from typing import Iterable, List, Set, Union


class Point:
    """
    Mendefinisikan titik 2-d untuk digunakan oleh semua algoritma lambung cembung.

    Parameter
    ----------
    x: int atau float, koordinat x dari titik 2-d
    y: int atau float, koordinat y dari titik 2-d

    Contoh
    --------
    >>> Point(1, 2)
    (1.0, 2.0)
    >>> Point("1", "2")
    (1.0, 2.0)
    >>> Point(1, 2) > Point(0, 1)
    True
    >>> Point(1, 1) == Point(1, 1)
    True
    >>> Point(-0.5, 1) == Point(0.5, 1)
    False
    >>> Point("pi", "e")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'pi'
    """

    def __init__(self, x, y):
        self.x, self.y = float(x), float(y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        if self.x > other.x:
            return True
        elif self.x == other.x:
            return self.y > other.y
        return False

    def __lt__(self, other):
        return not self > other

    def __ge__(self, other):
        if self.x > other.x:
            return True
        elif self.x == other.x:
            return self.y >= other.y
        return False

    def __le__(self, other):
        if self.x < other.x:
            return True
        elif self.x == other.x:
            return self.y <= other.y
        return False

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __hash__(self):
        return hash(self.x)


def _construct_points(
    list_of_tuples: list[Point] | list[list[float]] | Iterable[list[float]],
) -> list[Point]:
    """
    membangun daftar poin dari objek angka seperti array

    Argumen
    ---------

    list_of_tuples: objek seperti array dari nomor tipe.
    Jenis yang dapat diterima sejauh ini
    adalah daftar, tupel dan set.

    Return
    --------
    points: daftar di mana setiap item bertipe Point. Ini hanya berisi objek
    yang dapat diubah menjadi Point.

    Contoh
    -------
    >>> _construct_points([[1, 1], [2, -1], [0.3, 4]])
    [(1.0, 1.0), (2.0, -1.0), (0.3, 4.0)]
    >>> _construct_points([1, 2])
    Mengindahkan point 1. semua point setidaknya memiliki 2 koordinat.
    Mengindahkan point 2. semua point setidaknya memiliki 2 koordinat.
    []
    >>> _construct_points([])
    []
    >>> _construct_points(None)
    []
    """

    points: list[Point] = []
    if list_of_tuples:
        for p in list_of_tuples:
            if isinstance(p, Point):
                points.append(p)
            else:
                try:
                    points.append(Point(p[0], p[1]))
                except (IndexError, TypeError):
                    print(
                        f"Mengindahkan point {p}. semua point"
                        " setidaknya memiliki 2 koordinat."
                    )
    return points


def _validate_input(points: list[Point] | list[list[float]]) -> list[Point]:
    """
    memvalidasi instance input sebelum algoritma convex-hull menggunakannya

    Parameter
    ---------
    points:
    seperti array, poin 2d untuk divalidasi sebelum digunakan dengan
    algoritma lambung cembung. Elemen poin harus berupa daftar, tupel atau
    Poin.

    Returns
    -------
    points: array_like,
    sebuah iterable dari semua Poin yang terdefinisi dengan baik yang dibangun lewat.


    Exception
    ---------
    ValueError: jika poin kosong atau Tidak Ada,
    atau jika struktur data salah seperti skalar
    telah berlalu

    TypeError:
    jika objek yang dapat diubah tetapi tidak dapat diindeks (mis. kamus) dilewatkan.
    Pengecualian untuk set ini yang akan kami konversi ke daftar sebelum menggunakan


    Contoh
    -------
    >>> _validate_input([[1, 2]])
    [(1.0, 2.0)]
    >>> _validate_input([(1, 2)])
    [(1.0, 2.0)]
    >>> _validate_input([Point(2, 1), Point(-1, 2)])
    [(2.0, 1.0), (-1.0, 2.0)]
    >>> _validate_input([])
    Traceback (most recent call last):
    ...
    ValueError: Error []
    >>> _validate_input(1)
    Traceback (most recent call last):
    ...
    ValueError: Error, mendapat tipe yang tidak dapat diubah 1
    """

    if not hasattr(points, "__iter__"):
        raise ValueError(f"Error, mendapat tipe yang tidak dapat diubah {points}")

    if not points:
        raise ValueError(f"Error {points}")

    return _construct_points(points)


def _det(a: Point, b: Point, c: Point) -> float:
    """
    Menghitung jarak tegak lurus tanda titik 2d c dari ruas garis
    ab. Tanda menunjukkan arah c relatif terhadap ab.
    Nilai positif berarti c berada di atas ab (ke kiri), sedangkan nilai negatif
    berarti c di bawah ab (ke kanan). 0 berarti ketiga titik berada pada garis lurus.

    Sebagai catatan tambahan, 0,5 * abs|det| adalah luas segitiga abc

    Contoh
    ----------
    >>> _det(Point(1, 1), Point(1, 2), Point(1, 5))
    0.0
    >>> _det(Point(0, 0), Point(10, 0), Point(0, 10))
    100.0
    >>> _det(Point(0, 0), Point(10, 0), Point(0, -10))
    -100.0
    """

    det = (a.x * b.y + b.x * c.y + c.x * a.y) - (a.y * b.x + b.y * c.x + c.y * a.x)
    return det


def convex_hull_bf(points: list[Point]) -> list[Point]:
    """
    Membangun lambung cembung dari satu set poin
    2D menggunakan algoritma brute force.
    Algoritma pada dasarnya mempertimbangkan
    semua kombinasi titik (i, j) dan menggunakan
    definisi cembung untuk menentukan apakah (i, j)
    adalah bagian dari lambung cembung atau
    bukan. (i, j) adalah bagian dari lambung
    cembung jika dan hanya jika tidak ada titik pada keduanya
    sisi segmen garis yang menghubungkan ij,
    dan tidak ada titik k sedemikian rupa sehingga k adalah
    di kedua ujung ij.

    Contoh
    ---------
    >>> convex_hull_bf([[0, 0], [1, 0], [10, 1]])
    [(0.0, 0.0), (1.0, 0.0), (10.0, 1.0)]
    >>> convex_hull_bf([[0, 0], [1, 0], [10, 0]])
    [(0.0, 0.0), (10.0, 0.0)]
    >>> convex_hull_bf([[-1, 1],[-1, -1], [0, 0], [0.5, 0.5], [1, -1], [1, 1],
    ...                 [-0.75, 1]])
    [(-1.0, -1.0), (-1.0, 1.0), (1.0, -1.0), (1.0, 1.0)]
    >>> convex_hull_bf([(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3),
    ...                 (2, -1), (2, -4), (1, -3)])
    [(0.0, 0.0), (0.0, 3.0), (1.0, -3.0), (2.0, -4.0), (3.0, 0.0), (3.0, 3.0)]
    """

    points = sorted(_validate_input(points))
    n = len(points)
    convex_set = set()

    for i in range(n - 1):
        for j in range(i + 1, n):
            points_left_of_ij = points_right_of_ij = False
            ij_part_of_convex_hull = True
            for k in range(n):
                if k != i and k != j:
                    det_k = _det(points[i], points[j], points[k])

                    if det_k > 0:
                        points_left_of_ij = True
                    elif det_k < 0:
                        points_right_of_ij = True
                    else:
                        if points[k] < points[i] or points[k] > points[j]:
                            ij_part_of_convex_hull = False
                            break

                if points_left_of_ij and points_right_of_ij:
                    ij_part_of_convex_hull = False
                    break

            if ij_part_of_convex_hull:
                convex_set.update([points[i], points[j]])

    return sorted(convex_set)


def convex_hull_recursive(points: list[Point]) -> list[Point]:
    """
    Membangun lambung cembung dari satu set poin
    2D menggunakan strategi membagi-dan-menaklukkan
    Algoritma mengeksploitasi sifat geometris masalah dengan berulang kali
    mempartisi himpunan titik menjadi lambung yang lebih kecil,
    dan menemukan lambung cembung dari
    lambung yang lebih kecil ini.
    Penyatuan lambung cembung dari lambung yang lebih kecil adalah
    solusi untuk lambung cembung dari masalah yang lebih besar.

    Contoh
    ---------
    >>> convex_hull_recursive([[0, 0], [1, 0], [10, 1]])
    [(0.0, 0.0), (1.0, 0.0), (10.0, 1.0)]
    >>> convex_hull_recursive([[0, 0], [1, 0], [10, 0]])
    [(0.0, 0.0), (10.0, 0.0)]
    >>> convex_hull_recursive([[-1, 1],[-1, -1], [0, 0], [0.5, 0.5], [1, -1], [1, 1],
    ...                        [-0.75, 1]])
    [(-1.0, -1.0), (-1.0, 1.0), (1.0, -1.0), (1.0, 1.0)]
    >>> convex_hull_recursive([(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3),
    ...                        (2, -1), (2, -4), (1, -3)])
    [(0.0, 0.0), (0.0, 3.0), (1.0, -3.0), (2.0, -4.0), (3.0, 0.0), (3.0, 3.0)]
    """
    points = sorted(_validate_input(points))
    n = len(points)
    left_most_point = points[0]
    right_most_point = points[n - 1]

    convex_set = {left_most_point, right_most_point}
    upper_hull = []
    lower_hull = []

    for i in range(1, n - 1):
        det = _det(left_most_point, right_most_point, points[i])

        if det > 0:
            upper_hull.append(points[i])
        elif det < 0:
            lower_hull.append(points[i])

    _construct_hull(upper_hull, left_most_point, right_most_point, convex_set)
    _construct_hull(lower_hull, right_most_point, left_most_point, convex_set)

    return sorted(convex_set)


def _construct_hull(
    points: list[Point], left: Point, right: Point, convex_set: set[Point]
) -> None:
    if points:
        extreme_point = None
        extreme_point_distance = float("-inf")
        candidate_points = []

        for p in points:
            det = _det(left, right, p)

            if det > 0:
                candidate_points.append(p)

                if det > extreme_point_distance:
                    extreme_point_distance = det
                    extreme_point = p

        if extreme_point:
            _construct_hull(candidate_points, left, extreme_point, convex_set)
            convex_set.add(extreme_point)
            _construct_hull(candidate_points, extreme_point, right, convex_set)


def convex_hull_melkman(points: list[Point]) -> list[Point]:
    """
    Membangun lambung cembung dari satu set titik 2D menggunakan algoritma melkman.
    Algoritma ini bekerja dengan menyisipkan
    titik-titik dari rantai poligonal sederhana secara iteratif
    (artinya tidak ada segmen garis antara dua titik berurutan yang saling bersilangan).
    Menyortir poin menghasilkan rantai poligonal seperti itu.

    informasi lebih lanjut http://cgm.cs.mcgill.ca/~athens/cs601/Melkman.html

    Contoh
    ---------
    >>> convex_hull_melkman([[0, 0], [1, 0], [10, 1]])
    [(0.0, 0.0), (1.0, 0.0), (10.0, 1.0)]
    >>> convex_hull_melkman([[0, 0], [1, 0], [10, 0]])
    [(0.0, 0.0), (10.0, 0.0)]
    >>> convex_hull_melkman([[-1, 1],[-1, -1], [0, 0], [0.5, 0.5], [1, -1], [1, 1],
    ...                 [-0.75, 1]])
    [(-1.0, -1.0), (-1.0, 1.0), (1.0, -1.0), (1.0, 1.0)]
    >>> convex_hull_melkman([(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3),
    ...                 (2, -1), (2, -4), (1, -3)])
    [(0.0, 0.0), (0.0, 3.0), (1.0, -3.0), (2.0, -4.0), (3.0, 0.0), (3.0, 3.0)]
    """
    points = sorted(_validate_input(points))
    n = len(points)

    convex_hull = points[:2]
    for i in range(2, n):
        det = _det(convex_hull[1], convex_hull[0], points[i])
        if det > 0:
            convex_hull.insert(0, points[i])
            break
        elif det < 0:
            convex_hull.append(points[i])
            break
        else:
            convex_hull[1] = points[i]
    i += 1

    for i in range(i, n):
        if (
            _det(convex_hull[0], convex_hull[-1], points[i]) > 0
            and _det(convex_hull[-1], convex_hull[0], points[1]) < 0
        ):
            continue

        convex_hull.insert(0, points[i])
        convex_hull.append(points[i])
        while _det(convex_hull[0], convex_hull[1], convex_hull[2]) >= 0:
            del convex_hull[1]
        while _det(convex_hull[-1], convex_hull[-2], convex_hull[-3]) <= 0:
            del convex_hull[-2]

    # `convex_hull` is contains the convex hull in circular order
    return sorted(convex_hull[1:] if len(convex_hull) > 3 else convex_hull)


def main():
    points = [
        (0, 3),
        (2, 2),
        (1, 1),
        (2, 1),
        (3, 0),
        (0, 0),
        (3, 3),
        (2, -1),
        (2, -4),
        (1, -3),
    ]
    results_bf = convex_hull_bf(points)

    results_recursive = convex_hull_recursive(points)
    assert results_bf == results_recursive

    results_melkman = convex_hull_melkman(points)
    assert results_bf == results_melkman

    print(results_bf)


if __name__ == "__main__":
    import doctest

    # main()
    doctest.testmod()
