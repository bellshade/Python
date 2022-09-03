# Input/Output Python

Pada Python terdapat fungsi dimana kita bisa membuat sebuah inputan. Contohnya sebagai berikut:

```python
nama = input("masukkan nama kamu ")
print(nama)
```

pada kode diatas jika dijalankan akan menampilkan:

```bash
masukkan nama kamu
```

Jika kita memasukkan nama maka program akan menampilkan nama yang sebelumnya kita ketik:

```bash
masukkan nama kamu
arfy
arfy
```

Contoh lain:

```python
nama = input("masukkan nama ")
print("selamat pagi ", nama)
```

Maka akan menampilkan berupa ``selamat pagi nama_yang_diinputkan``. Contoh output:

```bash
masukkan nama
arfy
selamat pagi arfy
```

Kita juga bisa merubah value dari variabel yang sudah ada dengan menggunakan input.

```python
nama = "arfy"
# menampikan isi value dari nama terlebih dahulu
print(nama)
nama = input("masukkan nama ")
print("di variabel nama sekarang adalah ", nama)
```

Maka output yang keluar adalah:

```bash
arfy
masukkan nama
jole
di variabel nama sekarang adalah jole
```

Video penjelasan tentang operator input output = [Belajar python dasar - mengambil input data dari user](https://www.youtube.com/watch?v=Ar1xxIsyuvI&list=PLZS-MHyEIRo59lUBwU-XHH7Ymmb04ffOY&index=8)

[Materi Selanjutnya](../07_logika_percabangan)