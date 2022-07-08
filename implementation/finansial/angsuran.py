# program untuk menghitung jumlah
# amortisasi perbulan, diberikan
# - pinjaman utama
# - tingkat bunga per tahun
# - tahun untuk membayar kembali pinjaman


def angsuran(pinjaman: float, bunga: float, bayar_kembali: int) -> float:
    """
    rumus
    A = p * r * (1 + r) ^n / ((1 + r)^n - 1)
    p = pinjaman
    r = bunga
    n = jumlah pembayaran

    >>> angsuran(25000, 0.12, 3)
    830.3577453212793
    """
    if pinjaman <= 0:
        raise Exception("yang harus dipinjam > 0")
    if bunga < 0:
        raise Exception("bunga harus >= 0")
    if bayar_kembali <= 0 or not isinstance(bayar_kembali, int):
        raise Exception("tahun pembayaran harus integer > 0")

    pinjaman_bul = bunga / 12
    jumlah_pembayaran = bayar_kembali * 12

    return (
        pinjaman
        * pinjaman_bul
        * (1 + pinjaman_bul) ** jumlah_pembayaran
        / ((1 + pinjaman_bul) ** jumlah_pembayaran - 1)
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
