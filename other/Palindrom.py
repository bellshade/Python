# Palindrom adalah kata yang dapat
# dibaca dari depan maupun belakang
def palindrom(x):
    # Pengecekan apakah huruf didepan dan belakang itu sama
    return x == x[::-1]


print(palindrom("katak"))  # output "True/Palindrom"
print(palindrom("label"))  # output "False/Bukan Palindrom"
