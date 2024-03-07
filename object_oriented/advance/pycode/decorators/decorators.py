# bellshade function: fungsi ini akan kita jadikan sebagai decorators function
def bellshade(func):
  x = 'Belajar Membuat Website' # <- Variable x: agar di cetak didalam fungsi (wrap)
  
  def wrap():
    print('Selamat datang di ruang Bellshade.')
    print('bersama narasumber:', end='') # <- end="": agar keluar ke konsol hanya satu baris sejajar dengan parameter fungsi (bellshade)
    func() # <- Space func dari parameter fungsi (bellshade)
    print(f'Dalam rangka: {x}\nDieksekusi dari fungsi: {func.__name__}') # <- Mencetak Variable dari fungsi (bellshade) 
  
  return wrap # <- Mengembalikan fungsi (wrap) sebagai fungsi terdalam (bellshade)
  
# ----------| Cara Penggunaan Decorators |---------- #

# Cara memanggil fungsi (wrap & bellshade)
@bellshade
def wpu():
  print('Web Programming UNPAS!')

wpu()