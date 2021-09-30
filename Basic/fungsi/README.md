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

<a href="https://github.com/bellshade/Python/blob/task/fungsi/Basic/fungsi/fungsi.py">Bellshade Python Function</a>
