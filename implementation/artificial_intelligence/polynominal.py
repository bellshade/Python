import numpy as np


class PolynomialRegression:

    def __init__(self, degree, learning_rate: float = 0.00001, iterations: int = 10000):
        """
        # PolynomialRegression
        ----------

        Polynominal Regression adalah merupakan model melatih
        hubungan parameter non-linear dengan paramter β dengan
        membentuk garis curved seperti persamaan polinominal
        dibandingkan dengan simple linear regession,simple
        linear regession hanya bekerja ketika hubungan para-
        meter datanya bersifat linear

        # Paramters:
        ------------
        :param degree: parameter derajat ini merupakan
                       regestor model data train
        :param learning_rate: parameter ini merupakan update
                              estimasi hasil pembelajaran setiap
                              berapa kali di belajar
        :param iterations: parameter ini merupakan merupakan berapa
                          ke berapa kali data itu belajar
        """
        self.degree = degree
        self.learning_rate = learning_rate
        self.iterations = iterations

    def transform(self, X):
        X_transform = np.ones((self.m, 1))
        for j in range(self.degree + 1):
            if j != 0:
                x_pow = np.power(X, j)
                X_transform = np.append(X_transform, x_pow.reshape(-1, 1), axis=1)
        return X_transform

    def normalize(self, X):
        X[:, 1:] = (X[:, 1:] - np.mean(X[:, 1:], axis=0)) / np.std(X[:, 1:], axis=0)
        return X

    def fit(self, X: np.array, Y: np.array):
        """
        # Parameters:
        :param X: merupakan data input bersifat independent
        :param y: merupakan data real output bersifat
                  dependent
        # Returns:
        :param return: berupa nama Class
        """
        self.X = X
        self.Y = Y
        self.m, self.n = self.X.shape
        self.W = np.zeros(self.degree + 1)
        X_transform = self.transform(self.X)
        X_normalize = self.normalize(X_transform)
        for _ in range(self.iterations):
            h = self.predict(self.X)
            error = h - self.Y
            self.W = self.W - self.learning_rate * (1 / self.m) * np.dot(X_normalize.T,
                                                                         error)
        return self

    def fit_tranform(self, X):
        """
        menjalankan fungsi dari Polynomial regression
        >>  X = np.array([[1], [2], [3], [4], [5], [6], [7]])
        >>  Y = np.array([45000, 50000, 60000, 80000, 110000, 150000, 200000])
        >>  model = PolynomialRegression(degree=2, learning_rate=0.01, iterations=500)
        """
        X_transform = self.transform(X)
        return np.dot(X_transform, self.W)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
