# Pewarnaan Grafik juga disebut "masalah pewarnaan m"
# terdiri dari pewarnaan yang diberikan grafik dengan warna paling banyak m
# sedemikian rupa sehingga tidak ada simpul yang berdekatan yang diberi warna yang sama
# Wikipedia: https://en.wikipedia.org/wiki/Graph_coloring


def coloring(neighbours: list[int], colored_vertices: list[int], color: int) -> bool:
    """
    Untuk setiap pemeriksaan apakah kendala pewarna terpenuhi
    Jika salah satu dari kegagalan, kendala return False
    Jika semua validasi kendala return False

    >>> neighbours = [0, 1, 0, 1, 0]
    >>> colored_vertices = [0, 2, 1, 2, 0]
    >>> color = 1
    >>> coloring(neighbours, colored_vertices, color)
    True
    """
    return not any(
        neighbour == 1 and colored_vertices[i] == color
        for i, neighbour in enumerate(neighbours)
    )


def util_color(
    graph: list[list[int]], max_color: int, colored_vertices: list[int], index: int
) -> bool:
    """
    alur :
    1. Periksa apakah pewarnaan selesai
        1.1 Jika pengembalian lengkap True
        (artinya kita berhasil mewarnai grafik)
    Langkah Rekursif:
    2. Iterasi atas setiap warna:
        Periksa apakah pewarnaan saat ini valid:
            2.1. Warna yang diberikan vertex
            2.2. Lakukan pemeriksaan panggilan rekursif
                jika pewarnaan ini mengarah pada pemecahan masalah
            2.4. jika pewarnaan saat ini mengarah ke pengembalian solusi
            2.5. Uncolor diberikan vertex

    >>> graph = [[0, 1, 0, 0, 0],
    ...          [1, 0, 1, 0, 1],
    ...          [0, 1, 0, 1, 0],
    ...          [0, 1, 1, 0, 0],
    ...          [0, 1, 0, 0, 0]]
    >>> max_colors = 3
    >>> colored_vertices = [0, 1, 0, 0, 0]
    >>> index = 3

    >>> util_color(graph, max_colors, colored_vertices, index)
    True
    >>> max_colors = 2
    >>> util_color(graph, max_colors, colored_vertices, index)
    False
    """
    if index == len(graph):
        return True

    for i in range(max_color):
        if coloring(graph[index], colored_vertices, i):
            colored_vertices[index] = i
            if util_color(graph, max_color, colored_vertices, index + 1):
                return True

            colored_vertices[i] = -1

    return False


def color(graph: list[list[int]], max_color: int) -> list[int]:
    """
    Fungsi pembungkus untuk memanggil subrutin yang disebut util_color
    yang akan mengembalikan True atau False.
    Jika True dikembalikan colored_vertices
    daftar diisi dengan pewarnaan yang benar

    >>> graph = [[0, 1, 0, 0, 0],
    ...          [1, 0, 1, 0, 1],
    ...          [0, 1, 0, 1, 0],
    ...          [0, 1, 1, 0, 0],
    ...          [0, 1, 0, 0, 0]]
    >>> max_colors = 3
    >>> color(graph, max_colors)
    [0, 1, 0, 2, 0]

    >>> max_colors = 2
    >>> color(graph, max_colors)
    []

    >>> graph = [[0, 1, 0, 0, 0],
    ...          [1, 0, 1, 0, 1],
    ...          [0, 1, 0, 1, 0],
    ...          [0, 1, 1, 0, 0],
    ...          [0, 1, 0, 0, 0]]

    >>> max_colors = 3
    >>> color(graph, max_colors)
    [0, 1, 0, 2, 0]
    """
    colored_vertices = [-1] * len(graph)
    if util_color(graph, max_color, colored_vertices, 0):
        return colored_vertices
    return []


if __name__ == "__main__":
    import doctest

    doctest.testmod()
