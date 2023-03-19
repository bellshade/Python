import numpy as np


def entropy(labels, base=None) -> float:
    """
    menghitung entropy dari suatu fitur pada suatu dataset.

    Parameter:

    -----------
    labels:numpy.array
        Array 1-D yang berisi fitur yang akan dihitung entropynya
    base: int
        base ini merupakan basis log yang diingikan oleh pemakai
    refensi:
    https://www.youtube.com/watch?v=2s3aJfRr9gE (Video Tutorial)
    https://en.wikipedia.org/wiki/Entropy_(information_theory) (online reading)
    https://towardsdatascience.com/entropy-how-decision-trees-make-decisions-2946b9c18c8
    (Towards Data Science)

    example:

    --------
    >>> label=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    >>> entropy(label,base=2)
    0.9967916319816366
    """
    _, counts = np.unique(labels, return_counts=True)
    probs = counts / len(labels)
    logs = np.log(probs) if base is None else np.log(probs) / np.log(base)
    return np.sum(abs(probs * logs))


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
