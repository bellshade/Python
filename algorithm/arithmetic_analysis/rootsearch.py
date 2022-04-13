from numpy import sign


def root_search(
    f: Callable[[float], float], a: float, b: float, dx: float
) -> tuple[float, float]:
    # Fungsi untuk menghitung nilai akar dari sebuah persamaan non linear
    # satu variable. Ide dasarnya adalah jika f(a) dan f(b) punya tanda yang berbeda
    # (f(a) positif, f(b) negatif atau sebaliknya),
    # maka setidaknya ada 1 akar di interval [a, b].
    #
    # Parameter:
    # f   -- persamaan yang akan dihitung nilai akarnya (function)
    # a   -- batas bawah interval (float)
    # b   -- batas atas interval (float)
    # dx  -- lebar bins (besar interval yang digunakan untuk membagi suatu
    #         area di bawah kurva persamaan f.
    x0 = a
    f0 = f(a)
    x1 = a + dx
    f1 = f(x1)

    while sign(f0) == sign(f1):
        if x0 >= b:
            raise ValueError("Akar tidak ditemukan pada interval tersebut")
        x0 = x1
        f0 = f1
        x1 = x0 + dx
        f1 = f(x1)
    return x0, x1


def incremental_root_search(
    f: Callable[[float], float], x0: float, x1: float, n: int
) -> float:
    """
    Secara iteratif mencari nilai akar berdasarkan fungsi root_search.
    Secara intuitif, semakin besar nilai n, semakin akurat nilai akar yang didapatkan.

    Parameter:
    f   -- persamaan yang akan dihitung nilai akarnya (function)
    x0   -- batas bawah interval (float)
    x1  -- batas atas interval (float)
    n  -- jumlah bins yang membagi interval [x0, x1] sama besar.

    >>> incremental_root_search(lambda x: x ** 3 - 10.0 * x ** 2 + 5.0, 0.7, 1.0, 6)
    0.7346036499999994
    >>> x = incremental_root_search(lambda x: x**2 - 4*x + 1, 2.0, 4.0, 6)
    >>> x
    3.7320509999999993
    >>> incremental_root_search(lambda x: x**2 - 4*x + 4, 0.0, 4.0, 6)
    1.9999980000000013
    >>> incremental_root_search(lambda x: x**2 - 4*x + 4, 0.0, 1.0, 6)
    Traceback (most recent call last):
    ...
    ValueError: Akar tidak ditemukan pada interval tersebut
    """
    for _ in range(n):
        dx = (x1 - x0) / 10.0
        x0, x1 = root_search(f, x0, x1, dx)
    x = (x0 + x1) / 2.0

    return x


def equation(x: float) -> float:
    # Berisi persamaan polinomial yang akan dicari akarnya.
    # Bilangan basis berupa float. Bilangan pangkat (eksponen) berupa bilangan bulat.
    # Persamaan di bawah dapat diganti-ganti.
    #
    # Pada kasus ini:
    # f(x) = x^3 - 10x^2 + 5
    return x**3 - 10.0 * x**2 + 5.0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
