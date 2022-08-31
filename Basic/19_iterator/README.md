# Iterator

Iterator adalah objek yang berisi sesuatu yang bisa dihitung atau *iterable*.

Objek *iterable* adalah String, List, Tuple, Set, Dictionary.

contoh dari penggunaan iterator:
```py
nama_maintainer = ("majed", "permen", "kelvin", "hen")
show = iter(nama_maintainer)
print(next(show))
print(next(show))
print(next(show))
print(next(show))
```

menggunakan `__iter__()`
```py
class AngkaSaya:
  def __iter__(self):
    self.angka = 1
    return self

  def __next__(self):
    nomor = self.angka
    self.angka += 1
    return nomor

kelas_angka = AngkaSaya()
test_iter = iter(kelas_angka)

print(next(test_iter))
print(next(test_iter))
print(next(test_iter))
```

untuk lebih jelasnya kamu bisa lihat [disini](iterator.py)

[Materi Selanjutnya](../20_lambda)