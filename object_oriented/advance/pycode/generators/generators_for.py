# Generators
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