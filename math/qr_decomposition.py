import numpy as np


def qr_householder(A):
    """
    Dekomposisi QR menguraikan matriks A berbentuk (m, n) menjadi an
    matriks ortogonal Q bentuk (m, m) dan matriks segitiga atas R dari
    bentuk (m, n). Perhatikan bahwa matriks A tidak harus persegi. Ini
    metode penguraian A menggunakan refleksi Householder, yaitu
    stabil secara numerik dan kompleksitas O(n^3).

    informasi lebih lanjut
    https://en.wikipedia.org/wiki/QR_decomposition#Using_Householder_reflections

    >>> A = np.array([[12, -51, 4], [6, 167, -68], [-5, 24, -14]], dtype=float)
    >>> Q, R = qr_householder(A)

    >>> # cek apabila dekomposisi benar
    >>> np.allclose(Q@R, A)
    True
    """
    m, n = A.shape
    t = min(m, n)
    Q = np.eye(m)
    R = A.copy()

    for k in range(t - 1):
        x = R[k:, [k]]
        e1 = np.zeros_like(x)
        e1[0] = 1.0
        alpha = np.linalg.norm(x)
        v = x + np.sign(x[0]) * alpha * e1
        v /= np.linalg.norm(v)

        Q_k = np.eye(m - k) - 2.0 * v @ v.T
        Q_k = np.block([[np.eye(k), np.zeros((k, m - k))], [np.zeros((m - k, k)), Q_k]])

        Q = Q @ Q_k.T
        R = Q_k @ R

    return Q, R


if __name__ == "__main__":
    import doctest

    doctest.testmod()
