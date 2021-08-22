# Contributing

**contributor**

Salam, terima kasih anda telah ikut berkontribusi dalam implementasi algortima, struktur data atau perbaikan error.
Semua orang boleh ikut berkontribusi walaupun kecil dengan persyaratan sebagai berikut:

- hasil kerja adalah buatan sendiri dan tidak melanggar hak cipta orang lain
  - jika ditemukan kesamaan maka tidak akan dilakukan `merged`.
- hasil kerja yang diserahkan akan berlisensi [MIT](LICENSE) ketika *pull request* (PR) kamu sudah di merged
- hasil kerja wajib mengikuti standar dan style koding kami

**apa itu algoritma?**

Algoritma adalah satu atau lebih fungsi (atau kelas) yang:

- memiliki satu atau lebih *input*
- melakukan beberapa kalkulasi internal atau manipulasi data
- mengembalikan satu atau lebih nilai hasil
- memiliki kekurangan minimal (contoh : `print()`,`plot()`,`read()`,`write()`)

Algoritma harus dikemas sedemikian rupa sehingga memudahkan pembaca untuk memasukkannya ke dalam program yang lebih besar.

Algoritma harus memiliki:

- nama kelas & fungsi yang intuitif dan dapat menjelaskan tujuannya bagi pembaca
- implementasi tata nama variabel sesuai PEP8 dan intuitif untuk memudahkan pemahaman
- fleksibilitas untuk mengambil nilai input yang berbeda
- petunjuk tipe data untuk parameter input dan nilai pengembaliannya
- tindakan pengecualian (ValueError, dll.) pada nilai input yang salah
- docstrings yang berisi penjelasan dan/atau URL ke materi sumber
- doctests yang berfungsi untuk menguji nilai input yang valid
- hasil perhitungan dalam bentuk `return` alih-alih mencetak atau memplotnya

# docstrings

**penggunaan docstrings**

penggunaan doctstring bertujuan untuk memudahkan pembaca membaca dan mengimplementasikan algoritma.

**docstring yang baik**

```py
def adding(num1, num2):
    """
    menambahkan kedua bilangan
    num1 dan num2 dan dikembalikan hasilnya
    num1 = integer
    num2 = integer
    mengembalikan hasil yang berupa integer
    """
    return num1 + num2
```

**docstring yang buruk**

```py
def adding(num1, num2):
    """
    num1 + num2
    """
    return num1 + num2
```

**saran penggunaan docstring yang baik**
```py
def adding(num1, num2):
  """
  menambahkan kedua bilangan
  num1 dan num2 dan dikembalikan hasilnya
  num1 = integer
  num2 = integer
  mengembalikan hasil yang berupa integer
  >>> adding(2, 3)
  5
  >>> adding(4, 2)
  6
  """
  return num1 + num2
```

## lint test
**instalasi**

kami menggunakan flake8 untuk lint testing agar penulisan code lebih baik.
installasi flake8
```bash
pip install flake8
```

**testing**

untuk lint testing,kami menyarankan kepada kamu untuk test lokal dengan flake8 dengan cara
```bash
flake8 perubahan_kamu.py --ignore=E203,W503 --max-complexity=25 --max-line-length=88
```
```bash
flake8 . --ignore=E203,W503 --max-complexity=25 --max-line-length=88
```

**saran**

[*list comprehension* dan *generator*](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) lebih disarankan daripada penggunaan `lambda`, `map`, `filter`, tetapi yang penting adalah menunjukkan kemampuan Python dalam kode yang mudah dibaca dan dipelihara.

# Pull Request

**Pull request yang baik**

- lakukan fork pada repository kami
- setelah melakukan fork anda dibebaskan untuk mengubah atau menambah algoritma.
  - untuk pull request merubah diusahakan kamu menerapkan algoritma yang lebih baik dan lebih mudah
- setelah merubah merubah, atau menambahkan algoritma, usahakan kamu membuat dengan branch kamu
  ```bash
  git checkout -b <branch_name>
  git add .
  git commit -m "add: menambahkan algoritma terbaru"
  ```
- lakukan push ke branch kamu dan kemudian open pull request

**saran pesan commit**

- `add` untuk menambah algoritma atau tambahan lainnya
- `fix` untuk mengubah algoritma yang sudah ada atau memperbaiki
- `docs` untuk mengubah atau membuat dokumentasi
- `style` untuk mengubah atau memperbaiki style kode
  untuk contohnya bisa dilihat pada contoh commit yang diatas.

pull request akan di `merged` jika:

- mengikuti standar dan arahan dari `CONTRIBUTING.md`
- lulus test dan cek dari beberapa test yang sudah kami siapkan.

**tambahan**:

- jika ada kendala atau masalah dalam pull request, kamu bisa laporkan masalahnya dalam [issue](https://github.com/bellshade/PythonAlgorithm/issues)
- jika ada tes yang tidak lewat atau gagal, kami akan mengecek kembali perubahan anda.

untuk pull request kami sarankan untuk menjelaskan secara detail yang kamu ubah atau tambahkan, dan bersikap sopan,
serta selalu berterima kasih, itu salah satu bentuk tata krama yang baik terhadap sesama contributor dan programmer lainnya.
