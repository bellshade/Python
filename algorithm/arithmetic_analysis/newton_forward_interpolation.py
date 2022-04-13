import math

# kalkulasi nilai u


def ucal(u: float, p: int) -> float:
    """
    >>> ucal(1, 2)
    0
    >>> ucal(1.1, 2)
    0.11000000000000011
    >>> ucal(1.2, 2)
    0.23999999999999994
    """
    temp = u
    for i in range(1, p):
        temp = temp * (u - i)
    return temp


def setcal() -> None:
    n = int(input("masukkan jumlah nilai: "))
    y: list[list[float]] = []
    for i in range(n):
        y.append([])
    for i in range(n):
        for j in range(n):
            y[i].append(j)
            y[i][j] = 0

    print("masukkan nilai parameter dalam list: ")
    x = list(map(int, input().split()))

    print("masukkan nilai parameter yang sesuai: ")
    for i in range(n):
        y[i][0] = float(input())

    value = int(input("masukkan nilai untuk diinterpolasi :"))
    u = (value - x[0]) / (x[1] - x[0])

    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = y[j + 1][i - 1] - y[j][i - 1]

    summ = y[0][0]
    for i in range(1, n):
        summ += (ucal(u, i) * y[0][i]) / math.factorial(i)

    print(f"Nilai di {value} adalah {summ}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
