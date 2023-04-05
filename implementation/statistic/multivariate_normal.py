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


def multivariate_normal(vector : np.array, mean=None, cov=None) -> np.array:
    """
    multivariate_normal adalah merupakan
    tipe peluang continues bertujuan menciptakan
    data random yang mirip value aslinya

    Param:
    ------
    vector:array dengan dimensi 2D

    Return:
    -----
    array: berisi number yang telah dilakukan normal distrbution

    Refence:
    --------
    https://towardsdatascience.com/gaussian-mixture-models-implemented-from-scratch-1857e40ea566
    https://github.com/Nuage21/Machine-Learning-from-Scratch/blob/master/Mgd.py
    Example:
    --------
    >>> x=np.random.randint(1,100,size=(100,2))
    >>> y=multivariate_normal(x)
    >>> y
    array(
        [-1.26135853e-18,  4.13560174e-19,  1.36474857e-18, -1.49915563e-19,
       -9.51188399e-19,  1.44746061e-19, -1.24068052e-18, -7.85764330e-19,
       -6.41018269e-19, -2.63644611e-19, -9.04662880e-20,  1.22000251e-18,
        3.87712663e-20,  1.03390043e-19, -5.47967230e-19, -8.16781343e-19,
        1.69559671e-18,  1.42678260e-18, -1.84034277e-18, -1.61546943e-21,
        1.69559671e-18, -1.69559671e-18,  1.83517327e-19, -8.89154373e-19,
       -2.89492121e-19,  1.11661247e-18,  7.80594827e-19, -5.47967230e-19,
       -4.34238182e-19,  6.41018269e-19,  3.10170130e-19, -1.65424069e-18,
        8.16781343e-19, -5.78984243e-19,  9.09832382e-19,  1.62839318e-19,
       -8.52967858e-20,  2.23322494e-18,  6.82374286e-19, -3.78019846e-20,
        1.59220667e-18, -7.96103334e-19,  1.48881662e-18,  1.03390043e-18,
       -0.00000000e+00, -1.65424069e-18, -9.82205412e-19,  1.86102078e-18,
       -3.17924383e-19, -2.94661624e-19, -1.01322243e-18, -1.34407056e-18,
       -4.00636418e-20,  1.53017264e-18,  7.03052295e-19, -8.16781343e-19,
        3.82543160e-19, -2.89492121e-19, -7.23730304e-20, -1.08559546e-19,
       -9.40849395e-19,  3.10170130e-19,  2.68814113e-19,  5.47967230e-19,
        2.58475108e-19,  1.03390043e-20,  5.27289221e-19,  6.82374286e-19,
        7.50224002e-19,  1.34407056e-18,  1.38542658e-18, -7.85764330e-19,
        3.46356645e-19,  1.96441082e-19, -8.68476364e-19,  2.06780087e-19,
       -1.81966476e-18,  1.73695273e-18,  8.58137360e-19, -2.15051290e-18,
        7.65086321e-19, -1.73178323e-19,  7.65086321e-19, -1.81966476e-18,
       -1.24068052e-18, -3.56695650e-19,  1.03390043e-19,  1.91271580e-19,
       -5.47967230e-19, -1.59220667e-18,  8.06442338e-19,  1.75763074e-18,
       -5.99662252e-19,  7.85764330e-19, -1.44746061e-18, -1.42678260e-18,
       -7.65086321e-19,  1.98508883e-18, -7.75425325e-19, -1.05457844e-18]
       )
    """
    # apabila ada mean sama dengan None
    if mean is None:
        mean = np.mean(vector, axis=0)
    if cov is None:
        X = vector - mean
        cov = (X.T @ X)
    # check apakah vectornya berdimensi 2
    if vector.ndim != 2:
        raise ValueError("Matrixnya harus berdimensi 2")
    _, m = vector.shape
    formula = (1. / np.sqrt((2 * np.pi) ** m * np.linalg.det(cov))
               * (-0.5 * np.sum(X @ (np.linalg.inv(cov) @ X.T), axis=1)))
    output = formula.squeeze()
    return output


if __name__ == "__main__":
    data = np.random.normal(loc=0, scale=1, size=(100, 2))
    print(multivariate_normal(dataset()))
    print(multivariate_normal(data))
