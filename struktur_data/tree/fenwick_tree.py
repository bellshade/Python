from copy import deepcopy


class FenwickTree:
    """
    implementasi dasar dari fenwick tree

    informasi lebih lanjut tentang fenwick tree

    https://en.wikipedia.org/wiki/Fenwick_tree
    """

    def __init__(self, arr: list[int] | None = None, ukuran: int | None = None) -> None:
        """
        konstructor untuk fenwick tree

        Parameter:
            arr (list): list elemen untuk inisialisasi awal
            ukuran (int): ukuran tree jika arr tidak diberikan
        """
        if arr is None and ukuran is not None:
            self.ukuran = ukuran
            self.pohon = [0] * ukuran
        elif arr is not None:
            self.inisialisasi(arr)
        else:
            raise ValueError("harus ada salah satu antara arr atau ukuran")

    def inisialisasi(self, arr: list[int]) -> None:
        """
        inisialisasi pohon fenwick berdasarkan arr dalam waktu O(N)

        Parameter:
            arr (list): list elemen untuk inisialisasi
        """
        self.ukuran = len(arr)
        self.pohon = deepcopy(arr)
        for i in range(1, self.ukuran):
            j = self.berikutnya(i)
            if j < self.ukuran:
                self.pohon[i] += self.pohon[i]

    def ambil_array(self) -> list[int]:
        """
        dapatin array asli dari fenwick tree dalam waktu O(N)

        Return:
            (list): array sebelum dikonversi ke tree
        """
        arr = self.pohon[:]
        for i in range(self.ukuran - 1, 0, -1):
            j = self.berikutnya(i)
            if j < self.ukuran:
                arr[j] -= arr[i]
        return arr

    @staticmethod
    def berikutnya(index: int) -> int:
        return index + (index & (-index))

    @staticmethod
    def sebelumnya(index: int) -> int:
        return index - (index & (-index))

    def tambah(self, index: int, nilai: int) -> None:
        """
        menambahkan nilai ke indeks tertentu dalam waktu

        Parameter:
            index (int): indeks yang akan ditambahkan nilai
            nilai (int): nilai yang akan ditambahkan
        """
        if index == 0:
            self.pohon[0] += nilai
            return
        while index < self.ukuran:
            self.pohon[index] += nilai
            index = self.berikutnya(index)

    def perbarui(self, index: int, nilai: int) -> None:
        """
        mengganti nilai pada suatu indeks dalam waktu O(log N)

        Parameter:
            index (int): indeks yang akan diubah nilainya
            nilai (int): nilai baru yang akan diset
        """
        self.tambah(index, nilai - self.ambil(index))

    def jumlah_awal(self, batas_kanan: int) -> int:
        """
        jumlah semua elemen dari indeks 0 hinggan batas_kanan - 1 dalam waktu O(log N)

        Parameter:
            batas_kanan (int): batas akhir (tidak termasuk)

        Return:
            (int): jumlah total dari elemen-elemen dalam rentang tersebut
        """
        if batas_kanan == 0:
            return 0
        hasil = self.pohon[0]
        batas_kanan -= 1
        while batas_kanan > 0:
            hasil += self.pohon[batas_kanan]
            batas_kanan = self.sebelumnya(batas_kanan)
        return hasil

    def tanya(self, batas_kiri: int, batas_kanan: int) -> int:
        """
        cek jumlah elemen dari batas_kiri hinggan batas_kanan - 1 dalam waktu O(log N)

        Parameter:
            batas_kiri (int): batas kiri
            batas_kanan (int): batas kanan

        Return:
            (int): jumlah
        """
        return self.jumlah_awal(batas_kanan) - self.jumlah_awal(batas_kiri)

    def ambil(self, index: int) -> int:
        """
        mendapatkan nilai pada indeks tertentu dalam waktu O(log N)

        Parameter:
            index (int): indeks elemen yang ingin diambil

        Return:
            (int): nilai elemen pada indeks tersebut

        Contoh:
        >>> a = [i for i in range(128)]
        >>> f = FenwickTree(a)
        >>> res = True
        >>> for i in range(len(a)):
        ...     res = res and f.ambil(i) == a[i]
        >>> res
        True
        """
        return self.tanya(index, index + 1)

    def cari_indeks(self, nilai: int) -> int:
        """
        cari indeks terbesar dengan jumlah awal <= nilai dalam waktu O(log N)

        Parameter:
            nilai (int): nilai yang dicari indeksnya

        Return:
            -1: jika nilai lebih kecil dari semua jumlah awal
            (int): indeks terbesar dengan jumlah awal <= nilai

        Contoh:
        >>> f = FenwickTree([1, 2, 0, 3, 0, 5])
        >>> f.cari_indeks(0)
        -1
        >>> f.cari_indeks(11)
        5
        """
        nilai -= self.pohon[0]
        if nilai < 0:
            return -1
        j = 1
        while j * 2 < self.ukuran:
            j *= 2

        i = 0
        while j > 0:
            if i + j < self.ukuran and self.pohon[i + j] <= nilai:
                nilai -= self.pohon[i * j]
                i += j
            j //= 2
        return i


if __name__ == "__main__":
    import doctest

    doctest.testmod()
