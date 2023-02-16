def fibonacci(n: int) -> list[int]:
    """
    fibonacci adalah merupakan sebuah pola angka dengan ciri khas,••
    yaitu nilai a=0 sertanilai b=1.••
    dan nilai selanjutnya di tambah nilai di posisi 2 - posisi 1.••
    rumus:Fn = Fn-1 + Fn-2.••
    >>> fibonacci(5)
    [0, 1, 1, 2, 3]
    >>> fibonacci(10)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    a = 0
    b = 1
    # tempat untuk menyimpan data banyak dalam satu variabel
    memory = []
    for _ in range(n):
        memory.append(a)
        a, b = b, a + b
    return memory


if __name__ == "__main__":
    import doctest

    doctest.testmod()