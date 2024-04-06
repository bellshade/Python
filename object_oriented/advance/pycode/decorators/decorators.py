from typing import Callable


# Decorators
def bellshade(func : Callable) -> Callable:
    """
    Fungsi ini akan kita jadikan sebagai decoratord decorators (@)
    Saat Mengeksekusi, kita cukup panggil Fungsi wpu
    >>> wpu('Bellshade')
    'Selamat datang Bellshade'
    """

    def wrap(str1 : str) -> str:
        return f'Selamat datang {str1}'

    return wrap  # <- Mengembalikan fungsi (wrap) sebagai fungsi terdalam (bellshade)


@bellshade
def wpu(str1 : str) -> str:
    return str1


# ----------| Cara Penggunaan Decorators |---------- #
def test_decorators():
    @bellshade
    def wpu(str1):
        return str1
        assert str1 == 'Bellshade'
