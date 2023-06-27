def dekorator_huruf_kecil(kata):
    # membuat fungsi nested yang kita sebut 'wrapper'
    def wrapper():
        # memanggil yang diteruskan dekorator_huruf_kecil
        # dan kemudian dimasukkan ke dalam variabel
        # 'kata_message'
        kata_message = kata()
        # menggunakan fungsi 'lower()' untuk membuat
        # variabel dari kata_message menjadi kecil
        # dan kemudian ditugaskan dalam variabel
        # buat_kata_kecil
        buat_kata_kecil = kata_message.lower()
        # mengembalikan nilai dari 'wrapper'
        return buat_kata_kecil

    # mengembalikan fungsi dari wrapper
    return wrapper


def kata_besar():
    return "BELLSHADE"


dekorator = dekorator_huruf_kecil(kata_besar)

print(dekorator() + "\n")


@dekorator_huruf_kecil
def kata_besar_():
    return "BELLSHADE"


print(kata_besar_())
