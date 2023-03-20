import numpy as np


def fuzzy(n: int | float, close_number) -> float:
    """
    Fuzzy logic adalah suatu sistem logika yang memungkinkan untuk
    mengatasi ketidakpastian
    atau ambiguitas dalam pengambilan keputusan,
    dengan menggunakan nilai-nilai yang tidak hanya bersifat benar atau salah,
    tetapi juga dapat diukur dalam bentuk derajat kebenaran yang kabur.
    Misalnya,penggunaan fuzzy logic dalam kendali otomatis
    dapat membantu memperbaiki kinerja sistem,
    karena dapat mengakomodasi variasi dan ketidakpastian
    dalam lingkungan yang dioperasikan.
    **Params**

    -------
    n:variabel n ini merupakan input angka baik bentuk bulat maupun desimal
    close_number:angka ini merupakan angka terdekat

    **Return**

    -----------
    keluar dari output ini berupa bilangan desimal di karenakan rumusnya
    **refence**
    http://staff.cs.upt.ro/~todinca/cad/Lectures/cad_fuzzysets.pdf(PDF file)
    """
    formula = 1 / (1 + pow(n - close_number, 2))

    return formula


def fuzzy_set(vector: np.array, close_number) -> float:
    """
    Fuzzy set dalam fuzzy logic adalah himpunan yang terdiri
    dari elemen-elemen yang memiliki derajat keanggotaan yang kabur atau tidak tegas.
    Dengan menggunakan konsep fuzzy set, fuzzy logic dapat menggambarkan secara
    matematis pengambilan keputusan yang kompleks,
    seperti pada sistem kendali otomatis yang mengandalkan
    masukan berupa variabel-variabel kabur
    yang dapat dinyatakan dalam bentuk fungsi keanggotaan.
    """
    result = 0
    for value in vector:
        formula = fuzzy(value, close_number) / value
        result += formula
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
