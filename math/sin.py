

def factorial(n: int):
    """
    Args:
        n (int): input yang berupa tipe data
                 integer yang betujuan untukmenglipatkan
                 ganda nilai dengan perkalian di sendiri
    Raises:
        ValueError: faktorial harus positif

    Returns:
        int : merupakan hasil dari perkalian diri sendiri
    """
    if n < 0:
        raise ValueError("faktorial harus positif")
    if n in (0, 1):
        return 1
    else:
        return n * factorial(n - 1)


def sin(x: int | float):
    """
    merupakan sin yang ada trigonometric.nah pada algorithm ini
    menggunakan taylor series factorial dan hyperbolic karena
    untuk menghasilkan input sesuai dengan kuadran I,II,III
    dan IV
    Args:
        x (int | float): input parameter yang berupa derajat
                         yang kita ketahui
    Returns:
        float: hasil dari perhitungan sesuai dengan aturan
               lingkaran dan juga hyperbolic
    contoh
    >>> from math import pi
    >>> sin(0)
    0.0
    >>> sin(pi/4)
    -0.8686709614860095
    """
    result = 0

    for i in range(0, 25):
        numerator = (-1 ** i) * (x ** (2 * i + 1))
        denumerator = factorial(2 * i + 1)
        result += (numerator / denumerator)
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
