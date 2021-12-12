# Inheritance dengan python

Inheritance/pewarisan adalah salah satu dari konsep Object Oriented Programming yang membahas mengenai bagaimana suatu kelas bisa menggunakan atribut dan fungsi dari kelas yang lain, penggunaan atribut dan fungsi ini bersifat 'mewarisi'. Manfaatnya adalah dari keterhubungan antar kelas ini kita dapat mengetahui kegunaan suatu kelas atas kelas yang lain dan sebagainya.

Konsep Inheritance/pewarisan juga berhubungan dengan konsep abstract class. Abstract class adalah kelas yang tidak memiliki implementasi pada method-nya dalam kata lain method-nya bersifat abstrak, sehingga kelas turunannya yang harus mengimplementasikan method tersebut. Contoh kelas abstrak: kelas Mobil yang memiliki atribut "nama" dan "jenis", lalu memiliki method "akselerasi"

Berikut contoh dari konsep Inheritance/pewarisan: Terdapat sebuah kelas mobil Civic yang memiliki property seperti berikut: 
nama = "Honda Civic"
jenis = "Sedan"

Lalu memiliki method seperti berikut:
- akselerasi 0-100 km/jam membutuhkan waktu selama 10 detik

kita dapat membuat mobil yang lebih baik performanya dengan menggunakan blueprint yang sudah ada di atas dengan menambah kemampuannya sehingga kemampuan akselerasinya menjadi 7 detik, misalkan seperti berikut:
nama = "Honda Civic Type R"
jenis = "Sedan"

Lalu memiliki method seperti berikut:
- akselerasi 0-100 km/jam membutuhkan waktu selama 7 detik

Contoh kelas abstrak:
```python
class Mobil:
    def __init__(self):
        self.nama = None
        self.jenis = None

    def akselerasi:
        pass
```

Contoh pada program seperti berikut (parent class):
```python
class Civic:
    def __init__(self):
        super().__init__()
        self.nama = "Honda Civic"
        self.jenis = "Sedan"
    
    def akselerasi(self):
        print("Akselerasi 0-100 KM/Jam dalam 10 detik! NGENGGG~")
```

Versi mobil yang lebih baik (child class):
```python
class CivicTypeR(Civic):
    def __init__(self):
        super().__init__()
        self.nama = "Honda Civic Type R"
    
    def akselerasi(self):
        print("Akselerasi 0-100 KM/Jam dalam 7 detik! BRRMMM~")
```

Perhatikan pada kelas CivicTypeR, atribut nama dan method akselerasi() diganti valuenya sedangkan property jenis tidak diganti karena CivicTypeR masih merupakan mobil berjenis sedan.

```super().__init__()``` digunakan untuk mewarisi semua yang ada pada kelas induknya.

materi selanjutnya: [polimorfisme](../polimorfis)
