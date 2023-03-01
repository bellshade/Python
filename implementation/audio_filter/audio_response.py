from __future__ import annotations

from math import pi
from typing import Protocol

import matplotlib.pyplot as plt
import numpy as np

class TipeFilter(Protocol):
    def proses(self, sample: float):
        """
        kalkulasi y[n]
        
        >>> issubclass(TipeFilter, Protocol)
        True
        """
        return 0.0

def batasan(hasil_fft: np.ndarray, samplerate: int) -> tuple[int | float, int | float ]:
    """
    >>> import numpy
    >>> array = numpy.linspace(-20.0, 20.0, 1000)
    >>> batasan(array, 1000)
    (-20, 20)
    """
    terendah = min([-20, np.min(hasil_fft[1:samplerate // 2 - 1])])
    tertinggi = max([20, np.max(hasil_fft[1:samplerate // 2 - 1])])
    return terendah, tertinggi

def tampilan_frekuensi(tipe_filter: TipeFilter, samplerate: int) -> None:
    ukuran = 512
    inputs =[1] + [0] * (ukuran - 1)
    outputs = [tipe_filter.proses(item) for item in inputs]

    filler = [0] * (samplerate - ukuran)
    outputs  += filler
    fft_keluar = np.abs(np.fft.fft(outputs))
    fft_db = 20 *np.log10(fft_keluar)

    plt.xlim(24, samplerate / 2 - 1)
    plt.xlabel("frekuensi (Hz)")
    plt.xscale("log")

    bound = batasan(fft_db, samplerate)
    plt.ylim(max([-80, bound[0]]), min([80, bound[1]]))
    plt.ylabel("desibel (dB)")

    plt.plot(fft_db)
    plt.show()

def tampilan_fase_respon(tipe_filter: TipeFilter, samplerate:int) -> None:
    ukuran = 512
    inputs = [1] + [0] * (ukuran - 1)
    outputs = [tipe_filter.proses(item) for item in inputs]

    filter = [0] * (samplerate - ukuran)
    outputs += filter
    output_fft = np.angle(np.fft.fft(outputs))

    plt.xlim(24, samplerate / 2 - 1)
    plt.xlabel("frekuensi (Hz)")
    plt.xscale("log")
    
    plt.ylim(-2 * pi, 2 * pi)
    plt.ylabel("radian")
    plt.plot(np.unwrap(output_fft, -2 * pi))
    plt.show()

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    
