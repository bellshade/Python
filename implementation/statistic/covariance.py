import numpy as np
import requests


def dataset_collect():
    collect = requests.get(
        "https://raw.githubusercontent.com/yashLadha/The_Math_of_Intelligence/"
        "master/Week1/ADRvsRating.csv")
    line = collect.text.splitlines()
    data = []
    for item in line:
        item = item.split(',')
        data.append(item)
    data.pop(0)
    dataset = np.matrix(data).astype(float)
    return dataset


def cov(vector : np.array) -> np.array:
    """
    covariasi adalah pengukuran untuk hubungan dua variabel
    apabaila ada salah satu variabel meningkat maka variabel lain
    nya akan mengningkat pula

    Parameter:

    ----------
    vector: kumpulan data yang dimensi 2

    Return:

    --------
    vector: output ini berupa float di bungkus dgn vector

    refence:
    https://stats.stackexchange.com/questions/467306/how-calculate-variance-covariance-matrix-of-coefficients-for-multivariate-multi
    https://en.wikipedia.org/wiki/Covariance
    """
    n_sample = vector.shape[0] - 1
    mean_ = np.mean(vector, axis=0)
    X = vector - mean_
    return (X.T @ X) / n_sample


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    df = dataset_collect()
    covariance = cov(df)
    print(covariance)
