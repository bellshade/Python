def fibo(n):
    """
    Deret fibonacci merupakan salah satu permasalahan yang diselesaikan
    menggunakan pendekatan rekursi. Pada beberapa literatur,
    deret fibonacci  dimulai dengan 0,1,1,2,... namun ada
    literatur yang menjelaskan bahwa deret ini dimulai dengan 1,1,2,... .
    Fungsi fibo(n) memiliki parameter n yang akan mengembalikan nilai
    fibonacci pada urutan ke-n. Fungsi ini menggunakan deret 1,1,2,...
    """

    # base case
    if n == 1 or n == 2:
        return 1
    # proses rekursi
    else:
        return fibo(n-1) + fibo(n-2)


n = 3
result = fibo(n)
# result menghasilkan 2
print(result)
