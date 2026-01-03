# macam macam deret taylor
# https://en.wikipedia.org/wiki/Taylor_series
import math


def faktorial(n : int = 2) -> int:
    """
    Fungsi untuk kalkulasi faktorial

    parameter :
    n = bilangan bulat

    return :
    hasil = hasil dari operasi faktorial
    """
    if n == 1 or n == 0:
        return 1
    if n > 1:
        return n * faktorial(n - 1)


def sin(x : float) -> float:
    """
    Fungsi untuk kalkulasi dari deret sin.
    Input dari fungsi ini dikonvergensi menjadi
    radian.

    >>> sin(0)
    0.0
    >>> sin(45)
    0.7071067811865475
    """
    result = 0.0
    interable = 10
    radian = x * math.pi / 180
    for i in range(interable + 1):
        numerator = math.pow(radian, (1 + i * 2)) * math.pow(-1, i)
        detector = faktorial((1 + 2 * i))
        result = result + (numerator / detector)
    return float(result)


def cos(x : float) -> float:
    """
    Fungsi untuk kalkulasi dari deret cosinus.
    Input dari fungsi ini dikonvergensi menjadi
    radian.

    >>> cos(0)
    1.0
    >>> cos(45)
    0.7071067811865475
    """
    result = 0.0
    interable = 10
    radian = x * math.pi / 180
    for i in range(interable):
        numerator = math.pow(radian, 2 * i) * math.pow(-1, i)
        detector = faktorial(2 * i)
        result = result + (numerator / detector)
    return float(result)


def euler(x: int = 1) -> float:
    """
    Fungsi untuk kalkulasi dari deret
    taylor euler e^x

    >>> euler(1)
    2.7182815255731922
    >>> euler(2)
    7.3887125220458545
    """
    result = 0.0
    interable = 10
    for i in range(interable):
        numerator = math.pow(x, (i))
        detector = faktorial(i)
        result = result + (numerator / detector)
    return float(result)


def ln(x : float) -> float:
    """
    Fungsi untuk melakukan kalkulasi deret taylor
    ln(x + 1).Dengan batas -1 < x <= 1.


    >>> ln(0.5)
    0.4054346478174603
    >>> ln(1)
    0.6456349206349207
    """
    if x > -1 and x <= 1:
        result = 0.0
        interable = 10
        for i in range(1, interable + 1):
            numerator = math.pow(x, i) * math.pow(-1, i + 1)
            detector = i
            result = result + (numerator / detector)
        return float(result)
    else :
        return ValueError("Angka tidak valid")


def main(args=None):
    import doctest

    doctest.testmod()

    # test untuk fungsi cos
    print(cos(0))
    print(cos(45))

    # test untuk fungsi sin
    print(sin(0))
    print(sin(45))

    # test untuk fungsi euler
    print(euler(1))
    print(euler(2))

    # test untuk fungsi ln(1 + x)
    print(ln(0.5))
    print(ln(1))


if __name__ == "__main__":
    main()
