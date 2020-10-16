#Variable assignment
import math

jarak = 795
print('Pak Budi menempuh jarak perjalanan sejauh 795 kilometer')

konsumsiBbm = 12
print('Mobil Pak Budi mnghabiskan 1 liter bensin untuk jarak 12 kilometer')

kapasitasTangki = 50
print('Kapasitas tangki mobil Pak Budi adalah 50 liter')

#Hitung bensin
literBensin = jarak / konsumsiBbm
minimalIsi = (literBensin - 50) / kapasitasTangki
literBensin = int(literBensin)
totalIsi = math.ceil(minimalIsi)

#Tampilkan hasil

print('Pak Budi harus mengisi bensin minimal sebanyak :' + str(totalIsi) + 'kali')
