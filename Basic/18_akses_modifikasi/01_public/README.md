# public modifier

Anggota kelas yang dideklarasikan publik mudah diakses dari bagian mana pun dari program. Semua anggota data dan fungsi anggota kelas bersifat publik secara default.

```python
class NamaSaya:
    def __init__(self, nama, umur):
        self.nama_saya = name
        self.umur_saya = umur

    def tampil_nama(self):
        print(f"Apa kabar {self.nama_saya}")

objek_kelas = NamaSaya("yoga", 31)
objek_kelas.tampil_nama()
print("Umur saya adalah ", objek_kelas.umur_saya)
```

Dalam program di atas, ``nama_saya`` dan ``umur_saya`` adalah anggota data publik dan metode ``tampil_nama()`` adalah fungsi anggota publik dari kelas ``NamaSaya``. Data anggota kelas ``NamaSaya`` ini dapat diakses dari mana saja dalam program.

[Materi Selanjutnya](../02_private)