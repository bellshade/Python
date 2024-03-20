<p align="center">
  <img src="https://i.ibb.co/wdKw3mc/decorator.png" alt="Python Advance">
</p>

# Decorators di Python

Decorators adalah alat yang sangat kuat dan berguna dalam Python karena memungkinkan pemrogram mengubah perilaku suatu fungsi atau kelas. Dekorator mengizinkan kita menggabungkan fungsi lain untuk memperluas perilaku fungsi yang dibungkus, tanpa mengubahnya secara permanen.

> Namun sebelum mendalami fungsi dekorator, mari kita pahami beberapa konsep yang akan berguna dalam mempelajari fungsi dekorator. Untuk melihat contoh beberapa silahkan lihat di [Contoh Decorators](../object_oriented/advance/pycode/decorators/contoh_decorators.md)

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
from typing import Callable


# Decorators
def bellshade(func : Callable) -> Callable:


    def wrap(str1 : str) -> str:
        return f'Selamat datang {str1}'

    return wrap  # <- Mengembalikan fungsi (wrap) sebagai fungsi terdalam (bellshade)


# ----------| Cara Penggunaan Decorators |---------- #
@bellshade
def wpu(str1 : str) -> str:
    return str1

```

saat program di jalankan, akan menampilkan:

```console
> Selamat datang Bellshade
```

### Bagaimana jika suatu fungsi mengembalikan sesuatu atau argumen parameter yang diteruskan ke fungsi tersebut?

Pada contoh kasus di bawah ini masih memiliki kesalahan dan menyebabkan TypeError.

```py
from typing import Union, Callable


def openseries(func : Callable) -> Callable:
    def wrap(*args) -> Union[int, float]:
        return_val = func()
        return return_val
    return wrap


@openseries
def add(a : Union[int, float], b : Union[int, float]) -> Union[int, str]:
    return f'Hasil dari parameter a & b ({a} + {b} = {a + b})'


print(add(5, 9))

```

Saat kita jalankan programnya, maka kita akan mendapatkan berupa surat cinta :D seperti di bawah ini:

```console
Traceback (most recent call last):
  File "/..../Python/object_oriented_programming/advance/pycode/decorators/decorators_return.py", line 19, in <module>
    print(add(5,9))
          ^^^^^^^^
TypeError: openseries.<locals>.wrap() takes 0 positional arguments but 2 were given
```

Lalu, cara menyelesaikan masalah TypeError gimana?
Heiiitss... Tenang dulu, disini kita akan memperbaikinya bersama-sama. Jadi kamu gak perlu khawatir dengan Errornya.

Untuk menyelesaikannya kita cukup menambahkan code: `*args` didalam fungsi **wrap & func**, supaya kita tidak perlu menuliskan codenya 1 per 1 parameter argumennya. Sekarang mari kita coba kirim balik surat cintanya :D

```py
# from typing import Union, Callable


def openseries(func : Callable) -> Callable:
    def wrap(*args : Union[int, float]) -> Union[int, float]:
        return_val = func(*args)
        return return_val
    return wrap


@openseries
def add(a : Union[int, float], b : Union[int, float]) -> Union[int, str]:
    return f'Hasil dari parameter a & b ({a} + {b} = {a + b})'


print(add(5, 9))

```
Pada saat program kita jalankan kembali, maka surat cinta yang tadi kita dapatkan udah gak muncul lagi loh...

```console
> Hasil dari parameter a & b (5 + 9 = 14)
```

# Chaining Decorators (Rantai Decorators)

Pada contoh kali ini kita akan membuat 2 fungsi yakni **add & add_quadrat**, langsung saja kita pelari bersama-sama cara menuliskan rantai decorators.

```py
from typing import Callable


# DECORATORS CHAINING
def add(func : Callable) -> Callable:


    def wrap() -> int:
        x = func()
        return x + x
    return wrap


def add_quadrat(func : Callable) -> Callable:


    def wrap() -> int:
        x = func()
        return x**2
    return wrap


# Cara menggunakan rantai decorators
@add
@add_quadrat
def num1() -> int:
    return 25


@add_quadrat
@add
def num2() -> int:
    return 25

```

Horeee.... Selamat kita sudah sampai pada puncak mengenai materi cara membuat _**Decorators Function**_, jika teman-teman masih bingung dengan materi decorators ini. Sangat di sarankan untuk teman-teman senua mempelajari ulang mengenai fungsi / definisi python secara Procedural Oriented Programming tanpa harus memulai dengan Object Oriented Programming.