import numpy as np


def Z_score(data: np.array) -> np.array:
    """
     Deskripsi:
     ---

     Z_score atau biasa lebih terkenal dengan Standard scaler
     nama yang sering jumpai pada memakai library
     pada sklearn

    Param
     ---
     :param data: parameter untuk input data bisa dalam bentuk
                 1-D array maupun 2-D array

     Return:
     :result: yaitu hasi dari input tersebut dengan menggunakan
             input ouput z_score
    """
    x = np.array(data)
    if x.ndim == 1:
        mean_x = np.mean(x)
        std_x = np.std(x)
    else:
        mean_x = np.mean(x, axis=1)
        std_x = np.std(x, axis=1)

    return (x - mean_x) / std_x


def min_max_normalization(
    data: np.array, new_min: float = 0.0, new_max: float = 1.0
) -> np.array:
    """
    Deskripsi:
    ---

    Melakukan normalisasi Min-Max pada data adalah
    suatu teknik yang digunakan untuk mengubah rentang nilai data
    menjadi interval yang ditentukan, biasanya dari 0 hingga 1.
    Tujuan dari normalisasi ini adalah agar data memiliki skala
    yang seragam dan dapat dibandingkan secara relatif.

    Parameter:
    ---
    :param data: paramter input data
    :param new_min: paramter memasukan input baru untuk min
    :param new_max: paramter memasukan input baru untuk max

    """
    x = np.array(data)
    if x.ndim == 1:
        min_x = np.min(x)
        max_x = np.max(x)
    else:
        min_x = np.min(x, axis=1)
        max_x = np.max(x, axis=1)

    result = ((data - min_x) / (max_x - min_x)) * (new_max - new_min) + new_min

    return result


def MaxAbsScaler(data: np.array):
    """
    Deskripsi
    ---
    Melakukan MaxAbs scaling pada data.
    StandardScaler rentan terhadap outlier karena
    outlier mempengaruhi rata-rata

    Parameter:
    ---
    :param data: Data yang akan di-scaled.

    Return:
    :result: Hasil scaling MaxAbs pada data.

    """
    x = np.array(data)

    if x.ndim == 1:
        value_max = np.max(np.abs(x))
        result = x / value_max
        return result

    if x.ndim == 2:
        value_max = np.max(np.abs(x), axis=1)
        result = x / value_max[:, np.newaxis]
        return result


def RobustScaler(data: np.array):
    """
    Deskripsi
    ---
    Melakukan Robust Scaling pada data.
    Scaler ini menghapus median dan menskalakan
    data sesuai dengan rentang kuartil

    Parameter:
    ---
    :param data: Data yang akan di-scaled.

    Return:
    :result: Hasil scaling Robust pada data.
    """
    x = np.array(data)
    numerator = x / np.quantile(x, 0.5)
    denumerator = np.quantile(x, 0.75) - np.quantile(x, 0.25)

    result = numerator / denumerator

    return result


def log_scaling(data: np.array):
    """
    Melakukan scaling logaritmik pada data.

    Parameter:
    ---
    :param data: Data yang akan di-scaled.

    Return:
    :result: Hasil scaling logaritmik pada data.

    """
    x = np.array(data)
    formula = np.log(x)
    return formula


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
