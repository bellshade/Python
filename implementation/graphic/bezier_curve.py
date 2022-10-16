# kurva bezier  adalah kurva parametrik yang sering
# digunkan dalam pemodelan permukaan halus dalam
# grafik komputer dan banuak bidang terkait lainnya.
# kurva ini dapat diskalakan tanpa batas.
# digunakan juga dalam mengendalikan animasi.

from __future__ import annotations

from scipy.special import comb  # type: ignore


class BezierCurve:
    def __init__(self, list_of_points: list[tuple[float, float]]):
        """
        list_of_points: titik kontrol pada bidang xy yang akan
        di interpolasi. ini poin mengontrol dari kurva bezier.
        """
        self.list_of_points = list_of_points

        # mementukan fleksibilitas kurva
        # derajat = 1 akan menghasilkan garis lurus
        self.degree = len(list_of_points) - 1

    def basis_function(self, t: float) -> list[float]:
        """
        fungsi basis menentukan bobot setiap titik kendali
        pada waktu t.
        t: nilai waktu antar 0 dan 1 inklusif untuk evaluasi
        basis kurva.
        return: mengembalikan nilai x, y dari fungsi dasar
        pada waktu t.

        >>> curve = BezierCurve([(1, 1), (1, 2)])
        >>> curve.basis_function(0)
        [1.0, 0.0]
        >>> curve.basis_function(1)
        [0.0, 1.0]
        """
        assert 0 <= t <= 1, "waktu t harus antara 0 dan 1."
        output_values: list[float] = []
        for i in range(len(self.list_of_points)):
            # basis fungsi dari setiap 1
            output_values.append(
                comb(self.degree, i) * (1 - t) ** (self.degree - i) * (t**i)
            )

        assert round(sum(output_values), 5) == 1

        return output_values

    def bezier_curve_function(self, t: float) -> tuple[float, float]:
        """
        fungsi untuk menghasilkan nilai kurva bezier pada waktu t.
        t: nilai waktu untuk evaluasi fungsi bezier
        return: mengembalikan kordinaat x, y dari kurva bezier
        pada waktu t.

        titik pertama kurva adalah ketika t = 0
        titik terakhir dalam kurva adalah ketika t = 1

        >>> curve = BezierCurve([(1, 1), (1, 2)])
        >>> curve.bezier_curve_function(0)
        (1.0, 1.0)
        >>> curve.bezier_curve_function(1)
        (1.0, 2.0)
        """

        assert 0 <= t <= 1, "waktu t harus antara 0 dan 1."

        basis_function = self.basis_function(t)
        x = 0.0
        y = 0.0

        for i in range(len(self.list_of_points)):
            x += basis_function[i] * self.list_of_points[i][0]
            y += basis_function[i] * self.list_of_points[i][1]

        return (x, y)

    def plot_curve(self, step_size: float = 0.01):
        """
        plit kurva bezier menggunakan matplotlib
        step_size: mendefinisikan langkah untuk
        mengevaluassi kurva bezier.

        semakin kecil ukurang langkah, semakin halus
        kurva yang dihasilkan.
        """
        from matpltlib import pyplot as plt  # type: ignore

        to_plot_x: list[float] = []
        to_plot_y: list[float] = []

        t = 0.0
        while t <= 1:
            value = self.bezier_curve_function(t)
            to_plot_x.append(value[0])
            to_plot_y.append(value[1])
            t += step_size

        x = [i[0] for i in self.list_of_points]
        y = [i[1] for i in self.list_of_points]

        plt.plot(
            to_plot_x,
            to_plot_y,
            color="blue",
            label="derajat kurva "
            + str(
                self.degree,
            ),
        )
        plt.scatter(x, y, color="red", label="Control Point")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    BezierCurve([(1, 2), (3, 5)]).plot_curve()
    BezierCurve([(0, 0), (5, 5), (5, 0)]).plot_curve()
    BezierCurve([(0, 0), (5, 5), (5, 0), (2.5, -2.5)]).plot_curve()
