# Menghitung cosisnus dengan menggunakan deret taylor
# https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions
import numpy as np


def factorial(x):
    if x < 0:
        return ValueError("Angkanya harus bilangan real")
    if x == 0 or x == 1:
        return 1
    else:
        return x * (factorial(x - 1))


def cosinus(sudut):
    """
    Cosinus adalah sebuah perbandingan dari sisi samping dan
    miring segitiga siku-siku.

    >>> cosinus(0)
    1.0
    >>> cosinus(30)
    0.8660254037844386
    >>> cosinus(45)
    0.7071067811865475
    >>> cosinus(60)
    0.5000000000000001
    >>> cosinus(90)
    -3.3769215522516056e-15
    """
    result = 0.0
    interable = 10
    radian = sudut * np.pi / 180
    for i in range(interable):
        numerator = np.pow(radian, 2 * i) * np.pow(-1, i)
        detector = factorial(2 * i)
        result = result + (numerator / detector)

    return float(result)


def main(args=None):
    import doctest

    doctest.testmod()

    # base case
    print(cosinus(0))  # 1.0
    print(cosinus(30))  # 0.8660254037844386
    print(cosinus(45))  # 0.7071067811865475
    print(cosinus(60))  # 0.5000000000000001
    print(cosinus(90))  # -3.3769215522516056e-15


if __name__ == "__main__":
    main()
