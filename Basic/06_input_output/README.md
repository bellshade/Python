# input python

pada python terdapat fungsi dimana kita bisa membuat sebuah inputan dimana bisa berubah secara dinamis tanpa harus dirubah ke dalam kodingan. contohnya sebagai berikut

```python
nama = input("masukkan nama kamu ")
print(nama)
```

pada kode diatas jika dijalkan akan menamppilkan
```
masukkan nama kamu
```
jika kita memasukkan nama maka program akan menampilkan nama yang sebelumnya kita ketik
```
masukkan nama kamu
arfy
arfy
```
contoh lain
```python
nama = input("masukkan nama ")
print("selamat pagi ", nama)
```
maka akan menampilkan berupa ``selamat pagi nama_yang_diinputkan`` contoh output
```
masukkan nama
arfy
selamat pagi arfy
```

kita juga bisa merubah value dari variabel yang sudah ada dengan menggunakan input
```python
nama = "arfy"
# menampikan isi value dari nama terlebih dahulu
print(nama)
nama = input("masukkan nama ")
print("di variabel nama sekarang adalah ", nama)
```
maka output yang keluar adalah
```
arfy
masukkan nama
jole
di variabel nama sekarang adalah jole
```


## keywords yang tidak bisa digunakan pada python

contoh penggunaan keywords yang dilarang pada python
```python
class sma_saya = "bahasa"
print(sma_saya)
```
hasil esekusi diatas akan menyebabkan error karena ``class`` merupaakan salah satu nama fungsi dari python

- False
- None
- True
- and
- as
- assert
- break
- class
- continue
- def
- del
- elif
- else
- except
- finally
- for
- from
- global
- if
- import
- in
- is
- lambda
- nonlocal
- not 
- or
- pass
- raise
- try
- return
- while
- with
- yield

video penjelasan tentang operator input output = [Belajar python dasar - mengambil input data dari user](https://www.youtube.com/watch?v=Ar1xxIsyuvI&list=PLZS-MHyEIRo59lUBwU-XHH7Ymmb04ffOY&index=8)

[Materi Selanjutnya](../07_logika_percabangan)