# fungsi

fungsi adalah sebuah blok kode yang berjalan ketika ingin digunakan

contoh
```python
def hello():
    print('Hello !')
```

apabila kita ingin meng-gunakan fungsi tersebut kita tinggal command
```python
hello()
```

lantas, apakah kita bisa memasukkan input ke dalam fungsi ? tentu bisa
input yang kita kirimkan ke dalam fungsi disebut sebagai Argument, seperti apa contohnya ?

```python
def hello(nama):
    print('Hello '+str(nama)+' !')
```

apabila kita ingin memakai fungsi tersebut dan memasukkan argument kita cukup mengetikkan
```python
hello('Bellshade')
```

apa kita cuma bisa memasukkan satu argument aja kah ? jawabannya, tentunya ga dong, kita bisa memasukkan lebih dari satu argument
contohnya
```python
def triangle(alas,tinggi):
    hasil = (alas * tinggi)/2
    print(hasil)
```

dan kita pun akan memakai fungsi segitiga kita !!
```python
triangle(2,3)
```

next, pembahasan kita tentang ```return```, apa itu return ? return adalah sebuah function keyword yang mengembalikan nilai dan juga sekaligus "mengakhiri" function itu sendiri

contohnya
```python
def triangle(alas,tinggi):
    hasil = (alas * tinggi)/2
    return hasil
    
print(triangle(2,3))
```

return pada koding diatas, mengakhiri function dari triangle, jadi kita tidak bisa lagi melakukan command apapun yang lewat dari line `return hasil`

next, kita akan bahas sesuatu yang disebut, `default argument`, apa tu ? default argument terjadi apabila kita mendefault / mengatur nilai default dari sebuah argument, misalnya

```python

def salam(waktu="Pagi"):
    greet = "Selamat " + str(waktu)
    return greet

print(salam("Siang")) # Selamat Siang
print(salam("Malam")) # Selamat Malam
print(salam("Sore")) # Selamat Sore
print(salam()) # Selamat Pagi
```

disini kita melakukan default value terhadap argument dari waktu menjadi "Pagi", jadi apabila kita memanggil ```salam()```,
maka itu tidak akan menimbulkan error, karena sudah ada default valuenya, dan default value juga bersifat `flexibel` dimana masih bisa diubah menjadi, 'Siang', 'Malam', dan lainnya.

next kita akan bicara tentang suatu konsep yang menarik, yaitu, `Unlimited` atau `Infinite`, dimana artinya adalah, tak terbatas, apa yang tak terbatas ?
yang tak terbatas di python function adalah argument yang dapat kita inputkan, "caranya begimane tuh ya ? pake infinity stone ga ?", berikut caranya

```python
def unlimited(*args):
    for item in args:
        print(item)
        
unlimited(1,2,3,4)
unlimited([1,2],[3,4])
```

contoh dari unlimited nya adalah, pada command pertama, kita memasukkan 4 parameter, command kedua, kita memasukkan 2 parameter

last, but not least, unlimited keyword argument, dimana kita memberi tahu bahwa argument kita ini memiliki key, atau kunci, hal ini sama dengan dictionary
dimana pada unlimited keyword argument, python memakai prinsip dictionary, sementara pada unlimited argument, python mengadopsi konsep tuple

contohnya ?

```python
def unlimitedkeyword(**infinite):
    for key, value in infinite.items():
        print("index {} memiliki nilai {}".format(key,value))
        
unlimitedkeyword(a=2,b=1,c=3)
unlimitedkeyword(fname="Harry",lname="Potter")
```

dimana pada command pertama, kita memasukkan 3 parameter dengan masing-masing key a,b,c dan value 1,2,3
dan pada command kedua, kita memasukkan 2 parameter dengan masing-masing key yaitu fname dan lname dengan value Harry, Potter

# Fungsi Rekursi
## Definisi Fungsi Rekursi
Fungsi yang dapat memanggil dirinya sendiri dinamakan fungsi rekursi. Beberapa permasalahan dalam algoritma dan struktur data menggunakan
rekursi sebagai solusi penyelesaian, misalnya, dalam struktur data *linked list* atau *tree*. Perhatikan fungsi ```recursion``` di bawah

```python
def recursion(param):
    return recursion(param)
```

Kita harus memperhatikan dua hal ketika berurusan dengan rekursi :. 
1. *Base Case*      : *Base Case* berfungsi untuk mengentikan proses rekursi. Kita harus jeli ketika mendefinisikan *base case*, sebab tiap
permasalahan memiliki *base case* yang berbeda. Salah mendefinisikan *base case* dapat berakhir dengan *infinite recursion*. *Base Case* biasanya
didefinisikan ketika ```n = 0``` atau ```n = 1```
2. Proses Rekursi   : Proses rekursi merupakan solusi penyederhanaan dari masalah yang besar menjadi subpermasalahan yang lebih kecil. Sama seperti
*base case*, proses rekursi setiap permasalahan berbeda-beda.

