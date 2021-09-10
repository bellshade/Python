def max_difference(a: list[int]) -> tuple[int, int]:
    """
    diberi array A[1..n] bilangan int, n >= 1. Kami ingin
    tentukan pasangan indeks (i,j) sedemikian rupa sehingga
    1 <= i <= j <= n dan A[j] - A[i] sebesar mungkin.
    informasi lebih lanjut
    https://www.geeksforgeeks.org/maximum-difference-between-two-elements/

    >>> max_difference([5, 11, 2, 1, 7, 9, 0, 7])
    (1, 9)
    """
    if len(a) == 1:
        return a[0], a[0]
    else:
        # membagi A menjadi setengah
        first = a[: len(a) // 2]
        second = a[len(a) // 2 :]

        # 2 sub masalah, 1/2 dari ukuran aslinya.
        small1, big1 = max_difference(first)
        small2, big2 = max_difference(second)

        min_first = min(first)
        max_second = max(second)

        if big2 - small2 > max_second - min_first and big2 - small2 > big1 - small1:
            return small2, big2
        elif big1 - small1 > max_second - min_first:
            return small1, big1
        else:
            return min_first, max_second


if __name__ == "__main__":
    import doctest

    doctest.testmod()
