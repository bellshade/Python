import numpy as np


def fuzzy(n: int | float, close_number) -> float:
    """
    refence:
    http://staff.cs.upt.ro/~todinca/cad/Lectures/cad_fuzzysets.pdf(PDF file)
    """
    formula = 1 / (1 + pow(n - close_number, 2))

    return formula


def fuzzy_set(vector: np.array, close_number) -> float:
    """
    suatu himpunan yang elemennya memiliki derajat keanggotaan
    yang tidak hanya bernilai
    0 atau 1.
    melainkan juga dapat bernilai di antara keduanya.
    """
    result = 0
    for value in vector:
        formula = fuzzy(value, close_number) / value
        result += formula
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
