= int(input("Angka1 : "))
y= int(input("Angka2 : "))

def tambah(x,y):
   return x+y

def kurang(x,y):
   return x-y

def kali(x,y):
   return x*y

def bagi(x,y):
   return x/y

print("\nHasil Penjumlahan : %d" %tambah(x,y))
print("Hasil Pengurangan : %d" %kurang(x,y))
print("Hasil Perkalian : %d" %kali(x,y))
print("Hasil Pembagian : %d" %bagi(x,y))
