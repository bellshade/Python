# ridge regession adalah dimana merupakan tipe
# regessi untuk modifikasi OLS regesi yang bertujuan
# agar membantu untuk menolak overfitting
# overfiting itu adalah pemodelan matematis
# bahwa koresponden yang terlalu dekat dengan nilai
# actual yang bisa menggangu akurasi pemodelan kita

import numpy as np


def costfunction(
    x_data: np.ndarray,
    y_data: np.ndarray,
    alpha: float,
    weigth: np.ndarray,
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
        weigth (np.ndarray): _description_
        panjang_data (int): _description_

    Returns:
        float: _description_
    """
    prod = np.dot(weigth, x_data)
    prod = prod - y_data
    sum_element = np.sum(prod**2) + (alpha * np.sum(weigth.T**2))
    error = (sum_element) / (2 * panjang_data)
    return error


def step_gradient_descent(
    data_x: np.ndarray,
    data_y: np.ndarray,
    alpha: float,
    weight: np.ndarray,
    panjang_data: int,
) -> float:
    """
    gradient descent merupakan rumusan turunan dari cost function
    dan ridge regession yang berguna untuk menghitung performa
    gradient descent biasa digunakan bukan hanya machine learning
    model,tetapi juga neural network juga
    Args:
        data_x (np.ndarray): parameter ini merupakan input data ber-
                             sifat dependent
        data_y (np.ndarray): parameter ini merupakan input data(aktual)
                             bersifat independent
        alpha (float): merupakan bentuk batasan-batasan dari persamaan
                       rigde regession
        weight (np.ndarray): merupakan bobot array tersebut
        panjang_data (int): merupakan panjang dari parameter data independent

    Returns:
        float: hasil kakulasi berupa angka desimal
    """
    prod = np.dot(weight, data_x)
    prod = prod - data_y
    # kita hitung perjumlahan nilai weight dengan alpha
    # yang dikalikan dengan weight transpose
    sum_grad = np.dot(prod, data_x.T) + alpha * weight.T
    weight = weight - (alpha / panjang_data) * sum_grad
    return weight


class Ridge:
    def __init__(
        self,
        alpha: float = 1.0,
        fit_intercept: bool = True,
        iterable=100000,
        learning_path: float = 0.0001550,
    ) -> None:
        """
        merupakan salah satu model machine learning pada supervised learning,
        yang berkembangan dari
        model persamaan multi linear regession
        Args:
            alpha (float, optional): merupakan bentuk batasan persamaan.
                                     Defaults to 1.0.
            fit_intercept (bool, optional): merupakan penambahan bias 1 array pada data
                                            input independent.
                                            Defaults to True.
            iterable (int, optional): merupakan banyaknya permodelan
                                      melakukan pembelajaran.
                                      Defaults to 1000.
            learning_path (float, optional): merupakan langkah diambil dalam
                                             melakukan pembelajaran.
                                             Defaults to 0.00001.
        refence :
        https://towardsdatascience.com \
        /from-linear-regression-to-ridge-regression-\
        the-lasso-and-the-elastic-net-4eaecaf5f7e6

        Example:
        >>> import numpy as np
        >>> n_samples, n_features = 10, 5
        >>> rng = np.random.RandomState(0)
        >>> y = rng.randn(n_samples)
        >>> X = rng.randn(n_samples, n_features)
        >>> clf = Ridge(alpha=1.0)
        >>> clf.fit(X, y)
        """
        self.alpha = alpha
        self.intercept = fit_intercept
        self.iterasi = iterable
        self.learning = learning_path
        self.weight = None

    def fit(self, x: np.ndarray, y: np.ndarray) -> object:
        """
        Parameters:
        ---
        :param X: merupakan data yang bersifat bebas
        :param y: merupakan data input yang bersifat target

        Return:
        ---
        :param self: merupakan object yang disimpan dengan variabel
        """
        X = np.array(x)
        if self.intercept:
            X = np.c_[np.ones((X.shape[0], 1)), X]
        panjang_data, panjang_fitur = X.shape
        Y = np.array(y)
        W = np.zeros(panjang_fitur)
        for i in range(0, self.iterasi):
            W = step_gradient_descent(X, Y, self.learning, W, panjang_data)
            error = costfunction(X, Y, self.learning, W, panjang_data)
            print(f"pada iterasi {i + 1} - error : {error:.5f}")
        self.weight = W
        return self

    def transform(self, x: np.ndarray) -> np.ndarray:
        """
        Parameter:
        ---
        :param x:merupakan data input yang ingin mendapatkan
                ouput dari hasil algoritma
        Returns:
        ---
        :param self.predictions: merupakan hasil dari outputnya
        """
        X = np.array(x)
        if self.intercept:
            X = np.c_[np.ones((X.shape[0], 1)), X]
        self.predictions = X.dot(self.weight)
        return self.predictions

    def error_value(self, x: np.ndarray, y: np.ndarray):
        """
        ini merupakan salah satu metode loss function yang digunakan
        untuk mengtahui
        Args:
            x (np.ndarray): input data besifat bebas(independent)
            y (np.ndarray): input data bersifat pastu (dependent)
        Returns:
            _type_: _description_
        """
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


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
