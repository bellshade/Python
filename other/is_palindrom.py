# Palindrom adalah kata yang dapat
# dibaca dari depan maupun belakang
def is_palindrom(x):
    # Pengecekan apakah huruf didepan dan belakang itu sama
    return x == x[::-1]

print(is_palindrom("katak"))  # output "True/Palindrom"
print(is_palindrom("label"))  # output "False/Bukan Palindrom"
