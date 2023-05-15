# implementasi dari fungsi skoring
# untuk mengkalkulasikan perbedaan antara
# value yang terprediksi dengan value yang aktual
# terdapat juga mode dari:
# - MAE (mean absolute error)
#   menghitung perbedaan mutlak rata-rata antara
#   dua vektor numerik
# - RMSE (root mean squared error)
#   untuk mengukur seberapa jauh nilai observasi
#   dalam analisis regresi
# - MSE (mean squared error)
#   fungsi untuk mengukur square error
# - RMSLE (root mean square logarithmic error)
#   menambahkan satu ke aktual sebelum mengambil
#   nilai logaritma natural untuk menghindari
#   catching log natural nilai nol
# - MAPE (Mean Absoult Prediction Error)
#   fungsi ini untuk mengukur pesentasi akurasi method forecasting

import numpy as np


def fungsi_mae(prediksi: list, nilai_aktual: list) -> float:
    """
    >>> nilai_aktual = [1,2,3]
    >>> prediksi = [1, 4, 3]
    >>> np.around(fungsi_mae(prediksi, nilai_aktual), decimals=2)
    0.67
    """
    prediksi = np.array(prediksi)
    nilai_aktual = np.array(nilai_aktual)
    perbedaan = abs(prediksi - nilai_aktual)
    hasil = perbedaan.mean()
    return hasil


def fungsi_mse(prediksi: list, nilai_aktual: list) -> float:
    """
    >>> nilai_aktual = [1, 1, 1]
    >>> prediksi = [1, 1, 1]
    >>> fungsi_mse(prediksi, nilai_aktual)
    0.0
    """
    prediksi = np.array(prediksi)
    nilai_aktual = np.array(nilai_aktual)
    perbedaan = prediksi - nilai_aktual
    root_diff = np.square(perbedaan)
    hasil = root_diff.mean()
    return hasil


def fungsi_rmse(prediksi: list, nilai_aktual: list) -> float:
    """
    >>> nilai_aktual = [1, 2, 3]
    >>> prediksi = [1, 4, 3]
    >>> np.around(fungsi_rmse(prediksi, nilai_aktual), decimals=2)
    1.15
    """
    prediksi = np.array(prediksi)
    nilai_aktual = np.array(nilai_aktual)
    perbedaan = prediksi - nilai_aktual
    root_diff = np.square(perbedaan)
    mean_square_diff = root_diff.mean()
    hasil = np.sqrt(mean_square_diff)
    return hasil


def fungsi_rmsle(prediksi: list, nilai_aktual: list) -> float:
    """
    >>> nilai_aktual = [10, 10, 30]
    >>> prediksi = [10, 2, 30]
    >>> np.around(fungsi_rmsle(prediksi, nilai_aktual), decimals = 2)
    0.75
    """
    prediksi = np.array(prediksi)
    nilai_aktual = np.array(nilai_aktual)
    prediksi_log = np.log(prediksi + 1)
    nilai_log_aktual = np.log(nilai_aktual + 1)
    perbedaan = prediksi_log - nilai_log_aktual
    square_diff = np.square(perbedaan)
    mean_square_diff = square_diff.mean()
    hasil = np.sqrt(mean_square_diff)
    return hasil


def fungsi_mbd(prediksi: list, nilai_aktual: list) -> float:
    """
    Deskripsi:
    ---
    mean bias deviation adalah merupakan
    pengukuran untuk presentasi kualitas
    karateristik model

    Parameters:
    ---
    :param prekdisi: parameter berisi nilai prediksi
    :param aktual: parameter berisi nilai prediksi
    """
    prediksi = np.array(prediksi)
    nilai_aktual = np.array(nilai_aktual)
    perbedaan = prediksi - nilai_aktual
    numerator = np.sum(perbedaan) / len(prediksi)
    denumerator = np.sum(nilai_aktual) / len(prediksi)
    hasil = float(numerator) / denumerator * 100
    return hasil


def fungsi_mape(prediksi: list, nilai_aktual: list) -> float:
    """
    Deskripsi:
    ---
    Mean Absolute Percentage Error (MAPE) merupakan
    pengukuran akurasi nilai prediksi untuk
    metode forcesting
    Paramaters:
    ---
    :param prediksi: parameter berisi nilai prediksi
    :param aktual: paramter berisi nilai aktual

    Example:
    ---
    >>> nilai_aktual=[12,10,11]
    >>> nilai_prediksi=[12,9,12]
    >>> fungsi_mape(nilai_prediksi,nilai_aktual)
    6.363636363636364
    Refensi:
    ---
    Time Series Forecasting in Python hal.48
    https://en.wikipedia.org/wiki/Mean_absolute_percentage_error
    """
    nilai_aktual = np.array(nilai_aktual)
    nilai_prediksi = np.array(prediksi)
    # numertor pada MAPE dimana absolute
    # selesih nilai aktual sama nilai prediksi
    # dibagi dengan nilai prediksi tersebut
    numerator = np.abs((nilai_aktual - nilai_prediksi) / nilai_aktual)
    hasil = np.mean(numerator) * 100
    return hasil


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
