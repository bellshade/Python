# Fungsi Matematika (_math_)

Ada kalanya ketika kita akan melakukan perhitungan numerik yang teknis atau saintifik. Perhitungan tersebut seperti trigonometri, eksponen, logaritma, pembulatan bilangan, dan lain sebagainya. Bahasa pemrograman Python menyediakan sebuah standar pustaka (_standard library_) yang memungkinkan kita untuk melakukan operasi perhitungan tersebut. Modul tersebut adalah `math`, di mana terdapat fungsi-fungsi matematis yang dapat digunakan. Gunakan keyword `import` untuk menggunakan modul tersebut.
```python
import math
```

Kali ini, kita akan menggunakan beberapa fungsi yang sering digunakan untuk melakukan operasi fungsi matematis yang dasar

## Nilai Konstanta
Konstanta merupakan nilai tetap yang ditemukan ilmuan setelah melalui serangkaian proses penelitian. Terdapat nilai konstanta yang disediakan oleh modul python, yaitu:
- `math.pi` : Nilai konstanta dari $\pi$ = 3.141592... dengan nilai yang lebih presisi. Nilai ini biasanya digunakan untuk konversi satuan radian ke derajat, menghitung keliling dan luas lingkaran, volume bola, volume tabung, dan lain sebagainya
- `math.e` : Nilai konstanta dari _e_ = 2.71828... dengan nilai yang lebih presisi. Dapat disebut juga sebagai konstanta Euler. Nilai ini biasanya digunakan untuk perhitungan bunga bank, menghitung jumlah penduduk suatu negara, mengukur peluruhan unsur radioaktif, dan lain sebagainya
- `math.tau` : Nilai konstanta yang setara dengan 2 kali dari nilai $\pi$, yaitu $\tau$ = 6.283185..., untuk mengetahui lebih lanjut tentang bilangan ini, tonton video dari Vi Hart berikut [Pi is (still) Wrong](https://www.youtube.com/watch?v=jG7vhMMXagQ)
- `math.inf` : Merupakan nilai positif tak terhingga (_infinity_). Untuk nilai negatif tak terhingga, gunakan `-math.inf`
- `math.nan` : Merupakan nilai yang bukan merupakan angka (_not a number/NaN_). Ini ekuivalen dengan `float('nan')`

```python
import math

print(math.pi)
print(math.e)
print(math.tau)
print(math.inf)
print(-math.inf)
print(math.nan)
```

Output:
```
3.141592653589793
2.718281828459045
6.283185307179586
inf
-inf
nan
```

## Pembulatan
Nilai bilangan desimal (_float_) dapat dibulatkan baik ke atas maupun ke bawah. Modul `math` menyediakan fungsi untuk melakukan itu, yaitu:
- `math.floor(x)` : Sesuai dengan namanya (_floor_=lantai), fungsi ini untuk membulatkan bilangan ke bawah, dimana `x` adalah tipe data _float_. Contoh nilai 14.8 akan dibulatkan ke bawah menjadi 14
- `math.ceil(x)` : Sesuai dengan namanya (_ceil_=langit atau genteng), fungsi ini untuk membulatkan bilangan ke atas, dimana `x` adalah tipe data _float_. Contoh nilai 14.3 akan dibulatkan ke atas menjadi 15

```python
import math

print(math.floor(14.8))
print(math.floor(14.3))
```

Output:
```
14
15
```

## Konversi Satuan Sudut
Sudut dapat dikonversikan dari satuan derajat ke radian, maupun sebaliknya. Fungsi yang digunakan adalah `degrees()` dan `radians()`
- `math.degrees(x)` : Mengkonversikan sudut dari `x` radian ke derajat
- `math.radians(x)` : Mengkonversikan sudut dari `x` derajat ke radian

Nilai konstanta dari `pi` (pada penjelasan sebelumnya tentang "Nilai Konstanta") diperlukan untuk melakukan konversi satuan sudut dari radian ke derajat. Seperti diketahui, besar sudut dari 2 $\pi$ radian = 360 derajat, maka jika ingin melakukan konversi dari nilai 2 $\pi$ radian dan outputnya 360 derajat, gunakan konstanta dari `pi` tersebut. Berikut contoh penggunaan dari fungsi `degrees()` dan `radians()`

```python
import math

print(math.degrees(2 * math.pi))
print(math.radians(90))
```

Output:
```
360.0
1.5707963267948966
```

## Trigonometri
Modul `math` memiliki fungsi trigonometri seperti _sinus_, _cosinus_ dan _tangen_. Fungsi yang digunakan adalah `sin(x)`, `cos(x)` dan `tan(x)`. Dimana nilai `x` adalah sudut tipe _float_ dengan satuan radian. Misalkan, jika ingin mengetahui nilai kosinus dari sudut 30 derajat, maka nilai 30 derajat tersebut harus dikonversikan terlebih dahulu menjadi radian seperti yang dijelaskan pada bagian sebelumnya tentang "Konversi Satuan Sudut".

```python
import math

sudut_30 = math.radians(30)
print(math.sin(sudut_30))
print(math.cos(sudut_30))
print(math.tan(sudut_30))
```

Output:
```
0.49999999999999994
0.8660254037844387
0.5773502691896257
```

## Eksponen dan Logaritma
Eksponen merupakan perpangkatan x terhadap y yang dinotasikan sebagai $x^y$. Sedangkan logaritma merupakan kebalikan dari perpangkatan, dengan bilangan pokok b dan basis a yang dinotasikan sebagai $^a\log_b$. Contoh, jika $5^3$ maka hasilnya 125. Jika diubah dalam bentuk logaritma, maka $^5\log_{125}$ hasilnya adalah 3.

Contoh diatas, dapat dilakukan menggunakan modul bantuan `math`. Beberapa fungsi dasar eksponen dan logaritma yang disediakan adalah sebagai berikut.
- `math.sqrt(x)` : Memperoleh hasil akar kuadrat dari bilangan `x` ($\sqrt x$)
- `math.pow(x, y)`: Memperoleh hasil pangkat antara x dan y ($x^y$)
- `math.log10(x)` : Memperoleh hasil logaritma dari `x` yang bilangan basisnya 10 ($\log_x$)
- `math.log(x, y)` : Memperoleh hasil logaritma dari `x` yang bilangan basisnya `y` ($^y\log_x$)

```python3
import math

print(math.sqrt(25))
print(math.pow(5, 3))
print(math.log10(1000))
print(math.log(125, 5))
```

Output:
```
5.0
125.0
3.0
3.0000000000000004
```

## Referensi
Informasi lebih lanjut tentang penggunaan modul `math` ini, silahkan mengunjungi dokumentasi resmi dari Python [di sini](https://docs.python.org/3.9/library/math.html)

[Materi Selanjutnya](../16_class)