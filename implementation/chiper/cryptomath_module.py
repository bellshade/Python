def gcd(a: int, b: int) -> int:
    """
    >>> gcd(10, 5)
    5
    >>> gcd(5, 10)
    5
    >>> gcd(0, 5)
    5
    """
    while a != 0:
        a, b = b % a, a
    return b


def find_mod_inverse(a: int, m: int) -> int:
    """
    >>> find_mod_inverse(2, 5)
    3
    >>> find_mod_inverse(7, 26)
    15
    >>> find_mod_inverse(1, 26)
    1
    """
    if gcd(a, m) != 1:
        raise ValueError(f"mod kebalikan dari {a!r} dan {m!r} tidak ada")
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m
