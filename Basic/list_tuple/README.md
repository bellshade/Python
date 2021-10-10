## list
list digunakan untuk menyimpan data yang banyak dengan hanya satu variable, list menggunakan square bracket atau kurung petak, contoh.
```python
nama_hewan = ["sapi", "gajah", "ayam", "bebek"]
print(nama_hewan)
```
list memiliki index, index dimulai dari 0, dan index kedua dimulai dari angka 1

kelebihan antara dari list adalah

- bisa dirubah
    list bisa dirubah dengan dengan cara
    ```python
    nama_hewan = ["sapi", "gajah", "ayam", "bebek"]
    nama_hewan[1] = "kucing"
    print(nama_hewan)
    ```
- menerima duplikasi
    list juga duplikasi item, sebagai contoh
    ```python
    nama_hewan = ["ikan", "singa", "ikan", "sapi"]
    print(nama_hewan)
    ```

## tuple
list digunakan untuk menyimpan data yang banyak dengan menggunakan satu variabel. tuple menggunakan round bracket atau kurung bulat, tuple adalah salah satu tipe data yang **tidak dapat dirubah**,contoh.
```python
nama_hewan = ("ikan", "gajah", "sapi", "paus")
print(nama_hewan)
```

buat tuple dengan hanya satu item di dalamnya, jangan lupa menggunakan koma
```python
nama_hewan = ("sapi",)
print(nama_hewan)
```
