"""
Bubble Sort

Bubble Sort merupakan metode pengurutan algotitma dengan cara swaping/penukaran sebuah data
secara terus menerus sampai pada iterasi tertentu tidak ada lagi perubahan/penukaran. 
"""


def bubbshort(arr):
    # Inisialisasi data
    lengthArr = len(arr)
    print("Data sebelum disort:", arr, end="\n\n")

    # melakukan looping sebanyak jumlah data
    no = 0
    for i in range(lengthArr-1, 0,-1):
        
        # pada setiap iterasi akan ada pengecekan nilai element
        # apabila element pada index pertama lebih besar maka akan ditukar pada index setelahnya
        # karena udah ditukar maka akan menjadi index ke 2 nah pada index ke dua juga dicocokan lagi seperti sebelumnya
        # sampai nilai element itu tidak bisa ditukar lagi
        # ini dilakukan secara terus menerus pada setiap iterasi

        # melakukan looping pada setiap element dan membandingkan data terus menukar nilanya
        for j in range(i):

            # pengecekana nilai lebih besar mana
            if(arr[j] > arr[j+1]):
                # swaping nilai pada data
                arr[j], arr[j+1] = arr[j+1], arr[j]
            # print(arr)

        no += 1
        print(f"Iterasi {no}:", arr, end="\n")

    print("Data setelah disort:", arr)


if __name__ == "__main__":
    bubbshort([83, 10, 54, 92, 62, 47, 15, 72])
