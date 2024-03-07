# Generators

Generators: Alat atau sumber daya yang akan menghasilkan jenis kode atau bahasa pemrograman komputer tertentu.

Dengan generator juga kita bisa membuat apapun baik itu Fake EmailDNS, User Fullname, HEX to RGB, dan masih banyak yang lainnya.

## Cara membuat kode generator sederhana

Kita bisa membuat angka acak mulai dari sekian ke sekian yang di kuadratkan berapapun nilai yang kita inginkan untuk di hasilkan.

### Membuat Generators dengan For

```py
# Generators For
# import terlebih dahulu module yang kita butuhkan
import os, sys, time

# Buatlah kelas dengan nama (Generators)
class Generators():
  # Disini kita akan membuat fungsi inisialisasi, agar kelas yang kita buat dapat memiliki argumen parameter
  def __init__(self, input_usr : int) -> None :
    self.user = int(input_usr)

  # Buatlah fungsi untuk mengenerate angka secara random
  def start(self):
    time.sleep(1)
    if sys.platform != 'linux':
      os.system('cls')
    else:
      os.system('clear')
    print('Nama Program:',Generators.__name__)
    print('Generators akan segera di mulai')
    time.sleep(2)
    for i in range(5,self.user):
      print('=> ',i**50)
      time.sleep(1)
    
    print(f'Memory yang di gunakan: {sys.getsizeof(i)} bytes')
# Instansiasikan kelas yang sudah di definisikan ke dalam variable agar menjadi object
app = Generators('20')

if __name__ == '__main__':
  app.start()
```

### Membuat Generators dengan While

```py
# Generators While
# import terlebih dahulu module yang kita butuhkan
import os, sys, time
# Buatlah kelas dengan nama (Generators)
class Generators_While():
  """
  Menambahkan satu parameter pada kelas (Generators_While) yang akan di konversikan ke tipe data integer atau number
  >>> Generators_While(5, infite_loop=False)
  secara default nilai dari keyword max_loop adalah 5, jika ingin di ubah silahkan ubah dengan angka yang di inginkan.
  [1] 25 => 125
  [2] 125 => 625
  [3] 625 => 3125
  [4] 3125 => 15625
  [5] 15625 => 78125
  """
  # Disini kita akan membuat fungsi inisialisasi, agar kelas yang kita buat dapat memiliki argumen parameter
  def __init__(self, input_usr : int, max_loop : int = 5, infite_loop : bool = False) -> None :
    self.user = int(input_usr)
    self.loop = int(max_loop)
    self.infite = int(infite_loop)
  # Buatlah fungsi untuk mengenerate angka secara random
  def start(self):
    time.sleep(1)
    if sys.platform != 'linux':
      os.system('cls')
    else:
      os.system('clear')
    print(f'Nama Program: {Generators_While.__name__}')
    print('Catatan: Jika kamu memilih infite_loop dan ingin menghentikan generator ini tekan [ctr + z]')
    time.sleep(.5)
    index, count = 0, self.user
    while True:
      try:
        index += 1
        count *= self.user
        result = self.user * count
        time.sleep(1)
        print(f'\033[0;32m\t[{index}] {count} => {result}')
        if self.infite:
          pass
        else:
          if index == self.loop:
            break
      except KeyboardInterrupt:
        print('\033[0;34m [INFO] Tekan [ctr + z] untuk menghentikan generator')
# Instansiasikan kelas yang sudah di definisikan ke dalam variable agar menjadi object
app = Generators_While('5',)
if __name__ == '__main__':
  app.start()
```