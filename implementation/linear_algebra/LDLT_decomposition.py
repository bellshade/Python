# https://en.wikipedia.org/wiki/Cholesky_decomposition#LDL_decomposition


def transpose(x: list[list[int]]) -> list[list[int]]:
    """
    >>> transpose([[1, 2], [3, 4]])
    [[1, 3], [2, 4]]
    """
    x = [[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]
    return x


def LDLT_decomposition(x: list[list[int]]) -> list[list[int]]:
    """
    >>> L, D, Lt = LDLT_decomposition([[2, 4, 6], [4, 9, 14], [6, 14, 19]])
    >>> L
    [[1, 0, 0], [2.0, 1, 0], [3.0, 2.0, 1]]
    >>> D
    [2.0, 1.0, -3.0]
    >>> Lt
    [[1, 2.0, 3.0], [0, 1, 2.0], [0, 0, 1]]
    """
    if transpose(x) == x:
        n = len(x)
        L = [[0 for _ in range(len(x))] for _ in range(len(x))]
        d = [0 for _ in range(len(x))]
        for i in range(n):
            sum_val = 0.0
            for k in range(i):
                sum_val += (L[i][k] ** 2) * d[k]
            d[i] = x[i][i] - sum_val

            for j in range(i + 1, n):
                sum_val = 0.0
                for k in range(i):
                    sum_val += L[j][k] * L[i][k] * d[k]
                L[j][i] = (x[j][i] - sum_val) / d[i]
            L[i][i] = 1
        Lt = transpose(L)
        return L, d, Lt
    else:
        return ValueError("Matriks tidak simetri")


def main(args=None):
    import doctest

    doctest.testmod()


if __name__ == "__main__":
    main()
