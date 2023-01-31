# *Contributing*
![contributor](https://img.shields.io/github/contributors/bellshade/PythonAlgorithm?label=kontributor&style=for-the-badge)

***Contributor***

Kami sangat senang anda telah ikut berkontribusi dalam implementasi algortima, struktur data, atau memperbaiki *error*.
Semua boleh ikut berkontribusi sekecil apapun dengan pengecualian sebagai berikut:

- Hasil pekerjaan kamu adalah buatan kamu sendiri dan tidak ada hak cipta dari orang lain. Jika kami menemukan kesamaan, maka tidak kami *merge*.
- Hasil kerja kamu akan berlisensi [MIT](LICENSE) ketika *pull request* kamu sudah di-*merge*.
- Hasil kerja kamu wajib mengikuti standar dan *style* koding dari kami.
- Hanya menerima *file* dengan ekstensi ``*.py``, selain itu dibuat pengecualian dengan menjelaskan secara detail.

**Apa itu algoritma?**

Algoritma adalah satu atau lebih fungsi dan/atau kelas yang:

- memiliki satu atau lebih *input*;
- melakukan beberapa internal kalkulasi atau manipulasi data;
- mengembalikan satu atau lebih nilai hasil;
- memiliki kekurangan minimal (contoh: `print()`,`plot()`,`read()`,`write()`) terkecuali jika memperbaiki materi tutorial.

Algoritma harus dikemas sedemikian rupa agar dapat dengan mudah dimasukkan ke dalam program yang lebih besar.

Algoritma harus:

- memiliki nama kelas dan fungsi intuitif yang memperjelas tujuannya bagi pembaca;
- menggunakan konvensi penamaan Python dan nama variabel intuitif untuk memudahkan pemahaman;
- fleksibel untuk mengambil nilai *input* yang berbeda;
- memiliki petunjuk tipe Python untuk parameter *input* dan nilai pengembaliannya;
- tingkatkan pengecualian Python (ValueError, dll.) pada nilai *input* yang salah;
- memiliki *docstring* dengan penjelasan yang jelas dan/atau URL ke materi sumber;
- berisi *doctests* yang menguji nilai *input* yang valid dan salah;
- mengembalikan semua hasil perhitungan alih-alih mencetak atau memplotnya.

# Docstrings

**Penggunaan *docstring***

Penggunaan *docstring* bertujuan untuk memudahkan pembaca membaca dan mengimplementasikan algoritma.

***Docstring* yang baik:**

```py
def adding(num1, num2):
    """
    menambahkan kedua bilangan
    num1 dan num2 dan dikembalikan hasilnya
    num1 = integer
    num2 = integer
    mengembalikan hasil yang berupa integer
    >>> adding(2, 50)
    52
    >>> adding(3, 2)
    5
    """
    return num1 + num2
```

***Docstring* yang kurang baik:**

```py
def adding(num1, num2):
    """
    num1 + num2
    """
    return num1 + num2
```

**Saran penggunaan *docstring* yang baik untuk *doctest*:**

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

## Lint Test

**Instalasi**

Kami menggunakan ``flake8`` untuk *lint testing* agar penulisan kode jadi lebih baik.

Installasi ``flake8``:

```bash
pip install flake8
```

**Testing**

Untuk *lint testing*, kami menyarankan kamu untuk melakukan tes lokal dengan ``flake8``:

```bash
flake8 perubahan_kamu.py
```

```bash
flake8 .
```

Untuk *doctests*:

```bash
pytest . --doctest-modules
```

```bash
pytest perubahan_kamu.py --doctest-modules --ignore=Basic/
```

**Saran**

[Pemahaman list dan generator](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) lebih disukai daripada penggunaan `lambda`, `map`, `filter`. Tetapi yang penting adalah menunjukkan kekuatan Python dalam kode yang mudah dibaca dan dipelihara.

## Tambahan Perubahan

Jika ingin menambahkan algoritma atau *script* Python 3 yang sederhana atau menambahkan kode yang sederhana, kamu bisa menambahkan perubahan di folder `other`. Jika terdapat beberapa *file*, sebaiknya *file-file* tersebut ke dalam folder sesuai dengan nama *script* tersebut sebagai contoh:

```
count_bullet_speed
├── count__bullet_speed.py
└── file_tambahan.py
```

**Catatan :** **Tidak boleh merubah-rubah apapun yang terdapat pada file [DIRECTORY.md](DIRECTORY.md) karena akan menggenerate daftar file kode secara otoamatis dan dimasukkan kedalam ``DIRECTORY.md``

# *Pull Request*

***Pull request* yang baik**

Informasi: gunakan [*issue*](https://github.com/bellshade/Python/issues) apabila ingin menambahkan kode atau implementasi algoritma, dll (*basic*) agar tidak ada konflik dengan *pull request* lainnya. Kamu juga bisa menggunakan issue jika kamu ada 
kendala atau masalah ketika melakukan pull request. Kamu juga bisa bertanya pada forum discord **WPU** dan **Kelas Terbuka** perihal bellshade.

- Lakukan penjelasan deskripsi perubahan yang anda lakukan pada repositori kami dengan membuat penjelasan di [*issue*](https://github.com/bellshade/Python/issues).
- Setelah menjelaskan perubahan anda di [*issue*](https://github.com/bellshade/Python/issues) kemudian lakukan *fork* pada repositori kami.
- Setelah melakukan *fork*, anda dibebaskan untuk mengubah atau menambah algoritma.
  - Untuk *pull request* merubah atau memperbaiki, diusahakan kamu menerapkan algoritma yang lebih baik dan lebih mudah serta memeberikan penjelasan lebih detail alasan dari perubahaan tersebut lebih baik dari sebelumnya.
- Lakukan tes dengan menggunakan ``pytest`` dan ``flake8`` secara lokal.
- Setelah merubah-rubah atau menambahkan algoritma serta melakukan tes lokal kode kamu, usahakan kamu membuat *local branch* baru:
  ```bash
  git checkout -b <branch_name>
  git add . # atau git add nama_perubahan_kamu.py
  git commit -m "feat: menambahkan algoritma terbaru"
  ```
- Lakukan *push* ke *branch* kamu dan kemudian *open pull request*.

**Saran pesan commit**

- `feat:` untuk menambah algoritma atau tambahan lainnya;
- `fix:` untuk mengubah algoritma yang sudah ada atau memperbaiki;
- `docs:` untuk mengubah atau membuat dokumentasi;
- `add:` untuk menambah algoritma atau tambahan lainnya (opsional);

Catatan: pesan commit harus menjelaskan perubahan secara singkat.

Contoh:
- &#9746; feat: test_x.py
- &#9745; feat: tambah unittest untuk algoritma x

Lebih lengkapnya bisa dilihat di:
- [EN](https://www.conventionalcommits.org/en/v1.0.0/)
- [ID](https://www.conventionalcommits.org/id/v1.0.0/)

Pull request akan di-*merge* jika:

- mengikuti standar dan arahan dari `CONTRIBUTING.md`;
- lulus tes dan cek dari beberapa tes yang sudah kami siapkan.

**Tambahan**:

- Jika ada kendala atau masalah dalam *pull request*, kamu bisa laporkan masalahnya dalam [issue](https://github.com/bellshade/PythonAlgorithm/issues).
- Jika ada tes yang tidak lewat atau gagal, kami akan cek kembali perubahan anda.

Untuk *pull request*, disarankan untuk menjelaskan secara detail yang kamu ubah atau tambahkan, dan bersikap sopan serta selalu berterima kasih. Itu salah satu bentuk tata krama yang baik terhadap sesama *contributor* dan *programmer* lainnya.

