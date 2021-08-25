# Siklus Hamiltonian (sirkuit Hamiltonian)
# adalah siklus grafik melalui grafik yang
# mengunjungi setiap node tepat sekali.
# Menentukan apakah jalur dan
# siklus tersebut ada dalam grafik Adalah
# 'masalah jalur Hamiltonian', yang NP-complete.
# Wikipedia: https://en.wikipedia.org/wiki/Hamiltonian_path

from typing import List


def connect(
    graph: List[List[int]], next_ver: int, current_ind: int, path: List[int]
) -> bool:
    """
    Memeriksa apakah mungkin untuk menambahkan
    berikutnya ke jalur dengan memvalidasi 2 pernyataan
    1. Harus ada jalan antara titik saat ini dan berikutnya
    2. Vertex berikutnya tidak boleh berada di jalur
    Jika kedua validasi berhasil,return True
    >>> graph = [[0, 1, 0, 1, 0],
    ...          [1, 0, 1, 1, 1],
    ...          [0, 1, 0, 0, 1],
    ...          [1, 1, 0, 0, 1],
    ...          [0, 1, 1, 1, 0]]
    >>> path = [0, -1, -1, -1, -1, 0]
    >>> curr_ind = 1
    >>> next_ver = 1
    >>> connect(graph, next_ver, curr_ind, path)
    True

    sama graph tapi coba connect ke node yang sudah ada di jalur
    >>> path = [0, 1, 2, 4, -1, 0]
    >>> curr_ind = 4
    >>> next_ver = 1
    >>> connect(graph, next_ver, curr_ind, path)
    False
    """
    if graph[path[current_ind - 1]][next_ver] == 0:
        return False
    return not any(vertex == next_ver for vertex in path)


def set_hamilton_cycle(graph: List[List[int]], path: List[int], curr_ind: int) -> bool:
    """
    kode base:
    1. cek jika mengecek semua sudut
     Jika simpul yang terakhir dikunjungi
     memiliki jalur ke simpul awal,
     return true salah satu return false
    langkah rekursif:
    1. Iterasi pada setiap simpul
     cek jika simpul berikutnya valid
     untuk transit dari simpul sekarang

    contoh
    Gunakan grafik yang tepat seperti pada fungsi utama,
    dengan nilai yang diinisialisasi
    >>> graph = [[0, 1, 0, 1, 0],
    ...          [1, 0, 1, 1, 1],
    ...          [0, 1, 0, 0, 1],
    ...          [1, 1, 0, 0, 1],
    ...          [0, 1, 1, 1, 0]]
    >>> path = [0, -1, -1, -1, -1, 0]
    >>> curr_ind = 1
    >>> set_hamilton_cycle(graph, path, curr_ind)
    True

    contoh kedua
    Gunakan graf eksak seperti pada kasus sebelumnya,
    tetapi dalam sifat-sifat yang diambil dari
    tengah perhitungan
    >>> graph = [[0, 1, 0, 1, 0],
    ...          [1, 0, 1, 1, 1],
    ...          [0, 1, 0, 0, 1],
    ...          [1, 1, 0, 0, 1],
    ...          [0, 1, 1, 1, 0]]
    >>> path = [0, 1, 2, -1, -1, 0]
    >>> curr_ind = 3
    >>> set_hamilton_cycle(graph, path, curr_ind)
    True
    >>> print(path)
    [0, 1, 2, 4, 3, 0]
    """
    if curr_ind == len(graph):
        return graph[path[curr_ind - 1]][path[0]] == 1

    for next in range(0, len(graph)):
        if connect(graph, next, curr_ind, path):
            # Masukkan simpul saat ini ke jalur sebagai transisi berikutnya
            path[curr_ind] = next

            if set_hamilton_cycle(graph, path, curr_ind + 1):
                return True
            # backtrack
            path[curr_ind] = -1
    return False


def hamilton_cycle(graph: List[List[int]], start_index: int = 0) -> List[int]:
    r"""
    fungsi untuk memanggil subrutin yang disebut set_hamilton_cycle,
    yang akan mengembalikan array simpul yang menunjukkan siklus hamiltonian
    atau daftar kosong yang menunjukkan bahwa siklus hamiltonian tidak ditemukan.

    contoh
    Graf berikut terdiri dari 5 sisi.
    Jika kita perhatikan lebih dekat,
    kita dapat melihat bahwa ada beberapa siklus Hamilton.
    Misalnya satu hasil adalah ketika kami mengulangi seperti:
    (0)->(1)->(2)->(4)->(3)->(0)
    (0)---(1)---(2)
     |   /   \   |
     |  /     \  |
     | /       \ |
     |/         \|
    (3)---------(4)
    >>> graph = [[0, 1, 0, 1, 0],
    ...          [1, 0, 1, 1, 1],
    ...          [0, 1, 0, 0, 1],
    ...          [1, 1, 0, 0, 1],
    ...          [0, 1, 1, 1, 0]]
    >>> hamilton_cycle(graph)
    [0, 1, 2, 4, 3, 0]

    contoh kedua
    sama seperti graph kedua, tetapi starting index dari default ke 3
    (0)---(1)---(2)
     |   /   \   |
     |  /     \  |
     | /       \ |
     |/         \|
    (3)---------(4)
    >>> graph = [[0, 1, 0, 1, 0],
    ...          [1, 0, 1, 1, 1],
    ...          [0, 1, 0, 0, 1],
    ...          [1, 1, 0, 0, 1],
    ...          [0, 1, 1, 1, 0]]
    >>> hamilton_cycle(graph, 3)
    [3, 0, 1, 2, 4, 3]

    contoh kedua
    Mengikuti Grafik persis seperti sebelumnya, tetapi tepi 3-4 dihapus.
    Hasilnya adalah tidak ada lagi Siklus Hamilton.
    (0)---(1)---(2)
     |   /   \   |
     |  /     \  |
     | /       \ |
     |/         \|
    (3)         (4)
    >>> graph = [[0, 1, 0, 1, 0],
    ...          [1, 0, 1, 1, 1],
    ...          [0, 1, 0, 0, 1],
    ...          [1, 1, 0, 0, 0],
    ...          [0, 1, 1, 0, 0]]
    >>> hamilton_cycle(graph,4)
    []
    """
    path = [-1] * (len(graph) + 1)
    path[0] = path[-1] = start_index
    return path if set_hamilton_cycle(graph, path, 1) else []


if __name__ == "__main__":
    import doctest

    doctest.testmod()
