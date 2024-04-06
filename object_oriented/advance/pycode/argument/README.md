<p align="center">
  <img src="https://i.ibb.co/9cCHHdh/argument.png" alt="Python Advance">
</p>

# Argument Parsing (Argument Parse)

Argument Parsing adalah salah satu metode penguraian argumen baris perintah yang berbeda di gunakan oleh bahasa pemrogramman yang berbeda juga untuk mengurai argumen baris perintah.

### Membuat Argument Parse Tanpa Opsi

Untuk bisa menangkap argumen variable pada system program kita, tentu saja kita membutuhkan package/module `sys` supaya kita bisa menangkap argumen variable ke dalam program kita. Mari kita langsung coba buat progamnya.

```py
import sys

arg : list[str] = sys.argv

print(arg)
```
Hasil yang kita tangkap dari argumen parsingnya.

```console
> ['main.py', 'belajar', 'python', 'itu', 'FUN']
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
```console
> ['belajar', 'python', 'itu', 'FUN']
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
```console
> belajar
> python
> itu
> FUN
```

### Membuat Argument Parse Dengan Opsi

Sekarang kita akan mencoba membuat suatu file menggunakan Command-Line yang kita buat sendiri, dengan contoh perintah seperti di bawah ini:

```console
python main.py -c filename.txt
```
atau bisa juga seperti ini
```console
python main.py --create filename.txt
```

### Sintaks Argument Options

```py
import sys
import os
from getopt import getopt, GetoptError
from typing import List


try:
    argv : List[str] = sys.argv[1:]
    opts, args = getopt(argv, 'c:', ['create='])

except GetoptError as e:
    raise e

for opt, arg in opts:
    if opt in ['-c', '--create']:
        with open(arg, 'w') as file:
            res = file.write('Berhasil membuat berkas dengan CLI...')
            file.close()
    else:
        ...

```
Saat program dijalankan maka tidak ada nilai yang di kembalikan ke konsol.

### Membuat Argument Parse dengan ArgParser

Tentu, dengan adanya module ini kita di permudah untuk membuat flow aplikasi yang berbasis Command-Line. Tanpa perlu memikirkan bagaimana opsi yang harus kita tangkap.

```py
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--create', '-c', help='Untuk kalian bisa membuat file baru')
args = parser.parse_args()

if args.create:
    with open(args.create, 'w') as file:
        file.write('Berhasil membuat berkas dengan CLI...')
        file.close()

```
Setelah program dijalankan tentu saja kita akan mendapatkan file baru di dalam direktori tempat program kita berada.
