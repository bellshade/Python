siswa = ['beni', 'budi', 'andi', 'julian', 'karim', 'toni']

cariSiswa = input("Masukan nama siswa yang dicari : ")

i = 0
while i < len(siswa):
    if cariSiswa == siswa[i] :
        print("Siswa yang dicari ketemu di index ke -", i)
        break

    print("bukan", siswa[i])
    i += 1

print("nama siswa yang dicari tidak ditemukan :(")
    
