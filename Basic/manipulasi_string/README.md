# manipulasi string

pada python kita bisa merubah, dan memanipulasi string yang sudah ada agar sesuai dengan kebutuhan yang diinginkan


- mengakses salah satu karakter dari string

    ```python
    nama_saya = "zoelfikrie"
    print(nama_saya[0])
    ```

- menghitung semua karakter string

    ```python
    nama_saya = "athallamajed"
    print(len(nama_saya))
    ```

- menghitung jumlah suatu huruf dari karakter

    ```python
    nama_saya = "carl loghmatten"
    print(nama_saya.count("l"))
    ```

- menghitung jumlah spasi pada string

    ```python
    kalimat = "program belajar indonesia"
    print(kalimat.count(' '))
    ```

- memotong karakter

    ```
    kata = "indonesia programming"
    ```

    - mengambil karakter pertama dari string
        ```python
        print(kata[0])
        ```
    
    - mengambil 3 karakter dari string
        ```python
        priint(kata[0:3])
        ```
        ```python
        print(kata{:3})
        ```
    
    - mengambil 3 karakter terakhir dari string
        ```python
        print(kata[-3:])
        ```
    
- mengulang sebanyak dari string
    ```python
    # mengulang sebanyak 100 kali
    print("indonesia" * 100)
    ```

- mengubah kata dari string

    ```python
    kata = "belajar memasak"
    ubah = kata.replace("belajar", "pintar")
    print(ubah)
    ```

|sintaks       | penjelasan                             | contoh kode       |
|:--        | :--:                                      | :--               |
| ``uper()``| mengubah semua huruf menjadi kapital      | ``kata.upper()``  |
| ``lower()``| mengubah semua huruf menjadi kecil       | ``kata.lower()``  |
| ``title()``| mengubah setiap awalan kata kalimat menjadi kapital | ``kata.title()``|
| ``capitalize()`` | mengubah awalan huruf utama menjadi kapital | ``kata.capitalize()`` |
| ``swapcase()``| mengubah setiap awalan kata kalimat menjadi huruf kecil | ``kata.swapcase()``|

- membalikkan string

    ```python
    kata = "bellshade python"
    # cara pertama
    print(kata[::-1])
    # cara kedua
    print(' '.join(reversed(kata)))
    ```

- penggabungan string

    ```python
    kata = "memasak"
    print("saya belajar " + kata)
    ```
    
    - join
        menambahkan karakter di setiap karakter
        ```python
        kata = "indonesia"
        print("x".join(kata))
        ```

- pengecekan

    - ``kata.isalnum()``
        cek kata tersebut mengandung alphanumerik atau tidak
    
    - ``kata.isalpha()``
        cek kata tersebut mengandung alphabet
        
    - ``kata.isdigit()``
        cek apakah kata mengandung digit atau angka

    - ``kata.istitle()``
        cek apakah kata mengandung title atau tidak

    - ``kata.isupper()``
        cek apakah kata mengandung huruf kapital
    
    - ``kata.islower()``
        cek apakah kata mengandung kata huruf kecil
    
    - ``kata.isspace()``
        cek apakah kata mengandung spasi atau tidak

    - ``kata.endswith('karakter')``
        cek apakah kata mengandung karakter tersebut atau tidak pada akhir
    
    - ``kata.startswith('karakter')``
        cek apakah kata mengandung karakter terseub atau tidak pada awal