import numpy as np


def variance(arr: np.array, ddof=0) -> float:
    """
    variance adalah untuk mengetahui keragaraman data terhadap selisih dari
    rata-rata tersebut

    **Params**
    ----------
    arr:parameter ini berfungsi untuk input data

    **Return**

    ----------
    float:hasil dari operasi ini berbentuk bilangan desimal
    """
    banyak_data = len(arr) - ddof
    formula = sum((arr - arr.mean()) ** 2) / banyak_data

    return formula


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
