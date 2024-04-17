from functools import wraps
from typing import Callable


# GENERATORS
def Generators(func: Callable) -> Callable:
    """
    Fungsi ini akan menerima parameter dari user untuk melakukan generate
    ubah bagian range function menjadi [for i in range(random.randint(5,35))]
    hapus [return i] jika ingin generate berlanjut

    :param func: Tipe parameter diharuskan object_func
    :return: Hasil Generators
    >>> coba1()
    49
    """

    @wraps(func)
    def start() -> int:
        i: int = 1
        for i in range(13, 50):
            i ** func()
        return i

    return start


def test_generators():

    @Generators
    def coba1():
        return 7

    assert coba1() == 49


@Generators
def coba1():
    return 7


if __name__ == "__main__":
    print(coba1())
