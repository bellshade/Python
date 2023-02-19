def fibonacci(n: int) -> list[int]:
    """
    fibbonacci adalah urutan angka dari jumlah dari dua bilangan sebelumnya,.
    kecuali dengan bilangan pertama dan kedua yang nilainya adalah 0 dan 1.
    >>> fibonacci(5)
    [0, 1, 1, 2, 3, 5]
    >>> fibonacci(10)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    """
    if n < 0:
        assert "Input integer value tidak boleh negatif"

    a = 0
    b = 1
    result = []
    for _ in range(n + 1):
        result.append(a)

        a, b = b, a + b

    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
