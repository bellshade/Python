## Class (Kelas)

Kelas dapat diartikan sebagai kerangka untuk membuat suatu objek, membuat suatu kelas sama dengan membuat tipe baru, dan meng-inisialisasi tipe tersebut sama dengan menghasilkan objek baru.

Kelas memiliki atribut untuk mempertahankan nilainya, dan memilki metode untuk mengubah nilainya. Untuk membuat class di python dapat menggunakan keyword class.

# Atribut

Atribut adalah variable dan fungsi yang ada didalam kelas, seluruh atribut bersifat publik dan dapat diakses menggunakan tanda titik (.) dibelakang objek. Note: atribut yang diawali dengan `_` umumnya dianggap *private*; tidak dimaksudkan untuk digunakan di luar kelas.

# Metode 

Metode adalah fungsi yang dibuat didalam kelas, karena metode adalah fungsi maka untuk membuatnya menggunakan keyword def.

Ada 3 jenis metode class, yaitu:

- instance method

metode ini harus memiliki parameter self, yang berguna untuk mengakses atribut objek, untuk menggunakannya harus melalui objek.

- classmethod

metode ini menggunakan deokrator @classmethod dan harus memiliki parameter clf, yang berguna untuk mengakses atributnya, untuk menggunakannya dapat langsung dari kelasnya tanpa menggunakan objek.

- staticmethod

metode ini menggunakan dekorator @staticmethod, metode ini sama seperti classmethod namun tidak perlu menggunakan parameter wajib

## Konstruktor dan Destruktor

- konstruktor

Konstruktor adalah metode yang dipanggil saat membuat suatu objek, konstruktor dapat berguna untuk meminta atribut apa saja yang diperlukan saat membuat objek. Membuat konstruktor dapat menggunakan dunder-method init dan harus memiliki parameter self, juga dapat memiliki parameter tambahan.

- destruktor

Destruktor adalah metode yang dipanggil saat suatu objek dihapus, untuk membuat destruktor dapat menggunakan dunder-method del dan memiliki parameter self.