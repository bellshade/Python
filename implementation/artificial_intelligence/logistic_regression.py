# logistik regression adalah teknik analisis data yang
# menggunakan matematika untuk menemukan antara dua
# faktor data. kemudian menggunakan hubungan ini untuk
# memprediksi nilai dari salah satu faktor tersebut
# berdasarkan faktor yang lain. prediksi biasanya
# memiliki jumlh hasil yang terbata, antara ya dan tidak.
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets


def fungsi_cost(h, y):
    """
    untuk memetakan proses atau nilai dari
    satu atau lebih bariabel ke bilangan rill
    secara intuitif mewakili berapa biaya yang
    terkait dengan proses
    """
    return (-y * np.log(h) - (1 - y) * np.log(1 - h)).mean()


def kemungkinan_maksimum(x, y, ukuran):
    """
    ini adalah metode untuk memperkirakan parameter
    dari distribusi probabilitas yang diasumsukan,
    mengingat beberapa data yang diamati.
    """
    skor = np.dot(x, ukuran)
    return np.sum(y * skor - np.log(1 + np.exp(skor)))


def fungsi_sigmoid(n):
    return 1 / (1 + np.exp(-n))


def logsitik_regresi(
    alpha: float, x: np.ndarray, y: np.ndarray, max_iterasi: int = 70000
):
    theta = np.zeros(x.shape[1])

    for iterasi in range(max_iterasi):
        z = np.dot(x, theta)
        h = fungsi_sigmoid(z)
        gradient = np.dot(x.T, h - y) / y.size
        theta = theta - alpha * gradient
        z = np.dot(x, theta)
        h = fungsi_sigmoid(z)
        j = fungsi_cost(h, y)
        if iterasi % 100 == 0:
            print(f"loss {j} \t")
    return theta


if __name__ == "__main__":
    iris = datasets.load_iris()
    x = iris.data[:, :2]
    y = (iris.target != 0) * 1

    alpha = 0.1
    theta = logsitik_regresi(alpha, x, y, max_iterasi=70000)
    print("theta: ", theta)

    def prediksi_probabilitas(x: np.ndarray):
        return fungsi_sigmoid(np.dot(x, theta))

    plt.figure(figsize=(10, 6))
    plt.scatter(x[y == 0][:, 0], x[y == 0][:, 1], color="b", label="0")
    plt.scatter(x[y == 1][:, 0], x[y == 1][:, 1], color="r", label="1")
    (x1_min, x1_max) = (x[:, 0].min(), x[:, 0].max())
    (x2_min, x2_max) = (x[:, 1].min(), x[:, 1].max())
    (xx1, xx2) = np.meshgrid(np.linspace(x1_min, x1_max), np.linspace(x2_min, x2_max))
    grid = np.c_[xx1.ravel(), xx2.ravel()]
    probs = prediksi_probabilitas(grid).reshape(xx1.shape)
    plt.contour(xx1, xx2, probs, [0.5], linewidths=1, colors="black")

    plt.legend()
    plt.show()
