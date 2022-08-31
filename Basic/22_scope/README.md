# Pengertian
Scope adalah sebuah variabel hanya dapat diakses didalam wilayah dia dibuat, inilah yang disebut dengan *Scope*.

# Jenis-Jenis Scope

## Local Scope
Sebuah variabel yang dibuat di dalam sebuah fungsi termasuk *Local Scope* dari fungsi tersebut
dan hanya dapat digunakan didalam fungsi tersebut.

Contoh:
```py
def myfunc():
    x = 300
    print(x)

myfunc()
# variabel x tidak dapat diakses di sini
```

### Fungsi di dalam Fungsi
Seperti penjelasan di atas, variabel `x` tidak dapat diakses di luar fungsi tersebut, tapi `x` dapat diakses
di fungsi manapun di dalam fungsi tersebut

Contoh:
```py
def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()
```

## Global Scope
Sebuah variabel yang dibuat di bagian utama kode python adalah *Global Variable* yang termasuk *Global Scope*
variabel global dapat digunakan dimanapun

Contoh:
```
x = 300

def myfunc():
    print(x)

myfunc()
print(x)
```


### Menamai Variabel
Jika kamu menamai suatu variabel `x` di global scope dan kamu juga menamai variabel lainnya dengan `x`,
maka python akan memisahkan variabel tersebut menjadi dua variabel yang berbeda

Contoh:
```py
x = 300

def myfunc():
    # ini adalah variabel x yang berbeda dengan yang diatas
    x = 200
    print(x)

myfunc()

print(x)
```

## Global Keyword
Jika kamu ingin membuat atau mengganti variabel tapi hanya bisa di *local scope*, kamu bisa menggunakan keyword global.

Contoh:
```py
def myfunc():
    global x
    x = 300

myfunc()

print(x)
```