# Command-Line Argument Parsing (Argument Parse)

Argument Parsing adalah salah satu metode penguraian argumen baris perintah yang berbeda di gunakan oleh bahasa pemrogramman yang berbeda juga untuk mengurai argumen baris perintah.

### Membuat Argument Parse Tanpa Opsi

Untuk bisa menangkap argumen variable pada system program kita, tentu saja kita membutuhkan module `sys` supaya kita bisa menangkap argumen variable ke dalam program kita. Mari kita langsung coba buat progamnya.

```py
import sys

arg : list[str]= sys.argv

print(arg)
```
Hasil yang kita tangkap dari argumen parsingnya.

```terminal
>>> ['main.py', 'belajar', 'python', 'itu', 'FUN']
```
Lalu bagaimana caranya supaya tulisan file kita tidak ikut serta dalam penangkapan argumen variablenya?
Karena argumen variable yang di tangkap itu berupa tipe data `list` atau `array` dalam bahasa program lain, maka cara kita untuk mengaksesnya membutuhkan indeks. Kita bisa memakai `for loop` untuk mengaksesnya atau kita juga bisa memasukan indeksnya secara manual.

```py
import sys

arg : list[str]= sys.argv

# Apa yang di tangkap oleh program pada argumen variable, maka program kita akan mengabaikan indeks ke 0
print(arg[1:])
```
Maka secara otomatis kita akan mendapatkan nilai dari argumen variable yang di tangkap oleh program kita dan akan melewati indeks ke 0, karena indeks ke 0 terssbut adalah nama file program kita.
```terminal
>>> ['belajar', 'python', 'itu', 'FUN']
```

Sekarang mari kita coba eksekusi argumen variable yang di tangkap menggunakan perulangan `for loop`.
Saat kita ingin eksekusi argumen variable dengan `for loop` maka kita perlu mengubah posisi indeksnya.

```py
import sys

arg : list[str]= sys.argv[1:]

for i in arg:
  print(i)
```
Hasil dari perulangan `for loop` ke layar konsole
```terminal
>>> belajar
>>> python
>>> itu
>>> FUN
```

### Membuat Argument Parse Dengan Opsi