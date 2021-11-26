# Anagram adalah sebuah kata yang dapat
# membentuk kata lain/kalimat lain.
def anagramCheck(x, y):
    # Fungsi sort disini untuk mengurutkan huruf
    # Karena anagram harus memiliki huruf yang sama
    if sorted(x) == sorted(y):
        return "Anagram"
    else:
        return "Bukan Anagram"


print(anagramCheck("silent", "listen"))  # output "Anagram"
print(anagramCheck("ignite", "gnite"))  # output "Bukan Anagram"
