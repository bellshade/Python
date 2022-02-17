# Stack

Stack atau tumpukan adalah struktur data linier yang menyimpan item dengan cara _Last in/first out_ (``LIFO`` ) atau _fist in/last out_. di stack, elemen baru ditambahkn di satu ujung elemen dihapus dari ujung itu saja. operasi penyisipan dan penghapusan sering disebut push dan pop

## implementasi

ada berbagai cara di mana stack dapat diimplementasikan dengan python.

## implementasi menggunakan list

daftar struktur data bawaan python dapat digunakan sebagai tumpukan. alih alih ``push()``, ``append()`` digunakan untuk menambahkan elemen ke bagian atas tumpukan sementara ``pop()`` menghapus elemen dalam urutan ``LIFO``. sayangnya list ini memiliki kukurangan, masalah terbesarnya dalah ia dapat mengalami masalah kecepatan seiring dengan pertumbuhannya. item dalam list disimpan bersebelahan dengan memori, jika tumpukan tumbuh lebih besar dari blok memori yang saat ini menampungnya, maka python perlu melakukan beberapa alokasi memori. ini dapat menyebabkan beberapa panggilan ``append()`` memakan wwaktu lebih lama daripada yang lain.

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

