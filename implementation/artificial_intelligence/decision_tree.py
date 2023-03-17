# decision tree adalah diagaram yang bia membantu dalam memilih
# salah satu dari beberapa banyak tindakan, disebut decision  tree
# karena  model struktur ini menyerupai sebuah pohon
# tahapan membuat model decision tree
# 1. membuat keputusan utama
# 2. menambahkan simpul keputusan
# 3. titik node akhir
import numpy as np


class DecisionTree:
    def __init__(self, depth=3, min_leaf_size=5):
        self.depth = depth
        self.decision_boundary = 0
        self.kiri = None
        self.kanan = None
        self.min_leaf_size = min_leaf_size
        self.prediksi = None

    def mean_squared_error(self, label, prediksi):
        """
        mengukur nilai kualitas pengestimasi
        :param label: array 1 dimensional
        :param prediksi: nilai float

        >>> testing = DecisionTree()
        >>> test_label = np.array([1,2,3,4,5,6,7,8,9,10])
        >>> test_prediksi = float(6)
        """
        if label.ndim != 1:
            print("error: input label harus array 1 dimensi")
        return np.mean((label - prediksi) ** 2)

    def train(self, x, y):
        """
        fungsi train
        bagian ini untuk memeriksa juga apakah input
        sesuai dengan batasan dimensi
        """
        if x.ndim != 1:
            print("error: input data set harus satu dimensi")
            return
        if len(x) != len(y):
            print("error: x dan y mempunyai perbedaaan panjang")
            return
        if y.ndim != 1:
            print("error: label dataset harus 1 dimensi")
            return

        if len(x) < 2 * self.min_leaf_size:
            self.prediksi = np.mean(y)
            return

        if self.depth == 1:
            self.prediksi = np.mean()
            return

        best_split = 0
        min_error = self.mean_squared_error(x, np.mean(y)) * 2

        # looping semua kemungkinan pemisahan untuk pohon keputusan dan
        # kemudian menemukan perpecahan terbik, jika tidak ada pemisahan
        # yang kurang dari 2 * error untuk larik maka kumpulan data
        # dan tidak terbagi dan rata-rata untuk seluruh larik digunakan
        #  sebagai prediktor
        for i in range(len(x)):
            if len(x[:i]) < self.min_leaf_size:
                continue
            elif len(x[i:]) < self.min_leaf_size:
                continue
            else:
                error_kiri = self.mean_squared_error(x[:i], np.mean(y[:i]))
                error_kanan = self.mean_squared_error(x[i:], np.mean(y[i:]))
                error = error_kiri + error_kanan
                if error < min_error:
                    best_split = 1
                    min_error = error

        if best_split != 0:
            kiri_x = x[:best_split]
            kiri_y = y[:best_split]
            kanan_x = x[best_split:]
            kanan_y = x[best_split:]

            self.decision_boundary = x[best_split]
            self.kiri = DecisionTree(
                depth=self.depth - 1, min_leaf_size=self.min_leaf_size
            )
            self.kanan = DecisionTree(
                depth=self.depth - 1, min_leaf_size=self.min_leaf_size
            )
            self.kiri.train(kiri_x, kiri_y)
            self.kanan.train(kanan_x, kanan_y)
        else:
            self.prediksi = np.mean(y)

        return

    def prediksi(self, x):
        if self.prediksi is not None:
            return self.prediksi
        elif self.kiri or self.kanan is not None:
            if x >= self.decision_boundary:
                return self.kanan.prediksi(x)
            else:
                return self.kiri.prediksi(x)
        else:
            print("error: decision tree tidak train")
            return None


class TestDecisionTree:
    @staticmethod
    def helper_mean_square_error_tes(labels, prediksi):
        hasil_squared_error = float(0)
        for label in labels:
            hasil_squared_error += (label - prediksi) ** 2
        return float(hasil_squared_error / labels.size)


def main():
    """
    kita akan membuat kumpulan data sample dari fungsi sin
    di numpy. kemudian kita train decision tree pada kumpulan
    data dan juga menggunakan decision tree untuk memprediksi
    label daari 10 nilai tes yang berbeda.
    """
    x = np.arange(-1.0, 1.0, 0.005)
    y = np.sin(x)

    tree = DecisionTree(depth=10, min_leaf_size=10)
    tree.train(x, y)

    test_kasus = (np.random.rand(10) * 2) - 1
    prediksi = np.array([tree.prediksi(x) for x in test_kasus])
    error_avg = np.mean((prediksi - test_kasus) ** 2)

    print(f"test value {str(test_kasus)}")
    print(f"prediksi {str(prediksi)}")
    print(f"meaan error: {str(error_avg)}")


if __name__ == "__main__":
    main()
