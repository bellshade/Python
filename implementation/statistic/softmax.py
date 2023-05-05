import numpy as np


def softmax(array: np.array) -> None:
    """
    Softmax adalah salah satu fungsi aktivasi yang sering
    digunakan pada jaringan saraf buatan untuk memetakan input ke
    dalam probabilitas keluaran yang sesuai dengan nilai target.
    """
    x = np.array(array)
    if x.ndim == 1:
        return np.exp(x) / np.sum(np.exp(x))
    elif x.ndim == 2:
        n, _ = x.shape
        return np.exp(x[:, n]) / np.sum(np.exp(x), axis=1)


if __name__ == "__main__":
    data = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])
    softmax_result = softmax(data)
    print(softmax_result)
