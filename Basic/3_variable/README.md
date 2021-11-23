# Variabel

Variabel adalah referensi dari sebuah value yang ingin dipanggil. Penggunaan variabel akan sangat mudah dikarenakan untuk menampilkan sebuah angka, dan huruf. Contoh penggunaan variabel pada Python:

```python
angka_saya = 100
print(angka_saya)
```

Kode di atas kita membuat sebuah variabel yang mereferensikan sebuah nilai angka berupa ``100`` dan dengan penggunaan dari variabel kita bisa memanggil lebih dari sekali:

```python
angka_saya = 20
print(angka_saya)
print(angka_saya)
```

## Assign variabel

Kita bisa assing variable dengan variabel lainnya agar mudah unduk mendklarasikan sebuah nilai yang sama dengan variabel yang berbeda sebagai contoh:

```python
angka_saya = 200
angka_lain = angka_saya
print(angka_saya)
print(angka_lain)
```
Maka program akan menampilkan:
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

Contoh pada String:
```python
nama = "adams"
print(nama)
```

## Peraturan penamaan dalam variabel pada Python

Python memiliki beberapa peraturan dalam penulisan sebuah variabel agar mengikuti standar dari Python dengan persayaratan dalam membuat variabel adalah:

1. Menggunakan kata tanpa didahuli dengan angka
    
    **contoh benar:**
    ```python
    nama = "bob"
    ```
    **contoh salah:**
    ```python
    1nama = "bob"
    ```
2. Menggunakan underscore (garis bawah) jika ingin menggunakan kata yang panjang

    **contoh yang benar:**
    ```python
    angka_saya = 12
    ```
    **contoh yang salah:**
    ```python
    12angka_saya = 12
    ```
3. Variabel pada python bersifat sensitif, penggunaan huruf besar dan kecil sangat diperhatikan

    contoh:
    ```python
    Nama_saya = "james"
    nama_saya = "james"
    ```
    Contoh diatas akan menghasilkan 2 nama karena variabel tersebut secara kalimat sama tapi secara penulisan berbeda, Python memperhatikan hal ini.

Pada Python penggunaan variabel disarankan menggunakan ``snake_case`` untuk mengikuti style bawaan dari Python.

[Materi Selanjutnya](../4_operator)
