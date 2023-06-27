# Python Dekorator

Dalam python, Dekorator atau ``Decorator`` adalah pola desain dalam python yang memungkinkan pengguna menambahkan fungsi baru ke dalam objek yang sudah ada tanpa ada perubahan dalam strukturnya.
Dekorator biasanya dipanggil sebelum definisi dari fungsi yang ingin dibuat.

Python memperbolehkan penggunaan fungsi yang bercabang atau nested function untuk mengakses statement diluar dari fungsi yang dibuat, sebagai contoh

```python
def menampilkan_kata(pesan):
    def kirim_pesan():
        print(pesan)

    kirim_pesan()

menampilkan_kata("bellshade")
```

dengan contoh diatas, kita bisa membuat dekorator yang sederhana yang merubah huruf besar menjadi huruf kecil

```python
# mendifinisikan fungsi bernama 'dekorator_huruf_kecil'
def dekorator_huruf_kecil(kata_besar):
    # membuat fungsi nested yang kita sebut 'wrapper'
    def wrapper():
        # memanggil yang diteruskan dekorator_huruf_kecil
        # dan kemudian dimasukkan ke dalam variabel
        # 'kata_message'
        kata_message = kata_besar()
        # menggunakan fungsi 'lower()' untuk membuat
        # variabel dari kata_message menjadi kecil
        # dan kemudian ditugaskan dalam variabel
        # buat_kata_kecil
        buat_kata_kecil = kata_message.lower()
        # mengembalikan nilai dari 'wrapper'
        return buat_kata_kecil
    # mengembalikan fungsi dari wrapper
    return wrapper
```

kemudian disini kita bisa bisa menggunakan fungsi baru lagi dengan cara
```python
def kata():
    return "BELLSHADE"

jadikan_kata_kecil = dekorator_huruf_kecil(kata)
jadikan_kata_kecil()
```

Python juga menyediakan cara yang lebih gampang dalam membuat kodingan diatas
dari yang kita buat dengan cara menambahkan simbol ``@``

```python
@dekorator_huruf_kecil
def kata():
    return "BELLSHADE"
kata()
```

## Aplikasikan dekorator yang banyak dalam satu fungsi

Kita bisa menggunakan decorator yang banyak dalam satu fungsi sebagai contoh:

sebelumnya kita sudah membuat dekorator yang bernama ``dekorator_huruf_kecil`` kali ini kita membuat kata menjadi dipecah menggunakan fungsi ``split()``

```python
def pecah_kata(kata_yang_mau_dipecah):
    def wrapper():
        kata = kata_yang_mau_dipecah()
        split_kata = kata.split()
        return split_kata
    return wrapper
```

dengan ini kita sudah ada 2 fungsi dekorator, kemudian kita bisa membuat contoh untuk memanggil keduanya dengan ``@``

```python
@dekorator_huruf_kecil
@pecah_kata
def kata():
    return "BELLSHADE"
```
