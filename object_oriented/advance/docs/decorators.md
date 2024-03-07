# Decorators di Python

Decorators adalah alat yang sangat kuat dan berguna dalam Python karena memungkinkan pemrogram mengubah perilaku suatu fungsi atau kelas. Dekorator mengizinkan kita menggabungkan fungsi lain untuk memperluas perilaku fungsi yang dibungkus, tanpa mengubahnya secara permanen.

> Namun sebelum mendalami fungsi dekorator, mari kita pahami beberapa konsep yang akan berguna dalam mempelajari fungsi dekorator.

## Contoh 1: Menjadikan Fungsi Sebagai Objek

Pada contoh kita yang pertama, kita akan membuat fungsi dengan nama **menyapa**.

```py
# Buatlah fungsi dengan nama apapun yang kamu inginkan, pada contoh pertama kita akan memberikan fungsi dengan nama menyapa.
def menyapa(s1):

  # Fungsi ini tidak memiliki keluaran / output di konsol, dan hanya mengembalikan nilai.
  return s1.upper()
  
# Mencetak isi nilai dari fungsi tanpa objek.
print(menyapa('halo semua sobat WPU!!!'))

# Berikan nama objek sesuai keinginan dan kebutuhan, disini kita akan memberikan nama objeknya yaitu (user)
user = menyapa

# Untuk memanggil fungsi di dalam objek yang telah kita definisikan bersama, kita hanya perlu menambahkan tanda kurung setelah nama objek. contoh: user([nilai])
user('halo semua sobat WPU!!!')

# Maka secara otomatis fungsi belajar didalam objek user yang bernilaikan Python akan muncul di konsol.
# >>> HALO SEMUA SOBAT WPU!!!
```

## Contoh 2: Menjadikan Fungsi Sebagai Parameter Fungsi

Pada contoh kita yang kedua, kita akan membuat beberapa fungsi dengan nama **kasar, lembut, & kalem**.

```py
# Apabila melihat tanda backslash n (\n) itu tandanya kita bisa memotong panjang karakter dan dapat memberikan baris baru.
# Fungsi pertama kita buat dengan nama (kasar), yang hanya mengembalikan suatu nilai perubahan text.
def kasar(s):
  return s.upper()
  
# Fungsi kedua kita buat dengan nama (lembut), yang hanya mengembalikan suatu nilai perubahan text.
def lembut(s):
  return s.lower()
  
# Fungsi ketiga kita buat dengan nama (kalem), yang bertujuan untuk menampilkan isi nilai dari Fungsi sebelumnya.
def kalem(func):

  # Selanjutnya kita buat objek dengan nama (menyapa)
  menyapa = func('Halo Semua Sobat WPU!!!\nJangan lupa titik koma yaa (;)\nEh iya lupa... kalau ini program Python :-D\n')
  
  # Keluarkan nilai dari objek menyapa yang memberikan nilai didalam parameter func(...) keluar layar / konsol.
  print(menyapa)

# Setelah di rasa cukup, saatnya kita panggil fungsi kalem(), dan memasukkan kedua fungsi di atas sebagai parameter dari fungsi kalem().
kalem(kasar)
kalem(lembut)
```

## Contoh 3: Mengembalikan Fungsi Di Dalam Fungsi

Pada contoh kita yang ketiga, kita akan membuat beberapa fungsi dengan nama **users & belajar**.

```py
# Kita buat fungsi terluar dengan nama (users)
def users(nama):

  # Saatnya kita buat fungsi didalam fungsi ddngan nama (belajar)
  def belajar(s):
    
    # Return ini mengembalikan nilai untuk fungsi (belajar)
    return f'username: {nama}\nsedang belajar: {s}'
  
  # Di return terluar, kita akan mengembalikan nilai berupa fungsi (belajar)
  return belajar
  
# Buatlah objek sesuai keinginan, dan berikan nilai fungsi (users) didalam objek.
s1 = users('bellshade')

# Cetak objek yang sudah di definisikan, yang di ikuti dengan tanda kurung ().
print(s1('Fullstack'))
```

# Decorators

Seperti yang dinyatakan di atas, dekorator digunakan untuk mengubah perilaku fungsi atau kelas. Di Dekorator, fungsi diambil sebagai argumen ke dalam fungsi lain dan kemudian dipanggil di dalam fungsi pembungkus.

Setelah kita mempelajari bersama mengenai beberapa contoh-contoh tentang fungsi diatas, sekarang saatnya untuk kita mempelajari Decorators Function bersama-sama.

Dalam membuat Decorator tentu saja kerap kaitannya dengan fungsi, yaa namanya juga Decorator Function kalau bukan fungsi apa lagi.

## Contoh Syntax Decorators

```py
@bellshade  # <- Decorators dari sintaks fungsi (bellshade)
def wpu_store(): # <- Membuat fungsi dengan nama (wpu_store)
  return 'Web Programming UNPAS!' # <- Mengembalikan nilai string [Web Programming UNPAS!]
  
'''
--> Kode di atas setara dengan <--

def wpu_store(): <- Membuat fungsi dengan nama (wpu_store)
  return 'Web Programming UNPAS!' <- Menampilkan nilai string [Web Programming UNPAS!] dari fungsi (wpu_store)
  
wpu = bellshade(wpu_store) <- Membuat variable / objek (wpu)

wpu() <- Mengeksekusi fungsi bellshade dengan perantara variable wpu 
'''
```

## Decorators Mengubah Perilaku:

