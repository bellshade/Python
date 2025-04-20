import math


def fungsi_gamma(nilai: float) -> float:
    """
    Hitung nilai fungsi gamma untuk `nilai`
    fungsi ini hanya mengdukung bilangan bulat seperti
    (1, 2, 3, 4 ... n) atau nilai pecahan, berkoma
    (0.1, 2.5, 3.4, 3.3 ... n)

    informasi relevan tentang fungsi gamma:
    - https://en.wikipedia.org/wiki/Gamma_function
    - https://mathworld.wolfram.com/GammaFunction.html

    Parameter:
        nilai(float): nilai yang diberikan

    Return:
        (float): hasil kalkulasi fungsi gamma

    Contoh:
    >>> fungsi_gamma(0.5)
    1.7724538509055159
    >>> hitung_gamma(1)
    1.0
    >>> hitung_gamma(3.5)
    3.3233509704478426
    """
    # memastikan nilai tidak kurang atau sama dengan 0
    # atau negatif
    if nilai <= 0:
        raise ValueError("nilai harus lebih besar dari nol")

    # membuat batasan maks dari nilai yang diberikan
    # fungsi logika ini hanya bersifat opsional
    if nilai > 175.5:
        raise OverflowError("nilai rentang terlalu besar")

    # memastikan nilai adalh bilangan bulat atau pecahan
    if nilai - int(nilai) not in (0, 0.5):
        raise NotImplementedError("nilai harus bilangan bulat atau berkoma")

    # buat basis rekursi dari gamma gamma(0.5) = sqrt(pi)
    if nilai == 0.5:
        return math.sqrt(math.pi)

    # buat basis rekursi jika gamma(1) = 1
    if nilai == 1:
        return 1.0

    return (nilai - 1) * fungsi_gamma(nilai - 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # contoh pemanggilan
    # print(fungsi_gamma(1))

    # nilai: float = 2.5
    # print(f"hasil fungsi_gamma({nilai}) adalah: {fungsi_gamma(nilai)}")
