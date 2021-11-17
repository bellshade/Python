# Tanggal dan Waktu (_datetime_)

_Datetime_ adalah suatu standar pustaka (standard library) bawaan _python_ untuk manipulasi tanggal dan waktu. Untuk menggunakannya, cukup `import` dari module `datetime`.

```python
import datetime
```

Setelah dilakukan _import_, fungsi-fungsi atau class di dalamnya dapat digunakan. Misalkan, jika ingin mengetahui waktu saat ini, gunakan fungsi `now()`.

```python
sekarang = datetime.datetime.now()
print(sekarang)
```

Output:
```
2021-10-24 22:12:29.476245
```

Pada hasil output di atas, berisi informasi yang terdiri tahun, bulan, hari, jam, menit, detik, dan milidetik. Karena merupakan tipe objek dari `datetime`, ada beberapa fungsi maupun atribut untuk mengembalikan informasi mengenai objek `datetime` tersebut. Misalkan, jika ingin mengetahui tahun, bulan dan hari, maka gunakan atribut `year`, `month`, dan `day`

```python
print(sekarang.year)
print(sekarang.month)
print(sekarang.day)
```

## Format penulisan tanggal

Modul `datetime` memungkinkan kita unuk menulis format tanggal sesuai yang diinginkan. Beberapa contoh penulisan tanggal adalah sebagai berikut
- 24-10-2021
- 24/10/2021
- 24 October 2021
- dan lain sebagainya

Untuk melakukannya, gunakan fungsi `strftime()`, yang menerima argument string format penulisan tanggal yang biasanya diawali dengan tanda `%` yang dapat disebut juga dengan _directive_. Misalkan, jika ingin mengubah format tanggal hari ini menjadi `DD-MM-YYYY`, maka contoh penggunaan fungsi adalah sebagai berikut

```python
print(sekarang.strftime('%d-%m-%Y'))
```

Contoh kode program di atas, terdapat 3 directive yang dapat dijelaskan sebagai berikut
- `%d` : menampilkan tanggal dalam bentuk angka (01-31)
- `%m` : menampilkan bulan dalam bentuk angka (01-12)
- `%Y` : menampilkan tahun dalam versi lengkap (4 digit)

Sehingga, jika kode di atas dieksekusi, maka hasilnya adalah sebagai berikut (hasil dapat berbeda tergantung tanggal saat ini)
```
24-10-2021
```
Format penulisan tanggal dan waktu lainnya dapat dilihat pada referensi berikut [https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)

## Membuat tanggal dan waktu sendiri
Pada bagian sebelumnya, telah dijelaskan bagaimana mengetahui tanggal saat ini dan bentuk penulisannya. Untuk bagian ini, akan dibahas bagaimana mendefinisikan tanggal dan waktu yang akan kita buat. Masih menggunakan `datetime.datetime()`, misalkan kita mendefinisikan tanggal untuk hari kemerdekaan 17 Agustus 1945

```python
import datetime

hari_kemerdekaan = datetime.datetime(1945, 8, 17)
```

Sehingga, jika dicetak variabel `hari_kemerdekaan`, maka hasilnya adalah `1945-08-17`. Hasil tersebut dapat diubah format penanggalannya sesuai dengan cara yang dijelaskan pada bagian sebelumnya.

## Operasi `datetime`
Tanggal dan waktu dapat dioperasikan seperti operator aritmatika pada umumnya. Salah satu contoh penerapannya adalah operasi pengurangan untuk menghitung umur kita saat ini dengan mengurangkan dari tanggal hari ini terhadap tanggal lahir. Contoh, jika tanggal lahirnya 29 Desember 1997, maka program perhitungan umur adalah sebagai berikut

```python
import datetime

tanggal_lahir = datetime.datetime(1997, 12, 29)
tanggal_sekarang = datetime.datetime.now()
umur_sekarang = tanggal_sekarang - tanggal_lahir
print(umur_sekarang)
```

Maka outputnya adalah `"8704 days, 12:49:29.801983"` (hasil dapat berbeda tergantung tanggal dieksekusi pada saat itu), yang berarti hasil pengurangannya adalah 8704 hari 12 jam 49 menit 29,801983 detik. Jika ingin menampilkan umur dalam tahun dan hari, maka langkah-langkahnya adalah sebagai berikut
- Ambil jumlah harinya menggunakan properti `days`
- Bagi jumlah hari tersebut dengan 365 menggunakan operator _floor division_ agar diperoleh hasil dalam tahun tipe integer
- Bagi jumlah hari tersebut dengan 365 menggunakan operator _modulus_ agar diperoleh sisa harinya.
Sehingga, jika kode di atas dilanjutkan, maka akan menjadi sebagai berikut

```python
jumlah_hari = umur_sekarang.days
umur_tahun = jumlah_hari // 365
sisa_hari = jumlah_hari % 365
print("Umur saya adalah %d tahun %d hari" % (umur_tahun, sisa_hari))
```

Jika dieksekusi kode di atas, maka hasilnya adalah `"Umur saya adalah 23 tahun 309 hari"`

## Referensi
Hal-hal lebih lanjut tentang modul tanggal dan waktu (_datetime_) ini dapat mengunjungi [dokumentasi](https://docs.python.org/3.9/library/datetime.html) berikut

[Materi Selanjutnya](../15_python_math)