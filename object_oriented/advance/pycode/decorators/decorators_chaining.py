from typing import Callable


# DECORATORS CHAINING
def add(func : Callable) -> Callable:
    """
    Fungsi ini akan memanggil fungsi lain dan mengembalikan fungsi
    >>> num1()
    1250
    """
    def wrap() -> int:
        x = func()
        return x + x
    return wrap


def add_quadrat(func : Callable) -> Callable:
    """
    Fungsi ini akan memanggil fungsi lain dan mengembalikan fungsi
    >>> num2()
    2500
    """
    def wrap() -> int:
        x = func()
        return x**2
    return wrap


# Cara menggunakan rantai decorators
@add
@add_quadrat
def num1() -> int:
    return 25


@add_quadrat
@add
def num2() -> int:
    return 25


def test_add():
    assert num1() == 1250


def test_add_quadrat():
    assert num2() == 2500
