from __future__ import annotations
import math
import numpy as np
from numpy.linalg import norm


def euclidean(input_a: np.ndarray, input_b: np.ndarray) -> float:
    """
    menghitung jarak euclidean antara dua data

    Args:
        input_a (np.ndarray): array dari vektor pertama
        input_b (np.ndarray): array dari vektor kedua

    Return:
        (float) : jarak euclidean antara input_a dan input_b
                    dengan menggunakan math.sqrt()

    Contoh:

    >>> euclidean(np.array([0]), np.array([1]))
    1.0
    """
    return math.sqrt(sum(pow(a - b, 2) for a, b in zip(input_a, input_b)))


def similar_search(
    dataset: np.ndarray, value_array: np.ndarray
) -> list[list[float] | float]:
    """
    similiar search atau pencarian kemiripan adalah teknik machine
    learning yang digunakan untuk menenumkan dokumen, gambar,
    atau data lainnya yang mirip dengan query yang diberikan

    referensi:
    https://www.pinecone.io/learn/what-is-similarity-search/
    https://en.wikipedia.org/wiki/Similarity_learning
    https://encord.com/blog/vector-similarity-search/

    Args:
        dataset (np.ndarray): kumpulan vektor-vektor
        value_array (np.ndarray): vektor yang ingin kita ketahui vektor
                                   terdekat dari dataset

    Return:
        berupa sebuah daftar yang berisi vektor terdekat, jarak dari
        vektor-vektor tersebut

    Contoh:

    >>> dataset = np.array([[0], [1], [2]])
    >>> value_array = np.array([[0]])
    >>> similar_search(dataset, value_array)
    [[[0], 0.0]]

    >>> dataset = np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2]])
    >>> value_array = np.array([[0, 0, 0], [0, 0, 1]])
    >>> similar_search(dataset, value_array)
    [[[0, 0, 0], 0.0], [[0, 0, 0], 1.0]]
    """
    if dataset.ndim != value_array.ndim:
        pesan = (
            f"dimensi data input salah, dataset: {dataset.ndim} : {value_array.ndim}"
        )
        raise ValueError(pesan)

    try:
        if dataset.shape[1] != value_array.shape[1]:
            pesan = f"bentuk data input salah, dataset {dataset.shape[1]}, value_array: {value_array.shape[1]}"
            raise ValueError(pesan)
    except IndexError as index_error:
        if dataset.ndim != value_array.ndim:
            print(index_error)
            raise TypeError("bentuk salah...")

    if dataset.dtype != value_array.dtype:
        pesan = f"tipe data input berbeda, dataset: {dataset.dtype}, value_array: {value_array.dtype}"
        raise TypeError(pesan)

    answer: list = []

    for value in value_array:
        dist = euclidean(value, dataset[0])
        vector = dataset[0].tolist()

        for dataset_value in dataset[1:]:
            temp_dist = euclidean(value, dataset_value)
            if dist > temp_dist:
                dist = temp_dist
                vector = dataset_value.tolist()
        answer.append([vector, dist])

    return answer


def cosine_similarity(input_a: np.ndarray, input_b: np.ndarray) -> float:
    """
    menghitung kesamaan kosinus antara dua data

    Args:
        input_a (np.ndarray): array dari vektor pertama
        input_b (np.ndarray): array dari vektor kedua

    Return:
        (float) : kesamaan kosinus input_a dan input_b. dengan menggunakan
                    math.sqrt()
    """
    return np.dot(input_a, input_b) / (norm(input_a) * norm(input_b))


if __name__ == "__main__":
    import doctest

    # dataset = np.array([[0], [1], [2]])
    # value_array = np.array([[0]])
    # result = similar_search(dataset, value_array)
    # print(result)

    doctest.testmod()
