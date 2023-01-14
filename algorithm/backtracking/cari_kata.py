# diberikan m x n grid matriks yang berisi kata
# dan diberikan input kata yang diinginkan
# maka akan huruf tersebut dicari, jika huruf dalam inputan
# memenuhi maka ouput bernilai true
# contoh problem
# https://leetcode.com/problems/word-search/


def kata_ada(board: list[list[str]], kata: str) -> bool:
    """
    >>> kata_ada([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
    True
    >>> kata_ada([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")
    False
    """
    # memvalidasi matriks
    board_error_message = (
        "matriks harus berupa string karakter tunggal yang tidak kosong"
    )
    if not isinstance(board, list) or len(board) == 0:
        raise ValueError(board_error_message)

    for row in board:
        if not isinstance(row, list) or len(row) == 0:
            raise ValueError(board_error_message)

        for item in row:
            if not isinstance(item, str) or len(item) != 1:
                raise ValueError(board_error_message)

    # memvalidasi kata
    if not isinstance(kata, str) or len(kata) == 0:
        raise ValueError(
            "parameter kata harus berupa string dengan panjang lebih dari 0"
        )

    traverts_directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    len_kata = len(kata)
    len_board = len(board)
    len_board_column = len(board[0])

    def dapatkan_kunci_poin(row: int, kolom: int) -> int:
        """
        >>> len_board=10
        >>> len_board_column=20
        >>> dapatkan_kunci_poin(0, 0)
        200
        """
        return len_board * len_board_column * row + kolom

    def kata_sudah_ada(
        row: int, kolom: int, index_kata: int, poin_kunjungan: set[int]
    ) -> bool:
        if board[row][kolom] != kata[index_kata]:
            return False

        if index_kata == len_kata - 1:
            return True

        for direction in traverts_directions:
            next_i = row + direction[0]
            next_j = kolom + direction[1]
            if not (0 <= next_i < len_board and 0 <= next_j < len_board_column):
                continue

            key = dapatkan_kunci_poin(next_i, next_j)
            if key in poin_kunjungan:
                continue

            poin_kunjungan.add(key)
            if kata_sudah_ada(next_i, next_j, index_kata + 1, poin_kunjungan):
                return True

            poin_kunjungan.remove(key)

        return False

    for i in range(len_board):
        for j in range(len_board_column):
            if kata_sudah_ada(i, j, 0, {dapatkan_kunci_poin(i, j)}):
                return True

    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
