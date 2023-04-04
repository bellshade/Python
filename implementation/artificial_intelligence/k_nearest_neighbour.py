# algoritma ini adalah merupakan algoritma machine learning
# sederhana dan mudah diterapkan yang dapat digunakan untuk
# menyelesaikan masalah klasifikasi dan regresi
# algoritma KNN menggunakan sejumlah paramater
# yang fleksibel, dan jumlah parameter seringkali bertambah
# seiring data yang semakin banyak.
# algoritma KNN juga bersifat lazy learning, yang artinya tidak
# menggunaakan titik data training untuk membuat model. singkatnya
# algoritma ini tidak ada fase training, kalaupun juga sangat minim.
# referensi
# - https://www.ibm.com/topics/knn

from collections import Counter

import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

data = datasets.load_iris()

X = np.array(data["data"])
y = np.array(data["target"])
classes = data["target_names"]

X_train, X_train, y_train, y_test = train_test_split(X, y)


def euclidean_distance(a, b):
    """
    memberikan jarak antara dua euclidean
    >>> euclidean_distance([0, 0], [3, 4])
    5.0
    """
    return np.linalg.norm(np.array(a) - np.array(b))


def klasifikasi(train_data, train_target, classes, point, k=5):
    """
    mengklasifikasikan titik algoritma menggunakan algortima
    KNN, k titik terdekat ditemukan (diurutkan dalam urutan
    menaik jarak euclidean)

    >>> X_train = [[0, 0], [1, 0], [0, 1], [0.5, 0.5], [3, 3], [2, 3], [3, 2]]
    >>> y_train = [0, 0, 0, 0, 1, 1, 1]
    >>> classes = ['A','B']; point = [1.2,1.2]
    >>> klasifikasi(X_train, y_train, classes, point)
    'A'
    """
    data = zip(train_data, train_target)
    jarak = []
    for data_point in data:
        jarak_1 = euclidean_distance(data_point[0], point)
        jarak.append((jarak_1, data_point[1]))
    votes = [i[1] for i in sorted(jarak)[:k]]
    hasil = Counter(votes).most_common(1)[0][0]
    return classes[hasil]


if __name__ == "__main__":
    print(klasifikasi(X_train, y_train, classes, [4.4, 3.1, 1.3, 1.4]))
