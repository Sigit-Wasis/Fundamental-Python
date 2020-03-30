# ================================
# Example Class of pythonindo.com
# ================================

class Karyawan():
	"""docstring for Karyawan"""
	jumlah_karyawan = 0

	def __init__(self, nama, gaji):
		self.nama = nama
		self.gaji = gaji
		Karyawan.jumlah_karyawan += 1

    # method diawali dengan kata def
	def tampilkan_jumlah(self):
		print('Total Karyawan:', Karyawan.jumlah_karyawan)

	def tampilkan_profil(self):
		print("Nama :", self.nama)
		print("Gaji : ", self.gaji)

# Instansiasi Objek
# membuat objek pertama dari kelas karyawan
karyawan1 = Karyawan('Sarah', 1000000)
# membuat objek kedua dari kelas karyawan
karyawan2 = Karyawan('Budi', 5000000)

# Mengakses Atribute Objek
karyawan1.tampilkan_profil()
karyawan2.tampilkan_profil()
print("Total Karyawan :", Karyawan.jumlah_karyawan)