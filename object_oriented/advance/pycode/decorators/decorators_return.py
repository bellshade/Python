from typing import Union, Callable


def openseries(func: Callable) -> Callable:
    """
    Fungsi openseries akan di jadikan sebagai decorators yang mengembalikan fungsi
    Sekarang coba jalankan fungsi add yang di decorators fungsi openseries
    >>> a = 5
    >>> b = 9
    >>> add(a, b)
    '(5 + 9): 14'
    """

    def wrap(*args: Union[int, float]) -> Union[int, float]:
        return_val = func(*args)
        return return_val

    return wrap


@openseries
def add(a: Union[int, float], b: Union[int, float]) -> Union[int, str]:
    return f"({a} + {b}): {a + b}"


def test_openseries_add_func():
    assert add(5, 9) == "(5 + 9): 14"
