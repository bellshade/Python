from typing import Callable
import math


def rieman_integral(f: Callable[[float], float],
                    a: float,
                    b: float,
                    n: int,
                    approx: str) -> float:
    """
    >>> rieman_integral(math.sin,0,math.pi/2,100,"tengah")
    1.0000102809119051
    >>> rieman_integral(math.sin,0,math.pi/2,100,"kanan")
    1.007833419873582
    >>> rieman_integral(math.sin,0,math.pi/2,100,"kiri")
    0.9921254566056331
    """
    delta_x = (b - a) / n
    sigma = 0.0
    approx = approx.lower()

    for i in range(n):
        left = a + i * delta_x
        right = left + delta_x

        if approx == "kiri":
            x_i = left
        elif approx == "kanan":
            x_i = right
        elif approx == "tengah":
            x_i = left + 0.5 * delta_x
        else:
            raise ValueError("masukkan approx benar")

        sigma += f(x_i)

    return delta_x * sigma


def main(args=None):
    import doctest

    doctest.testmod()

    # persamaan x
    def f(x):
        return x
    print(rieman_integral(f, 0, 1, 1, "tengah"))  # 0.5

    # persamaan 4/(1+x^2)
    def g(x):
        return (4) / (1 + x**2)
    print(rieman_integral(g, 0, 1, 1000, "tengah"))  # 3.1415927369231227

    # Persamaan sin
    def y(x):
        return math.sin(x)
    print(rieman_integral(y, 0, math.pi / 2, 100, "kiri"))  # 0.9921254566056331


if __name__ == "__main__":
    main()
