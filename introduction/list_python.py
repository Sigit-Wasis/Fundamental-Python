# ======================
# List dalam python
# ======================
# List digunakan untuk menyiman data yang banyak dalam satu variabel.
# list dibuat dengan menggunakan variabel biasa namun menggunakan ([])

# Example Program

# List kosong
warna = []
# List dengan isi membaca
hobi = ["membaca"]
# List jika diisi banyak data dipisah dengan koma(,)
# Dan dapat disi banyak tipe data  
makanan = ["roti bakar", True, "seblak", 100, 10.22, "kue tiaw"]

# Mengambil nilai list untuk awal index dimulai dari 0
makanan = ["roti bakar", True, "seblak", 100, 10.22, "kue tiaw"]
# mengambil seblak maka menggunakan index 2
getMakanan = makanan[1]

# Latihan1
myFriend = ["sigit", "dwi", "hamid", "wasis", "subekti"]
# Cetak yang nomor index 3
print("Nama teman saya yang ketiga adalah: ", format(myFriend[3]))
# Tampilankan Jumlah semua daftar teman dengan fungsi len()
print("Ini daftar semua keseluruhan teman saya: ", format(len(myFriend)))
# Tampilkan dengan menggunakan for
for friend in myFriend:
    print(friend)

# Mengganti Nilai List
data  = ["rajin", "tekun", "taat", "sopan"]
# ganti index 2 yaitu taat dengan hebat
gantiData = data[2] = "hebat"

print(gantiData)

# Menambah Item List
# Tiga method untuk menambahkan ke list:
# append(item) menambahkan list di depan
# prepend(item) menambahkan list di belakang
# inser(index, item) menambahkan item dengan indeks tertentu

warna = ["kuning", "merah", "hijau", "coklat", "hitam"]
addWarna = warna.append("biru")
print(warna)

war = ["kuning", "merah", "hijau", "coklat", "hitam"]
go = war.prepend("Biru muda")
# lang = war.insert(2, "Jingga")
print(war)









