# Koch snowflake adalah kurva fraktal dan salah satu fraktal paling awal yang
# telah dijelaskan. Kepingan salju Koch dapat dibangun secara berulang, dalam
# urutan tahapan. Tahap pertama adalah segitiga sama sisi, dan masing-masing
# tahap berturut-turut dibentuk dengan menambahkan tikungan ke luar ke setiap sisi
# tahap sebelumnya, membuat segitiga sama sisi yang lebih kecil.

from __future__ import annotations

import matplotlib.pyplot as plt  # type: ignore
import numpy as np

VECTOR_1 = np.array([0, 0])
VECTOR_2 = np.array([0.5, 0.8660254])
VECTOR_3 = np.array([1, 0])
INITIAL_VECTORS = [VECTOR_1, VECTOR_2, VECTOR_3, VECTOR_1]


def iterate(initial_error: list[np.ndarray], steps: int) -> list[np.ndarray]:
    vectors = initial_error
    for i in range(steps):
        vectors = iteration_step(vectors)
    return vectors


def iteration_step(vectors: list[np.ndarray]) -> list[np.ndarray]:
    new_vectors = []
    for i, start_vector in enumerate(vectors[:-1]):
        end_vector = vectors[i + 1]
        new_vectors.append(start_vector)
        difference_vector = end_vector - start_vector
        new_vectors.append(
            start_vector + difference_vector / 3 + rotate(difference_vector / 3, 60)
        )
        new_vectors.append(start_vector + difference_vector * 2 / 3)
    new_vectors.append(vectors[-1])
    return new_vectors


def rotate(vector: np.ndarray, angle_in_degrees: float) -> np.ndarray:
    theta = np.radians(angle_in_degrees)
    c, s = np.cos(theta), np.sin(theta)
    rotation_matrix = np.array(((c, -s), (s, c)))

    return np.dot(rotation_matrix, vector)


def plot(vectors: list[np.ndarray]) -> None:
    axes = plt.gca()
    axes.set_aspect("equal")

    x_coordinates, y_coordinates = zip(*vectors)
    plt.plot(x_coordinates, y_coordinates)
    plt.show()


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    processed_vector = iterate(INITIAL_VECTORS, 5)
    plot(processed_vector)
