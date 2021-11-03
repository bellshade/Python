# variabel

variabel adalah referensi dari sebuah value yang ingin dipanggil.penggunaan variabel akan sangat mudah dikarenakan untuk menampilkan sebuah angka, dan huruf, contoh penggunaan variabel pada python

```python
angka_saya = 100
print(angka_saya)
```

kode diatas kita membuat sebuah variabel yang mereferensikan sebuah nilai angka berupa ``100`` dan dengan penggunaan dari variabel kita bisa memanggil lebih dari sekali

```python
angka_saya = 20
print(angka_saya)
print(angka_saya)
```

## assign variabel

kita bisa assing variable dengan variabel lainnya agar mudah unduk mendklarasikan sebuah nilai yang sama dengan variabel yang berbeda sebagai contoh

```python
angka_saya = 200
angka_lain = angka_saya
print(angka_saya)
print(angka_lain)
```
maka program akan menampilkan
```
200
200
```
atau bisa juga dengan cara
```python
angka_saya = angka_lain = angka_banyak = 200
print(angka_saya)
print(angka_lain)
print(angka_banyak)
```

contoh pada string
```python
nama = "adams"
print(nama)
```

## peraturan penamaan dalam variabel pada python

python memiliki beberapa peraturan dalam penulisan sebuah variabel agar mengikuti standar dari python dengan persayaratan dalam membuat variabel adalah

1. menggunakan kata tanpa didahuli dengan angka
    
    **contoh benar**
    ```python
    nama = "bob"
    ```
    **contoh salah**
    ```python
    1nama = "bob"
    ```
2. menggunakan underscore (garis bawah) jika ingin menggunakan kata yang panjang

    **contoh yang benar**
    ```python
    angka_saya = 12
    ```
    **contoh yang salah**
    ```python
    12angka_saya = 12
    ```
3. variabel pada python bersifat sensitif, penggunaan huruf besar dan kecil sangat diperhatikan

    contoh
    ```python
    Nama_saya = "james"
    nama_saya = "james"
    ```
    contoh diatas akan menghasilkan 2 nama karena variabel tersebut secara kalimat sama tapi secara penulisan berbeda, python memperhatikan hal ini.

pada python penggunaan variabel disarankan menggunakan ``snake_case`` untuk mengikuti style bawaan dari python