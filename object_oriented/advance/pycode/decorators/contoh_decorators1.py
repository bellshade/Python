# Buatlah fungsi dengan nama apapun yang kamu inginkan, pada contoh pertama kita akan memberikan fungsi dengan nama menyapa.
def menyapa(s1):

  # Fungsi ini tidak memiliki keluaran / output di konsol, dan hanya mengembalikan nilai.
  return s1.upper()
  
# Mencetak isi nilai dari fungsi tanpa objek.
print(menyapa('halo semua sobat WPU!!!'))

# Berikan nama objek sesuai keinginan dan kebutuhan, disini kita akan memberikan nama objeknya yaitu (user)
user = menyapa

# Untuk memanggil fungsi di dalam objek yang telah kita definisikan bersama, kita hanya perlu menambahkan tanda kurung setelah nama objek. contoh: user([nilai])
user('halo semua sobat WPU!!!')

# Maka secara otomatis fungsi belajar didalam objek user yang bernilaikan Python akan muncul di konsol.
# >>> HALO SEMUA SOBAT WPU!!!