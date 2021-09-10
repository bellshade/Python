# Contributing
![contributor](https://img.shields.io/github/contributors/bellshade/PythonAlgorithm?label=kontributor&style=for-the-badge)

**contributor**

Kami sangat senang anda telah ikut berkontribusi dalam implementasi algortima, struktur data atau memperbaiki error.
semua boleh ikut berkontribusi walaupun hal kecil dengan pengecualian sebagai berikut:

- hasil pekerjaan kamu adalah buatan kamu sendiri dan tidak ada hak cipta dari orang lain
  - jika kami menemukan kesamaan maka kami tidak `merged`.
- hasil kerja kamu akan berlisensi [MIT](LICENSE) ketika permintaan pull kamu sudah di merged
- hasil kerja kamu wajib mengikuti standar dan style koding dari kami
- hanya menerima file yang berekstensi ``*.py`` selain itu dibuat pengecualian dengan menjelaskan secara detail

**apa itu algoritma?**

Algoritma adalah satu atau lebih fungsi (atau kelas) yang:

- memiliki satu atau lebih input
- melakukan beberapa internal kalkulasi atau manipulasi data
- mengembalikan nilai hasil satu atau lebih
- memiliki kekurangan minimal (contoh : `print()`,`plot()`,`read()`,`write()`)

Algoritma harus dikemas sedemikian rupa sehingga memudahkan pembaca untuk memasukkannya ke dalam program yang lebih besar.

Algoritma harus memiliki:

- memiliki nama kelas dan fungsi intuitif yang memperjelas tujuannya bagi pembaca
- menggunakan konvensi penamaan Python dan nama variabel intuitif untuk memudahkan pemahaman
- fleksibel untuk mengambil nilai input yang berbeda
- memiliki petunjuk tipe Python untuk parameter input dan nilai pengembaliannya
- tingkatkan pengecualian Python (ValueError, dll.) pada nilai input yang salah
- memiliki docstrings dengan penjelasan yang jelas dan/atau URL ke materi sumber
- berisi doctests yang menguji nilai input yang valid dan salah
- kembalikan semua hasil perhitungan alih-alih mencetak atau memplotnya

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

**saran penggunaan docstring yang baik untuk testing pytesting**

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
flake8 perubahan_kamu.py
```

```bash
flake8 .
```

untuk docstring dengan cara:

```bash
pytest . --doctest-modules
```

```bash
pytest perubahan_kamu.py --doctest-modules
```

**saran**

[Pemahaman list dan generator](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) lebih disukai daripada penggunaan `lambda`, `map`, `filter`, pengurangan tetapi yang penting adalah menunjukkan kekuatan Python dalam kode yang mudah dibaca dan dipelihara.

## tambahan perubahan

jika ingin menambahkan algoritma atau script python3 yang sederhana atau menambahkan kode yang sederhana, kamu bisa menambahkan perubahan di folder `other`, jika file tersebut melebihi satu file, sebaiknya file-file tersebut ke dalam folder sesuai dengan nama script tersebut sebagai contoh

```
count_bullet_speed
├── count__bullet_speed.py
└── file_tambahan.py
```

# Pull Request

**Pull request yang baik**

- lakukan fork pada repository kami
- setelah melakukan fork anda dibebaskan untuk mengubah atau menambah algoritma.
  - untuk pull request merubah atau memperbaiki diusahakan kamu menerapkan algoritma yang lebih baik dan lebih mudah serta memeberikan penjelasan lebih detail alasan dari perubahaan tersebut lebih baik dari sebelumnya
- lakukan testing dengan menggunakanan pytesting dan flake8 secara lokal
- setelah merubah merubah, atau menambahkan algoritma, serta testing lokal kode kamu, usahakan kamu membuat dengan branch kamu
  ```bash
  git checkout -b <branch_name>
  git add . # atau git add nama_perubahan_kamu.py
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

untuk pull request disarankan untuk menjelaskan secara detail yang kamu ubah atau tambahkan, dan bersikap sopan,serta selalu berterima kasih, itu salah satu bentuk tata krama yang baik terhadap sesama contributor dan programmer lainnya.
