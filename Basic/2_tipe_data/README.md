## Tipe Data

Dalam pemograman, tipe data adalah salah satu konsep yang sangat penting, dalam pemograman variabel dapat memberikan beberapa tipe data value yang sangat berguna dalam menentukan hasil dan operasi pada pemograman, tipe data melingkupi:

- Berupa text
    
    - ``str``

        Merupakan salah satu tipe data yang berupa string, berfungsi untuk menghasilkan tipe data string seperti huruf abjad atau simbol lain.
        ```python
        nama_saya = "franklin"
        email_saya = "benjamin@franklin"
        ```

- Berupa angka

    - ``int``

        Merupakan salah satu tipe numerik yang sering dipakai dalam pemograman, yang berupa bilangan bulat.
        ```python
        angka_saya = 25
        tahun_lahir = 1945
        ```

    - ``float``

        Merupakan salah satu tipe numerik yang menghasilkan berupa bilangan pecahan, sangat berguna dalam menghasilkan nilai secara detail.
        ```python
        nilai_saya = 95.281724
        nilai_teman = 30.25912
        ```

    - ``complex``

        Merupakan salah satu tipe data numerik yang berfungsi menghasil sebuah angka complex, contoh angka complex bisa dilihat [disini](https://id.wikipedia.org/wiki/Bilangan_kompleks).
        ```python
        angka_kompleks_saya = complex(1.5)
        angka_teman_saya = complex(2j)
        ```
    
- Berupa urutan (sekuensial)

    - ``list``

        Tipe data list adalah tipe data koleksi yang berisi beberapa value yang terdapat dalam satu variabel. List menggunakan kurung kotak.
        ```python
        nama_siswa = ['woody', 'buzz', 'andy']
        nilai_siswa = [12, 13, 14]
        ```

    - ``tuple``

        Tipe data tuple adalah tipe data koleksi yang berisi beberap value yang terdapat dalam satu variabel. Perbedaan diantara keduanya adalah:
        
        - tipe data tuple jika diberi value, maka tipe data tersebut tidak dapat diubah kembali
        - tipe data tuple menggunakan tutup kurung biasa ``()``
        
        ```python
        nama_siswa = ('buzz', 'andy', 'woody')
        nilai = (12, 13, 14)
        ```

    - ``set``

        Tipe data set adalah tipe data koleksi yang elemennya dapat dirubah, tidak terurut, dan bersifat unik. Sesuai dengan namanya, tipe data set memiliki operasi matematika himpunan seperti gabungan, irisan, selisih, dan lain-lain. Set menggunakan kurung kurawal ``{}``

        ```python
        nama_siswa = {'buzz', 'andy', 'woody'}
        nilai = {12, 13, 14}
        ```

    - ``frozenset``
        
        Tipe data frozenset adalah tipe data koleksi yang mirip dengan set, yang membedakannya dengan set adalah elemen pada frozenset tidak dapat dirubah setelah frozenset dibuat.

        ```python
        nama_siswa = frozenset(['woody', 'buzz', 'andy'])
        nilai = frozenset([12, 13, 14])
        ```

- Berupa map (kata kunci, dictionary)

    - ``dict``

        Tipe data dict atau dictionary adalah tipe data array dimana kunci atau __key__ dari array bisa berbentuk string, dan angka.
        ```python
        hari = {
            "sen": "senin",
            "sel": "selasa",
            "rab": "rabu"
        }
        ```

- Berupa tipe data binary (bytes, bytearray, memmoryview)

    - ``bytes``
    
        Merupakan sebuah object tipe data yang berisikan array tunggal.
        ```python
        angka_saya = bytes(12)
        angka_saya1 = bytes(300)
        ```
    
    - ``bytearray``
    
        Merupakan seubah object tipe data yang berisikan array byte tunggal yang tidak dapat dirubah.
        ```python
        angka_saya = bytearray(12)
        ```
    
    - ``memoryview``
    
        Memoryview adalah cara aman untuk mengekspos protokol buffer dengan python. ini memungkinkan untuk mengakses buffer internal suatu objek dengan membuat objek tampilan.

        Memoryview mengambalikan fungsi tampilan memori daripada objek yang diberikan.
        ```python
        angka_saya = memoryview(bytes(12))
        angka_saya1 = memoryview(bytes(1212))
        ```
