# ridge regession adalah dimana merupakan tipe
# regessi untuk modifikasi OLS regesi yang bertujuan
# agar membantu untuk menolak overfitting
# overfiting itu adalah pemodelan matematis
# bahwa koresponden yang terlalu dekat dengan nilai
# actual yang bisa menggangu akurasi pemodelan kita
import numpy as np


class Ridge:
    def __init__(self, ridge_parameter: float = 1.0) -> None:
        """
        Parameter:
        ---
        :param rigde_parameter: adalah merupakan alpha
                                yang berfungsi untuk bias
                                di OLS
        """
        self.alpha = ridge_parameter
        self.intercept = None
        self.coef_ = None
        self.theta = None

    def fit(self, x: np.array, y: np.array):
        """
        Parameters:
        ---
        :param X: merupakan data untuk melatih algoritma
        :param y: merupakan data target

        Return:
        ---
        :param self: merupakan estimator
        """
        X = np.array(x)
        X = np.c_[np.ones((X.shape[0], 1)), X]
        Y = np.array(y)
        W = X.T @ X
        identity = np.identity(Y.shape[0])
        bias = self.alpha * identity
        self.theta = np.linalg.inv(W + bias) @ X.T @ Y
        self.coef_ = self.theta[1:]
        self.intercept = self.theta[0]
        return self

    def transform(self, x: np.array):
        """
        Parameter:
        ---
        :param x:merupakan data input yang ingin mendapatkan
                ouput dari hasil algoritma
        Returns:
        ---
        :param self.predictions: merupakan hasil dari outputnya
        """
        thetas = self.theta
        X = np.array(x)
        X_predictor = np.c_[np.ones((X.shape[0], 1)), X]
        self.predictions = X_predictor.dot(thetas)
        return self.predictions

    def error_value(self, x: np.array, y: np.array):
        X = np.array(x)
        y = np.array(y)
        self.fit(X, y)
        error = y - self.transform(X)
        return error

    def score(self, y_actual: np.array, y_predict: np.array) -> float:
        tss = np.sum((y_actual - np.mean(y_actual)) ** 2)
        rss = np.sum((y_actual - y_predict) ** 2)
        r_squared = 1 - rss / tss
        return r_squared


def main():
    import matplotlib.pyplot as plt

    X = np.array([[1, 2], [2, 3], [4, 5]])
    y = np.array([[1], [7], [9]])
    print(X)
    print(y.shape)
    model = Ridge()
    # modeling=Ridge()
    model.fit(X, y)
    y_predict = model.transform(X)
    print(y_predict)
    print(model.score(y, y_predict))
    plt.scatter(X[:, 0], y, color="black")
    plt.plot(X[:, 0], y_predict)
    plt.title("Low-Alpha Ridge on Three Points")
    plt.show()


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    main()
