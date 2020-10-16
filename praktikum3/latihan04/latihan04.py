#Variable assignment
jarakAb = 125
jarakBc = 256
kecepatanAb = 62
kecepatanBc = 70
jamBerangkat = 06.00
waktuIstirahat = 00.45

#Hitung waktu
waktuTiba = jamBerangkat + waktuIstirahat + jarakAb // kecepatanAb + jarakBc // kecepatanBc

print('Pak Amir sampai di kota C pada pukul ' + str(waktuTiba))
