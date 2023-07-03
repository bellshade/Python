import numpy as np

# refence:
# https://stats.stackexchange.com/questions/\
# 502376/\
# what-is-gradient-of-the-objective-function-of-lasso-regression


def costFunction(
    x_data: np.ndarray,
    y_data: np.ndarray,
    alpha: float,
    theta: np.ndarray,
    panjang_data: int,
) -> float:
    """
    Program ini merupakan perhitungan untuk mengetahui performa
    pemodelan data.cost function ini merupakan turunan dari rumus
    rumusan machine learning khususnya
    Args:
        x_data (np.ndarray): parameter ini merupakan data inputan
                             yang bersifat independent
        y_data (np.ndarray): paramater ini adalah data dependentnya
                             merupakan nilai dari nilai aktual
        alpha (float): merupakan bentuk dari batasan dari persamaan
                       rigde regession
        weigth (np.ndarray): ini merupakan titik berat atau bisa di
                             bilang theta yang mengandung interpreted
        panjang_data (int): merupakan panjang dari baris data (dimensi 2)

    Returns:
        float: hasil dari algoritma cost pada lasso
    """
    prod = np.dot(theta, x_data)
    prod = prod - y_data
    sum_element = np.sum(prod**2) + (alpha * np.sum(np.sign(prod.T)))
    error = (sum_element) / (2 * panjang_data)
    return error


def gradient_descent_step(
    X_data: np.array, y_data: np.array, alpha: float, theta: np.array, panjang_data: int
) -> float:
    prod = np.dot(theta, X_data)
    prod = prod - y_data
    sum_grad = np.dot(prod, X_data.T) + alpha * np.sign(prod.T)
    theta = theta - (alpha / panjang_data) * sum_grad
    return theta


class Lasso:
    def __init__(
        self,
        alpha: float = 1.0,
        fit_intercept: bool = True,
        iterable: int = 1000,
        learning_path: float = 0.0001,
    ) -> None:
        """_summary_
        lasso regession merupakan regulasi alternatif
        pemodelan linear regession yang bertujuan agar model regessi
        tidak overfitting yang mengakibatkan model regessi tersebut
        jelek dan tidak bisa digunakan dalam case.
        Args:
            aplha (float, optional): alpha ini merupakan parameter penalti
                                     untuk mengontrol koefiesien regesi.
                                     Defaults to 1.0.
            fit_intercept (bool, optional): parameter ini untuk menambahkan dummy
                                            angka satu. Defaults to True.
            iterable (int, optional): parameter banyaknya model tersebut belajar.
                                      (Defaults to 1000.)
            learning_path (float, optional): langkah model belajar yang akan
                                             mempengaruhi akurasi model
                                             tersebut.
                                             (Defaults to .0001.)
        """

        self.intercept = fit_intercept
        self.iterable = iterable
        self.learning_path = learning_path
        self.alpha = alpha
        self.weight = None

    def fit(self, x: np.array, y: np.array) -> object:
        X = np.array(x)
        if self.intercept:
            X = np.c_[np.ones((X.shape[0], 1)), X]
        panjang_data, panjang_fitur = X.shape
        Y = np.array(y)
        self.weight = np.zeros(panjang_fitur)
        for i in range(1, self.iterable):
            self.weight = gradient_descent_step(
                X, Y, self.alpha, self.weight, panjang_data
            )
            error = costFunction(X, Y, self.alpha, self.weight, panjang_data)
            print(f"iter:{i},theta:{self.weight},error:{error}")
        return self.weight

    def transforms(self, x: np.array) -> np.array:
        X = np.array(x)
        if self.intercept:
            X = np.c_[np.ones((X.shape[0], 1)), X]
        self.predictions = X.dot(self.weight)
        return self.predictions


def main():
    X_train = np.array([[1, 2], [3, 4], [5, 6]])
    y_train = np.array([3, 5, 7])

    lasso = Lasso(alpha=0.5)
    lasso.fit(X_train, y_train)

    X_test = np.array([[2, 3], [4, 5]])
    predictions = lasso.transform(X_test)
    print(predictions)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
