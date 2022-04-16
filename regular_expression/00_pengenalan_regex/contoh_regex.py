# menggunakan fungsi modul re
import re

kata = "saya belajar python di bellshade"
regex_saya = re.search("^saya.*bellshade$", kata)

# jika regex yang dicari ditemukan
if regex_saya:
    print("kata ditemukan")
else:
    # jika kata tidak ditemukan
    print("kata tidak ditemukan")