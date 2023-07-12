from math import pi, e


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("angkanya harus bilangan real")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def sinus(x: float | int, iterable: int = 4):
    """
    Sinus ini merupakan perhitungan dasar yang ada pada
    teori pythagoras
    Args:
        x (float | int): input ini merupakan value dari sudut yang kita
                         inputkan
        iterable (int, optional): paramater ini untuk jumlah data yang kuta sum kan
                                  Defaults to 4.
    Returns:
        complex: hasil dari pembagian numerator (complex) dengan denominator
    """
    result = 0
    for n in range(iterable):
        # bikin numerial nya
        numerator = ((e ** (complex(0, pi / 180) * x))
                     - (e ** (-complex(0, pi / 180) * x)))
        # dengan menggunakan factorial
        denominator = factorial(2 * n + 1)
        result += (numerator / denominator)
    return result


if __name__ == "__main__":
    list_sudut = [0, pi / 2, pi * 3 / 4, pi]
    for sudut in list_sudut:
        print("Sudut:", sudut, "Sin:", sinus(sudut))
