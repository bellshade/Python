"""
Pop Sort

Pop Sort merupakan metode pengurutan dengan menggunakan pendekatan Tower of Homa
yaitu mengambil nilai dari paling luar sebuah array kemudian disusun kembali
dalam array baru.
"""


def pop_sort(arr):
    # Inisialisasi data
    arrA = arr
    arrB = []
    arrC = []
    print('Data sebelum disort:', arrA, end="\n\n")

    # Kita loop hingga data di $a kosong
    while len(arrA) > 0:
        # Keluarkan nilai paling atas dari array $a
        top = arrA.pop()
        print('Data yang diambil:', top)
        print('Array A:', arrA)

        """
        Apabila array B ada isinya dan isi paling atas dari array B
        lebih kecil dari array A, kita pindahkan semua nilai-nilai yang
        cocok dengan kondisi tersebut ke array C

        Pada bagian statement kedua, anda dapat mengganti "<" menjadi ">"
        sesuai keinginan anda.

        Catatan:
        Kita harus menghitung isi array terlebih dahulu sebelum mengambil
        data array lebih utama agar menghindari error "Undefined index"
        """
        while len(arrB) > 0 and top > arrB[len(arrB) - 1]:
            arrC.append(arrB.pop())

        # Setelah aman, kita masukkan data dari $a ke $b
        arrB.append(top)

        print('Array B:', arrB)
        print('Array C:', arrC)

        # Apabila isi $c ada, kita balikkan lagi ke $b secara berurutan.
        while len(arrC) > 0:
            arrB.append(arrC.pop())

        print('Hasil sementara:', arrB, end="\n\n")

    print('Data setelah disort:', arrB)


if __name__ == "__main__":
    pop_sort([83, 10, 54, 92, 62, 47, 15, 72])
