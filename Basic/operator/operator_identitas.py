"""
Operator Identitas adalah operator yang digunakan untuk cek 
apakah nilai dari suatu varibel berada pada memori yang sama atau tidak

contoh:
"""

# variabel
x = "Python"
y = "Cobra"
z = "Python"
list_ular1 = ["Python", "Cobra", "Sanca"]
list_ular2 = ["Python", "Cobra", "Sanca"]


# cek apakah nilai dari variabel x dan y ada pada memori yang sama 
print("x is y = ", x is y) # False

# cek apakah nilai dari variabel x dan z ada pada memori yang sama 
print("x is z = ", x is z) # True

# cek apakah nilai dari variabel list_ular1 dan list_ular2 ada pada memori yang sama
print("list_ular1 is list_ular2 = ", list_ular1 is list_ular2) # False
print("\n")

# cek apakah nilai dari variabel list_ular1 dan list_ular2 tidak pada memori yang sama
print("x is not y = ", x is not y) # True

# cek apakah nilai dari variabel list_ular1 dan list_ular2 tidak pada memori yang sama
print("x is not z = ", x is not z) # False

# cek apakah nilai dari variabel list_ular1 dan list_ular2 tidak pada memori yang sama 
print("list_ular1 is list_ular2 = ", list_ular1 is not list_ular2) # True

