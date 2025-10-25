# Menghitung sinus dengan deret taylor
# https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions
import numpy as np


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("angkanya harus bilangan real")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def sinus(sudut : float | int, iterable: int = 10):
    """
    Sinus ini merupakan perhitungan dasar yang ada pada
    teori pythagoras
    Args:
        sudut (float | int): input ini merupakan value dari sudut yang kita
                         inputkan
    Returns:
        (float): hasil dari pembagian numerator dengan denominator

    >>> sinus(0)
    0.0
    >>> sinus(30)
    0.49999999999999994
    >>> sinus(45)
    0.7071067811865475
    >>> sinus(60)
    0.8660254037844385
    >>> sinus(90)
    1.0
    """
    result = 0.0
    radian = sudut * np.pi / 180
    for n in range(iterable):
        numerator = np.pow(radian, 2 * n + 1) * np.pow(-1, n)
        denominator = factorial(2 * n + 1)
        result += numerator / denominator
    return float(result)


if __name__ == "__main__":
    list_sudut = [0, 30, 45, 60, 90]
    for sudut in list_sudut:
        print(f"Sudut : {sudut}, Sin : {sinus(sudut)}")
