# openseries function: fungsi ini akan kita jadikan sebagai decorators function
def openseries(func):
  def wrap(*args, **kwargs):
    print('OpenSeries: Matematika Dasar.')
    return_val = func(*args, **kwargs) # <- Space func dari parameter fungsi (openseries)
    print(f'Dieksekusi dari fungsi: {func.__name__}') # <- Mencetak nama dari fungsi (add) 
    return return_val
  
  return wrap # <- Mengembalikan fungsi (wrap) sebagai fungsi terdalam (openseries)
  
# ----------| Cara Penggunaan Decorators Yang  Argumen Parameter |---------- #

# Cara memanggil fungsi (wrap & openseries)
@openseries
def add(a,b):
  print(f'Fungsi penjumlahan dari {a} + {b} = {a + b}') # <- Fungsi print ini akan muncul di dalam fungsi (wrap) didalam fungsi (openseries)
  return f'Hasil dari parameter a & b ({a} + {b} = {a + b})'

print(add(5,9))