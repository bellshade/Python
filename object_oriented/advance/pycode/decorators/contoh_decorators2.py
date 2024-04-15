from typing import Callable


# Contoh Decorator 2
def wpu(str1: str) -> str:
    # Fungsi wpu yang mengembalikan nilai string upper
    return str1.upper()


def terbuka(str2: str) -> str:
    # Fungsi terbuka yang mengembalikan nilai string lower
    return str2.lower()


def bellshade(func: Callable) -> str:
    """
    Fungsi ini akan menampung fungsi dari luar fungsi bellshade
    :param func: parameter fungsi yang akan menampung fungsi lainnya
    >>> mhs1 = wpu
    >>> mhs2 = terbuka
    >>> bellshade(mhs1)
    'HALO SOBAT BELLSHADE!!!'
    >>> bellshade(mhs2)
    'halo sobat bellshade!!!'
    """
    return func("Halo Sobat bellshade!!!")


def test_func_upper():
    assert "HALO SOBAT BELLSHADE!!!" == bellshade(wpu)


def test_func_lower():
    assert "halo sobat bellshade!!!" == bellshade(terbuka)
