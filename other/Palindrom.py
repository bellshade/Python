# Palindrom adalah kata yang dapat
# dibaca dari depan maupun belakang
def Palindrom(x):
    # Perulangan disini berfungsi sebagai
    # pengecekan apakah huruf didepan dan belakang itu sama
    for i in range(0, len(x)):
        if x[i] != x[len(x) - 1 - i]:
            return "Bukan Palindrom"
    return "Palindrom"


print(Palindrom("kodok"))  # output "Palindrom"
print(Palindrom("label"))  # output "Bukan Palindrom"
