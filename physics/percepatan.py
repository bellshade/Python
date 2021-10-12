def kalkulasi_kecepatan_awal(
    kecepatan_akhir: float, perecepatan: float, waktu: float
) -> float:
    """
    Menghitung kecepatan awal dari suatu pergerakan
    dengan percepatan yang berbeda
    >>> kalkulasi_kecepatan_awal(10, 2.4, 5)
    -2.0
    >>> kalkulasi_kecepatan_awal(10, 7.2, 1)
    2.8
    """
    # jika waktu 0 diisi dengan 1 detik

    return kecepatan_akhir - perecepatan * waktu


def kalkulasi_kecepatan_akhir(
    kecepatan_awal: float, percepatan: float, waktu: float
) -> float:
    """
    Menghitung kecepatan akhir dari suatu pergerakan
    dengan percepatan yang berbeda
    >>> kalkulasi_kecepatan_akhir(10, 2.4, 5)
    22.0
    >>> kalkulasi_kecepatan_akhir(10, 7.2, 1)
    17.2
    """
    # jika waktu 0 diisi dengan 1 detik
    return kecepatan_awal + percepatan * waktu


def kalkulasi_percepatan(
    kecepatan_awal: float, kecepatan_akhir: float, waktu: float
) -> float:
    """
    Menghitung percepatan dari suatu pergerakan
    dengan kecepatan awal dan kecepatan akhir yang berbeda
    >>> kalkulasi_percepatan(10, 22, 5)
    2.4
    >>> kalkulasi_percepatan(10, 17.2, 1)
    7.199999999999999
    """
    return (kecepatan_akhir - kecepatan_awal) / waktu


def kalkulasi_waktu(
    kecepatan_akhir: float, kecepatan_awal: float, percepatan: float
) -> float:
    """
    Menghitung waktu
    >>> kalkulasi_waktu(10, 22, 2.4)
    -5.0
    >>> kalkulasi_waktu(9, 0, 7.2)
    1.25
    """
    return (kecepatan_akhir - kecepatan_awal) / percepatan


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # print(kalkulasi_percepatan(10, 22, 5))
