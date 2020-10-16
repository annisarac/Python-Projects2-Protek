#Variable assignment
jamMulai = 6
menitMulai = 00
print('mobil mulai disewa pada pukul 06:00')

jamSelesai = 23
menitSelesai = 50
print('mobil dikembalikan pada pukul 23:50')

#Operasi penghitungan
jamSewa = jamSelesai - jamMulai
menitSewa = menitSelesai - menitMulai
lamaSewa = jamSewa + menitSewa/60

totalSewa = int(lamaSewa)

totalBiaya = 200000 + (10000 * (totalSewa - 12))

#Tampilkan hasil
print('biaya yang perlu dibayarkan untuk rental mobil adalah :' + str(totalBiaya))
                       
