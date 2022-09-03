# Perulangan

Perulangan adalah urutan instruksi yang akan dijalankan, apabila suatu kondisi terpenuhi.

Perulangan pada Python terbagi 2, yaitu:
- while
- for

mari kita ulas terlebih dahulu while loop.

## While

Contoh:

```python
a = 1

while a <= 5:
    print(a)
    a += 1
```

Apabila variable `a` yang awalnya 1, tidak melebihi ataupun sama dengan 5 maka loop bisa berjalan, apabila kondisinya sudah tidak terpenuhi lagi, maka statement loop akan otomatis selesai.

Contoh lainnya:

```python
b = 5

while b >= 1:
    print(b)
    b -= 1
```

Apabila variable b yang awalnya 5, masih lebih besar atau sama dengan 1, apabila variable b sudah menyentuh angka 0, maka loop statement otomatis tidak akan bekerja.

Bisakah kita menghentikan proses looping di tengah statement yang masih memenuhi persyaratan?
Tentu bisa dong!

Yaitu denga menggunakan keyword ```break```. Contohnya:

```python
c = 1

while c <= 5:
    print(c)
    if c == 3:
        break
    c += 1
```

Apabila nilai variable `c` masih ada di bawah atau sama dengan `5` maka proses loop bisa dilakukan, tetapi, jika nilai `c` sudah di angka `3`, kita melakukan proses ```break```, atau berhenti. Jadi kita menghentikan loop nya meskipun hasil statement loop nya masih benar.

Terus, bisa diskip ga sih suatu bilangan? Bisa dong, kita memakai statement ```continue```, contohnya:

```python
d = 0

while d < 5:
    d += 1
    if d == 3:
        continue
    print(d)
```

Dari program di atas, kita melakukan statement yang sama dengan `3` statement di atas, tapi ni, bedanya adalah, apabila variable `d` sudah ada di angka `3`, kita ```continue``` aja, atau kita skip.

Last but not least, gimana sih cara ngasih tau kita kalau misalnya loop nya udah selesai gitu? tentu ada caranya, kita akan pakai statement ```else```. Contohnya:

```python
e = 0

while e <= 5:
    print(e)
    e += 1
else:
    print("Selamat, looping anda telah selesai !!")
```

Nah, jadi kalau misalnya loop kita udah selesai, Python akan memberikan statement, `"Selamat, looping anda telah selesai !!`


## For

Contohnya:

```python
angka = [1,2,3,4,5]

for item in angka:
    print(item)
```

Jadi maksud dari koding di atas adalah untuk setiap item di dalam list angka, silahkan tampilkan item tersebut.

Kita juga bisa menggunakan `break` di perulangan `for`:

```python
for item in angka:
    print(item)
    if item == 3:
        break
```

Meskipun statement dari `break` for loop ini beda dengan while loop, maknanya sama saja, kalau itemnya udah di angka 3, break aja, atau selesaikan aja.

apa di for loop ada ```continue```? pastinyaa:

```python
for item in angka:
    if item == 3:
        continue
    print(item)
```

Penjelasannya adalah, apabila item dari list angka tersebut udah ada di angka `3`, angka `3` nya diskip, dan berlanjut ke angka 4.

Last but not least,

```else``` statement

```python
for item in angka:
    print(item)
else:
    print("Selesai !")
```


Apa sih perbedaan antara while loop dan for loop?

- while loop itu bergerak/melakukan sesuatu berdasarkan "kondisi" seperti misalnya tadi, "jika nilai a masih dibawah 5, maka tampilkan a", tapi kalau tidak? tentu outputnya tidak ada lagi dan while loop selesai, hal ini bisa di dukung dengan arti dari ```while``` yang artinya ```ketika```.

- for loop adalah looping yang melakukan sesuatu berdasarkan "keanggotaan", seperti misalnya, "untuk setiap anggota dari list angka, tampilkan (print)", hal ini tentu di dukung dengan arti dari statement for loop yaitu ```for item in iterable``` yang artinya ```untuk setiap item yang ada di dalam iterable``` dan arti kata ```for``` itu sendiri yang artinya ```untuk```.


<a href="https://github.com/bellshade/Python/blob/task/loop/Basic/looping/while_loop.py">while loop</a><br>
<a href="https://github.com/bellshade/Python/blob/task/loop/Basic/looping/for_loop.py">for loop</a>

Video penjelasan tentang looping (for) = [Belajar dasar python - for loop (perulangan)](https://www.youtube.com/watch?v=Z4qfMhx4XzQ&list=PLZS-MHyEIRo59lUBwU-XHH7Ymmb04ffOY&index=25)

Video penjelasan tentang looping (while) = [Belajar dasar python - while loop (perulangan)](https://www.youtube.com/watch?v=ZupffvoCChQ&list=PLZS-MHyEIRo59lUBwU-XHH7Ymmb04ffOY&index=26)

[Materi Selanjutnya](../09_fungsi)