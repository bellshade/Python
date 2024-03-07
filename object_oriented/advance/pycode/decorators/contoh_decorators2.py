# Apabila melihat tanda backslash n (\n) itu tandanya kita bisa memotong panjang karakter dan dapat memberikan baris baru.
# Fungsi pertama kita buat dengan nama (kasar), yang hanya mengembalikan suatu nilai perubahan text.
def kasar(s):
  return s.upper()
  
# Fungsi kedua kita buat dengan nama (lembut), yang hanya mengembalikan suatu nilai perubahan text.
def lembut(s):
  return s.lower()
  
# Fungsi ketiga kita buat dengan nama (kalem), yang bertujuan untuk menampilkan isi nilai dari Fungsi sebelumnya.
def kalem(func):

  # Selanjutnya kita buat objek dengan nama (menyapa)
  menyapa = func('Halo Semua Sobat WPU!!!\nJangan lupa titik koma yaa (;)\nEh iya lupa... kalau ini program Python :-D\n')
  
  # Keluarkan nilai dari objek menyapa yang memberikan nilai didalam parameter func(...) keluar layar / konsol.
  print(menyapa)

# Setelah di rasa cukup, saatnya kita panggil fungsi kalem(), dan memasukkan kedua fungsi di atas sebagai parameter dari fungsi kalem().
kalem(kasar)
kalem(lembut)