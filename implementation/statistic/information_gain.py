import numpy as np
from entropy import entropy


def informain_gain(feature_df, label_df, base=None) -> float:
    """
    Menghitung information gain dari suatu fitur pada suatu dataset.

    Parameter:

    -----------
    feature_arr: numpy.ndarray
        Array 1D yang berisi fitur yang akan dihitung information gain-nya.
    label_arr: numpy.ndarray
        Array 1D yang berisi label dari dataset.
    base:int
        base ini digunakan untuk basis log

    Return:
    -------
    float
        infomasi gain dari fitur
    refence:
    https://homes.cs.washington.edu/~shapiro/EE596/notes/InfoGain.pdf
    https://towardsdatascience.com/entropy-how-decision-trees-make-decisions-2946b9c18c8
    """
    # Menghitung entropy label
    parent_entropy = entropy(label_df, base)

    # Menghitung entropy setiap feature
    child_entropy = 0
    for value in np.unique(feature_df):
        group_entropy = (entropy(label_df[feature_df == value], base)
                         * np.sum(feature_df == value))
        child_entropy += group_entropy

    # Menghitung information gain
    information_gain = parent_entropy - child_entropy / len(feature_df)

    return information_gain
