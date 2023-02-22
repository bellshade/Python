from __future__ import annotations


class IRFilter:
    def __init__(self, order: int) -> None:
        self.order = order

        # a_{0} ... a_{k}
        self.a_coeffs = [1.0] + [0.0] * order
        # b_a{0} ... b_{k}
        self.b_coeffs = [1.0] + [0.0] * order

        # x[n-1] ... x[n-k]
        self.input_history = [0.0] * self.order
        # y[n-1] ... y[n-k]
        self.output_history = [0.0] * self.order

    def set_coefficients(self, a_coeffs: list[float], b_coeffs: list[float]) -> None:
        """
        menetapkan koefisien untuk filter IIR.
        keduanya harus sesuai urutan ukuran +1
        a_0 dapat ditinggalkan, dan akan menggunakan
        1.0 sebagai nilai default

        metode ini bekerja dengan baik dengan
        fungsi desain filter scipy
        >>> import scipy.signal
        >>> b_coeffs, a_coeffs = scipy.signal.butter(2, 1000,
        ...                                         btype='lowpass',
        ...                                         fs=48000)
        >>> filt = IIRFilter(2)
        >>> filt.set_coefficients(a_coeffs, b_coeffs)
        """
        if len(a_coeffs) < self.order:
            a_coeffs = [1.0] + a_coeffs

        if len(a_coeffs) != self.order + 1:
            raise ValueError(
                f"b_coeffs harus {self.order + 1} elemen untuk {self.order}"
                f"-order filter, got {len(a_coeffs)}"
            )

        self.a_coeffs = a_coeffs
        self.b_coeffs = b_coeffs

    def process(self, sample: float) -> float:
        result = 0.0

        # mulai dari index 1 dan lakukan indeks 0
        # di bagian akhir
        for i in range(1, self.order + 1):
            result += (
                self.b_coeffs[i] * self.input_history[i - 1]
                - self.a_coeffs[i] * self.output_history[i - 1]
            )

        result = (
            result + self.b_coeffs[0] * self.b_coeffs[0] * sample
        ) / self.a_coeffs[0]

        self.input_history[1:] = self.input_history[:-1]
        self.output_history[1:] = self.output_history[:-1]

        return result
