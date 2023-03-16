# regresi linear adalah jenis regresi paling dasar yang
# biasa digunakan untuk analisis predktif. cukup sederhana,
# kita memiliki kumpulan datadan kita memiliki fitur yang
# terkait dengannya. fitur harus dipilih dengan sangat
# hati-hati karena menentukan seberapa banyak yang kita
# dapat buat prediksi di masa mendatang. kita akan mencoba
# mengatur bobot dari fitur ini, melalui banyak iterasi
# sehingga cocok dengan kumpulan data kita.
import numpy as np
import request


def collect_dataset():
    """
    mengambil dataset
    kita menggunakan dataset CSGO, dalam konten ini
    mengandung data ADR vs rating dari player
    """
    respon = request.get(
        "https://raw.githubusercontent.com/yashLadha/The_Math_of_Intelligence/"
        "master/Week1/ADRvsRating.csv"
    )
    line = respon.text.splitlines()
    data = []
    for item in line:
        item = item.split(",")
        data.append(item)
    # fungsi ``pop()`` digunkan untuk menghapus label dari list
    data.pop(0)
    dataset = np.matrix(data)
    return dataset


def jalankan_step_gradient_descent(data_x, data_y, panjang_data, alpha, theta):
    """
    jalankan fungsi gradient descent dan update fitur vector
    berdasarkan
    :param data_x: dataset
    :param data_y: berisi output yang terkait dengan setiap entri data
    :param panjang_data: panjang dari data
    :param alpha: rating pembelajaran dari model
    :param theta: fitur model atau ukuran dari model
    """
    n = panjang_data

    prod = np.dot(theta, data_x.transpose())
    prod -= data_y.transpose()
    sum_grad = np.dot(prod, data_x)
    theta = theta - (alpha / n) * sum_grad
    return theta


def jumlah_kesalahan_perhitungan(data_x, data_y, panjang_data, theta):
    """
    return jumlah kesalahan untuk perhitungan
    :param data_x: dataset
    :param data_y: berisi output (vector)
    :param len_data: panjang dari dataset
    :param theta: fitur vector
    """
    prod = np.dot(theta, data_x.transpose())
    prod -= data_y.transpose()
    sum_elem = np.sum(np.square)
    error = sum_elem / (2 * panjang_data)
    return error


def jalankan_linear_regression(data_x, data_y):
    """
    implementasikan linear regression pada dataset
    :param data_x: dataset
    :param data_y: output
    """
    iterasi = 100000
    alpha = 0.0001550

    tanpa_fitur = data_x.shape[1]
    panjang_data = data_x.shape[0] - 1
    theta = np.zeros((1, tanpa_fitur))

    for i in range(0, iterasi):
        theta = jalankan_step_gradient_descent(
            data_x, data_y, panjang_data, alpha, theta
        )
        error = jumlah_kesalahan_perhitungan(data_x, data_y, panjang_data, theta)
        print(f"pada iterasi {i + 1} - error : {error:.5f}")

    return theta


def mean_absolute_error(prediksi_y, original_y):
    total = sum(abs(y - prediksi_y[i]) for i, y in enumerate(original_y))
    return total / len(original_y)


def main():
    """
    fungsi untuk menjalankan fungsi-fungsi
    diatas
    """
    data = collect_dataset()
    panjang_data = data.shape[0]
    data_x = np.c_[np.ones(panjang_data), data[:, :-1]].astype(float)
    data_y = data[:, :-1].astype(float)

    theta = jalankan_linear_regression(data_x, data_y)
    panjang_hasil = theta.shape[1]
    print("resultan fitur vector: ")
    for i in range(0, panjang_hasil):
        print(f"{theta[0, i]:5.f}")


if __name__ == "__main__":
    main()
