"""
        Algoritme hutan acak bekerja dengan membuat ansambel pohon keputusan,
        di mana setiap pohon dilatih pada subset acak dari data pelatihan.
        Selama prediksi,
        setiap pohon di hutan secara independen memprediksi label untuk sampel masukan
        yang diberikan,
        dan prediksi akhir ditentukan oleh suara terbanyak.
        Pendekatan ansambel ini membantu meningkatkan akurasi dan ketahanan model
        secara keseluruhan.
"""
import numpy as np


class DecisionTree:
    def __init__(self, max_depth=5, min_samples_leaf=2):
        """
        Kelas DecisionTree mewakili pohon keputusan tunggal di hutan acak.
        Itu diinisialisasi dengan parameter max_depth (kedalaman maksimum pohon)
        dan min_samples_leaf (jumlah minimum sampel yang
        diperlukan untuk membuat simpul daun).
        """
        self.max_depth = max_depth
        self.min_samples_leaf = min_samples_leaf
        self.tree = {}

    def fit(self, X, y):
        """
        Metode fit membangun pohon keputusan secara rekursif dengan memanggil
        fungsi build_tree.
        argumen:
             X(__type__) : Nilai numerik array 2D
            y(__type__) : Array 1D dari int
            kedalaman (_type_):int
        """
        self.tree = self.build_tree(X, y, depth=0)

    def build_tree(self, X, y, depth):
        """
        Fungsi build_tree secara rekursif membagi data berdasarkan fitur dan nilai
        terbaik, dengan mempertimbangkan perolehan informasi
        argumen:
            X(__type__) : Nilai numerik array 2D
            y(__type__) : Array 1D dari int
            kedalaman (_type_):int
        """
        n_samples, n_features = X.shape
        labels = np.unique(y)

        # Base cases
        if (
            depth == self.max_depth
            or n_samples < self.min_samples_leaf
            or len(labels) == 1
        ):
            label_counts = np.bincount(y)
            return {"label": np.argmax(label_counts), "count": len(y)}

        # Randomly select features for splitting
        feature_indices = np.random.choice(
            n_features, int(np.sqrt(n_features)), replace=False
        )

        # Find the best split based on information gain
        best_gain = -1
        best_feature = None
        best_value = None
        best_partitions = None

        for feature in feature_indices:
            values = np.unique(X[:, feature])
            for value in values:
                left_indices = np.where(X[:, feature] <= value)[0]
                right_indices = np.where(X[:, feature] > value)[0]
                gain = self.information_gain(y, left_indices, right_indices)

                if gain > best_gain:
                    best_gain = gain
                    best_feature = feature
                    best_value = value
                    best_partitions = (left_indices, right_indices)

        # Recursively build the left and right subtrees
        left_tree = self.build_tree(
            X[best_partitions[0]], y[best_partitions[0]], depth + 1
        )
        right_tree = self.build_tree(
            X[best_partitions[1]], y[best_partitions[1]], depth + 1
        )

        return {
            "feature": best_feature,
            "value": best_value,
            "left": left_tree,
            "right": right_tree,
        }

    def information_gain(self, y, left_indices, right_indices):
        """
        Fungsi information_gain menghitung perolehan informasi untuk pembagian tertentu.
        Args:
            y (_type_):1D array of int
            left_indices (_type_): int
            right_indices (_type_): int
        """
        parent_entropy = self.calculate_entropy(y)
        left_entropy = self.calculate_entropy(y[left_indices])
        right_entropy = self.calculate_entropy(y[right_indices])

        n_samples = len(y)
        left_weight = len(left_indices) / n_samples
        right_weight = len(right_indices) / n_samples

        gain = parent_entropy - (
            left_weight * left_entropy + right_weight * right_entropy
        )
        return gain

    def calculate_entropy(self, y):
        """
            fungsi count_entropy menghitung entropi dari sekumpulan label.
        argumen:
            y (_type_): larik int 1D.
        """
        class_counts = np.bincount(y)
        probabilities = class_counts / len(y)
        entropy = -np.sum(probabilities * np.log2(probabilities + 1e-10))
        return entropy

    # Metode prediksi memprediksi label untuk sekumpulan sampel input.
    # Dengan memanggil fungsi predict_sample untuk setiap sampel.

    def prediksi(self, X):
        """
        Metode memprediksi label untuk satu set sampel input.
        Dengan memanggil fungsi predict_sample untuk setiap sampel.
        argumen:
            X (_type_): larik 2D dari nilai numerik

        Pengembalian:
            _type_: Larik label 1D (int)
        """
        return np.array([self.predict_sample(x) for x in X])

    def predict_sample(self, x):
        """
            Fungsi predict_sample menelusuri pohon keputusan untuk menentukan prediksi
            label untuk masukan satu sampel.
        argumen:
            x (_type_): larik 2D dari nilai numerik

        Pengembalian:
            _type_: kembalikan label(int)
        """
        node = self.tree
        while "label" not in node:
            if x[node["feature"]] <= node["value"]:
                node = node["left"]
            else:
                node = node["right"]
        return node["label"]


class RandomForest:
    def __init__(self, num_trees=10, max_depth=5, min_samples_leaf=2):
        """
        Kelas RandomForest mewakili ansambel hutan acak.
        Args:
            num_trees (int, optional):jumlah pohon di hutan Defaults to 10.
            max_depth (int, optional):kedalaman maksimum setiap pohon  Defaults to 5.
            min_samples_leaf (int, optional):jumlah minimum sampel yang diperlukan
            untuk membuat simpul daun.  Defaults to 2.
        """
        self.num_trees = num_trees
        self.max_depth = max_depth
        self.min_samples_leaf = min_samples_leaf
        self.trees = []

    def fit(self, X, y):
        """
        #Metode fit melatih hutan acak dengan membuat pohon keputusan num_trees dan
        # menyesuaikannya pada himpunan bagian acak dari data.
        argumen:
            X(__type__) : Nilai numerik array 2D
            y(__type__) : Array 1D dari int
        """
        for _ in range(self.num_trees):
            tree = DecisionTree(
                max_depth=self.max_depth, min_samples_leaf=self.min_samples_leaf
            )
            indices = np.random.choice(len(X), len(X), replace=True)
            tree.fit(X[indices], y[indices])
            self.trees.append(tree)

    def prediksi(self, X):
        """Metode prediksi membuat prediksi untuk sekumpulan sampel input dengan
        menggabungkan prediksi dari setiap pohon dan mengambil suara mayoritas.
        argumen:
            X (_type_): Nilai numerik larik 2D

        Pengembalian:
            _type_: Larik label 1D (int)
        """
        predictions = np.zeros((len(X), len(self.trees)))
        for i, tree in enumerate(self.trees):
            predictions[:, i] = tree.prediksi(X)
        return np.array([np.bincount(row.astype(int)).argmax() for row in predictions])


def main():
    # Example usage
    X_train = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    y_train = np.array([1, 2, 2, 3])

    # Buat dan latih model hutan acak
    num_trees = 10
    max_depth = 3
    min_samples_leaf = 2
    model = RandomForest(
        num_trees=num_trees, max_depth=max_depth, min_samples_leaf=min_samples_leaf
    )
    model.fit(X_train, y_train)

    #
    X_test = np.array([[2, 3], [8, 7]])

    # Siapkan data uji
    predictions = model.prediksi(X_test)

    # Cetak prediksi
    print("Predictions:", predictions)


if __name__ == "__main__":
    main()
