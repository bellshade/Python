def eksponen(a: int, n: int) -> int:
    """
    Fungsi ini mengevaluasi a ^ n dengan
    kompleksitas waktu (O(n)) sebesar O(log n)

    Fungsi ini mengevaluasi a ^ n dengan memecah (divide)
    komponen pemangkatan dan menyelesaikan hingga pangkat
    dari komponen tersebut sama dengan 0 (conquer)

    Rumus umum :
    (a ^ (n/2)) * (a ^ (n/2)) jika n genap
    (a ^ ((n-1)/2)) * (a ^ ((n-1)/2)) * a jika n ganjil

    Contoh :
    3 ^ 5 = (3 ^ 2) * (3 ^ 2) * (3 ^ 1)
    3 ^ 2 = (3 ^ 1) * (3 ^ 1)

    Valid input :
    >>> eksponen(3, 3)
    27

    Invalid input :
    >>> eksponen(3, 2.5)
    Traceback (most recent call last):
    ...
    ValueError: Pangkat negatif atau pecahan
    """
    # meng-handle invalid input
    if isinstance(n, int) is False or n < 0:
        raise ValueError("Pangkat negatif atau pecahan")

    # base case
    elif n == 0:
        return 1

    else:
        x = eksponen(a, int(n / 2))
        if n % 2 == 0:
            return x * x
        else:
            return x * x * a


if __name__ == "__main__":
    import doctest
    
    doctest.testmod()
    # menghasilkan 243
    hasil = eksponen(3, 5)
    print(hasil)
    # me-raise exception
    hasil3 = eksponen(3, -1)
    print(hasil3)
