# Waktu proses adalah O(n²).
# Tidak diperlukan ruang baru.

def Bubble_Sort(array, length):
    # array: array angka yang tidak diurutkan
    # length: panjang larik
    for i in range(0, length):
        for j in range(0, length - i - 1):
            # Jika elemen sebelumnya lebih besar dari pertukaran itu.
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
