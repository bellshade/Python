from math import factorial


def cos(x: int | float):
    """
    # Deskripsi
    merupakan cos yang ada trigonometric.nah pada algorithm ini
    menggunakan taylor series factorial dan hyperbolic karena
    untuk menghasilkan input sesuai dengan kuadran I,II,III
    dan IV

    # Args:
        x (int | float): parameter ini merupakan input
                         bervalue derajat
    # Returns:
        float: hasil dari taylor dengar hyperbolic

    Contoh:
    >>> from math import pi
    >>> cos(0)
    -1.0
    >>> cos(pi/4)
    -1.3246090892520062
    """
    result = 0

    for i in range(0, 25):

        numerator = (-1 ** i) * (x ** (2 * i))
        denumerator = factorial(2 * i)
        result += (numerator / denumerator)

    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
