# Masalah nqueens
# adalah menempatkan ratu N pada N * N papan catur
# sehingga tidak ada ratu yang bisa menyerang ratu lain
# yang ditempatkan di papan catur itu.
# Ini berarti bahwa satu ratu tidak dapat memiliki ratu lain di horizontal,
# vertikal dan garis diagonal.

from typing import List

solution = []

def safe(board: List[List[int]], row: int, col: int) -> bool:
    """
    Fungsi ini mengembalikan nilai boolean True jika aman untuk menempatkan
    ratu di sana Mempertimbangkan keadaan saat ini.
    Parameter: board(matriks 2D) : papan baris ,
    kolom : koordinat sel pada papan Kembali: Nilai Boolean
    """
    for i in range(len(board)):
        if board[row][i] == 1:
            return False
    
    for i in range(len(board)):
        if board[i][col] == 1:
            return False
    
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True

def solve(board: List[List[int]], row: int) -> bool:
    """
    Ini menciptakan pohon ruang
    dan memanggil fungsi yang aman sampai menerima
    False Boolean dan mengakhiri cabang itu dan mundur
    ke cabang berikutnya kemungkinan cabang solusi.

    """
    
    if row >= len(board):
        """
        Jika nomor baris melebihi N,
        kami memiliki papan dengan kombinasi yang
        baik dan kombinasi itu
        ditambahkan ke daftar solusi dan papan dicetak.
        """
        solution.append(board)
        printboard(board)
        print()
        
        return True
    for i in range(len(board)):
        """
        Untuk setiap baris itu iterasi melalui
        setiap kolom untuk memeriksa apakah layak untuk
        Tempatkan seorang ratu di sana.
        Jika semua kombinasi untuk cabang tertentu berhasil, papan adalah
        reinitialisasi untuk kombinasi berikutnya yang mungkin.
        """
        if safe(board, row, i):
            board[row][i] = 1
            solve(board, row + 1)
            board[row][i] = 0
    
    return False

def printboard(board: List[List[int]]) -> None:
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

if __name__ == "__main__":
    import doctest
    # n = 8
    # board = [[0 for _ in range(n)] for _ in range(n)]
    # solve(board, 0)
    # print(f"total solusi adalah {len(solution)}")
    doctest.testmod()