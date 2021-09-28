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