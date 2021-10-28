import datetime

# mengetahui waktu sekarang
sekarang = datetime.datetime.now()
print(sekarang)

# mengetahui tahun
print(sekarang.year)

# mengetahui bulan
print(sekarang.month)

# mengetahui hari
print(sekarang.day)

# format tanggal DD-MM-YYYY
print(sekarang.strftime('%d-%m-%Y'))

# mendefinisikan tanggal dan waktu
hari_kemerdekaan = datetime.date(1945, 8, 17)
print(hari_kemerdekaan)