Contoh fungsi rekursi adalah faktorial. Faktorial merupakan perkalian mundur suatu bilangan positif yang kurang lebih atau sama dengan *n*. Faktorial dilambangkan dengan ```n!```. Faktorial 0 atau ```0!``` bernilai 1. Nilai faktorial suatu bilangan positif dapat dihitung menggunakan proses rekursi yang ditunjukkan pada fungsi ```faktorial(n)``` di bawah :

```python
def faktorial(n):
    """
    menghitung nilai faktorial suatu bilangan positif n
    dan mengembalikan integer
    >>> faktorial(5)
    120
    >>> faktorial(6)
    720
    """
    
    #base case
    if n == 0 or n == 1:
        return 1
    #proses rekursi
    else :
        return n*faktorial(n-1)
```

Visualisasi dari proses rekursi di atas adalah sebagai berikut
![gini](https://user-images.githubusercontent.com/64145699/136579744-7c573f70-a0d8-4e43-b265-d4a66ebfc6a0.png)

## Rekursi Versus Loop
Sebenarnya, beberapa permasalahan dalam pemrograman bisa diselesaikan menggunakan *loop* biasa daripada menggunakan rekursi, seperti pada kasus faktorial di atas. Kode untuk menghitung nilai faktorial menggunakan *loop* ditunjukkan pada kode di bawah ini :

```python
    n = int(input())
    hasil = 1

    if n == 0 or n == 1:
        print(1)
    else :
        for i in range(n, 0, -1):
            hasil = hasil * n
            n = n - 1

    print(hasil)
```

Jika kita meng-```input``` variabel *n* dengan nilai 5, kita akan mendapatkan ```hasil``` 120. Dari hasil tersebut, kita sama-sama tahu, bahwa perhitungan faktorial menggunakan fungsi rekursi dan *loop* biasa menghasilkan solusi yang sama.

**Jadi, daripada memikirkan base case dan proses rekursi, lebih baik kita menggunakan loop biasa ketika menghadapi permasalahan yang melibatkan proses iterasi?**
Jawabannya : **tidak**. Sebab, beberapa permasalahan dalam algoritma dan struktur data menggunakan pendekatan rekursi sebagai penyelesaian masalah. Hal ini disebabkan penyelesaian permasalahan menggunakan *loop* atau iterasi biasa tidak intuitif untuk permasalahan tersebut. Contoh solusi yang kurang intuitif dari permasalahan pada algoritma dan struktur data adalah ketika kita ingin meng-*insert* *node* pada *linked list* atau menambahkan *node* pada *tree*. Setidaknya sampai tulisan ini dibuat, penulis belum mendapatkan penyelesaian untuk menambahkan *node* pada kedua struktur data di atas menggunakan pendekatan iteratsi biasa.

Contoh lain dari penyelesaian masalah menggunakan rekursi dapat dilihat di file ```recursion_example.py``` yang ada di repositori.

# Closure
## Definisi Closure
Kita bisa mendefinisikan fungsi di dalam fungsi. Di Python, teknik ini disebut sebagai *closure* atau *nested function*. *Closure* dapat mengakses variabel yang tidak berada di dalam *scope* fungsi tersebut. Variabel ini biasa disebut *nonlocal variable*. *Closure* juga dapat mengembalikan fungsi layaknya fungsi rekursi. Fungsi ```outerFunc()``` di bawah ini mendemonstrasikan bagaimana *closure* bekerja.

```python
def outerFunc(pesan):

    def innerFunc():
        # parameter "pesan" dapat diakses oleh innerFunc
        print("{} juga dari innerFunc".format(pesan))

    # ketika outerFunc(pesan) dipanggil, innerFunc() juga ikut terpanggil
    innerFunc()


pesan = "Halo"
hasil = outerFunc(pesan)
# memunculkan "Halo juga dari innerFunc" di console
hasil
```

Seperti yang sudah disebutkan pada bagian definisi, *closure* juga dapat mengembalikan fungsi. *Closure* yang memiliki kegunaan seperti ini biasa disebut sebgai *factory function*. Fungsi ```pangkat()``` di bawah mendemonstrasikan bagaimana cara kerja *factory function*

```python
def pangkat(n):

    def basis(x):
        return x ** n
    return basis


# membuat perpangkatan 2
pangkat2 = pangkat(2)

# membuat perpangkatan 3
pangkat3 = pangkat(3)

# menampilkan 4
print(pangkat2(2))

# menampilkan 27
print(pangkat3(3))
```


<a href="https://github.com/bellshade/Python/blob/task/fungsi/Basic/fungsi/fungsi.py">Bellshade Python Function</a>