```py
# bellshade function: fungsi ini akan kita jadikan sebagai decorators function
def bellshade(func):
  x = 'Belajar Membuat Website' # <- Variable x: agar di cetak didalam fungsi (wrap)
  
  def wrap():
    print('Selamat datang di ruang Bellshade.')
    print('bersama narasumber:', end='') # <- end="": agar keluar ke konsol hanya satu baris sejajar dengan parameter fungsi (bellshade)
    func() # <- Space func dari parameter fungsi (bellshade)
    print(f'Dalam rangka: {x}\nDieksekusi dari fungsi: {func.__name__}') # <- Mencetak Variable dari fungsi (bellshade) 
  
  return wrap # <- Mengembalikan fungsi (wrap) sebagai fungsi terdalam (bellshade)
  
# ----------| Cara Penggunaan Decorators |---------- #

# Cara memanggil fungsi (wrap & bellshade)
@bellshade
def wpu():
  print('Web Programming UNPAS!')

wpu()
```

saat program di jalankan, akan menampilkan:

```bash
>>> Selamat datang di ruang Bellshade.
>>> bersama narasumber: Web Programming UNPAS!
>>> Dalam rangka: Belajar Membuat Website
>>> Dieksekusi dari fungsi: wpu
```

### Bagaimana jika suatu fungsi mengembalikan sesuatu atau argumen parameter yang diteruskan ke fungsi tersebut?

Pada contoh kasus di bawah ini masih memiliki kesalahan dan menyebabkan TypeError.

```py
# openseries function: fungsi ini akan kita jadikan sebagai decorators function
def openseries(func):
  def wrap():
    print('OpenSeries: Matematika Dasar.')
    return_val = func() # <- Space func dari parameter fungsi (openseries)
    print(f'Dieksekusi dari fungsi: {func.__name__}') # <- Mencetak nama dari fungsi (add) 
    return return_val
  
  return wrap # <- Mengembalikan fungsi (wrap) sebagai fungsi terdalam (openseries)
  
# ----------| Cara Penggunaan Decorators Yang Mengembalikan Argumen Parameter |---------- #

# Cara memanggil fungsi (wrap & openseries)
@openseries
def add(a,b):
  print(f'Fungsi penjumlahan dari {a} + {b} = {a + b}') # <- Fungsi print ini akan muncul di dalam fungsi (wrap) didalam fungsi (openseries)
  return f'Hasil dari parameter a & b ({a} + {b} = {a + b})'

print(add(5,9))
```

Saat kita jalankan programnya, maka kita akan mendapatkan berupa surat cinta :D seperti di bawah ini:

```terminal
Traceback (most recent call last):
  File "/..../Python/object_oriented_programming/advance/pycode/decorators/decorators_return.py", line 19, in <module>
    print(add(5,9))
          ^^^^^^^^
TypeError: openseries.<locals>.wrap() takes 0 positional arguments but 2 were given
```

Lalu, cara menyelesaikan masalah TypeError gimana?
Heiiitss... Tenang dulu, disini kita akan memperbaikinya bersama-sama. Jadi kamu gak perlu khawatir dengan Errornya.

Untuk menyelesaikannya kita cukup menambahkan code: `*args, **kwargs` didalam fungsi **wrap & func**, supaya kita tidak perlu menuliskan codenya 1 per 1 parameter argumennya. Sekarang mari kita coba kirim balik surat cintanya :D

```py
# openseries function: fungsi ini akan kita jadikan sebagai decorators function
def openseries(func):
  def wrap(*args, **kwargs):
    print('OpenSeries: Matematika Dasar.')
    return_val = func(*args, **kwargs) # <- Space func dari parameter fungsi (openseries)
    print(f'Dieksekusi dari fungsi: {func.__name__}') # <- Mencetak nama dari fungsi (add) 
    return return_val
  
  return wrap # <- Mengembalikan fungsi (wrap) sebagai fungsi terdalam (openseries)
  
# ----------| Cara Penggunaan Decorators Yang  Argumen Parameter |---------- #

# Cara memanggil fungsi (wrap & openseries)
@openseries
def add(a,b):
  print(f'Fungsi penjumlahan dari {a} + {b} = {a + b}') # <- Fungsi print ini akan muncul di dalam fungsi (wrap) didalam fungsi (openseries)
  return f'Hasil dari parameter a & b ({a} + {b} = {a + b})'

print(add(5,9))
```
Pada saat program kita jalankan kembali, maka surat cinta yang tadi kita dapatkan udah gak muncul lagi loh...

```terminal
>>> OpenSeries: Matematika Dasar.
>>> Fungsi penjumlahan dari 5 + 9 = 14
>>> Dieksekusi dari fungsi: add
>>> Hasil dari parameter a & b (5 + 9 = 14)
```

# Chaining Decorators (Rantai Decorators)

Pada contoh kali ini kita akan membuat 2 fungsi yakni **add & add_quadrat**, langsung saja kita pelari bersama-sama cara menuliskan rantai decorators.

```py
# DECORATORS CHAINING
# Mari kita coba buat rantai fungsi decorators

# ================================= #

# Buatlah fungsi decorators yang di inginkan
def add(func):
  def wrap():
    x = func()
    return x + x
  return wrap

def add_quadrat(func):
  def wrap():
    x = func()
    return x**2
  return wrap
  
# Cara menggunakan rantai decorators
@add
@add_quadrat
def num1():
  return 25

@add_quadrat
@add
def num2():
  return 25
  
print(num1())
print(num2())
```

Horeee.... Selamat kita sudah sampai pada puncak mengenai materi cara membuat _**Decorators Function**_, jika teman-teman masih bingung dengan materi decorators ini. Sangat di sarankan untuk teman-teman senua mempelajari ulang mengenai fungsi / definisi python secara Procedural Oriented tanpa harus memulai dengan Object Oriented.