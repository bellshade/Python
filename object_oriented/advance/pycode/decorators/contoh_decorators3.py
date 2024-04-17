from typing import Callable


# Contoh Decorator 3
def users(nama: str) -> Callable:
    """
    Fungsi ini hanya mengembalikan sebuah fungsi
    :param name: Parameter nama dari fungsi users
    >>> nama = 'Udin'
    >>> belajar = users(nama)
    >>> belajar('Python')
    'Udin sedang belajar: Python'
    """

    def belajar(str1: Callable) -> str:
        """
        Fungsi ini akan membungkus parameter dari users
        """

        # Return ini mengembalikan nilai untuk fungsi (belajar)
        return f"{nama} sedang belajar: {str1}"

    # Di return terluar, kita akan mengembalikan nilai berupa fungsi (belajar)
    return belajar


def test_input_user():
    name = "Udin"
    belajar = users(name)
    assert "Udin sedang belajar: Python" == belajar("Python")
