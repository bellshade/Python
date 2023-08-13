from math import e, factorial


def exponent(x: int | float):
    """_summary_

    Args:
        x (_type_): _description_

    Returns:
        _type_: _description_
    Contoh:
    >>> exponent(2)
    7.38905609893
    >>> exponent(1)
    2.71828182846
    """
    n_term: int = 100
    result: float = 0.0
    for n in range(n_term):
        result += x**n / factorial(n)

    return round(result, 11)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
