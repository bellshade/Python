def rata_rata(data: list[int]) -> float:
    _sum=0
    panjang_data=0 #
    for number in (data):
        panjang_data+=1
        _sum+=number
    result=_sum/panjang_data
    return round(result,2)

def variance(data:list[int]):
    '''
    variansi atau dalam bahasa inggris disebut juga disebut variance.
    variansi ini berfungsi untuk menghitung ukuran nilai data agar mengetahui sifat-sifat serta semua titik data
    dalam kumpulan data
    >>> variance([10,20,20])
        33.3333335
    '''
    n=len(data)
    _sum=0
    for value in data:
        hitung=(value-rata_rata(data))**2
        _sum+=hitung
    result=_sum/(n-1)
    return round(result,2)
print(rata_rata([20,10,10]))
if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)