from math import pi, e

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("The input must be a non-negative integer.")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def sinus(x: float | int, iterable: int = 4):
    result = 0
    for n in range(iterable):
        numerator = ((e ** (complex(0, pi / 180) * x)) - (e ** (-complex(0, pi / 180) * x)))
        denominator = factorial(2 * n + 1)
        result += (numerator / denominator)
    return result

if __name__ == "__main__":
    list_sudut = [0,pi/2, pi * 3/4, pi]
    for sudut in list_sudut:
        print("Sudut:", sudut, "Sin:", sinus(sudut))
