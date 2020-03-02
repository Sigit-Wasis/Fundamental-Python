# subsetting 

keluarga = ["sigit", 4.76, "wasis", 9.87, "subekti", 7.65, "dwi", 6.87]

# no index dimulai dari 0
# get index ke 1 maka yang muncul 4.76
getindex = keluarga[1]
print(getindex)

# get index ke 2 dari belakang maka muncul dwi
getBelakang = keluarga[-2]
print(getBelakang)

# get index ke 3 - 5 maka muncul 9.87 - subekti
getTengah = keluarga[3:5]
print(getTengah)

# get index dari awal sampai index 4
awalAkhir = keluarga[:4]
print(awalAkhir)

# get index dari tengah hingga akhir
tengahAkhir = keluarga[4:]
print(tengahAkhir)