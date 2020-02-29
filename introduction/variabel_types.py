# ======================
# Variabel dalam python
# ======================
# Aturan Penulisan Variabel
# 1. Dapat menggunakan huruf dan garis bawah: nama, _nama, namaKu, nama_kamu
# 2. Karakter selanjutnya berupa huruf atau angka: _nama, nama1, nilai2
# 3. Tidak boleh menggunakan kata kunci yang sudah ada: if, while, for

variabel = "nilai"
nama = "budi"
kelas = 10

# Menghapus variabel dengan del

variabel = "nilai"
kelas = 10
del(variabel, kelas)

print(nama)
# print(kelas)
# print(variabel)

# Example

panjang = 70
lebar = 90
tinggi = 10
hasil = panjang * lebar * tinggi
print(hasil)

# ======================
# Tipe Data dalam python
# ======================
# Tipe data secara umum ada tipe data teks, angka dan boolean
# Tipe data Angka di bagi menjadi dua int(Integer) misalkan harga = 1200, dan float misalkan harga = 23,99
# Tipe data Teks di bagi menjadi dua Char contoh 'R' dan Varchar contoh 'Aku Ini Lo'
# Tipe data boolean memiliki dua nilai 0/1 atau True or False

# Example Program:

nama = "Sigit wasis subekti"
alamat = 'Lampung'
umur = 19
tinggi = 164.5
menikah = True

print("Nama Saya:",nama)
print('Alamat saya:',alamat)
print("Umur saya:", umur)
print("Tinggi Badan:", tinggi)
if(menikah):
    print("Status: Sudah Menikah")
else:
    print("Status: Belum Menikah")

# mengecek tipe data suatu variabel
cekNama = type(nama)
cekUmur = type(umur)
cekStatus = type(menikah)

print(cekNama)
print(cekUmur)
print(cekStatus)


