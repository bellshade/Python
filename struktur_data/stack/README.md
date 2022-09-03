# Stack

Stack atau tumpukan adalah struktur data linier yang menyimpan item dengan cara _Last in/first out_ (``LIFO`` ) atau _fist in/last out_. Di stack, elemen baru ditambahkn di satu ujung elemen dihapus dari ujung itu saja. Operasi penyisipan dan penghapusan sering disebut push dan pop.

## Implementasi

Ada berbagai cara dimana stack dapat diimplementasikan dengan Python.

### Implementasi menggunakan list

Daftar struktur data bawaan python dapat digunakan sebagai tumpukan. Alih alih ``push()``, ``append()`` digunakan untuk menambahkan elemen ke bagian atas tumpukan sementara ``pop()`` menghapus elemen dalam urutan ``LIFO``. Sayangnya list ini memiliki kukurangan, masalah terbesarnya dalah ia dapat mengalami masalah kecepatan seiring dengan pertumbuhannya. Item dalam list disimpan bersebelahan dengan memori, jika tumpukan tumbuh lebih besar dari blok memori yang saat ini menampungnya, maka python perlu melakukan beberapa alokasi memori. Ini dapat menyebabkan beberapa panggilan ``append()`` memakan waktu lebih lama daripada yang lain.

```py
stack = []

# menggunakan fungsi append untuk push
# ke dalam stack
stack.append("a")
stack.append("b")
stack.append("c")
stack.append("d")

# menggunakan fungsi pop()
print("element yang pop dari stack")
print(stack.pop())
print(stack.pop())

# melihat stack yang sudah di pop
print(stack)
```

