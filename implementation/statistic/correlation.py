import numpy as np
import requests


def dataset() -> np.array:
    respon = requests.get(
        "https://raw.githubusercontent.com/yashLadha/The_Math_of_Intelligence/"
        "master/Week1/ADRvsRating.csv"
    )
    line = respon.text.splitlines()
    data = []
    for item in line:
        item = item.split(',')
        data.append(item)
    data.pop(0)
    dataset = np.matrix(data).astype(float)
    return dataset


def correlation(matrix: np.array) -> np.array:
    """
    correlation merupakan hubungan dua variabel
    atau lebih baik variabel bersifat bebas atau
    terikat.
    Parama:
    -------
    params:matrix: merupakan bentuk array bersifat multivariat
    refence:
    https://en.wikipedia.org/wiki/Correlation
    """
    n = matrix.shape[0]
    mean_ = np.mean(matrix, axis=0)
    X = matrix - mean_
    cov = (X.T @ X) / (n)
    std_dev = np.sqrt(np.diag(cov))
    inv_std_dev = np.diag(1 / std_dev)
    return inv_std_dev @ cov @ inv_std_dev


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    matrix = dataset()
    print(dataset())
    print(correlation(matrix))
