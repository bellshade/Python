# Mempelajari Magic Mathod Python

# Membuat class dengan nama Pastikom, dengan memiliki 2 parameter yakni yourname & email.
class Pastikom:
  
  # Mendefinisikan fungsi __init__ atau menginisialisasikan untuk bertujuan agar class Pastikom dapat menerima input dengan 2 parameter [yourname & email]
  def __init__(self, yourname, email):
    self.name = yourname
    self.email = email
  
  # Mendefinisikan sebuah fungsi __repr__ yang bertujuan sebagai merepresentasikan hasil keluaran dari rangkaian yang sudah kita susun pada parameter
  def __repr__(self):
    return f'Class: {__class__}\n\tparameter[name]: {self.name}\n\t\tparameter[email]: {self.email}'
   
  # Mendefinisikan sebuah fungsi __del__ yang bertujuan untuk memberikan informasi jika ada yang terhapus di salah satu instance pada object
  def __del__(self):
    print(f'\nOh tidaaaak!\nYang kamu masukan dengan nama:{self.name} & \nemail:{self.email} sudah terhapus :\'(')

# Membuat object user1 dari Class Pastikom
user1 = Pastikom('Bellshade', 'Bellshade@Pastikom')
# Membuat object user1 dari Class Pastikom
user2 = Pastikom('TomsDroid', 'tomsdroid@Pastikom')


# Menampilkan value object user1 dari Class Pastikom
print(user1)
# Menghapus value object user1 dari Class Pastikom
del(user2)