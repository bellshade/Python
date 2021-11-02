# Masalah n ratu adalah: menempatkan N ratu
# di papan catur N * N sedemikian rupa sehingga tidak ada ratu
# dapat menyerang ratu lain yang ditempatkan di papan catur itu.
# Ini berarti bahwa satu ratu
# tidak dapat memiliki ratu lain pada garis horizontal, vertikal dan diagonal.

# solusi
# Untuk menyelesaikan soal ini kita akan menggunakan matematika sederhana.
# Pertama kita tahu ratu bisa bergerak semua
# cara yang mungkin, kita dapat menyederhanakannya dalam hal ini:
# vertikal, horizontal, diagonal kiri dan
# diagonal kanan.

# kita bisa menganalogikan

# diagonal kiri = \
# diagonal kanan = /

# Pada papan catur gerakan vertikal bisa berupa baris
# dan gerakan horizontal bisa
# kolom.

# Dalam pemrograman kita dapat menggunakan array,
# dan dalam array ini setiap indeks dapat berupa baris dan
# setiap nilai dalam array bisa menjadi kolom. Sebagai contoh:

#     . Q . .
#     . . . Q tidak bisa menyerang satu sama lain.
#     Q . . . Array untuk contoh ini akan terlihat seperti ini: [1, 3, 0, 2]
#     . . Q .
# Kita  memiliki papan catur ini dengan satu ratu di setiap kolom dan setiap ratu


# Jadi jika kita menggunakan array
# dan kita memverifikasi bahwa setiap nilai dalam array berbeda untuk masing-masing
# lain kita tahu bahwa setidaknya ratu
# tidak bisa menyerang satu sama lain secara horizontal dan
# vertikal.


from __future__ import annotations


def depth_first_search(
    possible_board: list[int],
    diagonal_right_collisions: list[int],
    diagonal_left_collisions: list[int],
    boards: list[list[str]],
    n: int,
) -> None:
    """
    >>> boards = []
    >>> depth_first_search([], [], [], boards, 4)
    >>> for board in boards:
    ...     print(board)
    ['. Q . . ', '. . . Q ', 'Q . . . ', '. . Q . ']
    ['. . Q . ', 'Q . . . ', '. . . Q ', '. Q . . ']
    """

    # Dapatkan baris berikutnya
    # di papan saat ini (possible_board) untuk mengisinya dengan ratu
    row = len(possible_board)

    # Jika baris sama dengan ukuran papan itu
    # berarti ada ratu di setiap baris di papan saat ini (kemungkinan papan)

    if row == n:
        boards.append([". " * i + "Q " + ". " * (n - 1 - i) for i in possible_board])
        return

    for col in range(n):
        # 45 derajat = y - x = b atau 45 = row - col = b
        # 145 derajat = y + x = b atau row + col = b
        if (
            col in possible_board
            or row - col in diagonal_right_collisions
            or row + col in diagonal_left_collisions
        ):
            continue

        depth_first_search(
            possible_board + [col],
            diagonal_right_collisions + [row - col],
            diagonal_left_collisions + [row + col],
            boards,
            n,
        )


def n_queen_solution(n: int) -> None:
    boards: list[list[str]] = []
    depth_first_search([], [], [], boards, n)

    for board in boards:
        for column in board:
            print(column)
        print("")

    print(len(boards), "solusi ditemukan !")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    n_queen_solution(4)
