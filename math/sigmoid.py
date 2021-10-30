import numpy as np


def sigmoid(vector: np.array) -> np.array:
    """fungsi sigmoid digunakan untuk mendapatkan output berupa non-linear

    Args:
        vector (np.array): Nilai input berupa vektor

    Returns:
        np.array: Nilai sigmoid dari vektor yang diinputkan

    >>> sigmoid(np.array([-1.0, 1.0, 2.0]))
    array([0.26894142, 0.73105858, 0.88079708])
    >>> sigmoid(np.array([0.0]))
    array([0.5])
    """
    return 1 / (1 + np.exp(-vector))
