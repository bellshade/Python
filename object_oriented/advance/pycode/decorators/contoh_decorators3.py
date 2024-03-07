# Kita buat fungsi terluar dengan nama (users)
def users(nama):

  # Saatnya kita buat fungsi didalam fungsi ddngan nama (belajar)
  def belajar(s):
    
    # Return ini mengembalikan nilai untuk fungsi (belajar)
    return f'username: {nama}\nsedang belajar: {s}'
  
  # Di return terluar, kita akan mengembalikan nilai berupa fungsi (belajar)
  return belajar
  
# Buatlah objek sesuai keinginan, dan berikan nilai fungsi (users) didalam objek.
s1 = users('bellshade')

# Cetak objek yang sudah di definisikan, yang di ikuti dengan tanda kurung ().
print(s1('Fullstack'))