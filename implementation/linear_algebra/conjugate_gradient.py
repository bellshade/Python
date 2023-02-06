from typing import Any

import numpy as np


def is_matrix_spd(matrix: np.ndarray) -> bool:
    """
    Mengembalikan True jika matriks
    input adalah definit positif simetris.
    Mengembalikan False sebaliknya.
    >>> import numpy as np
    >>> dimension = 3
    >>> set_matrix = create_spd_matrix(dimension)
    >>> is_matrix_spd(set_matrix)
    True
    """
    assert np.shape(matrix)[0] == np.shape(matrix)[1]

    # Jika matriks tidak simetris, exit
    if np.allclose(matrix, matrix.T) is False:
        return False

    # Dapatkan nilai eigen dan
    # vektor eigen untuk matriks simetris.
    eigen_value, _ = np.linalg.eigh(matrix)

    return bool(np.all(eigen_value > 0))


def create_spd_matrix(dimension: int) -> Any:
    """
    Mengembalikan matriks definit positif
    simetris yang diberi dimensi.
    """

    random_matrix = np.random.randn(dimension, dimension)
    spd_matrix = np.dot(random_matrix, random_matrix.T)
    assert is_matrix_spd(spd_matrix)
    return spd_matrix


def conjugate_gradient(
    spd_matrix,
    load_vector,
    max_iterations=1000,
    tol=1e-8,
):
    """
    return solusi linear sistem np.dot(spd_matrix, x) = b
    >>> import numpy as np
    >>> spd_matrix_1= np.array([
    ... [8.73256573, -5.02034289, -2.68709226],
    ... [-5.02034289,  3.78188322,  0.91980451],
    ... [-2.68709226,  0.91980451,  1.94746467]])
    >>> b = np.array([
    ... [-5.80872761],
    ... [ 3.23807431],
    ... [ 1.95381422]])
    >>> conjugate_gradient(spd_matrix_1, b)
    array([[-0.63114139],
           [-0.01561498],
           [ 0.13979294]])
    """
    assert np.shape(spd_matrix)[0] == np.shape(spd_matrix)[1]
    assert np.shape(load_vector)[0] == np.shape(spd_matrix)[0]
    assert is_matrix_spd(spd_matrix)

    x0 = np.zeros((np.shape(load_vector)[0], 1))
    r0 = np.copy(load_vector)
    p0 = np.copy(r0)

    error_residual = 1e9  # lgtm [py/multiple-definition]
    error_x_solution = 1e9  # lgtm [py/multiple-definition]
    error = 1e9

    iterations = 0

    while error > tol:
        w = np.dot(spd_matrix, p0)
        alpha = np.dot(r0.T, r0) / np.dot(p0.T, w)
        # update solusi
        x = x0 + alpha * p0
        # kalkulasi residual terbaru
        r = r0 - alpha * w
        # kalkulasi
        beta = np.dot(r.T, r) / np.dot(r0.T, r0)

        # kalkulais conjugate searching
        p = r + beta * p0

        # kalkulasi error
        error_residual = np.linalg.norm(r - r0)
        error_x_solution = np.linalg.norm(x - x0)
        error = np.maximum(error_residual, error_x_solution)

        # update variabel
        x0 = np.copy(x)
        r0 = np.copy(r)
        p0 = np.copy(p)

        # update number dari iterasi
        iterations += 1
        if iterations > max_iterations:
            break

    return x


def testing_conjugate_gradient() -> None:
    """
    >>> testing_conjugate_gradient()
    """
    dimension = 3
    spd_matrix = create_spd_matrix(dimension)
    x_true = np.random.randn(dimension, 1)
    b = np.dot(spd_matrix, x_true)

    # solusi pakai numpy
    x_numpy = np.linalg.solve(spd_matrix, b)

    # implementasi
    x_conjugate_gradient = conjugate_gradient(spd_matrix, b)

    assert np.linalg.norm(x_numpy - x_true) <= 1e-6
    assert np.linalg.norm(x_conjugate_gradient - x_true) <= 1e-6


if __name__ == "__main__":
    import doctest

    # test_conjugate_gradient()
    doctest.testmod()
