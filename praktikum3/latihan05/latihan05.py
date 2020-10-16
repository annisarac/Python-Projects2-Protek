#Membuat Diagram jumlah mahasiswa PTIK

print('--------------- Diagram Jumlah Siswa PTIK ---------------')

lakiLaki = int(input('Ada berapa mahasiswa laki-laki di jurusan PTIK?'))
perempuan = int(input('Ada berapa mahasiswa perempuan di jurusan PTIK?'))

l = int(lakiLaki / 10)
p = int(perempuan / 10)

print('laki-laki = ' + '*' * l)
print('perempuan = ' + '*' * p)
