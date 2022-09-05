# Variabel

Variabel adalah referensi dari sebuah value. Contoh penggunaan variabel pada Python:

```python
angka_saya = 100
print(angka_saya)
```

Pada kode diatas, kita membuat sebuah variabel yang mereferensikan nilai angka ``100``. Dengan penggunaan dari variabel kita bisa memanggil lebih dari sekali, misalnya:

```python
angka_saya = 20
print(angka_saya)
print(angka_saya)
```

## Assign variabel

Kita bisa assing variable dengan variabel lainnya agar mudah untuk mendeklarasikan sebuah nilai yang sama dengan variabel yang berbeda, sebagai contoh:

```python
angka_saya = 200
angka_lain = angka_saya
print(angka_saya)
print(angka_lain)
```

Akan menghasilkan:

```
200
200
```

Atau bisa juga dengan cara:

```python
angka_saya = angka_lain = angka_banyak = 200
print(angka_saya)
print(angka_lain)
print(angka_banyak)
```

Contoh pada string:

```python
nama = "adams"
print(nama)
```

## Peraturan penamaan variabel pada Python

Python memiliki beberapa peraturan dalam penulisan sebuah variabel. Peraturan tersebut adalah:

1. Menggunakan kata tanpa didahuli dengan angka:

    **contoh benar**
    ```python
    nama = "bob"
    ```
    **contoh salah**
    ```python
    1nama = "bob"
    ```
2. Menggunakan underscore (garis bawah) jika ingin menggunakan kata yang panjang:

    **contoh yang benar**
    ```python
    angka_saya = 12
    ```
    **contoh yang salah**
    ```python
    12angka_saya = 12
    ```
3. Variabel pada python bersifat sensitif, penggunaan huruf besar dan kecil sangat diperhatikan:

    contoh
    ```python
    Nama_saya = "james"
    nama_saya = "james"
    ```
    contoh diatas akan menghasilkan 2 nama karena variabel tersebut secara kalimat sama tapi secara penulisan berbeda, Python memperhatikan hal ini.

Pada Python, penggunaan variabel disarankan menggunakan ``snake_case``.

## Keywords yang tidak bisa digunakan pada python

Ada beberapa kata yang dilarang untuk digunakan sebagai nama variabel. Contoh penggunaan kata yang dilarang pada Python:

```python
class sma_saya = "bahasa"
print(sma_saya)
```

Hasil esekusi diatas akan menyebabkan error karena ``class`` merupakan salah satu nama fungsi dari Python.

Kata/keywords yang dilarang:

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

video penjelasan tentang variabel = [Belajar python dasar - mengenal variabel](https://www.youtube.com/watch?v=gxmTFXfrMzk&list=PLZS-MHyEIRo59lUBwU-XHH7Ymmb04ffOY&index=5)

[Materi Selanjutnya](../04_operator)
