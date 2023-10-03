import random


def bogo_sorting(arr: list[int]) -> list[int]:
    """
    algoritma bogo sorting adalah algoritma yang bekerja dengan
    mengurutkan elemen array secara acak kemudian memeriksa apakah array
    tersebut sudah diurutkan. jika tidak, maka akan mengacak kembali.
    proses tersebut dilanjutkan hingga semua array ter-urut.
    algoritma ini termasuk algoritma sorting yang paling tidak efisien

    >>> bogo_sorting([0, 2, 5, 1, 2])
    [0, 1, 2, 2, 5]
    """

    # membuat fungsi untuk mengecek apakah array
    # sudah disorting
    def sudah_disorting(data):
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                return False
        return True

    # jika array belum disorting maka lakukan
    # pengacakan hingga tersorting
    while not sudah_disorting(arr):
        random.shuffle(arr)
    return arr


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
