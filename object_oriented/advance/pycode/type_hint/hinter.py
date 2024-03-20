from typing import Callable

# variable with type hint
nama: str = 'Bellshade'


# definisi function with type hint with return function
def user(nama: str) -> str:
    """
    Fungsi untuk menangkap value dari fungsi id
    >>> nama = 'Bellshade'
    >>> user(nama)
    'Bellshade'
    """
    return id(nama)


# definisi function with type hint and return
def id(nama: str) -> str:
    return nama


# testing code
def test_runner_code():
    nama = 'Bellshade'
    assert user(nama) == 'Bellshade'


# running
if __name__ == '__main__':
    user(nama)
