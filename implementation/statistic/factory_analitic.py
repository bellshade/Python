import numpy as np
from sklearn.utils.extmath import randomized_svd


class StandardScaler:
    def __init__(self):
        self.mean_ = None

    def fit_transform(self, data, axis=0):
        self.mean_ = np.mean(data, axis=axis)
        std_data = np.std(data, axis=axis)
        if axis == 1:
            result = (data - self.mean_[:, np.newaxis]) / std_data[:, np.newaxis]
        else:
            result = (data - self.mean_) / std_data
        return result


class Factor_Analisis:
    def __init__(self, n_factors):
        """
        factory analisis adalah salah satu
        Params:
            n_factors :n_factor merupakan fitur dalam
            factor_loading:factor loading merupakan metode
                           untuk melihat variasi data yang
                           kita gunakan observasikan
            explained_variance:instance ini merupakan untuk mengukur
                               secara model matematis yang memperhitungkan
                               variasi dari kumpulan data yang diberikan
            factor_score:instance ini merupakan nilai numeric dengan menghasilkan
                         person's releative di atas latent factor
        """
        self.n_factors = n_factors
        self.factor_loadings = None
        self.explained_variance = None
        self.factor_score = None

    def fit(self, x: np.array):
        X = np.asarray(x)
        # transformasi data dulu
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X, axis=1)

        # Menghitung matriks kovarians
        covariance_matrix = np.cov(X_scaled, rowvar=False)

        # Menghitung eigenvalues dan eigenvectors dari matriks kovarians
        if X_scaled.shape[0] < X_scaled.shape[1]:
            # kodinfi ini apabila jumlah sample jumlah dari jumlah fitur
            U, S, V = randomized_svd(covariance_matrix, n_components=self.n_factors)
            eigenvalues = S**2
            eigenvectors = V.T
        else:
            # Menggunakan eigendecomposition biasa jika jumlah sampel lebih besar atau sama dengan jumlah fitur
            eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

        idx = np.argsort(eigenvalues)[::-1]
        # Mengurutkan eigenvalues dan eigenvectors dalam urutan menurun
        eigenvalues = eigenvalues[idx]
        eigenvectors = eigenvectors[:, idx]

        # Memilih n faktor teratas
        self.factor_loadings = eigenvectors[:, : self.n_factors]

        # Menghitung variance yang dijelaskan oleh setiap faktor
        self.explained_variance = eigenvalues[: self.n_factors] / np.sum(eigenvalues)

        return self

    def fit_transform(self, X: np.array):
        self.fit(X)
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X, axis=1)
        self.factor_score = np.dot(X_scaled, self.factor_loadings)
        return self.factor_score


if __name__ == "__main__":
    from sklearn.datasets import load_digits

    digits = load_digits()
    X = digits.data
    fa = Factor_Analisis(n_factors=2)
    X_transformed = fa.fit_transform(X)
    print("bikin sendiri", X_transformed)
