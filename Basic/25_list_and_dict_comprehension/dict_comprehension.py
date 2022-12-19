# Dictionary comprehension adalah
# Sebuah metode atau cara untuk membuat dictionary menggunakan for loop

# Syntax Dictionary Comprehension
# {key : value for vars in iterable}

# Kelebihan menggunakan Dictionary Comprehension adalah
# mampu menulis koding dengan elegan

# Membuat Dictionary
# contoh bisa dilakukan dengan membuat terlebih dahulu
# dengan membuat variabel dengan fungsi ``dict()``
# angka = dict()

# Basic Dict Comprehension
angka = {nilai: nilai * 2 for nilai in range(1, 6)}
print("Angka : ", angka)
# Output = Angka :  {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}

# Contoh lainnya pada Dict Comprehension
pangkat = {key * 2: value**2 for (key, value) in angka.items()}
print("Pangkat Dua: ", pangkat)
# Output = Pangkat Dua:  {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# Implementasi Dict Comprehension Dengan If Else
ten_nums = {value: value * 2 for value in range(1, 11)}
genap_only = {key: value for (key, value) in ten_nums.items() if key % 2 == 0}
print("Genap Only : ", genap_only)
# Output = Genap Only :  {2: 4, 4: 8, 6: 12, 8: 16, 10: 20}

# Implementasi Dict Comprehension Dengan If Else
age_name = {"Ronaldo": 37, "Messi": 34, "Greenwood": 20, "Sancho": 21}
status_umur = {
    nama: ("Tua" if umur > 30 else "Muda") for (nama, umur) in age_name.items()
}
print(status_umur)
# Output = {'Ronaldo': 'Tua', 'Messi': 'Tua', 'Greenwood': 'Muda', 'Sancho': 'Muda'}
