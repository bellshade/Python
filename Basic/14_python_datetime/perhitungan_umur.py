import datetime

# tentukan tanggal lahir, misalkan 29 Des 1997
tanggal_lahir = datetime.datetime(1997, 12, 29)

# ambil waktu sekarang
tanggal_sekarang = datetime.datetime.now()

# hitung umurnya
umur_sekarang = tanggal_sekarang - tanggal_lahir
print(umur_sekarang)

# ambil jumlah hari
jumlah_hari = umur_sekarang.days

# hitung umur dalam tahun
umur_tahun = jumlah_hari // 365

# hitung sisa hari
sisa_hari = jumlah_hari % 365
print("Umur saya adalah %d tahun %d hari" % (umur_tahun, sisa_hari))
