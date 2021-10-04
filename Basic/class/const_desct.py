class Warung:
    # Konstruktor
    # Konstruktor adalah metode yang dipanggil saat membuat suatu objek,
    # konstruktor dapat berguna untuk meminta atribut apa saja yang
    # diperlukan saat membuat objek. Membuat konstruktor dapat menggunakan
    # dunder-method init dan harus memiliki parameter self,
    # juga dapat memiliki parameter tambahan.
    def __init__(self, owner, alamat):
        self.owner = owner
        self.alamat = alamat
        self.menu = []

    # Destruktor
    # Destruktor adalah metode yang dipanggil saat suatu objek dihapus,
    # untuk membuat destruktor dapat menggunakan dunder-method del dan
    # memiliki parameter self.
    def __del__(self):
        print(
            'Warung dihapus, data terakhir warung:',
            self.data()
        )

    def tambah_menu(self, makanan):
        """
        metode ini berfungsi untuk menambahkan data
        ke atribut menu_makanan
        makanan = string
        """
        self.menu.append(makanan)

    def data(self):
        """
        metode ini berfungsi untuk mengembalikan data
        seluruh atribut warung dalam bentuk dict.
        """
        return {
            'alamat warung' : self.alamat,
            'owner' : self.owner,
            'menu' : self.menu
        }


# membuat objek dan meng-inisialisasi-nya
kedai_atuk = Warung(
    owner='Atuk Daka',
    alamat='Jl. Apel No. 23'
)

# mengakses metode tambah_menu untuk menambahkan menu
kedai_atuk.tambah_menu('kopi susu')
kedai_atuk.tambah_menu('roti bakar')

# mengakses metode data untuk melihat data warung
data_kedai_atuk = kedai_atuk.data()
print(data_kedai_atuk)
# output: {'alamat warung': 'Jl. Apel No. 23',
#          'owner': 'Atuk Daka',
#          'menu': ['kopi susu', 'roti bakar']}

# menghapus objek warung
del kedai_atuk
# output: Warung dihapus, data terakhir warung:
# {'alamat warung': 'Jl. Apel No. 23',
#  'owner': 'Atuk Daka',
#  'menu': ['kopi susu', 'roti bakar']}
