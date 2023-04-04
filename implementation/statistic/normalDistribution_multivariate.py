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
    dataset = dataset[:, [0, 1]]
    return dataset


def gauss_distribution_multivariate(vector : np.array) -> np.array:
    """
    gauss distribusi normal adalah merupakan
    tipe peluang continues bertujuan menciptakan
    data random yang mirip value aslinya

    Param:
    ------
    vector:array dengan dimensi 2D

    Return:
    -----
    array: berisi number yang telah dilakukan normal distrbution
    """
    n, m = vector.shape
    mean_ = np.mean(vector, axis=0)
    X = vector - mean_
    cov = (X.T @ X) / (n - 1)
    formula = (1. / np.sqrt((2 * np.pi) ** m * np.linalg.det(cov))
               * (-0.5 * np.sum(X @ (np.linalg.inv(cov) @ X.T), axis=1)))
    return formula


if __name__ == "__main__":
    data = np.random.normal(loc=0, scale=1, size=(100, 2))
    print(gauss_distribution_multivariate(dataset()))
    print(gauss_distribution_multivariate(data))
