# Inheritance dengan python

Inheritance/pewarisan adalah salah satu dari konsep Object Oriented Programming yang membahas mengenai bagaimana suatu kelas bisa menggunakan atribut dan fungsi dari kelas yang lain, penggunaan atribut dan fungsi ini bersifat 'mewarisi'. Manfaatnya adalah dari keterhubungan antar kelas ini kita dapat mengetahui kegunaan suatu kelas atas kelas yang lain dan sebagainya.

Contohnya seperti ini: Terdapat blueprint sebuah mobil yang memiliki property seperti: 
nama = "Honda Civic"
warna = "Hitam"
jenis = "Sedan"
ukuran ban = "18 Inci". 

Lalu memiliki method seperti:
- akselerasi 0-100 km/jam membutuhkan waktu selama 10 detik

kita dapat membuat mobil yang lebih baik performanya dengan menggunakan blueprint yang sudah ada di atas dengan sedikit menambah kemampuan akselerasinya menjadi 7 detik, misalkan.
nama = "Honda Civic Type R"
warna = "Putih"
jenis = "Sedan"
ukuran ban = "20 Inci". 

Lalu memiliki behaviour seperti:
- akselerasi 0-100 km/jam membutuhkan waktu selama 7 detik

Contoh pada program seperti berikut (parent class):
```python
class Civic:
    def __init__(self):
        self.nama = "Honda Civic"
        self.warna = "Hitam"
        self.jenis = "Sedan"
        self.ukuran_ban = "20 Inci"
    
    def akselerasi(self):
        print("Akselerasi 0-100 KM/Jam dalam 10 detik! NGENGGG~")
```

Versi mobil yang lebih baik (child class):
```python
class CivicTypeR(Civic):
    def __init__(self):
        super().__init__()
        self.nama = "Honda Civic Type R"
        self.warna = "Putih"
        self.ukuran_ban = "20 Inci"
    
    def akselerasi(self):
        print("Akselerasi 0-100 KM/Jam dalam 7 detik! BRRMMM~")
```

Perhatikan pada kelas CivicTypeR, property seperti nama, warna, dan ukuran_ban, lalu method akselerasi() diganti valuenya sedangkan property jenis tidak diganti karena CivicTypeR masih merupakan mobil berjenis sedan.

```super().__init__()``` digunakan untuk mewarisi semua yang ada pada kelas induknya.