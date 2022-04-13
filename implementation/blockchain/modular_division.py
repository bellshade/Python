def modular_division(a: int, b: int, n: int) -> int:
    """
    Algoritma yang efisien untuk membagi b dengan modulo n.
    GCD ( Greatest Common Divisor ) atau HCF ( Highest Common Factor )
    Diberikan tiga bilangan bulat a, b, dan
    n, sehingga gcd(a,n)=1 dan n>1, algoritma harus
    return bilangan integer x seperti 0≤x≤n−1 dan b/a=x(modn) (b=ax(modn))

    a memiliki modulo invers perkalian n iff gcd(a,n) = 1
    Ini menemukan x = b*a^(-1) mod n
    Menggunakan ExtendedEuclid untuk menemukan invers dari a
    """

    assert n > 1 and a > 0 and greatest_common_divisor(a, n) == 1
    (d, t, s) = extended_gcd(n, a)
    x = (b * s) % n

    return x


def invert_modulo(a: int, n: int) -> int:
    """
    Fungsi ini mencari invers dari a yaitu, a^(-1)
    >>> invert_modulo(2, 5)
    3
    >>> invert_modulo(8,7)
    1
    """
    (b, x) = extended_euclid(a, n)
    if b < 0:
        b = (b % n + n) % n

    return b


def modular_division2(a: int, b: int, n: int) -> int:
    """
    Fungsi ini menggunakan invers a di atas
    untuk menemukan x = (b*a^(-1))mod n
    >>> modular_division(4, 8, 5)
    2
    """
    s = invert_modulo(a, n)
    x = (b * s) % n
    return x


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """
    Extended Euclid's Algorithm :
    Jika d membagi a dan b dan d = a*x + b*y untuk bilangan bulat x
    dan y, maka d = gcd(a,b)

    >>> extended_gcd(10, 6)
    (2, -1, 2)
    >>> extended_gcd(7, 5)
    (1, -2, 3)
    """
    assert a >= 0 and b >= 0

    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)

    assert a % d == 0 and b % d == 0
    assert d == a * x + b * y

    return (d, x, y)


def extended_euclid(a: int, b: int) -> tuple[int, int]:
    """
    >>> extended_euclid(10, 6)
    (-1, 2)

    >>> extended_euclid(7, 5)
    (-2, 3)
    """
    if b == 0:
        return (1, 0)
    (x, y) = extended_euclid(b, a % b)
    k = a // b
    return (y, x - k * y)


def greatest_common_divisor(a: int, b: int) -> int:
    """
    Catatan : Dalam teori bilangan, dua bilangan bulat a dan b
    dikatakan relatif prima,
    saling prima, atau co-prima jika satu-satunya
    bilangan bulat positif (faktor) yang membagi
    keduanya adalah 1 yaitu, gcd(a,b) = 1.
    >>> greatest_common_divisor(7, 5)
    1

    >>> greatest_common_divisor(121, 11)
    11
    """
    if a < b:
        a, b = b, a

    while a % b != 0:
        a, b = b, a % b

    return b


if __name__ == "__main__":
    import doctest

    # doctest.testmod(name="modular_division", verbose=True)
    # doctest.testmod(name="modular_division2", verbose=True)
    # doctest.testmod(name="invert_modulo", verbose=True)
    # doctest.testmod(name="extended_gcd", verbose=True)
    # doctest.testmod(name="extended_euclid", verbose=True)
    # doctest.testmod(name="greatest_common_divisor", verbose=True)
    doctest.testmod()
