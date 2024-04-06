<p align="center">
  <img src="https://i.ibb.co/N1hgztf/magic-mathod.png" alt="Python Advance">
</p>

# Magic Method Python 

Magic Method adalah definisi / fungsi / method yang dimulai dan diakhiri dengan garis bawah 2x atau ganda '__'. Mereka ditentukan oleh kelas bawaan dalam Python dan biasanya digunakan untuk kelebihan beban operator. Disebut juga Dunder Method, Dunder di sini berarti “Double Under (Garis Bawah)”.

## Cara Penulisan Magic Method Python

```py
class Pastikom:

    def __init__(self, yourname : str, email : str) -> None:
        """Magic Method
        Kelas Pastikom memiliki 2 parameter dan/atau argumen
        :param yourname: tuliskan nama mu di parameter pertama
        :param email: tuliskan email mu di parameter ke dua
        nama = 'Bellshade'
        email = bellshade@pastikom.id
        >>> Pastikom(nama, email)
        Nama: Bellshade
        Email: bellshade@pastikom.id
        """
        self.name = yourname
        self.email = email

    def __repr__(self):
        """Fungsi representasi nilai parameter dan/atau argumen"""
        return f'Nama: { self.name }\nEmail: { self.email }'

    def __del__(self):
        """Fungsi informasi jika ada nilai parameter dan/atau argumen yang terhapus"""
        return "Oh tidaaaak! Data sudah terhapus :'("


nama : str = "Bellshade"
email : str = "bellshade@pastikom.id"
if __name__ == '__main__':
    Pastikom(nama, email)

```

Jika, Kamu ingin mencobanya sendiri melalui cmd / terminal untuk mendapatkan daftar atribut dari _**Magic Mathod**_ dengan Python, buka cmd atau terminal lalu ketik python3 untuk membuka interpreter Python, dan ketik kode berikut: `dir(int)`

Maka, akan muncul daftar atribut magic method seperti berikut:
```bash
>>> dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
```

### Di bawah ini adalah daftar Magic Method Python dan kegunaannya.

> Magic Mathod Initialization / Constructor

1. `__new__` = Dapat di gunakan didalam instansiasi pada suatu object
2. `__init__` = Dapat di panggil dengan method / fungsi `__new__`
3. `__del__` = Untuk memberi informasi jika ada salah satu instansiasi pada object terhapus (deconstructor)

> Magic Method Numeric

1. `__trunc__(self)` = Dapat di implementasikan pada `math.trunc()`
2. `__ceil__(self)` = Dapat di implementasikan pada `math.ceil()`
3. `__floor__(self)` = Dapat di implementasikan pada `math.floor()`
4. `__round__(self,n)` = Dapat di implementasikan pada built-in method `round()`
5. `__invert__(self)` = Dapat di implementasikan pada inversi menggunakan operator `~`
6. `__abs__(self)` = Dapat di implementasikan pada built-in method `abs()`
7. `__neg__(self)` = Menerapkan perilaku pada operator negasi
8. `__pos__(self)` = Menerapkan perilaku pada operator unary positif
 
> Magic Operator Aritmatika 

1. `__add__(self, other)` = Mengimplementasikan perilaku untuk `math.trunc()`
2. `__sub__(self, other)` = Mengimplementasikan perilaku untuk `math.ceil()`
3. `__mul__(self, other)` = Mengimplementasikan perilaku untuk `math.floor()`
4. `__floordiv__(self, other)` = Mengimplementasikan perilaku untuk putaran `round()`
5. `__div__(self, other)` = Mengimplementasikan perilaku inversi menggunakan operator `~`
6. `__truediv__(self, other)` = Mengimplementasikan perilaku untuk built-in `abs()`
7. `__mod__(self, other)` = Menerapkan perilaku untuk negasi
8. `__divmod__(self, other)` = Menerapkan perilaku untuk unary positif
9. `__pow__` = Mengimplementasikan perilaku eksponen menggunakan operator `**`
10. `__lshift__(self, other)` = Mengimplementasikan pergeseran bitwise kiri menggunakan operator `<<`
11. `__rshift__(self, other)` = Mengimplementasikan pergeseran bitwise kanan menggunakan operator `>>`
12. `__and__(self, other)` = Mengimplementasikan bitwise dan menggunakan operator `&`
13. `__or__(self, other)` = Mengimplementasikan bitwise atau menggunakan operator `|`
14. `__xor__(self, other)` = Mengimplementasikan xor bitwise menggunakan operator `^` (Tilde)

> Magic Method String

1. `__str__ (self)` = Mendefinisikan perilaku ketika str() dipanggil pada instance kelas
2. `__repr__(self)` = Untuk dipanggil dengan metode repr() bawaan untuk mengembalikan representasi tipe yang dapat dibaca mesin
3. `__unicode__(self)` = Method ini untuk mengembalikan string unicode dari suatu tipe
4. `__format__(self, formattr)` = Method ini mengembalikan gaya string baru
5. `__hash__(self)` = Ia harus mengembalikan bilangan bulat, dan hasilnya digunakan untuk perbandingan kunci cepat dalam kamus
6. `__nonzero__(self)` = Mendefinisikan perilaku ketika bool() dipanggil pada instance kelas
7. `__dir__(self)` = Method ini untuk mengembalikan daftar atribut suatu kelas
8. `__sizeof__( self)` = Method ini mengembalikan ukuran objek

> Magic Method Compasion (Perbandingan)

1. `__persamaan__(self, other)` = Mendefinisikan perilaku untuk operator kesetaraan `==`
2. `__ne__(self, other)` = Mendefinisikan perilaku untuk operator pertidaksamaan `!=`
3. `__lt__(self, other)` = Mendefinisikan perilaku untuk operator yang kurang dari `<`
4. `__gt__(self, other)` = Mendefinisikan perilaku untuk operator yang lebih besar dari `>`
5. `__le__(self, other)` = Mendefinisikan perilaku untuk operator yang kurang dari atau sama dengan `<=`
6. `__ge__(self, other)` = Mendefinisikan perilaku untuk operator yang lebih besar dari atau sama dengan `>=`