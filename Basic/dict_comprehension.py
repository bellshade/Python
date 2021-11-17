# Dictionary comprehension adalah
# Sebuah metode atau cara untuk membuat dictionary menggunakan for loop

# Syntax Dictionary Comprehension
# {key : value for vars in iterable}

# Kelebihan menggunakan Dictionary Comprehension adalah mampu menulis koding dengan elegan

# Membuat Dictionary
angka = dict()

# Basic Dict Comprehension
angka = {nilai: nilai * 2 for nilai in range(1, 6)}
print("Angka : ", angka)

# Contoh lainnya pada Dict Comprehension
pangkat = {key * 2: value ** 2 for (key, value) in angka.items()}
print("Pangkat Dua: ", pangkat)

# Implementasi Dict Comprehension Dengan If Else
ten_nums = {value: value * 2 for value in range(1, 11)}
genap_only = {key: value for (key, value) in ten_nums.items() if key % 2 == 0}
print("Genap Only : ", genap_only)

# Implementasi Dict Comprehension Dengan If Else
age_name = {"Ronaldo": 37, "Messi": 34, "Greenwood": 20, "Sancho": 21}
status_umur = {
    nama: ("Tua" if umur > 30 else "Muda") for (nama, umur) in age_name.items()
}
print(status_umur)
